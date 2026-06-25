---
name: journaling
description: |
  The skill for all journal operations — reading, writing, and maintaining my long-term memory notebook.

  Triggers:
  - **Creating a new journal from scratch (first install or new environment)**
  - Need to write a journal entry (decide where, what format, create vs update)
  - Need to maintain / clean up the journal
  - Unsure about journal usage decisions after reading index.md dashboard
  - **A discussion just produced a design decision that needs immediate capture in a project document**

  Do NOT load for:
  - Reading index.md dashboard (the dashboard itself says "读不需要加载 skill")
  - Browsing existing journal entries
  - Searching journal content
metadata:
  version: "4.0.0"
  last_updated: "2026-06-25"
  author: "Ĉalio"
---

# Journaling

> **Journal is my long-term memory notebook.** I write it. I use it. It serves me, not the user.

> **Journal is documentation.** Writing a journal entry and writing a project document follow the same principles — self-check, independence, boundary coverage, decision-capture timing. The skill's writing protocols (decision capture, self-check) apply to both.

This skill defines how the journal works — the design concept (why), the cover (index.md), the pages (entries), the daily operations (read/write), and the maintenance cycles.

> **Design concept →** `references/journal-concept.md`. Seven anchors (5 writing + 2 reading) + mechanism mapping + gate theory + memory positioning. Load when proposing new mechanisms or auditing journal design.

---

## Core Constraint

**index.md is the sole entrance to journal.** It is the notebook cover — a dashboard of state signals, not a directory listing. All journal norms (format, directory usage, maintenance) are defined by this skill.

## Linked Files

- [Journal Concept](references/journal-concept.md) — Design philosophy: what a journal is, 7 execution anchors, mechanism mapping, memory positioning, gate design principles.
- [Dashboard (index.md) Specification](references/index-spec.md) — Dashboard structure: protocol declaration, 3 core sections (experience summary, project work status, recent changes), plus optional organizational patterns. Workspace dashboard pattern.
- [Note Specification](references/note-spec.md) — Entry format and write procedure: frontmatter fields, directory assignment, summary anchoring, before-writing triage, after-writing index update, delivery self-check.
- [Maintenance Protocol](references/maintenance.md) — Four-phase maintenance: signal collection, evaluation, restructure, verification. Diagnostics, pitfalls, cascade rename, cleanup patterns.
- [Journal Initialization](references/initialization.md) — Create a new journal: directory structure, initial index.md, discovery contract, maintenance memo, bootstrap entry.
- [Tag Registry](references/tag-registry.md) — Controlled vocabulary for journal entry tags. Consult when writing and during maintenance.
- [Maintenance Memo](.maintenance-memo.md) — Running checklist of issues noticed during daily work. Append freely, process during maintenance Phase 1 Step 0. The memo is a maintenance trigger at 10+ items. (Lives at journal root.)
- [Inbox](`inbox/README.md`) — Zero-friction staging area for unsure content. Requires only `date`. Processed during maintenance.

---

## How to Use This Skill

This skill uses progressive disclosure. Load the reference document matching your scenario:

| Scenario | Load |
|----------|------|
| **Creating a new journal from scratch** | **`references/initialization.md`** |
| Writing/reviewing index.md dashboard structure | `references/index-spec.md` |
| Writing a journal entry (pre-check → format → write → update index → self-check) | `references/note-spec.md` |
| **Capturing a discussion decision immediately into a project document** | **Operating Rules below** |
| Maintaining or cleaning up the journal | `references/maintenance.md` |
| Recording a maintenance issue noticed during daily work | `.maintenance-memo.md` — append a line, don't load anything |
| Understanding the full journal design philosophy (concept, anchors, gate theory, memory positioning) | `references/journal-concept.md` |

If the scenario is ambiguous, load two references. Don't load all at once.

---

## Operating Rules

These rules govern journal operations. They are not suggestions — loading this skill means following them.

- **Verify actual entry state before proposing improvements.** The note spec mandates frontmatter, tags, summary anchoring, and directory assignment — all typically already in place. Check files in `experience/`, `research/`, etc. before recommending changes. Skill spec → actual files: verify both before proposing.

- **Don't ask the user for journal approval.** The journal is the Agent's own notebook. Maintenance decisions (archive, merge, delete, tag remediation) are the Agent's to make. Ask for *advice* on ambiguous cases, not *permission* on routine operations.

- **Select tags from the registry before writing.** Tags come from `references/tag-registry.md`. If a needed tag is missing, register it first. Freeform tags decay into noise.

- **Determine directory assignment before writing.** Read `references/note-spec.md`'s directory table. A blocked/investigation item is `active/`, not `experience/`. A pending question is `active/` or `goal/`, not `research/`.

- **Search journal for cross-references before any bulk deletion.** When deleting skills, config sections, or project files, search the journal directory first. The journal is a dependency map — deleting without checking causes silent breakage.

- **Treat cross-skill reference hits as low-confidence after skill digestion.** When a skill is deleted, its reference files copied into other skills persist as frozen snapshots. Priority: actual files > journal design docs > cross-skill references.

- **Present conclusions at the same level of detail as the analysis.** Don't compress by selecting a subset of insights. If the analysis identified 8 issues, the conclusion names all 8. If compression is needed, explicitly state what is deferred and where it will be addressed.

- **Separate Journal (content layer) from Journaling (mechanism layer) during audits.** Journal = actual entries, dashboard state, gate rules. Journaling = SKILL.md + references. Conflating the two produces misattributed findings. Before any audit: state which layer each finding targets.

- **Capture discussion decisions immediately.** When the user confirms a design decision (naming, path, field, boundary, behavior convention), write it to the target project document in the same turn — not later, not after the discussion ends. Pause conversation → open file → write → resume. If the target document doesn't exist, search the project for related files or create a decision log. Do not defer to journal.

  Capture urgency tiers:
  - 即时级 (simple, irreversible decision) → **MUST** write in the same round
  - 段落级 (multi-step design decision) → write all consensus at the natural paragraph boundary
  - Self-check after write: was this written in the same round as confirmation? If no → write now.

- **Trace-back: search journal first.** When the user says "last time", "previously", "before", "we discussed X" — search the journal directory first. Journal is the primary long-term memory. Fall back to session history only if journal returns no results.
