#!/usr/bin/env node
/**
 * check-links — Journal link checker (Node.js 18+ ESM implementation).
 *
 * Extracts all links from journal markdown files, checks target existence,
 * and reports inbound/outbound link relationships. Zero third-party
 * dependencies. Pure read-only — never modifies journal files.
 *
 * Usage:
 *   node check-links.mjs [options] <entry>
 *   node check-links.mjs --journal-root <path> [--file <path>]
 *
 * Node.js 18+ required. See --help for full options.
 */

import { readFileSync, existsSync, readdirSync, statSync } from 'node:fs';
import { dirname, basename, resolve, isAbsolute, relative, join, extname } from 'node:path';

// ── Constants ──────────────────────────────────────────────────────────

// Patterns for link extraction (§3)
// Standard markdown link: [text](target)
const RE_MD_LINK = /\[([^\]]*)\]\(([^)]+)\)/;
// Obsidian wikilink: [[target]] or [[target|text]]
const RE_WIKILINK = /\[\[([^\]|]+)(?:\|([^\]]*))?\]\]/;

// URL schemes that are skipped
const SKIP_PREFIXES = ["https://", "http://", "ftp://", "mailto:"];

// Directories to skip during file scan
const SKIP_DIRS = new Set([".git", "__pycache__", ".obsidian", "node_modules"]);


// ═══════════════════════════════════════════════════════════════════════
// Module: journal_discover
// ═══════════════════════════════════════════════════════════════════════

/**
 * Find journal root by searching upward from entry for INDEX.md.
 *
 * @param {string} entry - Path to a file or directory inside the journal.
 * @returns {string} Absolute path to journal root directory (forward slashes).
 *
 * Called by: main() — dispatch step 1.
 */
function journalDiscover(entry) {
  // Resolve entry to absolute path (§2 auto-discovery rule)
  // 【NON-PORTABLE】 path.resolve() vs pathlib.Path.resolve() — both normalize . and ..
  const entryPath = resolve(entry);

  if (!existsSync(entryPath)) {
    process.stderr.write(`${entry}: file not found\n`);
    process.exit(1);
  }

  // Start directory: entry itself if it's INDEX.md, else its parent
  const entryStat = statSync(entryPath);
  let currentDir;
  if (entryStat.isDirectory()) {
    currentDir = entryPath;
  } else {
    currentDir = dirname(entryPath);
  }

  // Walk upward looking for INDEX.md or index.md (§2 auto-discovery)
  // 【NON-PORTABLE】 Node dirname chain vs Python Path.parent chain — equivalent
  while (true) {
    // Check exact case-insensitive matches only (§5 step 2)
    for (const name of ["INDEX.md", "index.md"]) {
      const candidate = join(currentDir, name);
      try {
        if (existsSync(candidate) && statSync(candidate).isFile()) {
          return normPath(currentDir);
        }
      } catch (_) {
        // stat may fail on permission errors — skip
      }
    }
    // Move up one level
    const parent = dirname(currentDir);
    if (parent === currentDir) {
      // Reached filesystem root
      process.stderr.write(`INDEX.md not found in ancestors of ${entry}\n`);
      process.exit(1);
    }
    currentDir = parent;
  }
}

/**
 * Normalize path separators to forward slashes for cross-platform consistency.
 * 【NON-PORTABLE】 Windows uses backslash — normalize to / for consistent output and comparison.
 *
 * @param {string} p - Any path
 * @returns {string} Path with forward slashes
 */
function normPath(p) {
  return p.replace(/\\/g, '/');
}


// ═══════════════════════════════════════════════════════════════════════
// Module: target_expand
// ═══════════════════════════════════════════════════════════════════════

/**
 * Recursively find all .md files under journal_root.
 *
 * @param {string} journalRoot - Absolute path to journal root (forward slashes).
 * @returns {string[]} Sorted list of absolute paths to .md files (alphabetical),
 *                     excluding SKIP_DIRS, all with forward slashes.
 *
 * Called by: main() — dispatch step 2.
 */
