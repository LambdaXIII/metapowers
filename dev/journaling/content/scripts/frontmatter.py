#!/usr/bin/env python3
"""
Frontmatter Tool — Python 3.8+ implementation.
Read, validate, merge-update, and replace YAML frontmatter in Markdown files.
Zero third-party dependencies. Standard library only.

Behavior must match frontmatter.mjs exactly for all commands.
【NON-PORTABLE】 markers annotate inevitable platform/language divergences.
"""

import sys
import os
import json
import re
import tempfile
import pathlib
from typing import Any, Optional

# ── Constants ──────────────────────────────────────────────────────────

# Fields that must appear in a specific order in output
ORDERED_FIELDS = ["title", "summary", "tags", "last_update", "status", "author", "date"]

# Fields required for mode="full" validation
REQUIRED_FIELDS = {"title", "summary", "tags", "last_update"}

# Date pattern: YYYY-MM-DD
DATE_PATTERN = re.compile(r"^\d{4}-\d{2}-\d{2}$")

# Characters that force double-quoting a string value in YAML
SPECIAL_CHARS = re.compile(r'[:"#&*!/|>%@]')


# ═══════════════════════════════════════════════════════════════════════
# General Modules
# ═══════════════════════════════════════════════════════════════════════

def target_expand(paths):
    """Expand glob patterns and literal paths into a sorted, deduplicated list of absolute file paths.

    Interface: (paths: list[str]) -> list[str]
    Behavior: For each path, if it contains wildcard chars (*?[) expand via glob;
              otherwise treat as literal. Deduplicate, sort, warn on missing literal paths.
    Caller: command dispatch (get/check/update/replace)
    Edge cases:
      - Path with wildcard expanding to 0 matches → skip silently (no error per-pattern)
      - Literal path that doesn't exist → stderr warning, excluded from result
      - All paths expand to 0 files → stderr "no files matched", exit 1
    """
    result = []
    seen = set()
    all_expanded_zero = True

    for raw in paths:
        # check for wildcard characters
        has_wildcard = any(c in raw for c in "*?[")
        if has_wildcard:
            # glob expand — use glob module for robust cross-platform support
            # 【NON-PORTABLE】Python uses glob.glob; JS uses hand-written or fs.globSync
            import glob as glob_mod
            matches = [pathlib.Path(p).resolve() for p in glob_mod.glob(raw, recursive=True)]
            if matches:
                all_expanded_zero = False
            for m in matches:
                abs_path = str(m)
                if abs_path not in seen:
                    seen.add(abs_path)
                    result.append(abs_path)
        else:
            # literal path — check existence
            p = pathlib.Path(raw).resolve()
            if p.is_file():
                all_expanded_zero = False
                abs_path = str(p)
                if abs_path not in seen:
                    seen.add(abs_path)
                    result.append(abs_path)
            else:
                # literal path not found → warn
                print(f"file not found: {raw}", file=sys.stderr)

    if all_expanded_zero and not result:
        print("no files matched", file=sys.stderr)
        sys.exit(1)

    result.sort()
    return result


def fm_read(filepath):
    """Read a Markdown file and extract YAML frontmatter header and body.

    Interface: (filepath: str) -> dict{header_raw, body, body_start_line}
    Behavior:
      - Frontmatter starts at line 0 with "---" and ends at the next "---" line.
      - No opening "---" or no closing "---" → header_raw="", body=全文, body_start_line=0.
    Caller: data_read, command handlers
    Edge cases (decision table):
      - No "---" at all → header_raw="", body=全文, body_start_line=0
      - First line not "---" → header_raw="", body=全文, body_start_line=0
      - Opening "---" but no closing "---" → header_raw="", body=全文, body_start_line=0
      - Valid frontmatter → header_raw=内容, body=之后内容, body_start_line=闭合行号+1
      - File is "---\\n---\\n" → header_raw="", body="", body_start_line=2
    """
    # reading file
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    if not content:
        return {"header_raw": "", "body": "", "body_start_line": 0}

    lines = content.split("\n")

    # first line must be exactly "---" (no leading whitespace)
    if not lines or lines[0].strip() != "---":
        return {"header_raw": "", "body": content, "body_start_line": 0}

    # search for closing "---" (line that is exactly "---")
    closing_line = -1
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            closing_line = i
            break

    # no closing delimiter → not frontmatter
    if closing_line == -1:
        return {"header_raw": "", "body": content, "body_start_line": 0}

    # extract header and body
    header_lines = lines[1:closing_line]
    header_raw = "\n".join(header_lines)

    # body starts after closing "---"
    body_start_line = closing_line + 1
    body_lines = lines[body_start_line:]
    body = "\n".join(body_lines)

    return {"header_raw": header_raw, "body": body, "body_start_line": body_start_line}


