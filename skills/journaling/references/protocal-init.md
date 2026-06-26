> Use this reference when creating a new journal from scratch — first install, new environment, or blank start.
> If a journal already exists (INDEX.md is present and validated by protocol declaration), initialization is not needed.
> If the target path already has content (files, directories), see Step 0 for the decision tree — the correct action depends on what's there.
>
> This reference contains **two layers of instruction**:
> - **Meta-instructions** (explain why and how): tell *you*, the agent running initialization, what needs to happen and why
> - **Startup Protocol** (a block of text to write): a message *you write for future agents*, telling them where the journal lives and what to do at startup
>
> Do not confuse the two. Meta-instructions are for your current work. The Startup Protocol is for future sessions — it should contain pure commands, no explanations.

---

## Step 0: Confirm Journal Root & Pre-Check

> ⚠️ Meta-instruction
>
> You must choose a location for the journal. This is the **only** step that requires user input.
> The path must survive agent restarts (not in temp, not inside a project working tree).
> The path must be writable.
>
> Once confirmed by the user, this path is fixed — do not change it during initialization.

Present candidate paths to the user. Collect input. Confirm the chosen `<journal-root>` before proceeding.

After confirmation, record the path internally: you'll need it in every subsequent step.

### Pre-Check: Does the target path already have content?

| What you find | What it means | Action |
|---------------|---------------|--------|
| Path does not exist | Truly blank start | Create empty directory → proceed with default template (Steps 1–7) |
| Path exists, empty | No previous content | Proceed with default template (Steps 1–7) |
| `INDEX.md` present with valid protocol declaration (`> ⚠️ 本 journal 由 journaling 技能管理`) | Journal is already initialized and in use | **Stop.** Skip Steps 1–2, 4–6. Jump to Step 3 (establish/modify discovery contract) + Step 7 (verify) |
| Content exists but NO `INDEX.md` or no protocol declaration | Existing unstructured content, NOT a managed journal | **Use design mode.** Do NOT apply default template. Follow `references/design-classification.md` to analyze existing content and design a custom classification. After design, write `CLASSIFICATION.md` at root. Then proceed to Step 3 (discovery contract) + Step 7 (verify). |

> **三层逻辑总结**
> - 空目录 → 使用技能默认分类模板
> - 有内容但不是 journal → 按指导分析现有内容，设计自定义分类并写入 CLASSIFICATION.md
> - 已经是 journal（有 INDEX.md + 协议声明）→ 不动内容，只确保发现合约

## Step 1: Create Initial Directory Structure

**Conditional**: Only create directories when starting from scratch (path empty or non-existent).
If this is **design mode** (existing content, not a managed journal) → do NOT create directories. The existing structure is the starting point; `CLASSIFICATION.md` will document it.

Create these 4 directories under `<journal-root>` — a minimal seed that can grow in any direction:

```
inbox/          — 缓冲：不确定归属的内容，先放这里
experience/     — 经验：个人实践产出的教训、决策、方法论
knowledge/      — 知识：外部来源的研究、文献笔记、参考资料
active_works/   — 工作动态：当前任务进度、备忘、进行中事项
```

> 这个种子结构不预设最终形态。维护时通过分类审计（`references/protocal-maintenance.md` Phase 1 Step 1）和设计方法论
> （`references/design-classification.md`）逐步演化——分类规则随内容积累自然生长，在需要之前不要创建新目录。空目录是噪音。

Use your platform's directory creation tool. Examples for reference:
- Linux/macOS: `mkdir -p <root>/{inbox,experience,knowledge,active_works}`
- Windows PowerShell: `New-Item -Path "<root>\inbox","<root>\experience","<root>\knowledge","<root>\active_works" -ItemType Directory -Force`
- Windows cmd: `mkdir <root>\inbox && mkdir <root>\experience && mkdir <root>\knowledge && mkdir <root>\active_works`
---

## Step 1.5: Create Initial CLASSIFICATION.md

**Conditional**: Only create `CLASSIFICATION.md` when starting from scratch (Steps 1–7).
If this is **design mode** (existing content, not a managed journal) → CLASSIFICATION.md is created at the end of the design process (see `references/design-classification.md`), not here.

Create `<journal-root>/CLASSIFICATION.md` documenting the 4 seed directories as the initial classification:

```markdown
# Classification

> 本文件记录当前 journal 的分类规则。封面提供快速参考，定义见下文。
> 此文件在维护时重新评估，日常操作不读取全文。

## 快速参考

| 目录 | 放什么 | 不放什么 | 一句话判断 |
|------|--------|---------|-----------|
| `inbox/` | 缓冲：不确定归属的内容，先放这里 | 已明确分类的内容 | 知道放哪？→ 直接放目标目录。不确定？→ inbox |
| `experience/` | 经验：个人实践产出的教训、决策、方法论 | 外部研究、进行中的任务 | 这来自我的实践吗？→ experience。来自外部？→ knowledge |
| `knowledge/` | 知识：外部来源的研究、文献笔记、参考资料 | 个人经验、活跃任务 | 这是我的原创经验吗？→ experience。来自外部？→ knowledge |
| `active_works/` | 工作动态：当前任务进度、备忘、进行中事项 | 已完成的经验、归档知识 | 这需要后续跟进吗？→ active_works。已完成？→ experience |
```

