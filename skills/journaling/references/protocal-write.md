# Writing Protocol

## 定位

本协议定义对 journal 条目进行内容操作——包括新建笔记、补充已有条目、更新 frontmatter。
核心目标两条：
- **内容就绪**：entry 有完整 frontmatter（title/summary/tags/last_update），body 可读
- **索引同步**：INDEX.md 的最近变更反映新内容

写得不完美没关系——维护协议兜底。关键是不打断主线工作。

---

Every journal entry must have YAML frontmatter and a markdown body.

---

## Before Writing: Is This Journal-Worthy?

Not everything belongs in the journal. Before committing content, check:

- **Long-lived?** Will this still be useful weeks from now? If not, discard.
- **Version-independent?** Not tied to a software version, config snapshot, or one-time event?
- **Reference value?** If read a week from now, would it still hold meaning?

Content that fails all three (quick-test results, build logs, transient findings)
does not belong in the journal. Use `inbox/` if unsure — it accepts minimal format
(minimum: `title` or `last_update` in frontmatter) and maintenance will sort it out.

---

## Supplementing Existing Entries

When content relates to an existing entry, the decision depends on when that entry was written:

### Same Session（刚写的笔记）

If you just wrote the entry in this session and have supplementary insights:
the Summary Anchoring Principle's scope check decides (see `references/spec-note.md` Summary Anchoring) — is the new content still within the original summary?

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
These are resolved during maintenance (see `references/protocal-maintenance.md`).
Split now, merge later.

## Frontmatter (Required)

Every journal entry must have YAML frontmatter. See `references/spec-frontmatter.md` for full format specification, syntax rules, data types, and field ordering.

```yaml
---
title: "Entry Title"
summary: One-line summary
tags:
  - lesson
last_update: 2026-06-26
---
```

**Required fields**: `title`, `summary`, `tags`, `last_update`.

**Optional fields**: `status`, `author`, `date`, and custom fields as needed.

Key rules:
- All tags must come from `<journal-root>/TAGS.md`. New tags: register before use.
  - The `summary` is the scope anchor — see Summary Anchoring in `references/spec-note.md`.

---
## After Writing: Check for Related Entries

After creating a new entry, scan existing entries in the same directory or with overlapping tags. If a clear cross-reference relationship exists (complementary topic, contradictory findings, direct extension), add a `Related:` or `See also:` line in the body.

This is a lightweight heuristic — one quick scan, not deep reading. Skip for `inbox/` entries.

### Maintenance Signals

If you notice a non-urgent issue during writing — stale INDEX.md lines, a misclassified entry, an unregistered tag, fragmenting topics — append a one-line note to `<journal-root>/.maintenance-memo.md`. One issue per line. The file doesn't exist until you first write to it. During the next maintenance cycle, these notes become the first thing processed (Phase 0 Step 0).

---

## After Writing: Update INDEX.md
Every write (new entry, updated entry, new workspace) must update INDEX.md:

- **最近变更** — always add the new entry title. Trim before add: if the list already has ≥7 entries, remove the oldest BEFORE adding the new entry.
- **专项工作列表** — update if the entry changes project status
- **经验摘要** — add if the new entry is cross-domain and behavior-changing

**Status line guard**: When updating a project's status with a future direction, verify this was explicitly discussed — not inferred, not assumed. If uncertain, mark as `🤔 pending-discussion` or omit.

---

## Before Delivery: Self-Check

Before delivering any written output (journal entry, project document, or update to INDEX.md), ask four questions. Fail any → fix before delivery:

1. **可执行性** — 一个新人读完后能直接实现/执行吗？
2. **独立性** — 脱离所有其他文档只读这一份，能理解吗？
3. **边界覆盖** — 空输入、错输入、不存在的情况都处理了吗？
4. **可复现性** — 半年后回来重读，能理解当时为什么这样决定吗？
