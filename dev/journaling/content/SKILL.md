---
name: journaling
description: |
  **在任何 <journal-root> 写入性操作（创建、编辑、移动、归档、删除等）前必须加载。** 包括用户直接要求的 journal 操作。无需为仅读取 journal 内容而加载。

  写入操作示例：
  - 创建新 journal
  - 写入、编辑、移动、归档或删除 journal 条目
  - 维护 / 整理 journal
  - 将讨论中确认的设计决策写入 journal 文件
metadata:
  version: "5.0.0"
  last_updated: "2026-08-15"
---

# Journaling

> **在任何 <journal-root> 写入性操作（创建、编辑、移动、归档、删除等）前必须加载。**

Journal 是你的结构化长期记忆机制——跨 session 的经验、决策、研究和方法论存储。有了 journal，第二个 session 可以直接从上一个 session 结束的状态继续：读状态、接工作、避开过去的坑。

本技能定义 journal 的设计概念、结构，及其全部操作——初始化、读取、写入、导入、维护。

## Journal

Journal 位于 `<journal-root>`，由以下要素构成：

- **INDEX.md** — 封面与仪表盘。Journal 的唯一入口，显示当前状态信号。一切 journal 操作从这里开始。
- **规则文档（RULES.md）** — 规则单入口，定义这个 journal 的运作方式：分类、标签、INDEX 结构、笔记元数据字段、写作需求等。内容由 journal 自定，种子提供初始方案。
- **条目** — 各条笔记。条目组织方式（目录、生命周期等）由 journal 规则定义。


---


## Before You Begin

This skill's protocols depend on `<journal-root>/INDEX.md` context — maintenance signals, active works, and experience traps. If you have not read INDEX.md this session, open it now and note:

- **Active maintenance signals** — they determine whether a full maintenance cycle is needed
- **Active works** — your changes may conflict with ongoing operations if assessed without this context
- **Relevant experience entries** — traps and lessons that apply specifically to your current task

Operating without INDEX.md means operating blind. INDEX.md is the cover of your journal — it tells you what needs maintenance, what's in progress, and what traps to avoid. The file takes seconds to read and prevents hours of blind work.
## Core Constraint

**INDEX.md is the sole entrance to journal.** It is the notebook cover — a dashboard of state signals, not a directory listing. 本技能定义写入/维护流程协议（怎么写入、怎么维护）；内容组织规范（目录、标签、INDEX 结构等）由 journal 规则定义。

## Linked Files

- [INDEX.md Specification](references/spec-index.md) — INDEX.md 的核心规范：唯一入口定位、协议声明、格式归属（由 journal 规则规范）。关于项目级次级 INDEX 的设计参考，见 `references/patterns/dashboard.md`。
- [INDEX Design Reference](references/design-index.md) — INDEX 设计参考：常用板块建议、组织方式建议。设计自己的 INDEX 结构时加载。
- [Writing Protocol](references/protocal-write.md) — 写条目的工作流程：4 步写入流程（判断是否值得写 → 读取 journal 规则 → 编写 frontmatter 与 body → 检查可发现链路）+ 额外说明（补充已有条目/交叉引用/维护信号/自检提醒）。
- [Note Writing Guide](references/spec-note.md) — 条目格式指南：summary anchoring 三检查点、body 格式（一句一行/过度泛化/context boundary）、粒度控制、链接形态规范（Link Convention）。
- [Importing Protocol](references/protocal-import.md) — Bring existing external content into the journal: evaluation, copy, frontmatter, adjustment.
- [Journal Initialization](references/protocal-init.md) — Create a new journal from scratch: four-phase protocol (locate root + check existing content → init skeleton files → design discovery contract → maintenance takeover if content exists).
- [Discovery Contract Design Guide](references/design-discovery-contract.md) — 发现合约设计的系统化方法：载体清查、过滤评估、推荐方案、用户呈报。在 `references/protocal-init.md` Phase 3 执行期间加载。
- [Maintenance Protocol](references/protocal-maintenance.md) — 笔记库整理与规范演化：概述 + 推荐流程（扫描 → 设计（设计优化 + 规则区检查）→ 重组 → 细粒度收尾，执行路径可调整）+ 操作规范（硬性底线）+ 补充论述（启发）。若觉得 journal 过于混乱（如写入时错误尝试过多），适当向用户建议启动维护。
- [Journal Standards Examples](examples/journal-standards/) — INDEX.md、规则文档等的参考示例。
- [Templates](templates/seed/) — 初始化所需的种子文件模板（INDEX.md、RULES.md）。

- [Classification System Examples](examples/classification-systems/) — Reference catalog of common real-world classification systems (PARA, Zettelkasten, Johnny Decimal, MOC/LYT, Evergreen, GTD, and journaling default). Each file starts with a summary for quick scanning.
- [Rule Design Guide](references/design-rules.md) — 规则设计方法论：规则设计的建议、规则编写的原则、Pitfalls、建议的板块（含示例）。设计/修订 journal 规则（分类/标签/约定）时加载。
- [Frontmatter Specification](references/spec-frontmatter.md) — YAML format rules, required fields, recommended optional fields, custom field guidelines, and examples.
- [Project Dashboard Pattern](references/patterns/dashboard.md) — 项目/领域级次级 INDEX 设计参考。和 INDEX.md 类比：提供聚焦一域的状态概览，作为 session 的次级路由入口。不是规范——从实际需求中生长。
- [Script Tools Guide](references/script-tools.md) — frontmatter/check-links 脚本工具完整指南：命令参考、输出格式、链接解析语义、符号链接行为。
---