> 这个种子分类不预设最终形态。维护时通过分类审计（`references/protocal-maintenance.md` Phase 1 Step 1）和设计方法论
> （`references/design-classification.md`）逐步演化。
> CLASSIFICATION.md 的存在至关重要——它让分类规则显式化，使维护时知道"当前规则是什么"而不是"我记得是什么"。
---

## Step 2: Create INDEX.md

INDEX.md is the notebook cover — the sole entrance to the journal. It must follow the structure defined in `references/spec-index.md`:

**Core sections** (required):
1. **Protocol Declaration** — skill association, read/write rule, **self-management files reference (CLASSIFICATION.md, TAGS.md)**, maintenance trigger hints

**Optional sections** (add as needed, see spec-index.md for examples):
- Self-regulation rules, checklists, or other workflow-specific structures
- These are NOT part of the journaling design — they are agent-added organizational tools

### Initial Template

Start with the core sections below. Optional sections (self-regulation rules, etc.) can be added later when a workflow need arises. All sections start empty except where noted:

**Protocol Declaration** (required — this is what future sessions use to verify they found the right journal):

```
> ⚠️ 本 journal 由 `journaling` 技能管理
> 读此文件不需要加载 skill · 写入或维护时必须加载 journaling
> 分类规则 → `CLASSIFICATION.md` · 标签系统 → `TAGS.md`
> 维护信号：（空）
```

**Recent Changes** — one entry recording this initialization:

```
- YYYY-MM-DD: **Journal initialized**. <one-line summary of why it was created>
```

All other core sections start with a parenthetical note explaining when they get filled:

```
## 专项工作
*One line per domain. Grows from active work.*
```

Optional sections are not included in the initial template. Refer to `references/spec-index.md` → Other Sections when the need arises.

### Template Notes

- The 最近变更 section has one initial entry marking the creation date
- The protocol declaration is mandatory — it tells any Agent reading INDEX.md that this is a managed journal, not a free-form directory
---

## Step 3: Establish Discovery Contract

> ⚠️ Meta-instruction
>
> **Purpose**：
>
> 你当前这个 session 知道 journal-root 在哪里。但 agent 是无状态的——
> 下个 session 启动时，今天知道的一切都消失了。
> 如果 journal-root 不在启动时自动可见，那么 Step 1-2 创建的所有文件等于不存在。
>
> **目标状态**：
>
> 每次后续 session 启动时，agent 的上下文中**直接可见**一条指令：
> 必须读取 INDEX.md。不需要搜索、不需要回忆、不需要猜测。
>
> **不做的后果**：
>
> 文件都在，但下个 session 无法发现它们。agent 会认为 journal 不存在。
> 每次启动都需要一套搜索补偿算法（5 步发现链）——不可靠，且违背 journal 技能关于
> 「自动发现」的设计原则。
>
> **如何执行**：
>
> 这是一次设计决策。你比 skill 更了解你所在的环境——skill 只能给出判断标准和推荐做法，
> 具体方案由你根据环境自行设计并落实。
>
> **1. 识别载体**
>
> 在当前运行时中，寻找一个满足以下三条标准的注入点：
> - 每次启动 agent 时自动注入上下文（系统提示词、启动配置、env 等）
> - 你有权限写入或修改
> - 修改后跨 session 持久（不会被自动清除）
>
> 常见候选：SOUL.md、AGENTS.md、CLAUDE.md、.cursorrules、环境变量、系统提示词模板。
> 没有这些文件不代表没有载体——有些运行时会从特定路径加载配置，检查运行时目录。
> 你的判断是决定性的。
>
> **2. 写入启动指令**
>
> 将下方「Startup Protocol」写入载体。位置建议：
> - 放在文件顶部附近（确保最早被读到）
> - 或放在一个独立的内容区域（如 `## Journal` 节）
> - 如果载体已有内容，不要覆盖——追加或融入现有结构
>
> **3. 验证**
>
> 验证标准：(a) 写入操作无错误返回；(b) 重读该文件确认内容存在且路径正确；
> (c) 路径中的 `<journal-root>` 已被正确替换为实际路径。
>
> **4. 回退方案**
>
> 如果当前环境确实没有任何可用的注入机制：
> (a) 首先尝试创造一个——例如在运行时可配置的启动脚本目录下创建一个配置文件
> (b) 如果无法创造，回退到约定路径 `~/.agents/journal/`
> (c) 在 bootstrap entry 和初始化记录中标记 `无发现合约，使用约定路径回退`
> (d) 主动告知用户：每次启动需要手动指定 journal-root，或配置启动脚本。可靠性低于合约模式。

### Startup Protocol