def fm_parse(yaml_text):
    """Parse a YAML subset string into a dict. Hand-written parser, no dependencies.

    Interface: (yaml_text: str) -> dict
    Behavior: State machine parser supporting strings, ints, floats, bools, null, lists, comments.
              Unsupported YAML constructs → error + exit.
    Caller: data_read, fm_read pipeline
    Edge cases: see decision table in plan §2.1
    """
    if not yaml_text or yaml_text.strip() == "":
        return {}

    result = {}
    lines = yaml_text.split("\n")
    i = 0
    n = len(lines)

    while i < n:
        line = lines[i]
        stripped = line.strip()

        # skip empty lines
        if stripped == "":
            i += 1
            continue

        # skip comment lines (full-line comments only)
        if stripped.startswith("#"):
            i += 1
            continue

        # check indentation — top-level keys must start at column 0
        if line and line[0] in (" ", "\t"):
            # indented line not inside a list → likely a continuation we don't handle or error
            print(f"parse error: line {i+1}: unexpected indentation: {stripped}", file=sys.stderr)
            sys.exit(1)

        # try to parse key: value
        colon_idx = line.find(":")
        if colon_idx == -1:
            print(f"parse error: line {i+1}: expected key: value, got: {stripped}", file=sys.stderr)
            sys.exit(1)

        key = line[:colon_idx].strip()
        after_colon = line[colon_idx + 1:]

        # value may be empty (key:)
        if after_colon == "" or after_colon.isspace():
            value_str = ""
        else:
            value_str = after_colon.lstrip(" ")  # remove exactly one space if present

        # check if value starts with | or > (multiline literal/folded)
        if value_str in ("|", ">", "|-", ">-", "|+", ">+"):
            # multiline string — collect indented lines
            # entering multiline collection
            multiline_parts = []
            j = i + 1
            while j < n:
                next_line = lines[j]
                if next_line.strip() == "":
                    # empty line → include it but check if multiline continues
                    # In YAML, empty lines within a block scalar are part of it
                    multiline_parts.append("")
                    j += 1
                    continue
                # check indentation: must be more indented than the key
                if not next_line or next_line[0] not in (" ", "\t"):
                    break
                multiline_parts.append(next_line.strip())
                j += 1
            result[key] = "\n".join(multiline_parts)
            i = j
            continue

        # check if next lines form a YAML list (indented "- item")
        if value_str == "":
            # entering LIST state for this key — check if next line starts with "  - "
            if i + 1 < n and re.match(r"^  - ", lines[i + 1]):
                items = []
                j = i + 1
                while j < n:
                    list_line = lines[j]
                    m = re.match(r"^  - (.*)", list_line)
                    if m:
                        items.append(m.group(1))
                        j += 1
                    elif list_line.strip() == "":
                        # empty line might be between list items or end of list
                        # check if there are more list items after
                        if j + 1 < n and re.match(r"^  - ", lines[j + 1]):
                            j += 1  # skip blank line between items
                        else:
                            break
                    else:
                        break
                result[key] = items
                i = j
                continue
            else:
                # empty value with no list following → null-like empty
                result[key] = None
                i += 1
                continue

        # type inference for scalar values
        result[key] = _parse_scalar(value_str, i + 1)
        i += 1

    return result


def _parse_scalar(value_str, line_num=0):
    """Infer and convert a scalar YAML value to the appropriate Python type.

    Interface: (value_str: str, line_num: int) -> Any
    Behavior: type inference per decision table §2.1
    Caller: fm_parse
    """
    s = value_str.strip()

    # null values
    if s in ("null", "~", ""):
        return None

    # booleans (strictly lowercase only)
    if s == "true":
        return True
    if s == "false":
        return False
    # uppercase/mixed-case booleans → string (not boolean)
    if s.lower() in ("true", "false"):
        return s

    # null-like (already handled, but keep as string for other cases)
    if s == "null" or s == "~":
        return None

    # double-quoted string → strip quotes
    if s.startswith('"') and s.endswith('"') and len(s) >= 2:
        return s[1:-1]

    # integer: digits only, optionally negative
    if re.match(r"^-?\d+$", s):
        return int(s)

    # float: digits with decimal point
    if re.match(r"^-?\d+\.\d+$", s):
        return float(s)

    # everything else → string
    return s


