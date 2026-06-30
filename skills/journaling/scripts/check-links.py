#!/usr/bin/env python3
"""
check-links — Journal link checker.

Extracts all links from journal markdown files, checks target existence,
and reports inbound/outbound link relationships. Zero third-party
dependencies. Pure read-only — never modifies journal files.

Usage:
  check-links [options] <entry>
  check-links --journal-root <path> [--file <path>]

Python 3.8+ required. See --help for full options.
"""

import sys
import os
import os.path
import re
import json
from pathlib import Path

# ── Constants ──────────────────────────────────────────────────────────

# Patterns for link extraction (§3)
# Standard markdown link: [text](target)
RE_MD_LINK = re.compile(r"\[([^\]]*)\]\(([^)]+)\)")
# Obsidian wikilink: [[target]] or [[target|text]]
RE_WIKILINK = re.compile(r"\[\[([^\]|]+)(?:\|([^\]]*))?\]\]")

# URL schemes that are skipped
SKIP_PREFIXES = ("https://", "http://", "ftp://", "mailto:")

# Directories to skip during file scan
SKIP_DIRS = {".git", "__pycache__", ".obsidian", "node_modules"}


# ═══════════════════════════════════════════════════════════════════════
# Module: journal_discover
# ═══════════════════════════════════════════════════════════════════════

def journal_discover(entry):
    """Find journal root by searching upward from entry for INDEX.md.

    Args:
        entry (str): Path to a file or directory inside the journal.

    Returns:
        str: Absolute path to journal root directory.

    Raises:
        SystemExit: If entry doesn't exist or INDEX.md not found in ancestors.

    Called by: main() — dispatch step 1.
    """
    # Resolve entry to absolute path (§2 auto-discovery rule)
    # 【NON-PORTABLE】 pathlib.Path.resolve() behavior differs from Node path.resolve()
    entry_path = Path(entry).resolve()

    if not entry_path.exists():
        print(f"{entry}: file not found", file=sys.stderr)
        sys.exit(1)

    # Start directory: current directory for discovery
    # If entry is INDEX.md, start from its parent (the journal root)
    # If entry is a directory, start from that directory
    # If entry is a regular file, start from its parent directory
    if entry_path.name.lower() in ("index.md",):
        journal_root = entry_path.parent
    elif entry_path.is_dir():
        journal_root = entry_path
    else:
        journal_root = entry_path.parent

    # Walk upward looking for INDEX.md or index.md (§2 auto-discovery)
    current = journal_root
    while True:
        # Check exact case-insensitive matches only
        for name in ("INDEX.md", "index.md"):
            candidate = current / name
            if candidate.is_file():
                return str(current)
        # Move up one level
        parent = current.parent
        if parent == current:
            # Reached filesystem root
            print(f"INDEX.md not found in ancestors of {entry}", file=sys.stderr)
            sys.exit(1)
        current = parent


# ═══════════════════════════════════════════════════════════════════════
# Module: target_expand
# ═══════════════════════════════════════════════════════════════════════

def target_expand(journal_root):
    """Recursively find all .md files under journal_root.

    Args:
        journal_root (str): Absolute path to journal root.

    Returns:
        list[str]: Sorted list of absolute paths to .md files (alphabetical),
                   excluding SKIP_DIRS. Empty list raises SystemExit.

    Raises:
        SystemExit: If no .md files found.

    Called by: main() — dispatch step 2.
    """
    result = []
    journal_path = Path(journal_root)

    # Recursive walk with .gitignore/style skip dirs (§8)
    try:
        for dirpath_str, dirnames, filenames in os.walk(journal_root):
            dirpath = Path(dirpath_str)
            # Filter out skip directories before descent
            dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
            for fname in filenames:
                if fname.lower().endswith(".md"):
                    result.append(str(dirpath / fname))
    except OSError as e:
        print(f"scan error: {e}", file=sys.stderr)
        sys.exit(1)

    if not result:
        print(f"no markdown files found under {journal_root}", file=sys.stderr)
        sys.exit(1)

    # Deduplicate (shouldn't be needed but safe) and sort alphabetically
    result = sorted(set(result))
    return result


