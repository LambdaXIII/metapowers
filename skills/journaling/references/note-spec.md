# Note Entry Specification

Every journal entry must have YAML frontmatter and a markdown body.

---

## Before Writing: Is This Journal-Worthy?

Not everything belongs in the journal. Before committing content, check:

- **Long-lived?** Will this still be useful weeks from now? If not, discard.
- **Version-independent?** Not tied to a software version, config snapshot, or one-time event?
- **Reference value?** If read a week from now, would it still hold meaning?

Content that fails all three (quick-test results, build logs, transient findings)
does not belong in the journal. Use `inbox/` if unsure — it accepts minimal format
(minimum: `date` in frontmatter) and maintenance will sort it out.

---

## Importing Existing Content

When bringing an existing document into the journal:

1. **Evaluate** — apply the Before Writing three questions. If it doesn't belong, stop.
2. **Search** — check for related entries in the journal. If a related entry exists, apply the Supplementing rules below (same-session / cross-session).
3. **Copy** — copy the source file into the target journal directory. Do not type or extract — copy the whole file.
4. **Add frontmatter** — edit the copy: add title, date, tags, summary. The source's creation date is a reasonable `date` value.
5. **Adjust body** — adapt the copy to journal format guidelines (one sentence per line, wikilinks for cross-references). Keep the content complete.
6. **Proceed** — the copy is now a journal entry. Apply After Writing (Update index.md) and Before Delivery (Self-Check).

**Do not modify the source file.** The journal is a second copy, not a migration.

---

## Supplementing Existing Entries

When content relates to an existing entry, the decision depends on when that entry was written:

### Same Session（刚写的笔记）

If you just wrote the entry in this session and have supplementary insights:
the Summary Anchoring Principle's scope check decides — is the new content still within the original summary?

- Yes → expand the existing entry (update summary if scope widened)
- No → create a new entry with its own summary

The scope is still forming; don't over-think.

### Cross-Session（已有的旧笔记）

If the existing entry was written in a past session, the bar is stricter:
the new content must be a **direct extension** that does not require changing the original summary.

- **Direct extension** (summary unchanged) → add to the existing entry
- **Not a direct extension** (summary would change) → create a new entry.
  In the new entry's body or summary, link back to the related old entry:
  `Related: [old entry title](path/to/old-entry.md)`

Do not worry about redundancy, overlap, or contradictions between the two entries.
These are resolved during maintenance (see `references/maintenance.md`).
Split now, merge later.

## Frontmatter (Required)

```yaml
---
title: "Entry Title"
date: "2026-05-18"
tags: [key-tag1, key-tag2]
summary: One-line summary
status: draft
---
```

- **title**: concise, descriptive
- **date**: ISO format, date of creation or last major update
- **tags**: From the controlled vocabulary in `references/tag-registry.md`. Select at least one activity tag or meta tag. Project tags are optional — use them when the entry is clearly tied to a specific project. Domain tags are optional. Typically 2-4 tags per entry. New tags must be registered in the registry before use. Cross-cutting entries (environment migration, journal design, general methodology) do not need a project tag — the journal is a global notebook, not a per-project filing system.
- **summary**: ONE sentence. This is the anchor — used both for search and for judging whether new content belongs in this entry or a new one
- **status** (optional): Tracks the entry's position in its lifecycle. Values:
  - `draft` — still being written, content not yet stable
  - `active` — work in progress (default for entries in `active/`)
  - `completed` — work done, content stable (default for entries in `experience/` or `research/`)
  - `superseded` — replaced by a newer entry; include a link to the successor
  - `abandoned` — work stopped, no plan to resume

  When `status` is absent, infer from directory: `active/` → active, `experience/` or `research/` → completed, `goal/` → active.

## Summary Anchoring Principle

The summary is the primary tool for granularity control. It must be verified at three checkpoints during a note's lifecycle:

### On creation
Write the summary. It defines the note's scope boundary.

### Before modifying

**For edits that change scope, conclusions, or add substantive content**: read the existing summary. Ask: "Does the new content still fall within the scope of this summary?"

