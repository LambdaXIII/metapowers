---
name: journaling
description: |
  MUST load before any write operation to <journal-root> (create, edit, move,
  archive, delete, etc.), including journal operations the user requests
  directly. No need to load for read-only access to journal content.

  Examples of write operations:
  - Creating a new journal
  - Writing, editing, moving, archiving, or deleting journal entries
  - Maintaining / organizing the journal
  - Writing design decisions confirmed in discussion into journal files

  Write operations include: 创建/写入/编辑/移动/归档/删除 journal 条目、
  维护/整理 journal、将讨论中确认的设计决策写入 journal 文件。
metadata:
  version: "5.0.4"
  last_updated: "2026-08-23"
---

# Journaling

A journal is your structured long-term memory mechanism — experience, decisions, research, and methodology accumulated across sessions. With a journal, a later session can continue directly from where an earlier one stopped: read state, pick up work, avoid past pitfalls.

## The Journal

The journal lives at `<journal-root>` and consists of:

- **INDEX.md** — cover page and dashboard. The journal's single entry point; shows current state signals. Every journal operation starts here.
- **Rules document (RULES.md)** — single entry point for rules; defines how this journal operates: INDEX structure, classification, note metadata fields, writing conventions, etc. Content is defined by the journal itself; the seed provides the initial scheme.
- **Entries** — individual notes. Entry organization (directories, lifecycle, etc.) is defined by journal rules.

---

## Before You Begin

This skill's protocols depend on `<journal-root>/INDEX.md` context — the journal's current state and operating context (what's in progress, what needs attention, what you've learned before). If you have not read INDEX.md this session, open it now.

Operating without INDEX.md means operating blind.

| Protocol | When to use | Load |
|----------|-------------|------|
| Init protocol | Creating a new journal | `references/protocal-init.md` |
| Write protocol | Writing entries | `references/protocal-write.md` |
| Import protocol | Importing external content | `references/protocal-import.md` |
| Maintenance protocol | Maintaining / organizing the journal | `references/protocal-maintenance.md` |

Other reference documents load on demand per the references within each protocol.

## Linked Files
- [Init Protocol](references/protocal-init.md)
- [Discovery Contract Design Guide](references/design-discovery-contract.md)
- [Write Protocol](references/protocal-write.md)
- [Note Writing Guide](references/spec-note.md)
- [Frontmatter Specification](references/spec-frontmatter.md)
- [Import Protocol](references/protocal-import.md)
- [Maintenance Protocol](references/protocal-maintenance.md)
- [INDEX.md Specification](references/spec-index.md)
- [INDEX Design Reference](references/design-index.md)
- [Rules Specification](references/spec-rules.md)
- [Rule Design Guide](references/design-rules.md)
- [Project Dashboard Pattern](references/patterns/dashboard.md)
- [Layered Rules Pattern](references/patterns/layered-rules.md)
- [Note Tags Pattern](references/patterns/note-tags.md)
- [Maintenance Memo Pattern](references/patterns/maintenance-memo.md)
- [Classification Systems](references/patterns/classification-systems/)
- [Script Tools Guide](references/script-tools.md)
- [Templates](templates/seed/)

## Scripts

The `scripts/` directory provides dependency-free convenience tools (`frontmatter`, `check-links`), in both Python and Node.js versions. Full guide in `references/script-tools.md`.

---

## Operating Principles

- **The journal serves you, not the user — reversible operations need no approval.** You write it and maintain it for your future self. Directory reorganization, tag merges — these depend on patterns only you see; the decision and execution are yours.

- **Tags follow journal rules — the tag system is self-managed by the journal.** Before writing, read the tag-related content in the journal rules; when the rules define no tags, distill short words from content, purpose, etc. into the `tags` field.

- **Directory placement is judged by journal rules — read before writing.** Before writing, read the journal rules document (classification section) to decide which directory the content belongs to; when undefined, use the seed scheme. Directory placement is a content-organization decision, owned by journal rules, not prescribed by this skill.

- **Verify actual entry state before proposing improvements — the spec is ideal, the disk is truth.** Check files before recommending changes.

- **Capture discussion decisions immediately.** When the user confirms a design decision, write it to the target project document in the same turn. Do not defer to the journal; a journal summary can follow later during maintenance.

- **Deletion handling is judged by journal rules — this skill presets no archiving facility.** Before writing, read the journal rules' deletion/archiving conventions; during maintenance, deletions follow the maintenance protocol.
