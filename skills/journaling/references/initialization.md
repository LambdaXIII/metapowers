# Journal Initialization

> Use this reference when creating a new journal from scratch — first install, new environment, or blank start.
> If a journal already exists (index.md is present and validated by protocol declaration), initialization is not needed.
>
> This reference contains **two layers of instruction**:
> - **Meta-instructions** (explain why and how): tell *you*, the agent running initialization, what needs to happen and why
> - **Startup Protocol** (a block of text to write): a message *you write for future agents*, telling them where the journal lives and what to do at startup
>
> Do not confuse the two. Meta-instructions are for your current work. The Startup Protocol is for future sessions — it should contain pure commands, no explanations.

---

## Step 0: Confirm Journal Root

> ⚠️ Meta-instruction
>
> You must choose a location for the journal. This is the **only** step that requires user input.
> The path must survive agent restarts (not in temp, not inside a project working tree).
> The path must be writable.
>
> Once confirmed by the user, this path is fixed — do not change it during initialization.

Present candidate paths to the user. Collect input. Confirm the chosen `<journal-root>` before proceeding.

After confirmation, record the path internally: you'll need it in every subsequent step.

---

## Step 1: Create Directory Structure

Create these 7 directories under `<journal-root>`:

```
inbox/      — Unclassified content (minimal format, processed during maintenance)
active/     — In-progress tasks, blocked items needing continuation
goal/       — Future directions, ideas needing discussion before implementation
experience/ — Completed practice: design decisions, lessons, methodology
research/   — External study: surveys, competitive analysis, papers
archive/    — Cold storage: inactive entries preserved for history
workspace/  — Topic dashboards (created on demand, can be empty initially)
```

Use your platform's directory creation tool. Examples for reference:
- Linux/macOS: `mkdir -p <root>/{inbox,active,goal,experience,research,archive,workspace}`
- Windows PowerShell: `New-Item -Path "<root>\inbox","<root>\active",... -ItemType Directory -Force`
- Windows cmd: `mkdir <root>\inbox && mkdir <root>\active && ...`

---

## Step 2: Create index.md

index.md is the notebook cover — the sole entrance to the journal. It must follow the structure defined in `references/index-spec.md`:

**Core sections** (required):
1. **Protocol Declaration** — skill association, read/write rule, maintenance trigger hints
2. **Experience Summary** — cross-domain lessons, one line each with link to entry
3. **专项工作 (Active Work)** — one line per domain, scene-encoded
4. **最近变更 (Recent Changes)** — last 7 entries, most recent first

**Optional sections** (add as needed, see index-spec.md for examples):
- Behavioral gates, write gates, or other workflow-specific structures
- These are NOT part of the journaling design — they are user-added organizational tools

### Initial Template

Start with the core sections below. Optional sections (gates, etc.) can be added later when a workflow need arises. All sections start empty except where noted:

**Protocol Declaration** (required — this is what future sessions use to verify they found the right journal):

```
> ⚠️ 本 journal 由 `journaling` 技能管理
> 读此文件不需要加载 skill · 写入或维护时必须加载 journaling
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

Optional sections are not included in the initial template. Refer to `references/index-spec.md` → Other Sections when the need arises.

### Template Notes

- The protocol declaration line is mandatory — it tells any Agent reading index.md that this is a managed journal, not a free-form directory
- The 最近变更 section has one initial entry marking the creation date

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
> 必须读取 index.md。不需要搜索、不需要回忆、不需要猜测。
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
> - **不要修改结构和语义**——这是纯指令，写给未来 agent。
> - **语言可以翻译**——如果运行时环境使用非中文（如纯英文 AGENTS.md），将指令翻译为对应语言，保持结构不变。
> - **唯一需要替换的部分**：`<journal-root>` 替换为实际路径。
>
> 翻译后的核心结构必须保持：必须读取 → 按指引工作 → 写入时加载 skill。

```markdown
## Journal

At each session start:
1. **必须且优先** 读取 <journal-root>/index.md
   — 这是 session dashboard，包含当前工作状态、闸门规则和近期上下文
