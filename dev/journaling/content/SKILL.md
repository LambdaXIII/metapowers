---
name: journaling
description: |
  MUST load before any write operation to <journal-root> (create, edit, move,
  archive, delete, etc.), including journal operations the user requests
  directly. No need to load for read-only access to journal content.

  Examples of write operations:
  - Creating a new journal
  - Writing, editing, importing, moving, archiving, or deleting journal entries
  - Maintaining / organizing the journal
  - Writing design decisions confirmed in discussion into journal files

  Write operations include: 创建/写入/编辑/收录/移动/归档/删除 journal 条目、
  维护/整理 journal、将讨论中确认的设计决策写入 journal 文件。
license: "CC-BY-NC-SA-4.0"
metadata:
  version: "5.1.2"
  last_updated: "2026-10-15"
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
| Init protocol | Creating a new journal | `references/protocol-init.md` |
| Operations protocol | Any operation that changes journal state — creating, editing, importing, moving, archiving, deleting entries. Day-to-day entry work (edit, move, delete, merge) routes here, not to maintenance. | `references/protocol-operations.md` |
| Maintenance protocol | Dedicated maintenance / reorganization of the journal, triggered explicitly by the user | `references/protocol-maintenance.md` |

---

## Operating Principles

- **The journal serves you, not the user — the autonomy domain covers writing and user-guided operations.** You write it for your future self. Entry placement, splits, cross-references — these depend on patterns only you see; within the autonomy domain the decision and execution are yours. Dedicated maintenance is outside the autonomy domain: it is triggered only by the user, as a dedicated action (see the maintenance protocol).

- **Tags follow journal rules — the tag system is self-managed by the journal.** Before writing, read the tag-related content in the journal rules; when the rules define no tags, distill short words from content, purpose, etc. into the `tags` field.

- **Directory placement is judged by journal rules — read before writing.** Before writing, read the journal rules document (classification section) to decide which directory the content belongs to; when undefined, use the seed scheme. Directory placement is a content-organization decision, owned by journal rules, not prescribed by this skill.

- **Verify actual entry state before proposing improvements — the spec is ideal, the disk is truth.** Check files before recommending changes.

- **Capture discussion decisions immediately.** When the user confirms a design decision, write it to the target project document in the same turn. Do not defer to the journal; a journal summary can follow later during maintenance.

- **Deletion handling is judged by journal rules — routed via the operations protocol.** Deletion gets minimal guidance there and executes per the journal rules' deletion conventions; this skill presets no deletion protocol and no deletion semantics — the operations protocol carries only a safety fallback for when journal rules are silent.

---

## Scripts

The `scripts/` directory provides dependency-free convenience tools (`frontmatter`, `check-links`), in both Python and Node.js versions. Full guide in `references/script-tools.md`. Take them on demand only — during mainline work there is no reason to stop and run checks or validations specially.

---

## References

Load on demand; every entry states when to read it.

**Protocols**
- [Init Protocol](references/protocol-init.md) — creating a new journal
- [Operations Protocol](references/protocol-operations.md) — any journal-state-changing operation: creating, editing, importing, moving, archiving, deleting entries
- [Maintenance Protocol](references/protocol-maintenance.md) — user-triggered dedicated maintenance / reorganization

**Design guides**
- [Discovery Contract Design](references/design-discovery-contract.md) — designing or judging a discovery contract (the injection text that routes a host agent to its journal); the init protocol's discovery phase links here
- [Rule Design Guide](references/design-rules.md) — designing the journal's organization scheme (where content goes, naming, how it is found) before writing RULES.md
- [INDEX Design Reference](references/design-index.md) — designing INDEX structure and dashboards, including the INDEX-structure section of RULES.md

**Specifications**
- [Note Writing Guide](references/spec-note.md) — how to write a good entry; the writing flow itself lives in the Operations protocol
- [Frontmatter Specification](references/spec-frontmatter.md) — frontmatter format and grammar, including custom-field guidance
- [INDEX.md Specification](references/spec-index.md) — INDEX structure rules
- [Rules Specification](references/spec-rules.md) — writing RULES.md rule text: principles and reminders for recording the organization scheme

**Tools & templates**
- [Script Tools Guide](references/script-tools.md) — running the `frontmatter` / `check-links` scripts
- [Seed Templates](templates/seed/) — default scheme wherever journal rules leave a section undefined; source for bootstrapping the rules document

**Patterns** — read the summary first, open the full file only when it fits
- [Project Dashboard Pattern](references/patterns/dashboard.md) — building a dashboard-style INDEX
- [Layered Rules Pattern](references/patterns/layered-rules.md) — organizing RULES.md into layers
- [Note Tags Pattern](references/patterns/note-tags.md) — defining tag conventions
- [Maintenance Memo Pattern](references/patterns/maintenance-memo.md) — tracking maintenance backlog (used by the maintenance protocol)
- [Classification Systems](references/patterns/classification-systems/) — choosing a classification system for entries
