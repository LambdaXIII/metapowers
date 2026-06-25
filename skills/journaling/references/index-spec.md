# Dashboard (index.md) Specification

**index.md is the notebook cover — the sole entry point into the journal.**

The journal is a dynamically loaded prompt system:
- Reading it requires no skill — index.md is always accessible without loading journaling.
- Writing to it requires loading the journaling skill's references.
- From index.md, the agent sees the full picture in one glance and follows links into detailed notes.

index.md must be:
- **Concise enough** — dashboard, not document. One glance should tell the state.
- **Complete enough** — no signal is missing. The agent should never need a second pass.
- **Self-sufficient** — it works without any skill loaded, and tells the agent when to load one.
---

## Design Principles

These principles were derived from a real dashboard degradation event (2026-05-29), during which the index.md transitioned from a signal-emitting cover to a chronological log. They explain why the sections below have the shape they do.

| # | Principle | Core question | What it prevents |
|---|-----------|--------------|-----------------|
| 1 | **犯错测试** | "如果下次启动时没有这一行，我会不会犯错？" | 仪表盘退化为"日志"，信号被已完成记录淹没 |
| 2 | **一行一域** | 一个项目能压缩成一行吗？ | 结构性漂移：一个项目占据多行 |
| 3 | **场景编码** | 这一行编码了工作场景还是状态标签？ | 仪表盘与闸门之间失去桥接 |
| 4 | **公理分化** | 这条经验属于哪一类（enforcement/survival/axiom）？ | 有价值的公理支撑被删除 |
| 5 | **会话冷却** | 完成的里程碑有 2 次机会被看到吗？ | 信号在消费前消失 |
| 6 | **不同衰变率** | 各区域的淘汰节奏匹配其内容生命周期吗？ | 快衰和慢衰内容共用同一套规则 |

Each principle's rationale is embedded in the section it governs below. If you encounter a rule whose "why" is unclear, trace it back to this table.

---

## Sections

### 1. Protocol Declaration

Top of file. Four items:
- **Skill association**: `> ⚠️ 本 journal 由 `journaling` 技能管理`
- **Read/write rule**: 读 index.md 不需要加载 skill；写入或维护时必须加载 journaling skill
- **Maintenance trigger reminders** (dynamic snapshot + action hint): After each maintenance Phase 1, rewrite this line to reflect the current state. Format: `维护信号：<signals found>`. Example: `维护信号：经验摘要含 axiom(2) · 最近变更 9/7 · 维护备忘 12/10 · active/ 积灰`. An empty line = no signals. When 2+ signals are at threshold or memo exceeds 10 items, consider running a full maintenance pass — load journaling skill → `references/maintenance.md`.
- **Journal root** (optional, recorded during initialization): `> Journal root: <path>`. Used for multi-session discovery verification.

### 2. Experience Summary

Cross-domain, behavior-changing, sticky-note experiences. Selection criterion: **does this change how I behave in any task?** One line each, with a one-sentence summary. Link to experience/ for details.

Example:
```
• 先全景梳理再考虑扩展性 — "脚本级设计 vs 架构级设计"
• 讨论→共识→计划→行动，不跳步
• 机制优于变量 · 命名承载血统
```

Don't list every experience — only the most core ones on the cover. Details live on inner pages.

**Entry classification (the mistake test + axiom differentiation + scope):**

Each entry in the experience summary falls into one of these categories and scopes. During maintenance, audit every entry against these:

The mistake test is the sole gate: "If this line were absent from my next session startup, would I make a mistake?" Not "is this important?" — importance is subjective and everything can claim it. The mistake test is binary and falsifiable. An axiom about behavior is important, but it's already in working memory every turn — so it fails the test.

Differentiating entry categories (from principle 4) prevents a common failure: deleting all duplicates equally, which would strip enforcement entries that give gate rules their persuasive force.

| Category | Scope | Mistake test | Keep? |
|----------|-------|-------------|-------|
| `enforcement` | Meta | "Without this, does the gate rule lose its persuasive force?" | Yes — makes gates feel earned, not arbitrary |
| `survival` | Level-specific (project) | "Without this, would I hit this trap again?" | Yes — no other mechanism catches these |
| `axiom` | — | "Does working memory already say this?" | **No** — de-duplication: it's injected every turn |
| `level-specific` | A specific project | "Does this change how I work in project X?" | Yes — write into project entry point, not journal |
| `medium-level` | Documentation (any project) | "Without this, would my next doc fail the same way?" | Yes — independent of any project |
| `general` | Any work (meta) | "Would this help in a non-writing, non-project-specific task?" | Yes — broadest scope, cross-domain |

**Scope routing rule**:
- `level-specific` → project entry point (loaded per-project)
- `medium-level` → journal experience/ (loaded every session)
- `general` → journal experience/ (loaded every session)

**Anti-pattern**: listing axioms because "they're important." The dashboard is a supplement to memory, not a duplicate of it. An axiom that appears in both working memory and the dashboard is pollution — one of them should go, and the dashboard copy is the redundant one.

### 3. Project Work Status

Grouped by domain, **one line per domain** (principle 2). This is a structural constraint, not a suggestion: more lines than domains means drift has occurred. A single project maps to a single dashboard line — milestones, sub-tasks, and completion checklists live on inner pages, not the cover. A domain needing >1 line needs a workspace dashboard, not more cover entries.

Each line must pass the **mistake test** (principle 1): "If this line were absent from my next session startup, would I make a mistake?" Lines that fail are noise.