function targetExpand(journalRoot) {
  // 【NON-PORTABLE】 Custom recursive readdir vs Python os.walk — behavior equivalent
  const result = scanMdFiles(journalRoot);

  if (result.length === 0) {
    process.stderr.write(`no markdown files found under ${journalRoot}\n`);
    process.exit(1);
  }

  // Deduplicate and sort alphabetically (§8)
  return [...new Set(result)].sort();
}


/**
 * Recursively scan directory for .md files, skipping SKIP_DIRS.
 * All returned paths use forward slashes.
 *
 * @param {string} dir - Directory to scan.
 * @returns {string[]} Absolute paths to .md files with forward slashes.
 *
 * Called by: targetExpand().
 */
function scanMdFiles(dir) {
  let results = [];
  let entries;
  try {
    entries = readdirSync(dir, { withFileTypes: true });
  } catch (_) {
    return results;  // permission error → skip directory
  }

  for (const entry of entries) {
    const fullPath = join(dir, entry.name);
    if (entry.isDirectory()) {
      // Skip ignored directories (§8)
      if (SKIP_DIRS.has(entry.name)) {
        continue;
      }
      results.push(...scanMdFiles(fullPath));
    } else if (entry.isFile() && entry.name.toLowerCase().endsWith('.md')) {
      results.push(normPath(fullPath));
    }
  }

  return results;
}


// ═══════════════════════════════════════════════════════════════════════
// Module: link_extract
// ═══════════════════════════════════════════════════════════════════════

/**
 * Extract all internal links from markdown content.
 *
 * @param {string} content - Full file content.
 * @param {string} _filePath - Absolute path of the source file (unused, API symmetry).
 * @returns {Array<{target: string, line: number, text: string, type: string}>}
 *           Sorted by line number ascending. URL and pure-anchor targets excluded.
 *
 * Called by: main() — per-file scan step.
 */
function linkExtract(content, _filePath) {
  const links = [];

  // Scan each line independently for accurate line numbers (§3)
  const lines = content.split('\n');
  for (let lineNum = 0; lineNum < lines.length; lineNum++) {
    const line = lines[lineNum];
    const lineNo = lineNum + 1;  // 1-indexed

    // Extract standard markdown links: [text](target)
    // 【NON-PORTABLE】 JS RegExp matchAll — Python uses finditer; both iterate all matches
    for (const match of line.matchAll(new RegExp(RE_MD_LINK.source, 'g'))) {
      const target = match[2].trim();
      const text = match[1];
      // Filter: skip URLs and pure anchors (§3 filtering)
      if (shouldSkipTarget(target)) {
        continue;
      }
      // Strip #section suffix (§3)
      const cleanTarget = target.split('#')[0];
      links.push({
        target: cleanTarget,
        line: lineNo,
        text: text,
        type: "markdown",
      });
    }

    // Extract wikilinks: [[target]] or [[target|text]] (§3 type B)
    for (const match of line.matchAll(new RegExp(RE_WIKILINK.source, 'g'))) {
      const target = match[1].trim();
      const alias = match[2];
      const text = alias !== undefined ? alias.trim() : target;
      // Wikilinks don't normally contain URLs, but filter for safety
      if (shouldSkipTarget(target)) {
        continue;
      }
      // Strip #section suffix for consistency
      const cleanTarget = target.split('#')[0];
      links.push({
        target: cleanTarget,
        line: lineNo,
        text: text,
        type: "wikilink",
      });
    }
  }

  // Already in line-order; sort to guarantee
  links.sort((a, b) => a.line - b.line);
  return links;
}


/**
 * Return true if target should be excluded from output.
 *
 * @param {string} target - Raw link target.
 * @returns {boolean} True if target should be skipped.
 *
 * Called by: linkExtract().
 */
function shouldSkipTarget(target) {
  // URL schemes
  for (const prefix of SKIP_PREFIXES) {
    if (target.toLowerCase().startsWith(prefix)) {
      return true;
    }
  }
  // Pure anchor — starts with #, no file path before it
  if (target.startsWith('#')) {
    return true;
  }
  return false;
}