# ═══════════════════════════════════════════════════════════════════════
# Module: link_extract
# ═══════════════════════════════════════════════════════════════════════

def link_extract(content, file_path):
    """Extract all internal links from markdown content.

    Args:
        content (str): Full file content.
        file_path (str): Absolute path of the source file (unused, kept for API symmetry).

    Returns:
        list[dict]: Each dict has {target, line, text, type}.
                    Sorted by line number ascending.
                    URL and pure-anchor targets are excluded.

    Called by: main() — per-file scan step.
    """
    links = []

    # Scan each line independently to get accurate line numbers (§3)
    for line_num, line in enumerate(content.split("\n"), start=1):
        # Extract standard markdown links: [text](target)
        for m in RE_MD_LINK.finditer(line):
            target = m.group(2).strip()
            text = m.group(1)
            # Filter: skip URLs and pure anchors (§3 filtering)
            if _should_skip_target(target):
                continue
            # Strip #section suffix (§3)
            target = target.split("#")[0]
            links.append({
                "target": target,
                "line": line_num,
                "text": text,
                "type": "markdown",
            })

        # Extract wikilinks: [[target]] or [[target|text]] (§3 type B)
        for m in RE_WIKILINK.finditer(line):
            target = m.group(1).strip()
            alias = m.group(2)
            text = alias.strip() if alias is not None else target
            # Wikilinks don't normally contain URLs, but filter for safety
            if _should_skip_target(target):
                continue
            # Strip #section suffix for consistency
            target = target.split("#")[0]
            links.append({
                "target": target,
                "line": line_num,
                "text": text,
                "type": "wikilink",
            })

    # Already in line-order due to sequential scanning; enforce sort
    links.sort(key=lambda x: x["line"])
    return links


def _should_skip_target(target):
    """Return True if target should be excluded from output.

    Skips: URLs (http/https/ftp/mailto) and pure anchors (#section).

    Args:
        target (str): Raw link target.

    Returns:
        bool: True if target should be skipped.

    Called by: link_extract().
    """
    # URL schemes
    for prefix in SKIP_PREFIXES:
        if target.lower().startswith(prefix):
            return True
    # Pure anchor — starts with #, no file path before it
    if target.startswith("#"):
        return True
    return False


# ═══════════════════════════════════════════════════════════════════════
# Module: link_resolve
# ═══════════════════════════════════════════════════════════════════════

def link_resolve(target, source_path, link_type, journal_root):
    """Resolve a link target to an absolute path.

    Path resolution differs by link type (per §5 of check-links design):
    - markdown links [text](path): resolve relative to source file directory (standard)
    - wikilinks [[path]]: resolve relative to journal-root (Obsidian vault convention)

    Args:
        target (str): Raw target from link_extract.
        source_path (str): Absolute path of the file containing the link.
        link_type (str): "markdown" or "wikilink" — determines resolution base.
            markdown: resolve relative to source file directory.
            wikilink: resolve relative to journal_root (Obsidian convention).
        journal_root (str): Absolute path of journal root directory.

    Returns:
        str: Resolved absolute path (normalized, no symlink expansion).

    Called by: main() — per-link processing in scan loop.
    """
    # 【NON-PORTABLE】 Path.resolve() vs Node path.resolve() — both normalize . and ..
    source_dir = Path(source_path).parent

    # Determine resolution base per link type
    if link_type == "wikilink":
        # Obsidian convention: wikilinks [[path]] resolve from vault root (journal-root)
        base_dir = Path(journal_root)
    else:
        # Standard markdown: [text](path) resolves from source file directory
        base_dir = source_dir

    # Relative path: resolve against base_dir
    # Absolute path (starts with /): resolve from filesystem root
    if target.startswith("/"):
        # Absolute path within journal
        resolved = Path(target).resolve()
    else:
        resolved = (base_dir / target).resolve()
    return str(resolved)


# ═══════════════════════════════════════════════════════════════════════
# Module: fs_exist_check
# ═══════════════════════════════════════════════════════════════════════