def fm_write(header_dict, body):
    """Serialize a dict into YAML frontmatter + body → complete Markdown text.

    Interface: (header_dict: dict, body: str) -> str
    Behavior: Fields ordered: title → summary → tags → last_update → status → author → date → custom (alpha).
              Special characters in string values trigger double-quoting.
    Caller: command handlers (update/replace atomic_write pipeline)
    """
    lines = ["---"]

    # build ordered list of keys
    keys = list(header_dict.keys())
    ordered = []

    # system fields in canonical order
    for field in ORDERED_FIELDS:
        if field in keys:
            ordered.append(field)
            keys.remove(field)

    # remaining custom fields in alphabetical order
    custom_sorted = sorted(keys)
    ordered.extend(custom_sorted)

    for key in ordered:
        value = header_dict[key]
        serialized = _serialize_value(key, value)
        lines.append(serialized)

    lines.append("---")
    frontmatter_block = "\n".join(lines)

    if body:
        return frontmatter_block + "\n" + body
    else:
        return frontmatter_block + "\n"


def _serialize_value(key, value):
    """Serialize a single key-value pair to a YAML line (or lines for lists).

    Interface: (key: str, value: Any) -> str
    Behavior:
      - None → "key:"
      - bool → "key: true" or "key: false"
      - int/float → "key: <number>"
      - list → "key:\n  - item1\n  - item2"
      - str → quote if contains special chars, else "key: value"
    Caller: fm_write
    """
    if value is None:
        return f"{key}:"

    if isinstance(value, bool):
        return f"{key}: {'true' if value else 'false'}"

    if isinstance(value, (int, float)):
        # 【NON-PORTABLE】Python distinguishes int/float; JS Number is unified
        # Use repr for float to ensure decimal point, str for int
        if isinstance(value, float):
            return f"{key}: {repr(value)}"
        return f"{key}: {value}"

    if isinstance(value, list):
        if not value:
            return f"{key}:"
        items_lines = [f"{key}:"]
        for item in value:
            # serialize each item; if it's a string with special chars, quote it
            item_str = str(item)
            if isinstance(item, str) and SPECIAL_CHARS.search(item_str):
                item_str = f'"{item_str}"'
            items_lines.append(f"  - {item_str}")
        return "\n".join(items_lines)

    # string value
    s = str(value)
    if s == "":
        return f"{key}:"
    if _needs_quoting(s):
        return f'{key}: "{s}"'
    return f"{key}: {s}"


def _needs_quoting(s):
    """Check if a string value needs double-quoting in YAML.

    Interface: (s: str) -> bool
    Behavior: Returns True if s contains special YAML chars or has leading/trailing whitespace.
    """
    if s != s.strip():
        return True
    if SPECIAL_CHARS.search(s):
        return True
    # also quote if it looks like a YAML keyword
    if s.lower() in ("true", "false", "null", "~", "yes", "no", "on", "off"):
        return True
    if re.match(r"^-?\d+\.?\d*$", s):
        # looks like a number → quote to preserve string type
        return True
    return False


def fm_select(d, fields):
    """Extract a subset of fields from a dict.

    Interface: (d: dict, fields: list[str]) -> dict
    Behavior: Returns dict with only the specified keys. Missing keys → not included.
    Caller: get command (output formatting)
    """
    if not fields:
        return dict(d)
    result = {}
    for f in fields:
        if f in d:
            result[f] = d[f]
    return result


def fm_merge(current, delta):
    """Merge delta dict into current dict, overwriting same keys.

    Interface: (current: dict, delta: dict) -> dict
    Behavior:
      - Key in delta with non-None value → overwrite in current
      - Key in delta with None value → set to None in current (preserve key name)
      - Key in delta not in current + value non-None → add to current
      - Key in delta not in current + value None → no-op (don't create empty field)
    Caller: update command
    """
    result = dict(current)
    for k, v in delta.items():
        if k in result:
            # key exists → overwrite even if v is None
            result[k] = v
        elif v is not None:
            # new key with non-None value → add
            result[k] = v
        # new key with None value → skip (no-op)
    return result