// ═══════════════════════════════════════════════════════════════════════
// Module: link_resolve
// ═══════════════════════════════════════════════════════════════════════

/**
 * Resolve a link target to an absolute path.
 *
 * Path resolution differs by link type (per §5 of check-links design):
 * - markdown links `[text](path)`: resolve relative to source file directory (standard)
 * - wikilinks `[[path]]`: resolve relative to journal-root (Obsidian vault convention)
 *
 * @param {string} target - Raw target from linkExtract.
 * @param {string} sourcePath - Absolute path of the file containing the link (forward slashes).
 * @param {"markdown"|"wikilink"} linkType - Determines resolution base.
 *   markdown: resolve relative to source file directory.
 *   wikilink: resolve relative to journalRoot (Obsidian convention).
 * @param {string} journalRoot - Absolute path of journal root directory.
 * @returns {string} Resolved absolute path with forward slashes.
 *
 * Called by: main() — per-link processing in scan loop.
 */
function linkResolve(target, sourcePath, linkType, journalRoot) {
  // 【NON-PORTABLE】 path.resolve() vs Path.resolve() — both normalize . and ..
  const sourceDir = dirname(sourcePath);

  // Determine resolution base per link type
  const baseDir = linkType === "wikilink"
    // Obsidian convention: wikilinks [[path]] resolve from vault root (journal-root)
    ? journalRoot
    // Standard markdown: [text](path) resolves from source file directory
    : sourceDir;

  // Relative path: resolve against baseDir
  // Absolute path (starts with / or Windows root): resolve from absolute
  if (isAbsolute(target)) {
    return normPath(resolve(target));
  }
  return normPath(resolve(baseDir, target));
}


// ═══════════════════════════════════════════════════════════════════════
// Module: fs_exist_check
// ═══════════════════════════════════════════════════════════════════════

/**
 * Check if path exists on filesystem. Works with forward-slashed paths.
 *
 * @param {string} path - Absolute path to check (forward slashes ok).
 * @returns {boolean} True if path exists (file or directory).
 *
 * Called by: main() — per-link validation in scan loop.
 */
function fsExistCheck(path) {
  try {
    return existsSync(path);
  } catch (_) {
    // Permissions or encoding error → treat as nonexistent
    return false;
  }
}


// ═══════════════════════════════════════════════════════════════════════
// Module: graph_assemble
// ═══════════════════════════════════════════════════════════════════════

/**
 * Assemble link graph from per-file scan results.
 * All paths expected with forward slashes.
 *
 * @param {Array<Object>} fileData - Per-file results from scan loop.
 * @param {string} journalRoot - Absolute path to journal root (forward slashes).
 * @returns {Object} Full graph data structure with summary, broken_links,
 *                   orphan_files, most_referenced, per_file.
 *
 * Called by: main() — dispatch step 4.
 */