def fs_exist_check(path):
    """Check if path exists on filesystem.

    Args:
        path (str): Absolute path to check.

    Returns:
        bool: True if path exists (file or directory). False on error or nonexistence.

    Called by: main() — per-link validation in scan loop.
    """
    try:
        return os.path.exists(path)
    except (OSError, ValueError):
        # Permissions or encoding error → treat as nonexistent
        return False


# ═══════════════════════════════════════════════════════════════════════
# Module: graph_assemble
# ═══════════════════════════════════════════════════════════════════════

def graph_assemble(file_data, journal_root):
    """Assemble link graph from per-file scan results.

    Args:
        file_data (list[dict]): Per-file results from scan loop.
            Each: {file (abs), rel_path, links: [{target, type, resolved, exists,
                   inside_journal, occurrences: [{line, text}]}]}
        journal_root (str): Absolute path to journal root.

    Returns:
        dict: Full graph data structure with summary, broken_links, orphan_files,
              most_referenced, per_file.

    Called by: main() — dispatch step 4.
    """
    jr = journal_root.rstrip("/\\").replace("\\", "/") + "/"

    # Normalize all paths in file_data to forward slashes for comparison
    for fd in file_data:
        fd["file"] = fd["file"].replace("\\", "/")
        for link in fd["links"]:
            link["resolved"] = link["resolved"].replace("\\", "/")

    # ── Build inbound (referenced_by) map (§9 step 2) ──
    # inbound_map: resolved_path → [{source: rel_path, line, text}]
    inbound_map = {}
    for fd in file_data:
        source_rel = fd["rel_path"]
        for link in fd["links"]:
            resolved = link["resolved"]
            if resolved not in inbound_map:
                inbound_map[resolved] = []
            for occ in link["occurrences"]:
                inbound_map[resolved].append({
                    "source": source_rel,
                    "line": occ["line"],
                    "text": occ["text"],
                })

    # ── Compute broken links (§9 step 3) ──
    broken_map = {}
    for fd in file_data:
        for link in fd["links"]:
            if not link["exists"] and link["inside_journal"]:
                key = (link["target"], link["type"])
                if key not in broken_map:
                    broken_map[key] = []
                for occ in link["occurrences"]:
                    broken_map[key].append({
                        "source": fd["rel_path"],
                        "line": occ["line"],
                        "text": occ["text"],
                    })

    broken_links = []
    for (target, typ), occurrences in sorted(broken_map.items(), key=lambda x: x[0][0]):
        broken_links.append({
            "target": target,
            "type": typ,
            "occurrences": occurrences,
        })

    # ── Compute orphan files (§9 step 4) ──
    all_rel_paths = {fd["rel_path"] for fd in file_data}
    # Files that are referenced at least once (by resolved path)
    referenced = set()
    for resolved_path in inbound_map:
        # Convert resolved absolute path to rel_path for comparison
        if resolved_path.startswith(jr):
            rel = resolved_path[len(jr):].replace("\\", "/")
            referenced.add(rel)

    orphan_files = sorted(all_rel_paths - referenced - {"index.md", "INDEX.md"})

    # ── Compute self_refs (§9 step 1-5) ──
    total_links = 0
    broken_count = 0
    valid_count = 0
    external_count = 0
    self_refs_total = 0

    for fd in file_data:
        for link in fd["links"]:
            total_links += 1
            if not link["inside_journal"]:
                external_count += 1
                continue  # external links don't count toward valid/broken
            if link["exists"]:
                valid_count += 1
            else:
                broken_count += 1
            # Check self-reference
            if link["resolved"] == fd["file"]:
                self_refs_total += 1

    # ── Build most_referenced (§9 step 6) ──
    ref_counts = []
    for resolved_path, refs in inbound_map.items():
        if resolved_path.startswith(jr):
            rel = resolved_path[len(jr):].replace("\\", "/")
            # Count unique source files
            unique_sources = len(set(r["source"] for r in refs))
            ref_counts.append({"file": rel, "refs": unique_sources})

    # Sort by refs descending, then file ascending; take top 10
    ref_counts.sort(key=lambda x: (-x["refs"], x["file"].lower()))
    most_referenced = ref_counts[:10]

    # ── Build per_file with referenced_by (§9 output structure) ──
    per_file = []
    for fd in file_data:
        source_abs = fd["file"]
        # Collect self_refs list for this file
        self_ref_list = []
        for link in fd["links"]:
            if link["resolved"] == source_abs and link["inside_journal"]:
                self_ref_list.append(link["target"])

        # Collect referenced_by for this file
        file_refs = inbound_map.get(source_abs, [])
        # Group by source file
        ref_by_source = {}
        for ref in file_refs:
            src = ref["source"]
            if src not in ref_by_source:
                ref_by_source[src] = []
            ref_by_source[src].append({"line": ref["line"], "text": ref["text"]})

        referenced_by = []
        for src in sorted(ref_by_source.keys()):
            referenced_by.append({
                "source": src,
                "occurrences": ref_by_source[src],
            })

        per_file.append({
            "file": fd["rel_path"],
            "self_refs": self_ref_list,
            "links": fd["links"],
            "referenced_by": referenced_by,
        })

    # Sort per_file by file path
    per_file.sort(key=lambda x: x["file"].lower())

    summary = {
        "total_links": total_links,
        "broken": broken_count,
        "valid": valid_count,
        "external": external_count,
        "self_refs": self_refs_total,
        "orphan_files": len(orphan_files),
    }

    return {
        "journal_root": journal_root,
        "files_scanned": len(file_data),
        "summary": summary,
        "broken_links": broken_links,
        "orphan_files": orphan_files,
        "most_referenced": most_referenced,
        "per_file": per_file,
    }