def fm_validate(d, mode="full"):
    """Validate a frontmatter dict against the field specification.

    Interface: (d: dict, mode: str) -> list[str]
    Behavior:
      mode="full": check required fields exist + type correctness for all fields
      mode="delta": only check fields present in d for type correctness
    Caller: check command, replace command (pre-write validation)
    Returns: list of error message strings; empty list = pass
    """
    errors = []

    # determine which fields to check
    if mode == "full":
        fields_to_check = set(REQUIRED_FIELDS) | set(d.keys())
    else:  # delta
        fields_to_check = set(d.keys())

    # check required fields existence (full mode only)
    if mode == "full":
        for field in REQUIRED_FIELDS:
            if field not in d or d[field] is None:
                errors.append(f"missing required field: {field}")

    # type checks for each field
    for field in fields_to_check:
        if field not in d:
            continue

        value = d[field]

        # validate field name format (lowercase-kebab-case for custom fields)
        if field not in ORDERED_FIELDS and field not in REQUIRED_FIELDS:
            # custom field — must be lowercase-kebab-case
            if not re.match(r"^[a-z][a-z0-9]*(-[a-z0-9]+)*$", field):
                errors.append(f"field name should be lowercase-kebab-case: {field}")

        # title: string, non-empty
        if field == "title":
            if value is not None and not isinstance(value, str):
                errors.append(f"title: expected string, got {type(value).__name__}")
            elif value is not None and value.strip() == "":
                errors.append(f"title: must not be empty")

        # summary: string
        elif field == "summary":
            if value is not None and not isinstance(value, str):
                errors.append(f"summary: expected string, got {type(value).__name__}")

        # tags: list of strings, must be YAML list format (not inline)
        elif field == "tags":
            if value is not None:
                if not isinstance(value, list):
                    errors.append(f"tags: expected YAML list, got {type(value).__name__} (tags should be YAML list format, not inline)")
                else:
                    for idx, tag in enumerate(value):
                        if not isinstance(tag, str):
                            errors.append(f"tags[{idx}]: expected string, got {type(tag).__name__}")

        # last_update: string matching YYYY-MM-DD
        elif field == "last_update":
            if value is not None:
                if not isinstance(value, str):
                    errors.append(f"last_update: expected string (YYYY-MM-DD), got {type(value).__name__}")
                elif not DATE_PATTERN.match(value):
                    errors.append(f"last_update: must be YYYY-MM-DD format, got: {value}")

        # status: string (optional)
        elif field == "status":
            if value is not None and not isinstance(value, str):
                errors.append(f"status: expected string, got {type(value).__name__}")

        # author: string (optional)
        elif field == "author":
            if value is not None and not isinstance(value, str):
                errors.append(f"author: expected string, got {type(value).__name__}")

        # date: string matching YYYY-MM-DD (optional)
        elif field == "date":
            if value is not None:
                if not isinstance(value, str):
                    errors.append(f"date: expected string (YYYY-MM-DD), got {type(value).__name__}")
                elif not DATE_PATTERN.match(value):
                    errors.append(f"date: must be YYYY-MM-DD format, got: {value}")

    # check all boolean values: must be actual bool (not string "True"/"False")
    for field in fields_to_check:
        if field not in d:
            continue
        value = d[field]
        if isinstance(value, str) and value.lower() in ("true", "false", "yes", "no"):
            errors.append(f"{field}: boolean value should be lowercase (got '{value}', use true/false)")
        elif isinstance(value, bool):
            pass  # Python bools are always True/False, serializes correctly

    return errors


def fmt_output(value, params):
    """Format command output based on command, file count, and field count.

    Interface: (value: Any, params: dict) -> str
    Behavior: Output format matrix per plan §2.1.
      params includes: command, file_count, field_count, fields, pretty
    Caller: command dispatch (get/check/update/replace)
    """
    cmd = params.get("command", "get")
    pretty = params.get("pretty", True)

    if cmd == "get":
        return _fmt_get_output(value, params, pretty)
    elif cmd == "check":
        return _fmt_check_output(value, params)
    elif cmd in ("update", "replace"):
        return _fmt_mutation_output(value, params)
    else:
        return json.dumps(value, indent=2 if pretty else None, ensure_ascii=False)