function graphAssemble(fileData, journalRoot) {
  const jr = journalRoot.replace(/\/$/, '') + '/';  // ensure trailing slash

  // ── Build inbound (referenced_by) map (§9 step 2) ──
  // inboundMap: resolved_path → [{source: rel_path, line, text}]
  /** @type {Map<string, Array<{source: string, line: number, text: string}>>} */
  const inboundMap = new Map();
  for (const fd of fileData) {
    const sourceRel = fd.rel_path;
    for (const link of fd.links) {
      const resolved = link.resolved;
      if (!inboundMap.has(resolved)) {
        inboundMap.set(resolved, []);
      }
      for (const occ of link.occurrences) {
        inboundMap.get(resolved).push({
          source: sourceRel,
          line: occ.line,
          text: occ.text,
        });
      }
    }
  }

  // ── Compute broken links (§9 step 3) ──
  /** @type {Map<string, {target: string, type: string, occurrences: Array}>} */
  const brokenMap = new Map();
  for (const fd of fileData) {
    for (const link of fd.links) {
      if (!link.exists && link.inside_journal) {
        const key = `${link.target}::${link.type}`;
        if (!brokenMap.has(key)) {
          brokenMap.set(key, { target: link.target, type: link.type, occurrences: [] });
        }
        for (const occ of link.occurrences) {
          brokenMap.get(key).occurrences.push({
            source: fd.rel_path,
            line: occ.line,
            text: occ.text,
          });
        }
      }
    }
  }

  // Sort by target alphabetically
  const brokenLinks = [...brokenMap.values()].sort((a, b) => a.target.localeCompare(b.target));

  // ── Compute orphan files (§9 step 4) ──
  const allRelPaths = new Set(fileData.map(fd => fd.rel_path));
  // Files that are referenced at least once (by resolved path → rel_path)
  const referenced = new Set();
  for (const [resolvedPath] of inboundMap) {
    if (resolvedPath.startsWith(jr)) {
      const rel = resolvedPath.slice(jr.length);
      referenced.add(rel);
    }
  }

  const orphanFiles = [...allRelPaths]
    .filter(p => !referenced.has(p) && p.toLowerCase() !== 'index.md')
    .sort();

  // ── Compute statistics (§9 step 5) ──
  let totalLinks = 0;
  let brokenCount = 0;
  let validCount = 0;
  let externalCount = 0;
  let selfRefsTotal = 0;

  for (const fd of fileData) {
    for (const link of fd.links) {
      totalLinks++;
      if (!link.inside_journal) {
        externalCount++;  // external links
        continue;          // don't count toward valid/broken
      }
      if (link.exists) {
        validCount++;
      } else {
        brokenCount++;
      }
      // Check self-reference
      if (link.resolved === fd.file) {
        selfRefsTotal++;
      }
    }
  }

  // ── Build most_referenced (§9 step 6) ──
  const refCounts = [];
  for (const [resolvedPath, refs] of inboundMap) {
    if (resolvedPath.startsWith(jr)) {
      const rel = resolvedPath.slice(jr.length);
      // Count unique source files
      const uniqueSources = new Set(refs.map(r => r.source));
      refCounts.push({ file: rel, refs: uniqueSources.size });
    }
  }

  // Sort by refs descending, then file ascending; take top 10
  refCounts.sort((a, b) => b.refs - a.refs || a.file.localeCompare(b.file));
  const mostReferenced = refCounts.slice(0, 10);

  // ── Build per_file with referenced_by (§9 output structure) ──
  const perFile = [];
  for (const fd of fileData) {
    const sourceAbs = fd.file;

    // Collect self_refs list for this file
    const selfRefList = [];
    for (const link of fd.links) {
      if (link.resolved === sourceAbs && link.inside_journal) {
        selfRefList.push(link.target);
      }
    }

    // Collect referenced_by for this file
    const fileRefs = inboundMap.get(sourceAbs) || [];
    // Group by source file
    const refBySource = new Map();
    for (const ref of fileRefs) {
      const src = ref.source;
      if (!refBySource.has(src)) {
        refBySource.set(src, []);
      }
      refBySource.get(src).push({ line: ref.line, text: ref.text });
    }

    /** @type {Array<{source: string, occurrences: Array}>} */
    const referencedBy = [];
    for (const src of [...refBySource.keys()].sort()) {
      referencedBy.push({
        source: src,
        occurrences: refBySource.get(src),
      });
    }

    perFile.push({
      file: fd.rel_path,
      self_refs: selfRefList,
      links: fd.links,
      referenced_by: referencedBy,
    });
  }

  // Sort per_file by file path
  perFile.sort((a, b) => a.file.localeCompare(b.file));

  const summary = {
    total_links: totalLinks,
    broken: brokenCount,
    valid: validCount,
    external: externalCount,
    self_refs: selfRefsTotal,
    orphan_files: orphanFiles.length,
  };

  return {
    journal_root: journalRoot,
    files_scanned: fileData.length,
    summary: summary,
    broken_links: brokenLinks,
    orphan_files: orphanFiles,
    most_referenced: mostReferenced,
    per_file: perFile,
  };
}


// ═══════════════════════════════════════════════════════════════════════
// Module: fmt_output
// ═══════════════════════════════════════════════════════════════════════