# ═══════════════════════════════════════════════════════════════════════
# Module: fmt_output
# ═══════════════════════════════════════════════════════════════════════

def fmt_output(graph_data, resolve_mode, focus_file):
    """Format graph data for output, applying resolve mode and focus.

    Args:
        graph_data (dict): Output from graph_assemble.
        resolve_mode: "default" | "absolute" | {"relative_to": path}.
        focus_file (str | None): Relative path to focus, or None for full report.

    Returns:
        str: JSON string for stdout.

    Called by: main() — dispatch step 5.
    """
    journal_root = graph_data["journal_root"]
    jr = journal_root.rstrip("/\\") + os.sep

    # ── Determine resolve root (§10 resolve formatting) ──
    def format_resolved(resolved, source_file):
        """Format a resolved path according to resolve_mode."""
        if resolve_mode == "absolute":
            return resolved
        elif isinstance(resolve_mode, dict) and "relative_to" in resolve_mode:
            # Relative to the specified path
            base = resolve_mode["relative_to"]
            base_path = Path(base)
            if not base_path.is_dir():
                base_path = base_path.parent
            # 【NON-PORTABLE】 PurePosixPath behavior — use os.path.relpath
            try:
                return os.path.relpath(resolved, str(base_path)).replace("\\", "/")
            except ValueError:
                return resolved
        else:
            # Default: relative to source file's directory
            source_dir = str(Path(source_file).parent)
            try:
                return os.path.relpath(resolved, source_dir).replace("\\", "/")
            except ValueError:
                return resolved

    # ── Apply resolve formatting to all links ──
    for fd in graph_data["per_file"]:
        source_file = fd["file"]  # this is rel_path in per_file
        # Convert rel_path to absolute for resolve formatting
        source_abs = str(Path(journal_root) / source_file)
        for link in fd["links"]:
            link["resolved"] = format_resolved(link["resolved"], source_abs)

    # ── Focus or full output ──
    if focus_file is not None:
        # Find the focused file in per_file
        focused = None
        for fd in graph_data["per_file"]:
            if fd["file"] == focus_file:
                focused = fd
                break

        if focused is None:
            print(f"{focus_file}: not found under journal-root", file=sys.stderr)
            sys.exit(1)

        output = {
            "journal_root": journal_root,
            "files_scanned": graph_data["files_scanned"],
        }
        output.update(focused)
    else:
        output = graph_data

    return json.dumps(output, indent=2, ensure_ascii=False)


