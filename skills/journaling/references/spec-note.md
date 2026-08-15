# Note Writing Guide

> Methodology for writing journal entries. 此文件是笔记编写指南——告诉你怎么写好一条笔记。
> 写作流程见 `protocal-write.md`。Frontmatter 格式规范见 `spec-frontmatter.md`。

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
- Group paragraphs with blank lines
- **Beware over-generalization**: A lesson learned in one project context is not universal truth. "某项目在 Y 约束下用 X" not "应该用 X 模式". Tags alone are NOT enough — the body itself must name the constraints.
- **Context boundary**: If the content depends on a specific status, environment, or timeframe, name the conditions in the body so future readers know when this knowledge applies.

---

## Granularity

- **Crossing time boundaries:** If an entry naturally spans two time directions (e.g., completed decisions + future plans), add a `## Future` section for the forward-looking content, and split during maintenance.
- Don't aim for perfect granularity at write time
- An entry that grows too long or covers too many topics is fine — split during maintenance
- The maintenance protocol (`protocal-maintenance.md`) handles splitting, merging, and reorganizing
- Write first, refine later

---

## Link Convention

Two link forms are valid in this journal:

- **Wikilink**: `[[target]]` — resolves within the note library
- **Markdown link (mdlink)**: `[text](path)` — standard markdown

### Choosing a form

- Target is a filename or path inside the note library → prefer `[[wikilink]]`（mdlink 对库内目标同样有效，如需要特定显示文字时）
- Anything else (target outside the library, custom display text needed) → `[text](path)`

### Resolution semantics

Wikilinks and mdlinks resolve through the same table below (fallback behavior differs by form):

| Link | Meaning |
|------|---------|
| `[[foo]]` (bare name, no extension) | Library-wide search by name (any location); multiple matches → report ambiguity. This form is wikilink-only — an mdlink without extension is WRONG |
| `[[foo.md]]` (extension, no path) | Relative to the current file's directory (≡ `[./foo.md]`); fallback on failure: extension-less name search |
| `[foo.md]` (mdlink, extension, no path) | Relative to the current file's directory; fallback on failure: exact path under `<journal-root>/foo.md` |
| `[[a/b/c/foo.md]]` / `[a/b/c/foo.md]` (path, no `./`/`../` prefix) | Relative to journal-root |
| `[[./foo.md]]` / `[[../foo.md]]` (with `./`/`../` prefix) | Relative to the current file's directory |

### Classification

- **WRONG** — illegal: mdlink without extension（表外判定——mdlink 解析前先检查扩展名）
- **EXTERNAL** — valid external: URL, local absolute path (e.g. `C:/…`) — classified only, reachability not verified。指向库内的绝对路径违反 Path base constraints（禁用），指向库外的为 EXTERNAL——按目标实际位置判定
- **Internal** — resolved by the rules above
- **Ambiguous** — library-wide name search with multiple matches（第 1 行 `[[foo]]` 与第 2 行 `[[foo.md]]` 的 fallback 搜索均适用）

### Path base constraints

- Note-to-note links must follow the resolution bases above (relative to journal-root or to the current file) — **absolute paths to library files are forbidden**
- External-file links (URL, absolute path) are not constrained by this — absolute paths are recommended for cross-environment stability