/**
 * Format graph data for output, applying resolve mode and focus.
 *
 * @param {Object} graphData - Output from graphAssemble.
 * @param {string|Object} resolveMode - "default" | "absolute" | {relative_to: path}.
 * @param {string|null} focusFile - Relative path to focus, or null for full report.
 * @returns {Object} Output object (caller serializes to JSON).
 *
 * Called by: main() — dispatch step 5.
 */
function fmtOutput(graphData, resolveMode, focusFile) {
  const journalRoot = graphData.journal_root;

  // ── Determine resolve root (§10 resolve formatting) ──
  /**
   * Format a resolved path according to resolveMode.
   * @param {string} resolved - Absolute resolved path (forward slashes).
   * @param {string} sourceFile - Source file rel_path (relative to journal_root).
   * @returns {string} Formatted path with forward slashes.
   */
  function formatResolved(resolved, sourceFile) {
    if (resolveMode === 'absolute') {
      return resolved;
    } else if (typeof resolveMode === 'object' && resolveMode.relative_to) {
      // Relative to the specified path
      let base = resolveMode.relative_to;
      try {
        if (statSync(base).isFile()) {
          base = dirname(base);
        }
      } catch (_) {
        // base doesn't exist or can't stat → use as-is
      }
      // 【NON-PORTABLE】 path.relative() vs os.path.relpath — both compute relative
      return normPath(relative(base, resolved));
    } else {
      // Default: relative to source file's directory
      const sourceAbs = resolve(journalRoot, sourceFile);
      const sourceDir = dirname(sourceAbs);
      return normPath(relative(sourceDir, resolved));
    }
  }

  // ── Apply resolve formatting to all links ──
  for (const fd of graphData.per_file) {
    const sourceFile = fd.file;  // rel_path
    for (const link of fd.links) {
      link.resolved = formatResolved(link.resolved, sourceFile);
    }
  }

  // ── Focus or full output ──
  /** @type {Object} */
  let output;
  if (focusFile !== null) {
    // Find the focused file in per_file
    let focused = null;
    for (const fd of graphData.per_file) {
      if (fd.file === focusFile) {
        focused = fd;
        break;
      }
    }

    if (focused === null) {
      process.stderr.write(`${focusFile}: not found under journal-root\n`);
      process.exit(1);
    }

    output = {
      journal_root: journalRoot,
      files_scanned: graphData.files_scanned,
      ...focused,
    };
  } else {
    output = graphData;
  }

  return output;
}


// ═══════════════════════════════════════════════════════════════════════
// Module: parse_args
// ═══════════════════════════════════════════════════════════════════════

/**
 * Parse command-line arguments.
 *
 * @param {string[]} argv - process.argv.slice(2).
 * @returns {{entry: string|null, journal_root: string|null, file: string|null,
 *            absolute: boolean, relative_to: string|null,
 *            no_pretty: boolean, help: boolean}}
 *
 * Called by: main().
 */