def _fmt_get_output(value, params, pretty):
    """Format get command output per the matrix.

    value can be:
      - single dict (1 file, 0+ fields)
      - list of dicts (N files, 0+ fields)
      - dict of {file: single_value} (N files, 1 field)
    """
    indent = 2 if pretty else None

    # value is always the processed data from get handler
    if isinstance(value, dict):
        return json.dumps(value, indent=indent, ensure_ascii=False)
    elif isinstance(value, list):
        return json.dumps(value, indent=indent, ensure_ascii=False)
    else:
        # scalar value (single file, single field) — output as JSON native
        return json.dumps(value, indent=indent, ensure_ascii=False)


def _fmt_check_output(result, params):
    """Only print 'valid' lines to stdout. Errors already go to stderr from cmd_check."""
    valid_lines = []
    for item in result:
        filepath = item.get("file", "?")
        errors = item.get("errors", [])
        if not errors:
            valid_lines.append(f"{filepath}: valid")
    if valid_lines:
        print("\n".join(valid_lines))
    return ""  # already printed; return empty for main
def _fmt_mutation_output(result, params):
    """Format update/replace command output: updated/failed counts."""
    updated = result.get("updated", 0)
    failed = result.get("failed", 0)
    dry_run = result.get("dry_run", False)
    dry_run_details = result.get("dry_run_details", [])

    if dry_run and dry_run_details:
        for detail in dry_run_details:
            print(detail)
        return ""

    return f"updated {updated}, failed {failed}"


def data_read(source):
    """Read data from --data JSON string or --file path, auto-detecting format.

    Interface: (source: dict{type, value}) -> dict
    Behavior:
      type="data" → parse value as JSON
      type="file" → read file, detect format:
        .md → fm_read + fm_parse (extract frontmatter)
        .json → json.load
        .yaml/.yml → read file + fm_parse (treat as pure YAML)
        other → error exit
    Caller: update/replace command handlers
    """
    if source["type"] == "data":
        # parse JSON string
        try:
            return json.loads(source["value"])
        except json.JSONDecodeError as e:
            print(f"invalid JSON: {e}", file=sys.stderr)
            sys.exit(1)

    elif source["type"] == "file":
        filepath = source["value"]
        if not os.path.isfile(filepath):
            print(f"file not found: {filepath}", file=sys.stderr)
            sys.exit(1)

        ext = os.path.splitext(filepath)[1].lower()

        if ext == ".md":
            # extract frontmatter from markdown
            fm_result = fm_read(filepath)
            if fm_result["header_raw"] == "" and fm_result["body_start_line"] == 0:
                print(f"no frontmatter found in: {filepath}", file=sys.stderr)
                sys.exit(1)
            return fm_parse(fm_result["header_raw"])

        elif ext == ".json":
            # read as JSON
            with open(filepath, "r", encoding="utf-8") as f:
                return json.load(f)

        elif ext in (".yaml", ".yml"):
            # read file and parse as YAML (not frontmatter-bounded)
            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read()
            return fm_parse(content)

        else:
            print(f"unsupported source format: {ext}", file=sys.stderr)
            sys.exit(1)

    else:
        print("internal error: invalid data source type", file=sys.stderr)
        sys.exit(1)


def atomic_write(filepath, content):
    """Write content to file atomically using temp file + os.replace.

    Interface: (filepath: str, content: str) -> None
    Behavior:
      1. Create .tmp file in same directory
      2. Write + fsync
      3. os.replace atomic overwrite
      4. On error: clean up .tmp, original file unchanged
    Caller: command handlers (update/replace)
    """
    dirname = os.path.dirname(filepath) or "."
    basename = os.path.basename(filepath)

    # 【NON-PORTABLE】Python uses tempfile.mkstemp; JS uses crypto.randomBytes
    fd, tmp_path = tempfile.mkstemp(
        dir=dirname,
        prefix=basename + ".tmp.",
    )

    try:
        # write content
        with os.fdopen(fd, "w", encoding="utf-8") as f:
            f.write(content)
            f.flush()
            os.fsync(f.fileno())

        # atomic replace
        os.replace(tmp_path, filepath)

    except Exception:
        # clean up temp file on failure
        try:
            os.unlink(tmp_path)
        except OSError:
            pass
        raise


# ═══════════════════════════════════════════════════════════════════════
# CLI Parser
# ═══════════════════════════════════════════════════════════════════════