Each line must encode the current **work scene** (principle 3) — not just a status label like "active" or "completed", but what kind of work is happening. Scene encoding bridges the gap between the dashboard (what's going on) and the action gate (what to read before acting):

```
Project A — 📝 文档修缮：边界条件+设计决策对齐 [→](experience/2026-05-29-project-a-boundary-conditions.md)
```

The agent reading this knows: "the doc-review gate rule will likely trigger this session."

Contrast with a useless line that encodes only status:
```
Project A — 开发中
```
"开发中" passes the mistake test (forgetting project A is active → may switch to the wrong context), but it fails the gate bridge test — it doesn't tell the agent which gate rule to expect.

## Scene encoding format

`Domain — emoji current-work-scene: short-description [→](link)`. The emoji is a visual signal that speeds scanning. Common scene types: 📝 (documentation), 🏗️ (architecture/design), 🔧 (implementation), 🐛 (debugging), 🔍 (investigation/research), ✅ (completed — cooling period only).

**Anti-pattern — speculative future direction**: Never include a "下一步" that wasn't explicitly discussed. The scene describes work that *has been discussed or is in progress*, not what I imagine might come next. An inferred future direction with no discussion basis is a hallucination — it contaminates the dashboard and misleads future reads. If a direction was raised but not decided, mark it as `🤔 pending-discussion: topic` — this encodes uncertainty explicitly rather than pretending a decision exists.

**Cooling mechanism** (principle 5): Completed milestones stay on the dashboard for 2 sessions after completion, then sink to experience/. This ensures the signal is consumed before it disappears. The cooling period is session-based, not calendar-based — "2 sessions" means "the agent has had 2 opportunities to see this." Calendar days are fragile (completed Friday, next session Monday → signal expired before it was seen); session count is isomorphic.

Domains include concrete projects and meta-work (journal optimization, methodology realignment). Meta-work is a legitimate independent domain, not subordinate to any project.

Example (scene-encoded):
```
Project A — 📝 文档修缮：边界条件+设计决策对齐 [→](experience/2026-05-29-project-a-boundary-conditions.md)
Project B — 长期愿景：自定义协议 [→](goal/project-b-framework.md)
journal   — 闸门机制 v2 运行中 [→](experience/2026-05-20-journal-gate-mechanism.md)
```

Format: if a domain has a workspace dashboard, the domain name links to it. Otherwise, plain text with a link to the primary journal entry.

#### Workspace Dashboard Pattern

When a topic has entries scattered across multiple directories, create a topic dashboard in `workspace/` or a subdirectory. This keeps index.md at one-line-per-domain while providing navigation for the scattered topic.

**When to Create:**
- Topic has 5+ entries across directories
- index.md 专项工作 section has a subtree with 2+ indented items for one domain
- Topic is expected to grow (ongoing project / active investigation)

**When NOT to Create:**
- 1-2 entries — link directly from index.md
- Topic is concluded and fully archived — archive DASHBOARD suffices

**Template:**
```markdown
# <Topic> Dashboard

## Active Goals

| Goal | Status | Link |
|------|--------|------|

## Active Discussions

| Topic | Status | Link |
|-------|--------|------|

## Related

- Archive: [→](../archive/<topic>/DASHBOARD.md)
- Project docs: `<path>`
- Experience: `<links to key experience files>`
```

**index.md Link:**
```markdown
Topic Name — 状态简述 [→](workspace/<topic>.md)
```

Single line replaces what would have been a multi-line subtree.

### 4. Recent Changes

The most recent journal entry titles or one-line summaries, letting me know "what was last recorded". Date-descending. A **rolling window of the last 3 sessions**, capped at 7 entries. The purpose is recency signal — answering "what happened since I was last here?" — not a chronological archive. Older entries are findable via the file system.

Each section of the dashboard decays at its own rate (principle 6):

| Area | Decay rate | Management |
|------|-----------|------------|
| Recent Changes | Fast (session-level) | Rolling window 3 sessions, max 7 |
| Project Work | Medium (week/month-level) | One line per domain, 2-session cooling |
| Experience Summary (enforcement/survival) | Slow (month/year-level) | Only cleaned when related gate rule is removed |
| Experience Summary (axiom) | Immediate on deletion | Already in working memory; duplicate is instant-remove |

---

## Other Sections

Beyond the three core sections above, you may add additional sections that serve your workflow.
The examples below illustrate possible formats — they are not part of the journaling design,
and your index may look different.

### Behavioral Gate（行动闸门）— 可选示例

A behavioral gate is an interrupt table that maps specific actions to entries
that must be reviewed first. It answers "before I act on X, what must I review?"
It is optional — only create one if your workflow produces repetitive action patterns
that need interruption.

**Format** (one possible structure):

```
| 当我要... | 必须先读... | 跳过会怎样 |
|-----------|------------|-----------|
| [action phrase] | [entry paths + tags] | [one-line consequence] |
```

**Design tips** (only relevant if you use this pattern):
- Use first-person present-tense verbs for triggers
- Each rule must trace back to a real failure — no rule without a failure behind it
- Max 9 rules; at ≥10, trigger maintenance to merge or remove
- The consequence column must reference a specific past failure, not a general principle


### Write Gate（写入闸门）— 可选示例

A write gate is a self-question table that intercepts memory or profile writes.
Like the action gate, it is optional — add it only if memory pollution has been a problem.

**Format** (one possible structure):

```
| 自问 | 不过 → 放哪 |
|------|------------|
| [self-question] | [fallback destination] |
```

**Design tips** (only relevant if you use this pattern):
- Each question encodes a specific pollution failure
- Only add when pollution has actually caused problems
- Maintenance: remove questions whose failure mode no longer occurs