# ═══════════════════════════════════════════════════════════════════════
# Module: parse_args
# ═══════════════════════════════════════════════════════════════════════

def parse_args(argv):
    """Parse command-line arguments.

    Args:
        argv (list[str]): sys.argv[1:] or equivalent.

    Returns:
        dict: Parsed options: {entry, journal_root, file, absolute, relative_to,
              no_pretty, help}.

    Called by: main().
    """
    params = {
        "entry": None,          # positional entry path (may be None)
        "journal_root": None,   # manual journal root
        "file": None,           # focus file path (relative to journal-root)
        "absolute": False,      # output resolved as absolute paths
        "relative_to": None,    # resolve relative to this path
        "no_pretty": False,     # disable JSON indentation
        "help": False,          # print help and exit
    }

    # Track last resolve option for conflict resolution (§2)
    last_resolve = None  # "absolute" or "relative_to"

    i = 0
    positional = []
    while i < len(argv):
        arg = argv[i]

        # Handle options
        if arg in ("--help", "-h"):
            params["help"] = True
            i += 1
            continue

        if arg == "--journal-root":
            if i + 1 >= len(argv):
                print("--journal-root requires a value", file=sys.stderr)
                sys.exit(1)
            params["journal_root"] = argv[i + 1]
            i += 2
            continue

        if arg == "--file":
            if i + 1 >= len(argv):
                print("--file requires a value", file=sys.stderr)
            params["file"] = argv[i + 1]
            i += 2
            continue

        if arg == "--absolute":
            params["absolute"] = True
            last_resolve = "absolute"
            i += 1
            continue

        if arg == "--relative-to":
            if i + 1 >= len(argv):
                print("--relative-to requires a value", file=sys.stderr)
                sys.exit(1)
            params["relative_to"] = argv[i + 1]
            last_resolve = "relative_to"
            i += 2
            continue

        if arg == "--no-pretty":
            params["no_pretty"] = True
            i += 1
            continue

        # Positional argument
        if not arg.startswith("-"):
            positional.append(arg)
            i += 1
            continue

        # Unknown option
        print(f"unknown option: {arg}", file=sys.stderr)
        print("Run with --help for usage.", file=sys.stderr)
        sys.exit(1)

    # ── Validate argument combinations (§2 decision table) ──
    if positional:
        params["entry"] = positional[0]
        if len(positional) > 1:
            print("only one entry path allowed", file=sys.stderr)
            sys.exit(1)

    # help flag bypasses all validation — print and exit
    if params["help"]:
        return params

    if not params["entry"] and not params["journal_root"]:
        print("entry or --journal-root required", file=sys.stderr)
        print("Run with --help for usage.", file=sys.stderr)
        sys.exit(1)

    # Resolve conflict: last option wins (§2)
    if last_resolve == "relative_to":
        params["absolute"] = False

    return params


# ═══════════════════════════════════════════════════════════════════════
# Help Text
# ═══════════════════════════════════════════════════════════════════════

HELP_TEXT = """USAGE: check-links [options] <entry>

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

Node.js 18+ required for check-links.mjs counterpart.
"""


def print_help():
    """Print full help text and exit 0.

    Called by: main() when --help is given.
    """
    print(HELP_TEXT)


# ═══════════════════════════════════════════════════════════════════════
# Entry Point
# ═══════════════════════════════════════════════════════════════════════