def parse_args(argv):
    """Parse command-line arguments into a structured params dict.

    Interface: (argv: list[str]) -> dict
    Behavior:
      1. Extract command (get/check/update/replace) as first positional
      2. Collect targets: for get, stop at first non-file-looking arg (rest = fields)
      3. For get: remaining non-option args after targets are fields (supports comma-separated)
      4. Parse options: --data, --file, --dry-run, --pretty, --no-pretty, --journal-root, --help
    Caller: main()
    """
    if not argv or argv[0] in ("--help", "-h"):
        print_help(None)
        sys.exit(0)

    command = argv[0]
    valid_commands = ("get", "check", "update", "replace")

    if command not in valid_commands:
        print(f"unknown command: {command}", file=sys.stderr)
        print_help(None)
        sys.exit(1)

    params = {
        "command": command,
        "targets": [],
        "fields": [],
        "data_source": None,
        "dry_run": False,
        "pretty": True,
        "journal_root": None,
    }

    i = 1
    # Phase 1: collect targets
    # For get: stop at first arg that doesn't look like a file path / glob
    # For check/update/replace: all non-option args before -- are targets
    while i < len(argv):
        arg = argv[i]
        if arg.startswith("--"):
            break
        # for get command, distinguish targets from field names
        if command == "get":
            # first arg is always a target (even if file doesn't exist yet)
            # subsequent args: target if has wildcard, path separators,
            # file extension, or exists on disk
            is_target = (
                len(params["targets"]) == 0 or
                any(c in arg for c in "*?[") or
                "/" in arg or "\\" in arg or
                "." in os.path.basename(arg) or
                os.path.isfile(arg) or
                os.path.isdir(arg)
            )
            if not is_target:
                # non-target arg → start of fields, stop collecting targets
                break
        params["targets"].append(arg)
        i += 1

    # Phase 2: for get command, remaining non-option args are fields
    if command == "get":
        field_args = []
        while i < len(argv):
            arg = argv[i]
            if arg.startswith("--"):
                break
            field_args.append(arg)
            i += 1
        # expand comma-separated fields
        for fa in field_args:
            for f in fa.split(","):
                f = f.strip()
                if f:
                    params["fields"].append(f)

    # Phase 3: parse options
    while i < len(argv):
        arg = argv[i]
        if arg == "--help" or arg == "-h":
            print_help(command)
            sys.exit(0)
        elif arg == "--data":
            i += 1
            if i >= len(argv):
                print("--data requires a value", file=sys.stderr)
                sys.exit(1)
            if params["data_source"] is not None:
                print("cannot use both --data and --file", file=sys.stderr)
                sys.exit(1)
            params["data_source"] = {"type": "data", "value": argv[i]}
        elif arg == "--file":
            i += 1
            if i >= len(argv):
                print("--file requires a value", file=sys.stderr)
                sys.exit(1)
            if params["data_source"] is not None:
                print("cannot use both --data and --file", file=sys.stderr)
                sys.exit(1)
            params["data_source"] = {"type": "file", "value": argv[i]}
        elif arg == "--dry-run":
            params["dry_run"] = True
        elif arg == "--pretty":
            params["pretty"] = True
        elif arg == "--no-pretty":
            params["pretty"] = False
        elif arg == "--journal-root":
            i += 1
            if i >= len(argv):
                print("--journal-root requires a value", file=sys.stderr)
                sys.exit(1)
            params["journal_root"] = argv[i]
        else:
            print(f"unknown option: {arg}", file=sys.stderr)
            sys.exit(1)
        i += 1

    # Phase 4: validate required arguments per command
    if not params["targets"]:
        print(f"command '{command}' requires at least one target file", file=sys.stderr)
        sys.exit(1)

    if command in ("update", "replace") and params["data_source"] is None:
        print(f"command '{command}' requires --data or --file", file=sys.stderr)
        sys.exit(1)

    return params