function parseArgs(argv) {
  /** @type {Object} */
  const params = {
    entry: null,
    journal_root: null,
    file: null,
    absolute: false,
    relative_to: null,
    no_pretty: false,
    help: false,
  };

  // Track last resolve option for conflict resolution (§2)
  let lastResolve = null;  // "absolute" or "relative_to"

  const positional = [];
  let i = 0;
  while (i < argv.length) {
    const arg = argv[i];

    // Handle options
    if (arg === '--help' || arg === '-h') {
      params.help = true;
      i++;
      continue;
    }

    if (arg === '--journal-root') {
      if (i + 1 >= argv.length) {
        process.stderr.write('--journal-root requires a value\n');
        process.exit(1);
      }
      params.journal_root = argv[i + 1];
      i += 2;
      continue;
    }

    if (arg === '--file') {
      if (i + 1 >= argv.length) {
        process.stderr.write('--file requires a value\n');
        process.exit(1);
      }
      params.file = argv[i + 1];
      i += 2;
      continue;
    }

    if (arg === '--absolute') {
      params.absolute = true;
      lastResolve = 'absolute';
      i++;
      continue;
    }

    if (arg === '--relative-to') {
      if (i + 1 >= argv.length) {
        process.stderr.write('--relative-to requires a value\n');
        process.exit(1);
      }
      params.relative_to = argv[i + 1];
      lastResolve = 'relative_to';
      i += 2;
      continue;
    }

    if (arg === '--no-pretty') {
      params.no_pretty = true;
      i++;
      continue;
    }

    // Positional argument
    if (!arg.startsWith('-')) {
      positional.push(arg);
      i++;
      continue;
    }

    // Unknown option
    process.stderr.write(`unknown option: ${arg}\n`);
    process.stderr.write('Run with --help for usage.\n');
    process.exit(1);
  }

  // ── Validate argument combinations (§2 decision table) ──
  if (positional.length > 0) {
    params.entry = positional[0];
    if (positional.length > 1) {
      process.stderr.write('only one entry path allowed\n');
      process.exit(1);
    }
  }

  // help flag bypasses all validation — print and exit
  if (params.help) {
    return params;
  }

  if (!params.entry && !params.journal_root) {
    process.stderr.write('entry or --journal-root required\n');
    process.stderr.write('Run with --help for usage.\n');
    process.exit(1);
  }

  // Resolve conflict: last option wins (§2)
  if (lastResolve === 'relative_to') {
    params.absolute = false;
  }

  return params;
}


// ═══════════════════════════════════════════════════════════════════════
// Help Text
// ═══════════════════════════════════════════════════════════════════════

const HELP_TEXT = `USAGE: check-links [options] <entry>

Extract all links from journal markdown files, check target existence,
and report inbound/outbound link relationships. Zero dependencies, read-only.

ARGUMENTS:
  <entry>             Path to journal entry point (INDEX.md, any journal file,
                      or directory). Used to auto-discover journal root by
                      searching upward for INDEX.md.

OPTIONS:
  --journal-root <path>
                      Explicit journal root directory (file → uses parent).
                      Required when <entry> is omitted.

  --file <path>       Focus output on a single file's outbound/inbound links.
                      <path> is relative to journal root.

  --absolute          Output resolved paths as absolute paths.

  --relative-to <path>
                      Output resolved paths relative to <path> (file → parent dir).

  --no-pretty         Disable JSON pretty-printing (default: indented).

  --help              Show this help and exit.

EXAMPLES:
  check-links INDEX.md                           # Full journal report
  check-links INDEX.md --file active/note.md     # Focus on single file
  check-links --journal-root .                   # Full journal, from cwd
  check-links INDEX.md --absolute                # Resolved as absolute paths
  check-links INDEX.md --relative-to ../other    # Resolved relative to ../other

Node.js 18+ required.
`;


/**
 * Print full help text and exit 0.
 *
 * Called by: main() when --help is given.
 */
function printHelp() {
  process.stdout.write(HELP_TEXT);
}


// ═══════════════════════════════════════════════════════════════════════
// Entry Point
// ═══════════════════════════════════════════════════════════════════════

/**
 * Parse CLI args, discover journal, scan links, assemble graph, print JSON.
 *
 * dispatch: parseArgs → journalDiscover → targetExpand
 *           → (linkExtract → linkResolve → fsExistCheck) per file
 *           → graphAssemble → fmtOutput → print JSON
 */