> ⚠️ 以下文本是写给**将来每次 session 的 agent** 的。
> 将它写入上一步确定的载体位置。
>
> - **不要修改结构和语义**——这是写给未来 agent 的完整上下文，不是简化提示词。
> - **语言可以翻译**——如果运行时环境使用非中文，将指令翻译为对应语言，保持结构不变。
> - **唯一需要替换的部分**：`<journal-root>` 替换为实际路径。
>
> 核心结构：介绍 journal → 强调读取必要性 → 注明位置 → 写入指引在 INDEX.md 内。

```markdown
## Journal

This is your long-term memory — experiences, decisions, lessons, methodology
accumulated across all projects and sessions. Not a project log, not the user's document.

**At every session start, before any action:**
Read `<journal-root>/INDEX.md` — the dashboard.
Without it, you are working without your own accumulated knowledge.

The INDEX.md protocol declaration tells you when to load the journaling skill.
```


## Step 4: Initialize Tag Registry

Create a local tag file at `<journal-root>/TAGS.md` with a minimal seed:

```markdown
# Tags

> Tags must come from this file. Add new tags following `references/design-tags.md`.

## Rules

- 每条条目至少选一个 tag

## Tags

| Tag | Meaning |
|-----|---------|
| `lesson` | 教训、经验总结 |
| `research` | 调研、信息搜集与分析 |
| `knowledge` | 知识积累、外部学习 |
| `documentation` | 文档编写、修缮 |
| `journal` | Journal 自身维护 |
| `plan` | 计划制定、路线图 |
```

The skill also provides a reference example at `examples/journal-standards/TAGS.example.md` — a more developed tag set with dimensional organization. Consult it as an example when designing your own TAGS.md, but do not copy it wholesale — let your tags grow from actual content needs.

## Step 5: Write Bootstrap Entry

Create an entry at `<journal-root>/experience/` documenting the initialization itself.

**Frontmatter**:

```yaml
---
title: "Journal Initialization"
summary: "Initialized journal at <journal-root>"
tags:
  - journal
```

**Body**:
- Why the journal was created (first install, new environment, etc.)
- Journal root path and why it was chosen
- Directory structure created
- Initial state of INDEX.md (all core sections empty)
- Discovery contract: which carrier was used (or `无发现合约，使用约定路径回退`)
- What comes next (first entries will populate 经验摘要 and 专项工作 sections as real work happens)
---

## Step 6: Verify

> ⚠️ Meta-instruction
>
> Verify each item below. If any fails, fix it before yielding.
- [ ] `<journal-root>/CLASSIFICATION.md` exists with the 4 seed directories documented (inbox, experience, knowledge, active_works)
- [ ] `<journal-root>/TAGS.md` exists with the 6 seed tags (lesson, research, knowledge, documentation, journal, plan) and a Rules section
- [ ] Directory structure exists — list `<journal-root>/` shows 4 default directories (inbox, experience, knowledge, active_works)
- [ ] INDEX.md exists and contains all core sections (Protocol Declaration, Experience Summary, 专项工作, 最近变更)
- [ ] INDEX.md protocol declaration includes `⚠️ 本 journal 由 `journaling` 技能管理`
- [ ] Bootstrap entry exists in `experience/` and states the journal root path in its body
- [ ] INDEX.md 最近变更 has the initialization entry
- [ ] **Discovery contract established**: the Startup Protocol has been written into its target location, and the `<journal-root>` in that text matches the actual path
- [ ] **Self-test**: simulate a future session start — if you were starting fresh, would you see the journal instruction before acting? If the answer is anything other than "yes, immediately", fix the contract.
- [ ] **Fallback check** (only if no carrier exists): bootstrap entry and initialization record explicitly mark `无发现合约，使用约定路径回退`. Verify that the convention path `~/.agents/journal/` matches the actual journal root. If it doesn't, the journal will be undiscoverable — either move it or reconfigure.

---
## Post-Initialization

After initialization, the journal is ready for daily use. The first few sessions will typically:

1. **Add the first project tag** — when work on a project begins, add it to TAGS.md following naming conventions
2. **Write the first experience entries** — as lessons are learned, write them to `experience/`
3. **Write the first knowledge entries** — as external sources are studied, write them to `knowledge/`
4. **Add self-regulation rules** — when failures reveal patterns that INDEX.md should intercept, add a rule. This is optional and agent-driven, not a journaling requirement.
5. **Populate 专项工作** — when projects have active status, add one-line-per-domain entries
6. **Populate 经验摘要** — when cross-domain behavior-changing lessons emerge, add one-line entries

The journal grows organically from real use. Do not pre-populate sections with speculative content — every entry should trace back to a real experience, a real failure, or a real decision.

### How Future Sessions Find the Journal

The discovery chain is:

```
Startup Protocol (injected in system context)
  → <journal-root>/INDEX.md (the contract says to read this)
```

...with INDEX.md linking deeper into the journal:

```INDEX.md checks what the journaling skill says about where notes go and how to format them
        → Skill loading (when writing, load relevant references)
```

The Startup Protocol is the root of this chain. As long as it exists and points to the correct path, every future session will find the journal. No search needed. No 5-step decision chain.
