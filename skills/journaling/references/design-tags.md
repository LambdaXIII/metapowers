# Tag Design Guide

> Methodology for designing and maintaining a journal's tag system. Like classification rules, tags grow from actual content needs — not from pre-built taxonomies.
>
> Use this reference when:
> - Registering a new tag (naming + format)
> - Reviewing tags during maintenance (Phase 1 Step 2)
> - Redesigning TAGS.md when the current structure no longer fits

---

## When to Create a New Tag

A tag earns its place. Register a new tag only when:

| Condition | Example | Wait / Register |
|-----------|---------|----------------|
| A concept appears in 1 entry | "第一次遇到 WSL 文件权限问题" | 不注册——先用已有 tag 描述 |
| A concept appears in 2 entries across different contexts | "WSL 问题 + Docker 问题 → 都是环境类" | 可以考虑注册 `environment` |
| A concept appears in 3+ entries with no existing tag covering it | "工具链问题 → 已有 `tool-system`" | 如果词义匹配则不注册；如果不匹配则注册 |
| A project starts producing entries | "开始 metapowers 项目工作" | 注册 project tag |
| An existing tag feels too broad/narrow | "`frontend` 太大，需要区分 React/Vue" | 先观察——如果用量足够，再考虑拆分 |

> **Default**: don't register. A tag that is merely "nice to have" is not worth the maintenance cost. Wait until the third occurrence of a concept before registering — this filters out one-off events.

---

## Naming Conventions

### Rules (hard)

- **Lowercase only**: `design-decision` ✓, `Design-Decision` ✗
- **Kebab-case**: `tool-system` ✓, `tool_system` ✗, `toolSystem` ✗
- **Singular**: `lesson` ✓, `lessons` ✗
- **No abbreviations** unless universally understood: `frontend` ✓, `fe` ✗; `architecture` ✓, `arch` ✗
- **语义明确**: 另一个 agent 看到 tag 名能大致猜出含义，不需要反复查 TAGS.md

### Guidelines (soft)

- Use existing tag names as pattern reference — new tags should "look like" the existing set
- Avoid negations: `no-react` is worse than `vue` (use positive tags, not negative ones)
- Avoid overly specific tags: `wsl-vite-hotfix` → better as `environment` + tags in body
- If a tag needs a long description to explain, it's probably too specific

---

## Registration Process

When you need a new tag during daily writing:

1. **Check TAGS.md** — is this concept already covered by an existing tag? If yes, use that.
2. **Check for synonyms** — is there an unregistered tag you saw in other entries that means the same thing? If yes, either register it (if worth keeping) or use a different existing tag.
3. **Name it** — apply naming conventions above.
4. **Add to TAGS.md** — add a row to the Tags table with tag name and a one-line meaning.
5. **Use it** — now it's registered, use it in the current entry's frontmatter.

To keep registration friction low, the TAGS.md file is small and simple. Opening it, adding a row, and saving takes one tool call.

---

## Dimension Organization (Optional)

As the tag list grows past ~15 entries, navigation becomes harder. Dimension grouping is a way to organize tags into categories for easier scanning.

### Common Dimensions

| Dimension | Meaning | Example Tags |
|-----------|---------|-------------|
| **Activity** | What kind of work was done | `research`, `documentation`, `plan` |
| **Domain** | What subject area | `frontend`, `architecture`, `screenwriting` |
| **Meta** | What kind of cognitive output | `lesson`, `methodology` |
| **Project** | Which project this belongs to | `metapowers`, `scriptum` |

### When to Add Dimensions

- **Don't add dimensions upfront.** Start with a flat list. Dimensions are a navigation aid, not a structural requirement.
- **Add when** scanning the flat list becomes noticeably harder than scanning grouped sections — typically ~15+ tags.
- **Re-evaluate during maintenance** — Phase 1 Step 2c checks if the current dimensional structure still fits usage patterns.

### Format with Dimensions

```markdown
## Tags

### Activity
| Tag | Meaning |
|-----|---------|
| `research` | 调研、信息搜集与分析 |
| `plan` | 计划制定、路线图 |

### Domain
| Tag | Meaning |
|-----|---------|
| `frontend` | 前端/UI |
| `architecture` | 系统架构 |

### Meta
| Tag | Meaning |
|-----|---------|
| `lesson` | 教训、经验总结 |
| `methodology` | 方法论提炼 |

### Project
| Tag | Meaning |
|-----|---------|
| `scriptum` | 项目 A 相关 |
```

> Dimension classification is a **design choice** per journal. Some journals never need it. Others find it essential. The skill does not prescribe one over the other.

---

## TAGS.md Rules Design

The `## Rules` section in TAGS.md defines journal-specific usage constraints. The initialization seed includes one default rule (`每条至少选一个 tag`). Add more as usage patterns emerge.

### Common Rule Patterns

| Rule | When to Add |
|------|-------------|
| `每条至少选一个 tag` | Default — ensures no entry is untagged |
| `project tag 可选` | When project tags exist but aren't always relevant |
| `project tag 必选` | When most entries belong to a project and untagged entries are noise |
| `domain tag 至少一个` | When cross-domain search is a primary use case |
| `同时包含 activity 和 meta tag` | When you want to separate "what I did" from "what I learned" |

### When Rules Need Updating

Rules should be reviewed during maintenance Phase 1 alongside the rest of the tag review:

- A rule that no entry follows → remove or re-evaluate
- A rule that every entry trivially satisfies → consider removing (it adds no signal)
- A rule that forces a tag choice that doesn't fit actual usage → revise

---

## Tag Lifecycle

```
Created (registered in TAGS.md)
    ↓
Active (appears in new entries regularly)
    ↓
Rarely used (last used >6 months ago, 1-2 entries total)
    ↓
Retired (removed from TAGS.md, entries keep their tags for history)
```

### Merging Tags

When two tags mean the same thing (synonym detection during maintenance):

1. Pick the canonical tag (the one that is more used, more precise, or better named)
2. Replace all occurrences of the dropped tag with the canonical tag
3. Remove the dropped tag from TAGS.md
4. Keep the dropped tag's meaning as a note in the canonical tag's description if helpful

### Removing Tags

A tag should be removed from TAGS.md when:

- **Zero active entries use it** — entries in archive/ still have the tag, but new entries don't
- **It has been merged** into a canonical tag
- **It was created for a now-defunct project** — and no new entries will use it
- **It was a mistake** — too vague, too specific, or a duplicate from the start

Removing from TAGS.md does not require removing from archived entries. Historical entries retain their tags as-is.

---

The skill provides `examples/journal-standards/TAGS.example.md` as a reference example — a mature tag set with dimensional organization. Use it as inspiration, not as a template to copy.
