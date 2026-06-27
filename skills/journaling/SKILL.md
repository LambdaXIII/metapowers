---
name: journaling
description: |
  The skill for all journal operations — reading, writing, and maintaining your long-term memory notebook.

  Triggers:
  - **Creating a new journal from scratch (first install or new environment)**
  - Need to write a journal entry (decide where, what format, create vs update)
  - Need to maintain / clean up the journal
  - Unsure about journal usage decisions after reading INDEX.md dashboard
  - **A discussion just produced a design decision that needs immediate capture in a project document**

  Do NOT load for:
  - Reading INDEX.md dashboard (the dashboard itself says "读不需要加载 skill")
  - Browsing existing journal entries
  - Searching journal content
metadata:
  version: "4.3.0"
  last_updated: "2026-06-27"
  author: "Ĉalio"
---

# Journaling

> **Journal is your long-term memory notebook.** You write it. You use it. It serves you, not the user.

> **Journal is documentation.** Writing a journal entry and writing a project document follow the same principles — self-check, independence, boundary coverage, decision-capture timing. The skill's writing protocols (decision capture, self-check) apply to both.

This skill defines how the journal works — the design concept (why), the cover (INDEX.md), the pages (entries), the daily operations (read/write), and the maintenance cycles.


---

## Core Constraint

**INDEX.md is the sole entrance to journal.** It is the notebook cover — a dashboard of state signals, not a directory listing. All journal norms (format, directory usage, maintenance) are defined by this skill.

## Linked Files

- [INDEX.md Specification](references/spec-index.md) — INDEX.md 的核心规范：协议声明、设计原理、与自管理文件（CLASSIFICATION.md/TAGS.md）的关系。关于项目级次级 INDEX 的设计参考，见 `patterns/dashboard.md`。
- [Writing Protocol](references/protocal-write.md) — 写条目的工作流程：triage 判断、同 session 补充 vs 跨 session 补充、After Writing 更新 INDEX.md、Before Delivery 自检。
- [Note Writing Guide](references/spec-note.md) — 条目格式指南：summary anchoring 三检查点、body 格式（一句一行/wikilink/过度泛化/context boundary）、粒度控制、4 种子目录分配、条目生命周期。
- [Importing Protocol](references/protocal-import.md) — Bring existing external content into the journal: evaluation, copy, frontmatter, adjustment.
- [Journal Initialization](references/protocal-init.md) — Create a new journal from scratch: three-phase protocol (locate root → init skeleton files → design discovery contract).
- [Maintenance Protocol](references/protocal-maintenance.md) — Full maintenance cycle: Phase 0 scan, Phase 1 rule review, Phase 2 restructure, Phase 3 quality check, Phase 4 finalize. Trigger when dashboard signals or memo exceeds 10 items.
- [Journal Standards Examples](examples/journal-standards/) — Reference examples of journal self-managed files: INDEX.example.md, CLASSIFICATION.example.md, TAGS.example.md.
- [Templates](templates/seed/) — 初始化所需的种子文件模板（INDEX.md、CLASSIFICATION.md、TAGS.md）。

- [Inbox](`inbox/README.md`) — Zero-friction staging area for unsure content. Requires only minimum frontmatter (title or date). Processed during maintenance.
- [Classification Design Guide](references/design-classification.md) — Design your journal's own classification: when to customize, design process, verification.
- [Classification System Examples](examples/classification-systems/) — Reference catalog of common real-world classification systems (PARA, Zettelkasten, Johnny Decimal, MOC/LYT, Evergreen, GTD, and journaling default). Each file starts with a summary for quick scanning.
- [Tag Design Guide](references/design-tags.md) — Tag creation, naming, registration, and lifecycle methodology. Consult when registering new tags or during tag maintenance.
- [Frontmatter Specification](references/spec-frontmatter.md) — YAML format rules, required fields, recommended optional fields, custom field guidelines, and examples.
- [Project Dashboard Pattern](patterns/dashboard.md) — 项目/领域级次级 INDEX 设计参考。和 INDEX.md 类比：提供聚焦一域的状态概览，作为 session 的次级路由入口。不是规范——从实际需求中生长。
---

## How to Use This Skill

This skill uses progressive disclosure. Load the reference document matching your scenario:

| Scenario | Load |
|----------|------|
| **Creating a new journal from scratch** | **`references/protocal-init.md`** |
| Writing/reviewing INDEX.md core spec and protocol declaration | `references/spec-index.md` |
| Creating or reviewing a project-level dashboard (secondary INDEX) | `patterns/dashboard.md` |
| Writing a journal entry (workflow: triage → supplement → update INDEX.md → self-check) | `references/protocal-write.md` |
| Writing a journal entry (format: summary → body → granularity → directory → lifecycle) | `references/spec-note.md` |
| **Importing existing content into the journal** | **`references/protocal-import.md`** |
| **Capturing a discussion decision immediately into a project document** | **Operating Rules below** |
| Maintaining or cleaning up the journal | `references/protocal-maintenance.md` |
| Designing or revising journal classification | **`references/design-classification.md`** |
| Researching classification patterns for a custom design | **`examples/classification-systems/`** — read summaries, decide which to load |
| Designing or revising journal tag system | **`references/design-tags.md`** |
| Writing or checking entry frontmatter format | **`references/spec-frontmatter.md`** |
If the scenario is ambiguous, load two references. Don't load all at once.

---

## Operating Principles

These principles follow from the journal's design decisions. Each exists because a design choice creates a specific operational constraint.

- **Journal serves you, not the user — don't ask for approval.** You write it, you maintain it, for your future self. The user cannot effectively judge whether a directory reorganization, tag merge, or archive is correct — these depend on patterns only you see. So routine operations do not need permission. You MAY solicit the user's perspective on ambiguous cases to learn from their judgment, but the decision and execution are yours.

- **Select tags from TAGS.md before writing — the tag system is self-managed.** A tag not in `<journal-root>/TAGS.md` doesn't exist for this journal. If a needed tag is missing, register it there first. Freeform tags bypass the registry and silently decay into noise.

- **Determine directory assignment before writing — the directories are the classification.** Which directory an entry lands in is a decision about what kind of thing this is. Read `references/spec-note.md`'s Directory Assignment before creating.

- **Verify actual entry state before proposing improvements — the spec is ideal, the disk is truth.** The loaded spec describes what entries should look like; actual entries may already conform. Check files before recommending changes.

- **Search journal before any bulk deletion — the journal is a dependency map.** Entries cross-reference skills, configs, and project files. Deleting without checking breaks those references silently.

- **Capture discussion decisions immediately — confirmed decisions live on a different timeline than journal entries.** When the user confirms a design decision, write it to the target project document in the same turn. Do not defer to journal. A journal summary can follow later during maintenance.