- Yes → expand the note (and update summary if scope widened)
- No → create a new note with its own summary

**For typo fixes, formatting, or minor clarifications**: no need to re-read the summary. The mechanism should not be heavier than the edit.

**If you catch yourself adding substantive content without having checked the summary**, pause and check. The summary is the scope boundary — crossing it without noticing is how entries lose coherence.

This makes the "update vs create" decision cheap — the summary acts as a scope boundary. No pre-planning of perfect granularity required.

### After modifying
Re-read the summary against the current content. Does it still accurately describe what this note contains? If the content has changed—especially if a plan has been completed, a decision has been superseded, or the note's role has shifted—update the summary (and `date`) to reflect the current state.

**Anti-pattern**: summaries that describe what the note *was* rather than what it *is*. "以 SvelteKit 全栈重构项目 A v2" describes a plan; after completion, it should become "项目 A 重构的设计原则与决策记录（计划已于 YYYY-MM 完成）".

### The summary is not the understanding

The summary tells future-me *whether to open this file*. The body must deliver *understanding*:
- Not just "做了 X" but "为什么做 X 而非 Y，边界条件 Z 下成立"
- Not just a conclusion but the reasoning chain that produced it
- Not just a result but the failed attempts and discarded alternatives that preceded it

A summary that accurately describes content but whose body is a shallow checklist has passed the summary check but failed the journal's purpose.