def main():
    """Parse CLI args, discover journal, scan links, assemble graph, print JSON.

    dispatch: parse_args → journal_discover → target_expand
              → (link_extract → link_resolve → fs_exist_check) per file
              → graph_assemble → fmt_output → print JSON
    """
    params = parse_args(sys.argv[1:])

    if params["help"]:
        print_help()
        return

    # ── Step 1: Determine journal_root ──
    if params["journal_root"] is not None:
        # Manual journal_root: resolve to directory
        jr_path = Path(params["journal_root"]).resolve()
        if jr_path.is_file():
            journal_root = str(jr_path.parent)
        else:
            journal_root = str(jr_path).replace("\\", "/")
        if not os.path.isdir(journal_root):
            print(f"{params['journal_root']}: directory not found", file=sys.stderr)
            sys.exit(1)
    else:
        # Auto-discover from entry
        journal_root = journal_discover(params["entry"])

    # Normalize path separators for cross-platform output consistency
    journal_root = journal_root.replace("\\", "/")

    # ── Step 2: Scan all md files ──
    # scanning <N> files under journal_root
    all_files = target_expand(journal_root)

    # ── Step 3: Determine entry focus ──
    entry_path = None
    if params["entry"]:
        entry_path = str(Path(params["entry"]).resolve())

    # ── Step 4: Handle --file validation (§2) ──
    focus_file = None
    if params["file"]:
        # Resolve --file relative to journal_root
        file_path = Path(params["file"])
        if file_path.is_absolute():
            file_abs = str(file_path)
        else:
            file_abs = str(Path(journal_root) / params["file"])

        # Normalize for comparison
        file_abs_resolved = str(Path(file_abs).resolve())

        # Check within journal_root
        jr = str(Path(journal_root).resolve())
        if not file_abs_resolved.startswith(jr + os.sep) and file_abs_resolved != jr:
            print(f"{params['file']}: outside journal-root", file=sys.stderr)
            sys.exit(1)

        # Check file exists in scan results
        found = False
        for f in all_files:
            if str(Path(f).resolve()) == file_abs_resolved:
                focus_file = os.path.relpath(f, journal_root).replace("\\", "/")
                found = True
                break

        if not found:
            print(f"{params['file']}: not found under journal-root", file=sys.stderr)
            sys.exit(1)

    # ── Step 5: Per-file scan ──
    # extracting links from <file>
    file_data = []
    for fpath in all_files:
        rel_path = os.path.relpath(fpath, journal_root).replace("\\", "/")

        # Read file content
        try:
            with open(fpath, "r", encoding="utf-8") as fh:
                content = fh.read()
        except (OSError, UnicodeDecodeError) as e:
            print(f"read error: {fpath}: {e}", file=sys.stderr)
            continue

        # Extract links
        raw_links = link_extract(content, fpath)

        # Resolve and check each link
        # Group by target (aggregate occurrences same target)
        links_by_target = {}
        for rl in raw_links:
            key = (rl["target"], rl["type"])
            if key not in links_by_target:
                links_by_target[key] = {
                    "target": rl["target"],
                    "type": rl["type"],
                    "occurrences": [],
                }
            links_by_target[key]["occurrences"].append({
                "line": rl["line"],
                "text": rl["text"],
            })

        # Resolve each unique target
        links = []
        for (target, typ), link_info in links_by_target.items():
            resolved = link_resolve(target, fpath, typ, journal_root).replace("\\", "/")
            exists = fs_exist_check(resolved)
            inside_journal = resolved.startswith(
                journal_root + "/"
            ) or resolved == journal_root

            links.append({
                "target": target,
                "type": typ,
                "resolved": resolved,
                "exists": exists,
                "inside_journal": inside_journal,
                "occurrences": link_info["occurrences"],
            })

        # Sort links by target for consistency
        links.sort(key=lambda x: x["target"])

        file_data.append({
            "file": str(Path(fpath).resolve()).replace("\\", "/"),
            "rel_path": rel_path,
            "links": links,
        })

    # ── Step 6: Assemble graph ──
    # assembling link graph
    graph_data = graph_assemble(file_data, journal_root)

    # ── Step 7: Format output ──
    # Determine resolve mode
    if params["absolute"]:
        resolve_mode = "absolute"
    elif params["relative_to"] is not None:
        resolve_mode = {"relative_to": params["relative_to"]}
    else:
        resolve_mode = "default"

    # Format output
    json_str = fmt_output(graph_data, resolve_mode, focus_file)

    # ── Step 8: Print output ──
    # Apply pretty/compact formatting (§10 JSON format)
    if params["no_pretty"]:
        # Re-serialize without indentation
        data = json.loads(json_str)
        json_str = json.dumps(data, indent=None, ensure_ascii=False)

    print(json_str)


if __name__ == "__main__":
    main()
