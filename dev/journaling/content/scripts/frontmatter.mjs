#!/usr/bin/env node
/**
 * Frontmatter Tool — Node.js 18+ ESM implementation.
 * Read, validate, merge-update, and replace YAML frontmatter in Markdown files.
 * Zero third-party dependencies. Standard library only.
 *
 * Behavior must match frontmatter.py exactly for all commands.
 * 【NON-PORTABLE】 markers annotate inevitable platform/language divergences.
 */

import { readFileSync, writeFileSync, renameSync, existsSync, statSync, openSync, closeSync, fsyncSync, unlinkSync, readdirSync, mkdirSync } from 'node:fs';
import { dirname, basename, resolve, isAbsolute, join, extname } from 'node:path';
import { randomBytes } from 'node:crypto';

// ── Constants ──────────────────────────────────────────────────────────

const ORDERED_FIELDS = ["title", "summary", "tags", "last_update", "status", "author", "date"];
const REQUIRED_FIELDS = new Set(["title", "summary", "tags", "last_update"]);
const DATE_PATTERN = /^\d{4}-\d{2}-\d{2}$/;
const SPECIAL_CHARS = /[:"#&*!/|>%@]/;

// ═══════════════════════════════════════════════════════════════════════
// General Modules
// ═══════════════════════════════════════════════════════════════════════

/**
 * Expand glob patterns and literal paths into a sorted, deduplicated list of absolute file paths.
 * @param {string[]} paths - Raw path arguments (may contain wildcards)
 * @returns {string[]} Sorted, deduplicated, absolute file paths
 * @behavior Same as Python target_expand
 * Edge cases: see plan §2.1 decision tables
 */
function targetExpand(paths) {
  const result = [];
  const seen = new Set();
  let allExpandedZero = true;

  for (const raw of paths) {
    const hasWildcard = /[*?[]/.test(raw);
    if (hasWildcard) {
      // glob expand
      // 【NON-PORTABLE】JS uses hand-written glob or fs.globSync; Python uses pathlib.glob
      const matches = jsGlob(raw);
      if (matches.length > 0) {
        allExpandedZero = false;
      }
      for (const m of matches) {
        const absPath = resolve(m);
        if (!seen.has(absPath)) {
          seen.add(absPath);
          result.push(absPath);
        }
      }
    } else {
      // literal path — check existence
      const absPath = resolve(raw);
      if (existsSync(absPath) && statSync(absPath).isFile()) {
        allExpandedZero = false;
        if (!seen.has(absPath)) {
          seen.add(absPath);
          result.push(absPath);
        }
      } else {
        // literal path not found → warn
        process.stderr.write(`file not found: ${raw}\n`);
      }
    }
  }

  if (allExpandedZero && result.length === 0) {
    process.stderr.write(`no files matched\n`);
    process.exit(1);
  }

  result.sort();
  return result;
}

/**
 * Simple glob implementation using recursive readdir.
 * Supports *, ?, ** patterns.
 * @param {string} pattern - Glob pattern
 * @returns {string[]} Matching file paths
 */
function jsGlob(pattern) {
  // 【NON-PORTABLE】Hand-written glob; Python uses pathlib.Path.glob
  const results = [];
  const baseDir = process.cwd();
  _globRecursive(baseDir, pattern.split(/[/\\]/), 0, "", results);
  return results;
}

function _globRecursive(baseDir, parts, partIdx, currentPath, results) {
  if (partIdx >= parts.length) {
    // reached end of pattern — check if file exists
    const fullPath = join(baseDir, currentPath);
    if (existsSync(fullPath) && statSync(fullPath).isFile()) {
      results.push(fullPath);
    }
    return;
  }

  const part = parts[partIdx];

  if (part === "**") {
    // ** matches zero or more directories
    // Option A: match zero dirs (skip **)
    _globRecursive(baseDir, parts, partIdx + 1, currentPath, results);

    // Option B: match one or more dirs
    const searchDir = currentPath ? join(baseDir, currentPath) : baseDir;
    try {
      const entries = readdirSync(searchDir, { withFileTypes: true });
      for (const entry of entries) {
        if (entry.isDirectory() && !entry.name.startsWith(".")) {
          const newPath = currentPath ? join(currentPath, entry.name) : entry.name;
          // try matching ** at this level
          _globRecursive(baseDir, parts, partIdx, newPath, results);
          // also try consuming ** and matching next part
          _globRecursive(baseDir, parts, partIdx + 1, newPath, results);
        }
      }
    } catch (e) {
      // directory doesn't exist — ignore
    }
    return;
  }

  // check if part contains wildcards
  const hasWildcard = /[*?[]/.test(part);
  const searchDir = currentPath ? join(baseDir, currentPath) : baseDir;

  try {
    const entries = readdirSync(searchDir, { withFileTypes: true });
    const isLastPart = partIdx === parts.length - 1;

    for (const entry of entries) {
      if (hasWildcard) {
        // match pattern against entry name
        const regex = globPartToRegex(part);
        if (!regex.test(entry.name)) continue;
      } else if (entry.name !== part) {
        continue;
      }

      if (isLastPart) {
        // last part — must be a file
        if (entry.isFile()) {
          const fullPath = currentPath ? join(baseDir, currentPath, entry.name) : join(baseDir, entry.name);
          results.push(fullPath);
        }
      } else {
        // intermediate part — must be a directory
        if (entry.isDirectory()) {
          const newPath = currentPath ? join(currentPath, entry.name) : entry.name;
          _globRecursive(baseDir, parts, partIdx + 1, newPath, results);
        }
      }
    }
  } catch (e) {
    // directory doesn't exist — ignore
  }
}

function globPartToRegex(part) {
  let pattern = part
    .replace(/\./g, "\\.")
    .replace(/\*\*/g, "<<GLOBSTAR>>")
    .replace(/\*/g, "[^/]*")
    .replace(/<<GLOBSTAR>>/g, ".*")
    .replace(/\?/g, "[^/]");
  return new RegExp(`^${pattern}$`);
}


/**
 * Read a Markdown file and extract YAML frontmatter header and body.
 * @param {string} filepath - Path to .md file
 * @returns {{header_raw: string, body: string, body_start_line: number}}
 * @behavior Same as Python fm_read (see decision table §2.1)
 */
function fmRead(filepath) {
  // reading file
  const content = readFileSync(filepath, "utf-8");

  if (!content) {
    return { header_raw: "", body: "", body_start_line: 0 };
  }

  const lines = content.split("\n");

  // first line must be exactly "---" (no leading whitespace)
  if (lines.length === 0 || lines[0].trim() !== "---") {
    return { header_raw: "", body: content, body_start_line: 0 };
  }

  // search for closing "---"
  let closingLine = -1;
  for (let i = 1; i < lines.length; i++) {
    if (lines[i].trim() === "---") {
      closingLine = i;
      break;
    }
  }

  // no closing delimiter → not frontmatter
  if (closingLine === -1) {
    return { header_raw: "", body: content, body_start_line: 0 };
  }

  // extract header and body
  const headerLines = lines.slice(1, closingLine);
  const headerRaw = headerLines.join("\n");

  // body starts after closing "---"
  const bodyStartLine = closingLine + 1;
  const bodyLines = lines.slice(bodyStartLine);
  const body = bodyLines.join("\n");

  return { header_raw: headerRaw, body, body_start_line: bodyStartLine };
}


/**
 * Parse a YAML subset string into an object.
 * @param {string} yamlText - Raw YAML text (without --- delimiters)
 * @returns {Object} Parsed key-value pairs
 * @behavior Same as Python fm_parse (see decision table §2.1)
 */
function fmParse(yamlText) {
  if (!yamlText || yamlText.trim() === "") {
    return {};
  }

  const result = {};
  const lines = yamlText.split("\n");
  let i = 0;
  const n = lines.length;

  while (i < n) {
    const line = lines[i];
    const stripped = line.trim();

    // skip empty lines
    if (stripped === "") {
      i++;
      continue;
    }

    // skip comment lines (full-line comments only)
    if (stripped.startsWith("#")) {
      i++;
      continue;
    }

    // check indentation — top-level keys must start at column 0
    if (line && (line[0] === " " || line[0] === "\t")) {
      // indented line not inside a list → error
      process.stderr.write(`parse error: line ${i + 1}: unexpected indentation: ${stripped}\n`);
      process.exit(1);
    }

    // try to parse key: value
    const colonIdx = line.indexOf(":");
    if (colonIdx === -1) {
      process.stderr.write(`parse error: line ${i + 1}: expected key: value, got: ${stripped}\n`);
      process.exit(1);
    }

    const key = line.slice(0, colonIdx).trim();
    const afterColon = line.slice(colonIdx + 1);

    // value may be empty
    let valueStr;
    if (afterColon === "" || afterColon.trim() === "") {
      valueStr = "";
    } else {
      valueStr = afterColon.replace(/^ /, ""); // remove exactly one leading space
    }

    // check if value starts with | or > (multiline literal/folded)
    if (["|", ">", "|-", ">-", "|+", ">+"].includes(valueStr)) {
      // multiline string — collect indented lines
      // entering multiline collection
      const multilineParts = [];
      let j = i + 1;
      while (j < n) {
        const nextLine = lines[j];
        if (nextLine.trim() === "") {
          multilineParts.push("");
          j++;
          continue;
        }
        if (!nextLine || !(nextLine[0] === " " || nextLine[0] === "\t")) {
          break;
        }
        multilineParts.push(nextLine.trim());
        j++;
      }
      result[key] = multilineParts.join("\n");
      i = j;
      continue;
    }

    // check if next lines form a YAML list
    if (valueStr === "") {
      // entering LIST state for this key
      if (i + 1 < n && /^  - /.test(lines[i + 1])) {
        const items = [];
        let j = i + 1;
        while (j < n) {
          const listLine = lines[j];
          const m = listLine.match(/^  - (.*)/);
          if (m) {
            items.push(m[1]);
            j++;
          } else if (listLine.trim() === "") {
            // check if more list items follow
            if (j + 1 < n && /^  - /.test(lines[j + 1])) {
              j++;
            } else {
              break;
            }
          } else {
            break;
          }
        }
        result[key] = items;
        i = j;
        continue;
      } else {
        // empty value with no list → null
        result[key] = null;
        i++;
        continue;
      }
    }

    // type inference for scalar values
    result[key] = _parseScalarJs(valueStr);
    i++;
  }

  return result;
}


/**
 * Infer and convert a scalar YAML value to the appropriate JS type.
 * @param {string} valueStr - Raw YAML value string
 * @returns {*} Parsed value
 */
function _parseScalarJs(valueStr) {
  const s = valueStr.trim();

  // null values
  if (s === "null" || s === "~" || s === "") {
    return null;
  }

  // booleans (strictly lowercase only)
  if (s === "true") return true;
  if (s === "false") return false;
  // uppercase/mixed-case → string
  if (s.toLowerCase() === "true" || s.toLowerCase() === "false") {
    return s;
  }

  // double-quoted string → strip quotes
  if (s.startsWith('"') && s.endsWith('"') && s.length >= 2) {
    return s.slice(1, -1);
  }

  // integer
  if (/^-?\d+$/.test(s)) {
    // 【NON-PORTABLE】JS Number unified; Python distinguishes int/float
    return Number(s);
  }

  // float
  if (/^-?\d+\.\d+$/.test(s)) {
    return Number(s);
  }

  // everything else → string
  return s;
}


/**
 * Serialize an object into YAML frontmatter + body → complete Markdown text.
 * @param {Object} headerDict - Frontmatter fields
 * @param {string} body - Body text after frontmatter
 * @returns {string} Complete Markdown with frontmatter block
 * @behavior Same as Python fm_write
 */
function fmWrite(headerDict, body) {
  const lines = ["---"];

  // build ordered list of keys
  const keys = Object.keys(headerDict);
  const ordered = [];

  for (const field of ORDERED_FIELDS) {
    if (keys.includes(field)) {
      ordered.push(field);
    }
  }

  // remaining custom fields in alphabetical order
  const customSorted = keys
    .filter(k => !ORDERED_FIELDS.includes(k))
    .sort();
  ordered.push(...customSorted);

  for (const key of ordered) {
    const value = headerDict[key];
    lines.push(_serializeValueJs(key, value));
  }

  lines.push("---");
  const frontmatterBlock = lines.join("\n");

  if (body) {
    return frontmatterBlock + "\n" + body;
  } else {
    return frontmatterBlock + "\n";
  }
}


/**
 * Serialize a single key-value pair to a YAML line (or lines for lists).
 * @param {string} key
 * @param {*} value
 * @returns {string}
 */
function _serializeValueJs(key, value) {
  if (value === null || value === undefined) {
    return `${key}:`;
  }

  if (typeof value === "boolean") {
    return `${key}: ${value}`;
  }

  if (typeof value === "number") {
    // 【NON-PORTABLE】JS Number.isInteger to suppress decimal point for integers
    if (Number.isInteger(value)) {
      return `${key}: ${value}`;
    }
    return `${key}: ${value}`;
  }

  if (Array.isArray(value)) {
    if (value.length === 0) {
      return `${key}:`;
    }
    const lines = [`${key}:`];
    for (const item of value) {
      let itemStr = String(item);
      if (typeof item === "string" && SPECIAL_CHARS.test(itemStr)) {
        itemStr = `"${itemStr}"`;
      }
      lines.push(`  - ${itemStr}`);
    }
    return lines.join("\n");
  }

  // string value
  const s = String(value);
  if (s === "") {
    return `${key}:`;
  }
  if (_needsQuotingJs(s)) {
    return `${key}: "${s}"`;
  }
  return `${key}: ${s}`;
}


function _needsQuotingJs(s) {
  if (s !== s.trim()) return true;
  if (SPECIAL_CHARS.test(s)) return true;
  const lower = s.toLowerCase();
  if (["true", "false", "null", "~", "yes", "no", "on", "off"].includes(lower)) return true;
  if (/^-?\d+\.?\d*$/.test(s)) return true;
  return false;
}


/**
 * Extract a subset of fields from an object.
 * @param {Object} d - Source object
 * @param {string[]} fields - Field names to extract (empty = all)
 * @returns {Object}
 */
function fmSelect(d, fields) {
  if (!fields || fields.length === 0) {
    return { ...d };
  }
  const result = {};
  for (const f of fields) {
    if (f in d) {
      result[f] = d[f];
    }
  }
  return result;
}


/**
 * Merge delta object into current, overwriting same keys.
 * @param {Object} current - Existing frontmatter
 * @param {Object} delta - Fields to merge
 * @returns {Object} Merged result
 * @behavior See plan §2.1 merge decision table
 */
function fmMerge(current, delta) {
  const result = { ...current };
  for (const [k, v] of Object.entries(delta)) {
    if (k in result) {
      result[k] = v;
    } else if (v !== null && v !== undefined) {
      result[k] = v;
    }
    // new key with null/undefined → no-op
  }
  return result;
}


/**
 * Validate a frontmatter object against the field specification.
 * @param {Object} d - Frontmatter data
 * @param {"full"|"delta"} mode - Validation mode
 * @returns {string[]} List of error messages; empty = pass
 * @behavior Same as Python fm_validate
 */
function fmValidate(d, mode = "full") {
  const errors = [];

  const fieldsToCheck = mode === "full"
    ? new Set([...REQUIRED_FIELDS, ...Object.keys(d)])
    : new Set(Object.keys(d));

  // check required fields existence (full mode only)
  if (mode === "full") {
    for (const field of REQUIRED_FIELDS) {
      if (!(field in d) || d[field] === null || d[field] === undefined) {
        errors.push(`missing required field: ${field}`);
      }
    }
  }

  for (const field of fieldsToCheck) {
    if (!(field in d)) continue;
    const value = d[field];

    // validate field name format for custom fields
    if (!ORDERED_FIELDS.includes(field) && !REQUIRED_FIELDS.has(field)) {
      if (!/^[a-z][a-z0-9]*(-[a-z0-9]+)*$/.test(field)) {
        errors.push(`field name should be lowercase-kebab-case: ${field}`);
      }
    }

    // title: string, non-empty
    if (field === "title") {
      if (value !== null && value !== undefined && typeof value !== "string") {
        errors.push(`title: expected string, got ${typeof value}`);
      } else if (value !== null && value !== undefined && value.trim() === "") {
        errors.push(`title: must not be empty`);
      }
    }
    // summary: string
    else if (field === "summary") {
      if (value !== null && value !== undefined && typeof value !== "string") {
        errors.push(`summary: expected string, got ${typeof value}`);
      }
    }
    // tags: array of strings, must be YAML list (not inline)
    else if (field === "tags") {
      if (value !== null && value !== undefined) {
        if (!Array.isArray(value)) {
          errors.push(`tags: expected YAML list, got ${typeof value} (tags should be YAML list format, not inline)`);
        } else {
          for (let idx = 0; idx < value.length; idx++) {
            if (typeof value[idx] !== "string") {
              errors.push(`tags[${idx}]: expected string, got ${typeof value[idx]}`);
            }
          }
        }
      }
    }
    // last_update: string YYYY-MM-DD
    else if (field === "last_update") {
      if (value !== null && value !== undefined) {
        if (typeof value !== "string") {
          errors.push(`last_update: expected string (YYYY-MM-DD), got ${typeof value}`);
        } else if (!DATE_PATTERN.test(value)) {
          errors.push(`last_update: must be YYYY-MM-DD format, got: ${value}`);
        }
      }
    }
    // status: string (optional)
    else if (field === "status") {
      if (value !== null && value !== undefined && typeof value !== "string") {
        errors.push(`status: expected string, got ${typeof value}`);
      }
    }
    // author: string (optional)
    else if (field === "author") {
      if (value !== null && value !== undefined && typeof value !== "string") {
        errors.push(`author: expected string, got ${typeof value}`);
      }
    }
    // date: string YYYY-MM-DD (optional)
    else if (field === "date") {
      if (value !== null && value !== undefined) {
        if (typeof value !== "string") {
          errors.push(`date: expected string (YYYY-MM-DD), got ${typeof value}`);
        } else if (!DATE_PATTERN.test(value)) {
          errors.push(`date: must be YYYY-MM-DD format, got: ${value}`);
        }
      }
    }
  }


  // check all boolean values: must be actual boolean (not string "True"/"False")
  for (const field of fieldsToCheck) {
    if (!(field in d)) continue;
    const value = d[field];
    if (typeof value === "string" && ["true", "false", "True", "False", "TRUE", "FALSE", "yes", "no"].includes(value)) {
      errors.push(`${field}: boolean value should be lowercase (got '${value}', use true/false)`);
    }
  }
  return errors;
}


/**
 * Format output based on command, file count, and field count.
 * @param {*} value - Processed data
 * @param {Object} params - Formatting parameters
 * @returns {string} Formatted output (empty string if already printed)
 */
function fmtOutput(value, params) {
  const cmd = params.command || "get";
  const pretty = params.pretty !== false;

  if (cmd === "get") {
    return _fmtGetOutput(value, pretty);
  } else if (cmd === "check") {
    return _fmtCheckOutput(value);
  } else if (cmd === "update" || cmd === "replace") {
    return _fmtMutationOutput(value);
  }
  return JSON.stringify(value, null, pretty ? 2 : 0);
}


function _fmtGetOutput(value, pretty) {
  const indent = pretty ? 2 : 0;
  return JSON.stringify(value, null, indent);
}


function _fmtCheckOutput(result) {
  // Only print "valid" lines to stdout. Errors already go to stderr from cmdCheck.
  const validLines = [];
  for (const item of result) {
    const filepath = item.file || "?";
    const errors = item.errors || [];
    if (errors.length === 0) {
      validLines.push(`${filepath}: valid`);
    }
  }
  if (validLines.length > 0) {
    process.stdout.write(validLines.join("\n") + "\n");
  }
  return "";
}


function _fmtMutationOutput(result) {
  const updated = result.updated || 0;
  const failed = result.failed || 0;
  const dryRun = result.dry_run || false;
  const details = result.dry_run_details || [];

  if (dryRun && details.length > 0) {
    for (const detail of details) {
      process.stdout.write(detail + "\n");
    }
    return "";
  }

  return `updated ${updated}, failed ${failed}`;
}


/**
 * Read data from --data JSON string or --file path.
 * @param {{type: string, value: string}} source
 * @returns {Object} Parsed data
 */
function dataRead(source) {
  if (source.type === "data") {
    // parse JSON string
    try {
      return JSON.parse(source.value);
    } catch (e) {
      process.stderr.write(`invalid JSON: ${e.message}\n`);
      process.exit(1);
    }
  } else if (source.type === "file") {
    const filepath = source.value;
    if (!existsSync(filepath)) {
      process.stderr.write(`file not found: ${filepath}\n`);
      process.exit(1);
    }

    const ext = extname(filepath).toLowerCase();

    if (ext === ".md") {
      // extract frontmatter from markdown
      const fmResult = fmRead(filepath);
      if (fmResult.header_raw === "" && fmResult.body_start_line === 0) {
        process.stderr.write(`no frontmatter found in: ${filepath}\n`);
        process.exit(1);
      }
      return fmParse(fmResult.header_raw);
    } else if (ext === ".json") {
      // read as JSON
      const content = readFileSync(filepath, "utf-8");
      return JSON.parse(content);
    } else if (ext === ".yaml" || ext === ".yml") {
      // read file and parse as YAML
      const content = readFileSync(filepath, "utf-8");
      return fmParse(content);
    } else {
      process.stderr.write(`unsupported source format: ${ext}\n`);
      process.exit(1);
    }
  } else {
    process.stderr.write(`internal error: invalid data source type\n`);
    process.exit(1);
  }
}


/**
 * Write content to file atomically using temp file + rename.
 * @param {string} filepath - Target file path
 * @param {string} content - File content
 */
function atomicWrite(filepath, content) {
  const dir = dirname(filepath) || ".";
  const base = basename(filepath);
  // 【NON-PORTABLE】JS uses crypto.randomBytes; Python uses tempfile.mkstemp
  const tmpPath = join(dir, `${base}.tmp.${randomBytes(4).toString("hex")}`);

  try {
    // write content
    writeFileSync(tmpPath, content, "utf-8");

    // fsync — flush data to disk before rename
    // 【NON-PORTABLE】Try-catch for Windows EPERM; Python handles via tempfile + os.fsync
    try {
      const fd = openSync(tmpPath, "r");
      fsyncSync(fd);
      closeSync(fd);
    } catch (_) {
      // fsync can fail on Windows with EPERM — best-effort fsync
    }

    // atomic rename
    renameSync(tmpPath, filepath);
  } catch (e) {
    // clean up temp file on failure
    try {
      unlinkSync(tmpPath);
    } catch (_) {
      // ignore cleanup errors
    }
    throw e;
  }
}

// ═══════════════════════════════════════════════════════════════════════
// CLI Parser
// ═══════════════════════════════════════════════════════════════════════

/**
 * Parse command-line arguments.
 * @param {string[]} argv - process.argv.slice(2)
 * @returns {Object} Parsed parameters
 */
function parseArgs(argv) {
  if (argv.length === 0 || argv[0] === "--help" || argv[0] === "-h") {
    printHelp(null);
    process.exit(0);
  }

  const command = argv[0];
  const validCommands = ["get", "check", "update", "replace"];

  if (!validCommands.includes(command)) {
    process.stderr.write(`unknown command: ${command}\n`);
    printHelp(null);
    process.exit(1);
  }

  const params = {
    command,
    targets: [],
    fields: [],
    data_source: null,
    dry_run: false,
    pretty: true,
    journal_root: null,
  };

  let i = 1;
  // Phase 1: collect targets
  // For get: stop at first arg that doesn't look like a file path / glob
  // For check/update/replace: all non-option args before -- are targets
  while (i < argv.length) {
    const arg = argv[i];
    if (arg.startsWith("--")) break;
    // for get command, distinguish targets from field names
    if (command === "get") {
      // first arg is always treated as a target
      // subsequent args: target if has wildcard, or is existing file/dir
      const hasWildcard = /[*?[]/.test(arg);
      let isTarget = params.targets.length === 0 || hasWildcard;
      if (!isTarget) {
        try {
          const s = statSync(arg);
          isTarget = s.isFile() || s.isDirectory();
        } catch (e) {
          // file doesn't exist → not a target
        }
      }
      if (!isTarget) break;
    }
    params.targets.push(arg);
    i++;
  }

  // Phase 2: for get command, remaining non-option args are fields
  if (command === "get") {
    const fieldArgs = [];
    while (i < argv.length) {
      const arg = argv[i];
      if (arg.startsWith("--")) break;
      fieldArgs.push(arg);
      i++;
    }
    for (const fa of fieldArgs) {
      for (const f of fa.split(",")) {
        const trimmed = f.trim();
        if (trimmed) {
          params.fields.push(trimmed);
        }
      }
    }
  }

  // Phase 3: parse options
  while (i < argv.length) {
    const arg = argv[i];
    if (arg === "--help" || arg === "-h") {
      printHelp(command);
      process.exit(0);
    } else if (arg === "--data") {
      i++;
      if (i >= argv.length) {
        process.stderr.write("--data requires a value\n");
        process.exit(1);
      }
      if (params.data_source !== null) {
        process.stderr.write("cannot use both --data and --file\n");
        process.exit(1);
      }
      params.data_source = { type: "data", value: argv[i] };
    } else if (arg === "--file") {
      i++;
      if (i >= argv.length) {
        process.stderr.write("--file requires a value\n");
        process.exit(1);
      }
      if (params.data_source !== null) {
        process.stderr.write("cannot use both --data and --file\n");
        process.exit(1);
      }
      params.data_source = { type: "file", value: argv[i] };
    } else if (arg === "--dry-run") {
      params.dry_run = true;
    } else if (arg === "--pretty") {
      params.pretty = true;
    } else if (arg === "--no-pretty") {
      params.pretty = false;
    } else if (arg === "--journal-root") {
      i++;
      if (i >= argv.length) {
        process.stderr.write("--journal-root requires a value\n");
        process.exit(1);
      }
      params.journal_root = argv[i];
    } else {
      process.stderr.write(`unknown option: ${arg}\n`);
      process.exit(1);
    }
    i++;
  }

  // Phase 4: validate required arguments
  if (params.targets.length === 0) {
    process.stderr.write(`command '${command}' requires at least one target file\n`);
    process.exit(1);
  }

  if ((command === "update" || command === "replace") && params.data_source === null) {
    process.stderr.write(`command '${command}' requires --data or --file\n`);
    process.exit(1);
  }

  return params;
}

// ═══════════════════════════════════════════════════════════════════════
// Command Handlers
// ═══════════════════════════════════════════════════════════════════════

/**
 * Handle get command: read and output frontmatter fields.
 * dispatch: get → targetExpand → (fmRead → fmParse → fmSelect) → fmtOutput
 */
function cmdGet(params) {
  // expand targets
  const files = targetExpand(params.targets);
  const fields = params.fields;
  const fileCount = files.length;
  const fieldCount = fields.length;

  if (fileCount === 1) {
    // single file
    const filepath = files[0];
    const fmResult = fmRead(filepath);
    const data = (fmResult.header_raw === "" && fmResult.body_start_line === 0)
      ? {}
      : fmParse(fmResult.header_raw);

    let output;
    if (fieldCount === 0) {
      output = data;
    } else if (fieldCount === 1) {
      const field = fields[0];
      output = field in data ? data[field] : null;
    } else {
      const selected = fmSelect(data, fields);
      // fill missing fields with null
      for (const f of fields) {
        if (!(f in selected)) {
          selected[f] = null;
        }
      }
      output = selected;
    }

    const formatted = fmtOutput(output, {
      command: "get",
      fileCount: 1,
      fieldCount,
      fields,
      pretty: params.pretty,
    });
    if (formatted) {
      process.stdout.write(formatted + "\n");
    }
  } else {
    // multiple files
    let output;

    if (fieldCount === 0) {
      // output all fields → array of {file, ...fields}
      const results = [];
      for (const filepath of files) {
        const fmResult = fmRead(filepath);
        const data = (fmResult.header_raw === "" && fmResult.body_start_line === 0)
          ? {}
          : fmParse(fmResult.header_raw);
        results.push({ file: filepath, ...data });
      }
      output = results;
    } else if (fieldCount === 1) {
      // single field → {file: value} mapping
      const field = fields[0];
      const mapping = {};
      for (const filepath of files) {
        const fmResult = fmRead(filepath);
        if (fmResult.header_raw === "" && fmResult.body_start_line === 0) {
          mapping[filepath] = null;
        } else {
          const data = fmParse(fmResult.header_raw);
          mapping[filepath] = field in data ? data[field] : null;
        }
      }
      output = mapping;
    } else {
      // multiple fields → array of {file, field1, field2, ...}
      const results = [];
      for (const filepath of files) {
        const fmResult = fmRead(filepath);
        const data = (fmResult.header_raw === "" && fmResult.body_start_line === 0)
          ? {}
          : fmParse(fmResult.header_raw);
        const entry = { file: filepath, ...fmSelect(data, fields) };
        for (const f of fields) {
          if (!(f in entry)) {
            entry[f] = null;
          }
        }
        results.push(entry);
      }
      output = results;
    }

    const formatted = fmtOutput(output, {
      command: "get",
      fileCount,
      fieldCount,
      fields,
      pretty: params.pretty,
    });
    if (formatted) {
      process.stdout.write(formatted + "\n");
    }
  }
}


/**
 * Handle check command: validate frontmatter.
 * dispatch: check → targetExpand → (fmRead → fmParse → fmValidate) → fmtOutput
 */
function cmdCheck(params) {
  const files = targetExpand(params.targets);
  const results = [];
  let allOk = true;

  for (const filepath of files) {
    const fmResult = fmRead(filepath);
    // no frontmatter found → error
    if (fmResult.header_raw === "" && fmResult.body_start_line === 0) {
      results.push({ file: filepath, errors: ["no frontmatter found"] });
      allOk = false;
      process.stderr.write(`${filepath}: no frontmatter found\n`);
      continue;
    }

    // parse and validate
    const data = fmParse(fmResult.header_raw);
    const errors = fmValidate(data, "full");
    results.push({ file: filepath, errors });

    if (errors.length > 0) {
      allOk = false;
      for (const err of errors) {
        process.stderr.write(`${filepath}: ${err}\n`);
      }
    }
  }

  _fmtCheckOutput(results);

  if (!allOk) {
    process.exit(1);
  }
}


/**
 * Handle update command: merge delta into frontmatter.
 * dispatch: update → targetExpand → dataRead → (fmRead → fmParse → fmMerge → fmWrite → atomicWrite)
 */
function cmdUpdate(params) {
  const files = targetExpand(params.targets);
  const delta = dataRead(params.data_source);

  // validate delta fields (type checks only)
  const deltaErrors = fmValidate(delta, "delta");
  if (deltaErrors.length > 0) {
    for (const err of deltaErrors) {
      process.stderr.write(`delta: ${err}\n`);
    }
    process.exit(1);
  }

  const dryRun = params.dry_run;
  let updated = 0;
  let failed = 0;
  const dryRunDetails = [];

  for (const filepath of files) {
    try {
      const fmResult = fmRead(filepath);
      // parse existing frontmatter (may be empty)
      const current = (fmResult.header_raw === "" && fmResult.body_start_line === 0)
        ? {}
        : fmParse(fmResult.header_raw);
      const body = fmResult.body;

      // merge
      const merged = fmMerge(current, delta);

      // collect change summary for dry-run
      const setFields = [];
      const clearFields = [];
      for (const [k, v] of Object.entries(delta)) {
        if (v !== null && v !== undefined) {
          setFields.push(k);
        } else if (k in current) {
          clearFields.push(k);
        }
      }

      if (dryRun) {
        const parts = [];
        if (setFields.length > 0) parts.push(`would set: ${setFields.join(", ")}`);
        if (clearFields.length > 0) parts.push(`would clear: ${clearFields.join(", ")}`);
        if (parts.length > 0) {
          dryRunDetails.push(`${filepath}: ${parts.join("; ")}`);
        } else {
          dryRunDetails.push(`${filepath}: no changes`);
        }
        continue;
      }

      // serialize and write
      const newContent = fmWrite(merged, body);
      atomicWrite(filepath, newContent);
      updated++;
    } catch (e) {
      failed++;
      process.stderr.write(`${filepath}: ${e.message}\n`);
    }
  }

  if (dryRun) {
    const result = { updated: 0, failed: 0, dry_run: true, dry_run_details: dryRunDetails };
    const output = _fmtMutationOutput(result);
    // already printed in _fmtMutationOutput
  } else {
    process.stdout.write(`updated ${updated}, failed ${failed}\n`);
  }

  if (failed > 0) {
    process.exit(1);
  }
}


/**
 * Handle replace command: replace entire frontmatter of a single file.
 * dispatch: replace → dataRead → fmValidate(full) → fmRead → fmWrite → atomicWrite
 */
function cmdReplace(params) {
  // replace accepts exactly one target
  if (params.targets.length > 1) {
    process.stderr.write(`replace accepts exactly one target, got ${params.targets.length}\n`);
    process.exit(1);
  }

  const targets = targetExpand(params.targets);
  const filepath = targets[0];
  const newData = dataRead(params.data_source);

  // validate full required fields
  const errors = fmValidate(newData, "full");
  if (errors.length > 0) {
    for (const err of errors) {
      process.stderr.write(`${err}\n`);
    }
    process.exit(1);
  }

  const dryRun = params.dry_run;

  // read existing file
  const fmResult = fmRead(filepath);
  const body = fmResult.body;

  if (dryRun) {
    const setFields = Object.keys(newData);
    process.stdout.write(`${filepath}: would replace entire frontmatter with fields: ${setFields.join(", ")}\n`);
    return;
  }

  // serialize and write
  try {
    const newContent = fmWrite(newData, body);
    atomicWrite(filepath, newContent);
    process.stdout.write(`updated 1, failed 0\n`);
  } catch (e) {
    process.stderr.write(`${filepath}: ${e.message}\n`);
    process.exit(1);
  }
}

// ═══════════════════════════════════════════════════════════════════════
// Help Text
// ═══════════════════════════════════════════════════════════════════════

const HELP_MAIN = `USAGE: frontmatter <command> <target...> [options]

COMMANDS:
  get <target...> [<fields...>]
      Read frontmatter fields.
      Examples:
        frontmatter get note.md
        frontmatter get note.md summary
        frontmatter get note.md summary,tags
        frontmatter get note1.md note2.md title
        frontmatter get *.md
      Options:
        --pretty        Pretty-print JSON output (default; --no-pretty to disable)

  check <target...>
      Validate frontmatter format compliance.
      Examples:
        frontmatter check note.md
        frontmatter check *.md
      Options:
        --journal-root <path>   Check tags against TAGS.md registry (optional)

  update <target...> --data '<json>' | --file <path>
      Merge fields into frontmatter. JSON null values clear a field.
      Examples:
        frontmatter update note.md --data '{"summary":"new","status":null}'
        frontmatter update note.md --file data.json
        frontmatter update *.md --data '{"last_update":"2026-06-30"}'
      Options:
        --dry-run       Preview changes without writing

  replace <target> --data '<json>' | --file <path>
      Replace entire frontmatter. Single file target only.
      Examples:
        frontmatter replace note.md --data '{"title":"T","summary":"S","tags":["t"],"last_update":"2026-06-30"}'
        frontmatter replace note.md --file source.md
        frontmatter replace note.md --file template.yaml
      Options:
        --dry-run       Preview changes without writing

Run 'frontmatter <command> --help' for command-specific help.`;

const HELP_GET = `USAGE: frontmatter get <target...> [<fields...>]

Read frontmatter from one or more Markdown files.

Arguments:
  target...     One or more file paths or glob patterns
  fields...     Field names to extract (space or comma separated)
                Omit to output all fields

Output format (depends on file count and field count):
  Single file, all fields:  JSON object {field: value, ...}
  Single file, one field:   JSON scalar value (string, array, or null)
  Single file, N fields:    JSON object {field1: value1, ...}
  Multiple files, all:      JSON array [{file: ..., ...fields}, ...]
  Multiple files, one:      JSON object {file: value, ...}
  Multiple files, N:        JSON array [{file: ..., field1: ..., ...}]

Requesting a nonexistent field returns JSON null.

Options:
  --pretty        Pretty-print JSON output (default)
  --no-pretty     Disable pretty-printing`;

const HELP_CHECK = `USAGE: frontmatter check <target...>

Validate frontmatter format compliance for one or more Markdown files.

Checks performed:
  - Required fields: title (non-empty string), summary (string),
    tags (YAML list of strings), last_update (YYYY-MM-DD)
  - Optional fields type: status (string), author (string), date (YYYY-MM-DD)
  - Tags must be YAML list format (not inline/comma-separated)
  - Boolean values must be lowercase (true/false)
  - Custom field names must be lowercase-kebab-case

Exit codes:
  0 = all files pass validation
  1 = at least one file has issues

Options:
  --journal-root <path>   Check tags against TAGS.md registry (optional)`;

const HELP_UPDATE = `USAGE: frontmatter update <target...> --data '<json>' | --file <path>

Merge fields into the frontmatter of one or more Markdown files.

Required:
  --data '<json>'   JSON object with fields to merge
  --file <path>     Read merge data from a file (.md, .json, .yaml)

Merge semantics:
  - Field present with non-null value → overwrite/add
  - Field present with null value → clear field (keep key, set to null)
  - Field absent → no change
  - New field with null value → no-op (not created)

The body of the Markdown file is never modified.
If a file has no frontmatter, one is created.

Options:
  --dry-run         Preview changes without writing to disk`;

const HELP_REPLACE = `USAGE: frontmatter replace <target> --data '<json>' | --file <path>

Replace the entire frontmatter of a single Markdown file.

Required:
  --data '<json>'   JSON object with the new frontmatter
  --file <path>     Read replacement from a file (.md, .json, .yaml)

The --data content must include all four required fields:
  title, summary, tags (YAML list), last_update (YYYY-MM-DD)

The body of the Markdown file is never modified.
If the file has no frontmatter, one is created.

Options:
  --dry-run         Preview changes without writing to disk`;

function printHelp(command) {
  if (!command) {
    process.stdout.write(HELP_MAIN + "\n");
  } else if (command === "get") {
    process.stdout.write(HELP_GET + "\n");
  } else if (command === "check") {
    process.stdout.write(HELP_CHECK + "\n");
  } else if (command === "update") {
    process.stdout.write(HELP_UPDATE + "\n");
  } else if (command === "replace") {
    process.stdout.write(HELP_REPLACE + "\n");
  } else {
    process.stdout.write(HELP_MAIN + "\n");
  }
}

// ═══════════════════════════════════════════════════════════════════════
// Entry Point
// ═══════════════════════════════════════════════════════════════════════

function main() {
  const argv = process.argv.slice(2);

  if (argv.length === 0) {
    printHelp(null);
    process.exit(0);
  }

  // check for top-level --help
  if (argv[0] === "--help" || argv[0] === "-h") {
    printHelp(null);
    process.exit(0);
  }

  const params = parseArgs(argv);

  switch (params.command) {
    case "get":
      cmdGet(params);
      break;
    case "check":
      cmdCheck(params);
      break;
    case "update":
      cmdUpdate(params);
      break;
    case "replace":
      cmdReplace(params);
      break;
    default:
      process.stderr.write(`unknown command: ${params.command}\n`);
      process.exit(1);
  }
}

main();