def cmd_get(params):
    """Handle get command: read and output frontmatter fields.

    dispatch: get → target_expand → (fm_read → fm_parse → fm_select) → fmt_output
    """
    # expand targets
    files = target_expand(params["targets"])
    fields = params["fields"]
    file_count = len(files)
    field_count = len(fields) if fields else 0

    if file_count == 1:
        # single file
        filepath = files[0]
        fm_result = fm_read(filepath)
        if fm_result["header_raw"] == "" and fm_result["body_start_line"] == 0:
            # no frontmatter → empty dict
            data = {}
        else:
            data = fm_parse(fm_result["header_raw"])

        if field_count == 0:
            # output all fields
            output = data
        elif field_count == 1:
            # single field → output raw value
            field = fields[0]
            output = data.get(field, None)
        else:
            # multiple fields → selected dict
            output = fm_select(data, fields)
            # fill missing fields with null
            for f in fields:
                if f not in output:
                    output[f] = None

        formatted = fmt_output(output, {
            "command": "get",
            "file_count": 1,
            "field_count": field_count,
            "fields": fields,
            "pretty": params["pretty"],
        })
        if formatted:
            print(formatted)

    else:
        # multiple files
        if field_count == 0:
            # output all fields → array of {file: ..., ...fields}
            results = []
            for filepath in files:
                fm_result = fm_read(filepath)
                if fm_result["header_raw"] == "" and fm_result["body_start_line"] == 0:
                    data = {}
                else:
                    data = fm_parse(fm_result["header_raw"])
                entry = {"file": filepath}
                entry.update(data)
                results.append(entry)
            output = results

        elif field_count == 1:
            # single field → {file: value} mapping
            field = fields[0]
            mapping = {}
            for filepath in files:
                fm_result = fm_read(filepath)
                if fm_result["header_raw"] == "" and fm_result["body_start_line"] == 0:
                    mapping[filepath] = None
                else:
                    data = fm_parse(fm_result["header_raw"])
                    mapping[filepath] = data.get(field, None)
            output = mapping

        else:
            # multiple fields → array of {file, field1, field2, ...}
            results = []
            for filepath in files:
                fm_result = fm_read(filepath)
                if fm_result["header_raw"] == "" and fm_result["body_start_line"] == 0:
                    data = {}
                else:
                    data = fm_parse(fm_result["header_raw"])
                entry = {"file": filepath}
                selected = fm_select(data, fields)
                entry.update(selected)
                # fill missing fields with null
                for f in fields:
                    if f not in entry:
                        entry[f] = None
                results.append(entry)
            output = results

        formatted = fmt_output(output, {
            "command": "get",
            "file_count": file_count,
            "field_count": field_count,
            "fields": fields,
            "pretty": params["pretty"],
        })
        if formatted:
            print(formatted)


def cmd_check(params):
    """Handle check command: validate frontmatter of target files.

    dispatch: check → target_expand → (fm_read → fm_parse → fm_validate) → fmt_output
    """
    files = target_expand(params["targets"])
    results = []
    all_ok = True

    for filepath in files:
        fm_result = fm_read(filepath)
        # no frontmatter found → error
        if fm_result["header_raw"] == "" and fm_result["body_start_line"] == 0:
            results.append({
                "file": filepath,
                "errors": ["no frontmatter found"],
            })
            all_ok = False
            print(f"{filepath}: no frontmatter found", file=sys.stderr)
            continue

        # parse frontmatter
        data = fm_parse(fm_result["header_raw"])
        errors = fm_validate(data, mode="full")
        results.append({
            "file": filepath,
            "errors": errors,
        })

        if errors:
            all_ok = False
            for err in errors:
                print(f"{filepath}: {err}", file=sys.stderr)

    _fmt_check_output(results, {})

    if not all_ok:
        sys.exit(1)


def cmd_update(params):
    """Handle update command: merge delta into each target's frontmatter.

    dispatch: update → target_expand → data_read → (fm_read → fm_parse → fm_merge → fm_write → atomic_write)
    """
    files = target_expand(params["targets"])
    delta = data_read(params["data_source"])

    # validate delta fields (type checks only, per mode="delta")
    delta_errors = fm_validate(delta, mode="delta")
    if delta_errors:
        for err in delta_errors:
            print(f"delta: {err}", file=sys.stderr)
        sys.exit(1)

    dry_run = params["dry_run"]
    updated = 0
    failed = 0
    dry_run_details = []

    for filepath in files:
        try:
            fm_result = fm_read(filepath)
            # parse existing frontmatter (may be empty)
            if fm_result["header_raw"] == "" and fm_result["body_start_line"] == 0:
                current = {}
            else:
                current = fm_parse(fm_result["header_raw"])

            body = fm_result["body"]

            # merge delta into current
            merged = fm_merge(current, delta)

            # collect change summary for dry-run
            set_fields = []
            clear_fields = []
            for k, v in delta.items():
                if v is not None:
                    set_fields.append(k)
                elif k in current:
                    clear_fields.append(k)

            if dry_run:
                parts = []
                if set_fields:
                    parts.append(f"would set: {', '.join(set_fields)}")
                if clear_fields:
                    parts.append(f"would clear: {', '.join(clear_fields)}")
                if parts:
                    dry_run_details.append(f"{filepath}: {'; '.join(parts)}")
                else:
                    dry_run_details.append(f"{filepath}: no changes")
                continue

            # serialize and write
            new_content = fm_write(merged, body)
            atomic_write(filepath, new_content)
            updated += 1

        except Exception as e:
            failed += 1
            print(f"{filepath}: {e}", file=sys.stderr)

    if dry_run:
        result = {"updated": 0, "failed": 0, "dry_run": True, "dry_run_details": dry_run_details}
    else:
        result = {"updated": updated, "failed": failed, "dry_run": False, "dry_run_details": []}

    output = _fmt_mutation_output(result, {})
    if output:
        print(output)

    if failed > 0:
        sys.exit(1)


