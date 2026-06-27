# Note Writing Guide

> Methodology for writing journal entries. 此文件是笔记编写指南——告诉你怎么写好一条笔记。
> 写作流程见 `references/protocal-write.md`。Frontmatter 格式规范见 `references/spec-frontmatter.md`。

---

## Summary Anchoring

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

Re-read the summary against the current content. Does it still accurately describe what this note contains? If the content has changed—especially if a plan has been completed, a decision has been superseded, or the note's role has shifted—update the summary (and `last_update`) to reflect the current state.

**Anti-pattern**: summaries that describe what the note *was* rather than what it *is*. "以 SvelteKit 全栈重构项目 A v2" describes a plan; after completion, it should become "项目 A 重构的设计原则与决策记录（计划已于 YYYY-MM 完成）".

### The summary is not the understanding

The summary tells future-me *whether to open this file*. The body must deliver *understanding*:
- Not just "做了 X" but "为什么做 X 而非 Y，边界条件 Z 下成立"
- Not just a conclusion but the reasoning chain that produced it
- Not just a result but the failed attempts and discarded alternatives that preceded it

A summary that accurately describes content but whose body is a shallow checklist has passed the summary check but failed the journal's purpose.

---

## Body

Free markdown. Guidelines:
- One sentence per line
  Comparison: `[[wikilink]]` enables Obsidian auto-complete, rename tracking, and backlinks in the graph view; `[desc](path)` supports inline references to a specific claim ("论断出处[→](path)") and renders in any markdown viewer without Obsidian. Use either — both are standard in this journal. For precise citations that reference a specific sentence rather than an entire page, prefer `[desc](path)`.
- Group paragraphs with blank lines
- Use `[[wikilink]]` or `[desc](relative-path.md)` for cross-references
- Cross-reference project files with relative paths
- **Beware over-generalization**: A lesson learned in one project context is not universal truth. "某项目在 Y 约束下用 X" not "应该用 X 模式". A project tag is NOT enough — the body itself must name the constraints.
- **Context boundary**: If the content depends on a specific status, environment, or timeframe, name the conditions in the body so future readers know when this knowledge applies.

---

## Granularity Principle

- **Crossing time boundaries:** If an entry naturally spans two time directions (e.g., completed decisions + future plans), place it in the completed-status directory (`experience/` or `knowledge/`), add a `## Future` section for the forward-looking content, and split during maintenance.
- Don't aim for perfect granularity at write time
- An entry that grows too long or covers too many topics is fine — split during maintenance
- The maintenance protocol (`references/protocal-maintenance.md`) handles splitting, merging, and reorganizing
- Write first, refine later

---

## Directory Assignment

Entries are placed in one of four default directories. Additional directories may be added during maintenance as the journal grows.

### Default Directories

| Directory | When |
|-----------|------|
| `inbox/` | Incoming: content not yet classified. Use when unsure about long-term value, correct directory, or format completeness. Minimum frontmatter only (`title` or `last_update`). Processed during maintenance. |
| `experience/` | Completed: any reusable output from our own practice. Design decisions, bug fixes, learned lessons, methodology. The common thread: it came from doing, not from studying others. |
| `knowledge/` | External: systematic investigation of outside sources. What others do, how others solve this, reference material, academic papers. The common thread: it came from studying others, not from our own doing. |
| `active_works/` | In-progress: cross-session tasks, project progress, blocked items needing continuation. Entries here should describe what remains to be done. |

### experience/ vs knowledge/

The boundary is not "before vs after" but **"internal vs external"**:

- **experience/** = recording your own practice. You did something, it worked (or didn't), and you're capturing what you learned. Methodology manuals you wrote yourself belong here — they are systematized experience, not external knowledge. Examples: your competitive tracking methodology, quick-test results of your own skills, backup script design, debugging records.
- **knowledge/** = digesting external sources. You studied what others do and wrote it down. Even if you applied their ideas later, the entry itself is about their work, not yours. Examples: competitive analysis of other products, literature surveys, academic paper summaries, framework comparisons.

**Borderline cases:**
- You read a research paper → applied it → it worked: the paper summary stays in knowledge/; "what we learned from applying it" goes in experience/
- Quick-test results for your own skills: experience/ (it's verification of your own work)
- Competitive analysis of other products: knowledge/ (you're studying others)
- Your own competitive tracking methodology manual: experience/ (you built it from your own tracking practice)
- A design document written before implementation: if it describes your own design → experience/. If it's a survey of existing design patterns → knowledge/.

### Directory Decision Flow

When writing a new entry and unsure about the directory:

1. Is this from our own practice? → experience/. Is this from studying others? → knowledge/.
2. Is this still in progress? → active_works/.
3. Not sure about any of the above? → inbox/. Sort it out during maintenance.
4. If a classification feels persistently wrong, either the content is cross-domain (acceptable) or the classification needs redesign — audit during maintenance via `references/design-classification.md`.

Additional directories (`goal/`, `reference/`, `research/`, `archive/`, etc.) can be added during maintenance when content volume or diversity justifies the split. Do not pre-create them.

---

## Entry Lifecycle

Journal entries follow a defined lifecycle. Understanding the stages helps decide where to put things and when to move them.

```
[write to inbox/] → [maintenance: classify] → active_works/ (in progress)
                                            → experience/ (completed, from our practice)
                                            → knowledge/ (completed, from external study)

active_works/ → [task completed, content stable] → experience/ or knowledge/
              → [abandoned] → archive/ (create on demand)

experience/ or knowledge/ → [referenced in dashboard] → [2 sessions cooling] → [dashboard reference removed, entry stays in directory]
                          → [long-term inactive, no dashboard reference] → archive/ (create on demand)
```

### Stage Transition Rules

| Transition | Trigger |
|------------|---------|
| inbox/ → any directory | Maintenance: entry gets full frontmatter, classified, and moved |
| active_works/ → experience/ or knowledge/ | Entry has `status: completed` and content is stable. Without explicit status, look for evidence of completion in the body (e.g., "resolved", checkmarks, dated resolution) |
| Directory → dashboard reference | Entry is added to INDEX.md 专项工作 or a topic dashboard |
| Dashboard referenced → cooled | 2 agent sessions have passed since the milestone was completed. A session = one agent startup cycle. After cooling, the dashboard line is removed but the entry stays in its directory |
| → archive/ | Entry has been inactive for an extended period, is not referenced by any dashboard, and is not part of any active work. Archive preserves the content without polluting active directories |

Additional directories (`research/`, `reference/`, `goal/`, `archive/` as permanent directory, etc.) may be created during maintenance when entry volume justifies the split.

Entries that skip inbox/ and go directly to their target directory are the normal case — inbox/ is for content that needs deferred classification.