Before delivering a journal entry, ask: **如果我是半年后的自己，完全不记得这次讨论，读这篇能**理解**当时的判断吗？不只是知道"结论是什么"，而是理解"为什么是这个结论"？** If the answer is "maybe not" — the entry is not deep enough. This is the first writing anchor (journal-concept.md #1 "可复现深刻理解"), and it overrides all other concerns. A deeply understood wrong directory is better than a shallow correct one.

---

## Body

Free markdown. Guidelines:
- One sentence per line
- Group paragraphs with blank lines
- Use `[[wikilink]]` or `[desc](relative-path.md)` for cross-references
- Cross-reference project files with relative paths
- **Beware over-generalization**: A lesson learned in one project context is not universal truth. "某项目在 Y 约束下用 X" not "应该用 X 模式". A project tag is NOT enough — the body itself must name the constraints.
- **Shelf life awareness**: If the content depends on a specific status, environment, or timeframe, note the expected expiry in the body or consider `active/` instead of `experience/`.
---

## Granularity Principle

- Don't aim for perfect granularity at write time
- An entry that grows too long or covers too many topics is fine — split during maintenance
- The maintenance protocol (`references/maintenance.md`) handles splitting, merging, and reorganizing
- Write first, refine later
- **Crossing time boundaries:** If an entry naturally spans two time directions (e.g., completed decisions + future plans), place it in the completed-status directory (`experience/` or `research/`), add a `## Future` section for the forward-looking content, and split during maintenance.

---

## Directory Assignment

Entries are placed in one of seven directories.

### Directory Table

| Directory | When |
|-----------|------|
| `inbox/` | Incoming: content not yet classified. Use when unsure about long-term value, correct directory, or format completeness. Requires only `date` in frontmatter; other fields optional. Processed during maintenance. |
| `experience/` | Completed: any reusable output from our own practice. Design decisions, bug fixes, learned lessons, methodology manuals, workflow documents. The common thread: it came from doing, not from studying others. |
| `active/` | In-progress: cross-session tasks, blocked items needing continuation. Entries here should have `status: active` and describe what remains to be done. |
| `goal/` | Future: long-term directions, ideas needing discussion before implementation. A goal with no follow-up for 7+ days is likely stale — during maintenance, ask "if I deleted this, would any active work lose its north star?" |
| `workspace/` | Topic dashboards: aggregated views of entries across directories, created on demand |
| `research/` | Reference: systematic investigation of external sources. What others do, how others solve this, published methodologies, competitive landscape, academic papers. The common thread: it came from studying others, not from our own doing. |
| `archive/` | Cold storage: inactive but worth keeping. Entries here are not referenced from the dashboard. |

### research/ vs experience/

The boundary is not "before vs after" but **"external vs internal"**:

- **research/** = digesting external sources. You studied what others do and wrote it down. Even if you applied their ideas later, the entry itself is about their work, not yours. Examples: competitive analysis of other products, literature surveys, academic paper summaries, framework comparisons.
- **experience/** = recording your own practice. You did something, it worked (or didn't), and you're capturing what you learned. Methodology manuals you wrote yourself belong here — they are systematized experience, not external research. Examples: your competitive tracking methodology, quick-test results of your own skills, backup script design, debugging records.

**Borderline cases:**
- You read a research paper → applied it → it worked: the paper summary stays in research/; "what we learned from applying it" goes in experience/
- Quick-test results for your own skills: experience/ (it's verification of your own work)
- Competitive analysis of other products: research/ (you're studying others)
- Your own competitive tracking methodology manual: experience/ (you built it from your own tracking practice)
- A design document written before implementation: if it describes your own design → experience/. If it's a survey of existing design patterns → research/.

### Directory Decision Flow

When writing a new entry and unsure about the directory:

1. Is this from our own practice? → experience/. Is this from studying others? → research/.
2. Is this still in progress? → active/.
3. Is this a direction we haven't started? → goal/.
4. Not sure about any of the above? → inbox/. Sort it out during maintenance.

If unsure between active/ and goal/: ask "is this being actively worked on now?" → yes = active, no = goal.

If misclassified, fix during maintenance. Don't overthink at write time.

---

## Entry Lifecycle

Journal entries follow a defined lifecycle. Understanding the stages helps decide where to put things and when to move them.

```
[write to inbox/] → [maintenance: classify] → active/ (in progress)
                                            → experience/ (completed, from our practice)
                                            → research/ (completed, from external study)
                                            → goal/ (future direction)

active/ → [task completed, content stable] → experience/ or research/
        → [abandoned] → archive/

experience/ or research/ → [referenced in dashboard] → [2 sessions cooling] → [dashboard reference removed, entry stays in directory]
                         → [long-term inactive, no dashboard reference] → archive/

goal/ → [work started] → active/
      → [abandoned or superseded] → archive/
```

### Stage Transition Rules

| Transition | Trigger |
|------------|---------|
| inbox/ → any directory | Maintenance: entry gets full frontmatter, classified, and moved |
| active/ → experience/ or research/ | Entry has `status: completed` and content is stable. Without explicit status, look for evidence of completion in the body (e.g., "resolved", checkmarks, dated resolution) |
| Directory → dashboard reference | Entry is added to index.md 专项工作 or a topic dashboard |
| Dashboard referenced → cooled | 2 agent sessions have passed since the milestone was completed. A session = one agent startup cycle. After cooling, the dashboard line is removed but the entry stays in its directory |
| → archive/ | Entry has been inactive for an extended period, is not referenced by any dashboard, and is not part of any active work. Archive preserves the content without polluting active directories |

Entries that skip inbox/ and go directly to their target directory are the normal case — inbox/ is for content that needs deferred classification.

---

## After Writing: Update index.md

Every write (new entry, updated entry, new workspace) must update index.md:

- **最近变更** — always add the new entry title. Trim before add: if the list already has ≥7 entries, remove the oldest BEFORE adding the new entry.
- **专项工作列表** — update if the entry changes project status
- **经验摘要** — add if the new entry is cross-domain and behavior-changing

**Status line guard**: When updating a project's status with a future direction, verify this was explicitly discussed — not inferred, not assumed. If uncertain, mark as `🤔 pending-discussion` or omit.

---

## Before Delivery: Self-Check

Before delivering any written output (journal entry, project document, or update to index.md), ask four questions. Fail any → fix before delivery:

1. **可执行性** — 一个新人读完后能直接实现/执行吗？
2. **独立性** — 脱离所有其他文档只读这一份，能理解吗？
3. **边界覆盖** — 空输入、错输入、不存在的情况都处理了吗？
4. **可复现性** — 半年后回来重读，能理解当时为什么这样决定吗？