function main() {
  const params = parseArgs(process.argv.slice(2));

  if (params.help) {
    printHelp();
    return;
  }

  // ── Step 1: Determine journal_root (normalized to forward slashes) ──
  /** @type {string} */
  let journalRoot;
  if (params.journal_root !== null) {
    // Manual journal_root: resolve to directory
    const jrPath = resolve(params.journal_root);
    let jrStat;
    try {
      jrStat = statSync(jrPath);
    } catch (_) {
      process.stderr.write(`${params.journal_root}: directory not found\n`);
      process.exit(1);
    }
    if (jrStat.isFile()) {
      journalRoot = normPath(dirname(jrPath));
    } else {
      journalRoot = normPath(jrPath);
    }
  } else {
    // Auto-discover from entry
    journalRoot = journalDiscover(params.entry);
  }

  // ── Step 2: Scan all md files ──
  // scanning <N> files under journalRoot
  const allFiles = targetExpand(journalRoot);

  // ── Step 4: Handle --file validation (§2) ──
  let focusFile = null;
  if (params.file) {
    // Resolve --file relative to journal_root
    /** @type {string} */
    let fileAbs;
    if (isAbsolute(params.file)) {
      fileAbs = normPath(resolve(params.file));
    } else {
      fileAbs = normPath(resolve(journalRoot, params.file));
    }

    // Check within journal_root
    if (!fileAbs.startsWith(journalRoot + '/') && fileAbs !== journalRoot) {
      process.stderr.write(`${params.file}: outside journal-root\n`);
      process.exit(1);
    }

    // Check file exists in scan results
    let found = false;
    for (const f of allFiles) {
      if (f === fileAbs) {
        focusFile = fileAbs.slice(journalRoot.length + 1);  // +1 for trailing /
        found = true;
        break;
      }
    }

    if (!found) {
      process.stderr.write(`${params.file}: not found under journal-root\n`);
      process.exit(1);
    }
  }

  // ── Step 5: Per-file scan ──
  // extracting links from <file>
  /** @type {Array<Object>} */
  const fileData = [];
  for (const fpath of allFiles) {
    const relPath = fpath.slice(journalRoot.length + 1);  // strip journal_root/ prefix

    // Read file content
    let content;
    try {
      content = readFileSync(fpath, 'utf-8');
    } catch (e) {
      process.stderr.write(`read error: ${fpath}: ${e.message}\n`);
      continue;
    }

    // Extract links
    const rawLinks = linkExtract(content, fpath);

    // Resolve and check each link
    // Group by target (aggregate occurrences same target)
    /** @type {Map<string, {target: string, type: string, occurrences: Array}>} */
    const linksByTarget = new Map();
    for (const rl of rawLinks) {
      const key = `${rl.target}::${rl.type}`;
      if (!linksByTarget.has(key)) {
        linksByTarget.set(key, {
          target: rl.target,
          type: rl.type,
          occurrences: [],
        });
      }
      linksByTarget.get(key).occurrences.push({
        line: rl.line,
        text: rl.text,
      });
    }

    // Resolve each unique target
    /** @type {Array<Object>} */
    const links = [];
    for (const [, linkInfo] of linksByTarget) {
      const resolved = linkResolve(linkInfo.target, fpath, linkInfo.type, journalRoot);
      const exists = fsExistCheck(resolved);
      const insideJournal = resolved.startsWith(journalRoot + '/') || resolved === journalRoot;

      links.push({
        target: linkInfo.target,
        type: linkInfo.type,
        resolved: resolved,
        exists: exists,
        inside_journal: insideJournal,
        occurrences: linkInfo.occurrences,
      });
    }

    // Sort links by target for consistency
    links.sort((a, b) => a.target.localeCompare(b.target));

    fileData.push({
      file: fpath,  // absolute, normalized with forward slashes
      rel_path: relPath,
      links: links,
    });
  }

  // ── Step 6: Assemble graph ──
  // assembling link graph
  const graphData = graphAssemble(fileData, journalRoot);

  // ── Step 7: Format output ──
  // Determine resolve mode
  /** @type {string|Object} */
  let resolveMode = "default";
  if (params.absolute) {
    resolveMode = "absolute";
  } else if (params.relative_to !== null) {
    resolveMode = { relative_to: params.relative_to };
  }

  // Format output
  const output = fmtOutput(graphData, resolveMode, focusFile);

  // ── Step 8: Print output ──
  // Apply pretty/compact formatting (§10 JSON format)
  const indent = params.no_pretty ? null : 2;
  // Re-serialize for consistent formatting
  const jsonStr = JSON.stringify(output, null, indent);
  process.stdout.write(jsonStr + '\n');
}

main();