2. 根据 index.md 的指引工作
3. 需要写入 journal 时，加载 journaling 技能的对应参考文件
```

---

## Step 4: Create Maintenance Memo

Create an empty file at `<journal-root>/.maintenance-memo.md`.

The file starts empty. During daily work, append issues noticed but not immediately fixed:

```markdown
- [ ] YYYY-MM-DD [symptom description]
```

The memo is a maintenance trigger at 10+ items (see `references/maintenance.md`).

---

## Step 5: Initialize Tag Registry

The tag registry lives in this skill at `references/tag-registry.md`. It contains:
- Activity tags (8 predefined)
- Domain tags (9 predefined)
- Meta tags (4 predefined)
- Project tags: **empty placeholder** — register your own as needed

When writing the first entry tied to a specific project, add that project's tag to the registry's Project Tags table. Follow the format:

```
| [tag-name] | One-line description of the project |
```

---

## Step 6: Write Bootstrap Entry

Create an entry at `<journal-root>/experience/` documenting the initialization itself.

**Frontmatter**:

```yaml
---
title: "Journal Initialization"
date: "YYYY-MM-DD"
tags: [journal, skill]
summary: "Initialized journal at <journal-root>"
status: completed
---
```

**Body**:
- Why the journal was created (first install, new environment, etc.)
- Journal root path and why it was chosen
- Directory structure created
- Initial state of index.md (all sections empty, gates empty)
- Discovery contract: which carrier was used (or `无发现合约，使用约定路径回退`)
- What comes next (first entries will populate experience summary and project work sections; gate rules will be added as failures occur)
---

## Step 7: Verify

> ⚠️ Meta-instruction
>
> Verify each item below. If any fails, fix it before yielding.

- [ ] Directory structure exists — list `<journal-root>/` shows all 7 directories
- [ ] index.md exists and contains all core sections (Protocol Declaration, Experience Summary, 专项工作, 最近变更)
- [ ] index.md protocol declaration includes `⚠️ 本 journal 由 `journaling` 技能管理`
- [ ] .maintenance-memo.md exists (empty)
- [ ] Tag registry is accessible at the skill's `references/tag-registry.md`
- [ ] Bootstrap entry exists in `experience/` and states the journal root path in its body
- [ ] index.md 最近变更 has the initialization entry
- [ ] **Discovery contract established**: the Startup Protocol has been written into its target location, and the `<journal-root>` in that text matches the actual path
- [ ] **Self-test**: simulate a future session start — if you were starting fresh, would you see the journal instruction before acting? If the answer is anything other than "yes, immediately", fix the contract.
- [ ] **Fallback check** (only if no carrier exists): bootstrap entry and initialization record explicitly mark `无发现合约，使用约定路径回退`. Verify that the convention path `~/.agents/journal/` matches the actual journal root. If it doesn't, the journal will be undiscoverable — either move it or reconfigure.

---

## Post-Initialization

After initialization, the journal is ready for daily use. The first few sessions will typically:

1. **Add the first project tag** — when work on a project begins, register it in tag-registry.md
2. **Write the first experience entries** — as lessons are learned, write them to `experience/`
3. **Add the first gate rule** — when a failure proves a gate rule is needed, add it to index.md
4. **Populate 专项工作** — when projects have active status, add one-line-per-domain entries
5. **Populate 经验摘要** — when cross-domain behavior-changing lessons emerge, add one-line entries

The journal grows organically from real use. Do not pre-populate sections with speculative content — every entry should trace back to a real experience, a real failure, or a real decision.

### How Future Sessions Find the Journal

The discovery chain is:

```
Startup Protocol (injected in system context)
  → <journal-root>/index.md (the contract says to read this)
    → Protocol Declaration (verifies this is the right journal)
      → Dashboard (tells agent current state and what to do)
        → Skill loading (when writing, load relevant references)
```

The Startup Protocol is the root of this chain. As long as it exists and points to the correct path, every future session will find the journal. No search needed. No 5-step decision chain.