## How to Use This Skill

This skill uses progressive disclosure. Load the reference document matching your scenario:

| Scenario | Load |
|----------|------|
| **Creating a new journal from scratch** | **`references/protocal-init.md`** |
| **Designing the discovery contract for a new journal** | **`references/design-discovery-contract.md`** |
| Writing/reviewing INDEX.md core spec and protocol declaration | `references/spec-index.md` |
| Designing INDEX structure (sections/organization) | `references/design-index.md` |
| Creating or reviewing a project-level dashboard (secondary INDEX) | `references/patterns/dashboard.md` |
| Writing a journal entry (workflow: triage → read journal rules → frontmatter+body → discoverability) | `references/protocal-write.md` |
| Writing a journal entry (format: summary → body → granularity → links) | `references/spec-note.md` |
| **Importing existing content into the journal** | **`references/protocal-import.md`** |
| **Capturing a discussion decision immediately into a project document** | **Operating Rules below** |
| Maintaining or cleaning up the journal | `references/protocal-maintenance.md` |
| Designing or revising journal rules (classification/tags/conventions) | **`references/design-rules.md`** |
| Researching classification patterns for a custom design | **`examples/classification-systems/`** — read summaries, decide which to load |
| Writing or checking entry frontmatter format | **`references/spec-frontmatter.md`** |
If the scenario is ambiguous, load two references. Don't load all at once.

## Scripts

The `scripts/` directory contains zero-dependency convenience tools for common journal operations. All tools are dual-version (Python 3.8+ and Node.js 18+ ESM), with identical behavior across versions. Run `script.py --help` or `script.mjs --help` for usage; the complete guide (command reference, output formats, link resolution semantics, symlink behavior) is `references/script-tools.md`.

| Script | When to use |
|--------|-------------|
| `frontmatter` | Read, validate, update, or replace YAML frontmatter in journal entries. Use `get` to extract fields, `check` for format compliance, `update` for field-level merges, `replace` for full frontmatter swaps. |
| `check-links` | Extract all links from journal markdown files, verify target existence, and report broken links, orphan files, inbound references, and reference rankings. Use during maintenance quality check (broken links) or any time you need to know "who links to this file." |

**Key usage patterns**:

```bash
# Check all links in the journal — full report with summary, broken links, orphan files
python scripts/check-links.py INDEX.md

# Check links focused on a single file — outbound links + who references it
python scripts/check-links.py INDEX.md --file active_works/note.md

# Validate frontmatter format across all entries
python scripts/frontmatter.py check experience/*.md knowledge/*.md

# Batch-update last_update after maintenance
python scripts/frontmatter.py update *.md --data '{"last_update":"2026-06-30"}'
```

Scripts are convenience utilities — the agent can perform all operations manually using file tools (`grep`, `read`, `test -f`). Scripts provide faster, more reliable results for bulk operations.

---

## Operating Principles

These principles follow from the journal's design decisions. Each exists because a design choice creates a specific operational constraint.

- **Journal serves you, not the user — don't ask for approval, for reversible operations.** You write it, you maintain it, for your future self. The user cannot effectively judge whether a directory reorganization, tag merge, or archive is correct — these depend on patterns only you see. So reversible operations (directory reorganization, tag merge, archive) do not need permission. All journal operations are reversible — hard deletion is not a valid operation in this journal. You MAY solicit the user's perspective on ambiguous cases to learn from their judgment, but the decision and execution are yours for reversible ops.

- **标签遵循 journal 规则标签板块——标签系统由 journal 自管理。** 写前按 journal 规则标签板块选标签；未定义时用种子标签集。新标签按规则文档的注册约定注册。

- **目录归属按 journal 规则判断——写前读取。** 写前读取 journal 规则文档（分类板块），判断这条内容属于哪个目录；未定义时用种子方案。目录归属是内容组织决策，归 journal 规则，不由技能规定。

- **Verify actual entry state before proposing improvements — the spec is ideal, the disk is truth.** The loaded spec describes what entries should look like; actual entries may already conform. Check files before recommending changes.


- **Capture discussion decisions immediately — confirmed decisions live on a different timeline than journal entries.** When the user confirms a design decision, write it to the target project document in the same turn. Do not defer to journal. A journal summary can follow later during maintenance.

- **'Delete' in journal means move to `archive/` — never direct file removal.** Everything that looks like deletion is actually moving to `archive/`. This applies to daily operations and to maintenance alike — the maintenance protocol's hard rule is "不删除任何文件". This replaces and supersedes any previous "check before deletion" or cooling-period rules — deletion is not a valid operation in this journal.