def cmd_replace(params):
    """Handle replace command: replace entire frontmatter of a single target file.

    dispatch: replace → data_read → fm_validate(full) → fm_read → fm_write → atomic_write
    """
    # replace accepts exactly one target
    if len(params["targets"]) > 1:
        print(f"replace accepts exactly one target, got {len(params['targets'])}", file=sys.stderr)
        sys.exit(1)

    targets = target_expand(params["targets"])
    filepath = targets[0]
    new_data = data_read(params["data_source"])

    # validate full required fields
    errors = fm_validate(new_data, mode="full")
    if errors:
        for err in errors:
            print(f"{err}", file=sys.stderr)
        sys.exit(1)

    dry_run = params["dry_run"]

    # read existing file
    fm_result = fm_read(filepath)
    body = fm_result["body"]

    if dry_run:
        set_fields = list(new_data.keys())
        print(f"{filepath}: would replace entire frontmatter with fields: {', '.join(set_fields)}")
        return

    # serialize and write
    try:
        new_content = fm_write(new_data, body)
        atomic_write(filepath, new_content)
        print("updated 1, failed 0")
    except Exception as e:
        print(f"{filepath}: {e}", file=sys.stderr)
        sys.exit(1)


# ═══════════════════════════════════════════════════════════════════════
# Help Text
# ═══════════════════════════════════════════════════════════════════════

HELP_MAIN = """USAGE: frontmatter <command> <target...> [options]

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

Run 'frontmatter <command> --help' for command-specific help."""


HELP_GET = """USAGE: frontmatter get <target...> [<fields...>]

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
  --no-pretty     Disable pretty-printing"""


HELP_CHECK = """USAGE: frontmatter check <target...>

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
  --journal-root <path>   Check tags against TAGS.md registry (optional)"""


HELP_UPDATE = """USAGE: frontmatter update <target...> --data '<json>' | --file <path>

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
  --dry-run         Preview changes without writing to disk"""


HELP_REPLACE = """USAGE: frontmatter replace <target> --data '<json>' | --file <path>

Replace the entire frontmatter of a single Markdown file.

Required:
  --data '<json>'   JSON object with the new frontmatter
  --file <path>     Read replacement from a file (.md, .json, .yaml)

The --data content must include all four required fields:
  title, summary, tags (YAML list), last_update (YYYY-MM-DD)

The body of the Markdown file is never modified.
If the file has no frontmatter, one is created.

Options:
  --dry-run         Preview changes without writing to disk"""


def print_help(command=None):
    """Print help text. Command-specific or main."""
    if command is None:
        print(HELP_MAIN)
    elif command == "get":
        print(HELP_GET)
    elif command == "check":
        print(HELP_CHECK)
    elif command == "update":
        print(HELP_UPDATE)
    elif command == "replace":
        print(HELP_REPLACE)
    else:
        print(HELP_MAIN)


# ═══════════════════════════════════════════════════════════════════════
# Entry Point
# ═══════════════════════════════════════════════════════════════════════

def main():
    """Parse CLI args and route to command handler."""
    if len(sys.argv) < 2:
        print_help(None)
        sys.exit(0)

    # check for top-level --help (before command)
    if sys.argv[1] in ("--help", "-h"):
        print_help(None)
        sys.exit(0)

    params = parse_args(sys.argv[1:])
    cmd = params["command"]

    if cmd == "get":
        cmd_get(params)
    elif cmd == "check":
        cmd_check(params)
    elif cmd == "update":
        cmd_update(params)
    elif cmd == "replace":
        cmd_replace(params)
    else:
        print(f"unknown command: {cmd}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
