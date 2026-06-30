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
  version: "4.9.0"
  last_updated: "2026-06-30"
---

# Journaling

> **在任何 <journal-root> 写入性操作（创建、编辑、移动、归档、删除等）前必须加载。**

Journal 是你的结构化长期记忆机制——跨 session 的经验、决策、研究和方法论存储。有了 journal，第二个 session 可以直接从上一个 session 结束的状态继续：读状态、接工作、避开过去的坑。

本技能定义 journal 的设计概念、结构，及其全部操作——初始化、读取、写入、导入、维护。

## Journal

Journal 位于 `<journal-root>`，由以下要素构成：

- **INDEX.md** — 封面与仪表盘。Journal 的唯一入口，显示当前状态信号。一切 journal 操作从这里开始。
- **个性化规则文件** — 三份文件，定义这个 journal 的运作方式：
  - `CLASSIFICATION.md` — 目录分类规则
  - `TAGS.md` — 标签注册表及使用规则
  - `CONVENTIONS.md` — 设计模式实例（可选；存在时优先级高于前两份——特例覆盖默认规则）
- **条目** — 各条笔记，按生命周期目录组织（inbox → experience | knowledge | active_works → archive）


---


## Before You Begin

This skill's protocols depend on `<journal-root>/index.md` context — maintenance signals, active works, and experience traps. If you have not read INDEX.md this session, open it now and note:

- **Active maintenance signals** — they determine whether a full maintenance cycle is needed
- **Active works** — your changes may conflict with ongoing operations if assessed without this context
- **Relevant experience entries** — traps and lessons that apply specifically to your current task

Operating without INDEX.md means operating blind. INDEX.md is the cover of your journal — it tells you what needs maintenance, what's in progress, and what traps to avoid. The file takes seconds to read and prevents hours of blind work.
## Core Constraint

**INDEX.md is the sole entrance to journal.** It is the notebook cover — a dashboard of state signals, not a directory listing. All journal norms (format, directory usage, maintenance) are defined by this skill.

## Linked Files

- [INDEX.md Specification](references/spec-index.md) — INDEX.md 的核心规范：协议声明、设计原理、与个性化规则文件的关系。关于项目级次级 INDEX 的设计参考，见 `references/patterns/dashboard.md`。
- [Writing Protocol](references/protocal-write.md) — 写条目的工作流程：triage 判断、同 session 补充 vs 跨 session 补充、After Writing 更新 INDEX.md、Before Delivery 自检。
- [Note Writing Guide](references/spec-note.md) — 条目格式指南：summary anchoring 三检查点、body 格式（一句一行/wikilink/过度泛化/context boundary）、粒度控制、4 种子目录分配、条目生命周期。
- [Importing Protocol](references/protocal-import.md) — Bring existing external content into the journal: evaluation, copy, frontmatter, adjustment.
- [Journal Initialization](references/protocal-init.md) — Create a new journal from scratch: three-phase protocol (locate root → init skeleton files → design discovery contract).
- [Discovery Contract Design Guide](references/design-discovery-contract.md) — 发现合约设计的系统化方法：载体清查、过滤评估、推荐方案、用户呈报。在 `protocal-init.md` Phase 3 执行期间加载。
- [Maintenance Protocol](references/protocal-maintenance.md) — Full maintenance cycle: Phase 0 scan → Phase 1 review-design-settle-plan (3 rules) → Phase 2 rules-first then restructure → Phase 3 bidirectional verification → Phase 4 finalize. Trigger when dashboard signals or memo exceeds 10 items.
- [Journal Standards Examples](examples/journal-standards/) — INDEX.md、个性化规则文件等的参考示例。
- [Templates](templates/seed/) — 初始化所需的种子文件模板（INDEX.md、CLASSIFICATION.md、TAGS.md）。

- [Inbox](`inbox/README.md`) — Zero-friction staging area for unsure content. Requires only minimum frontmatter (title or date). Processed during maintenance.
- [Classification Design Guide](references/design-classification.md) — Design your journal's own classification: when to customize, design process, verification.
- [Classification System Examples](examples/classification-systems/) — Reference catalog of common real-world classification systems (PARA, Zettelkasten, Johnny Decimal, MOC/LYT, Evergreen, GTD, and journaling default). Each file starts with a summary for quick scanning.
- [Tag Design Guide](references/design-tags.md) — Tag creation, naming, registration, and lifecycle methodology. Consult when registering new tags or during tag maintenance.
- [Frontmatter Specification](references/spec-frontmatter.md) — YAML format rules, required fields, recommended optional fields, custom field guidelines, and examples.
- [Project Dashboard Pattern](references/patterns/dashboard.md) — 项目/领域级次级 INDEX 设计参考。和 INDEX.md 类比：提供聚焦一域的状态概览，作为 session 的次级路由入口。不是规范——从实际需求中生长。

- [Conventions Specification](references/spec-conventions.md) — CONVENTIONS.md 的设计原则与操作建议。描述 convention 机制的三条核心原则、文件格式、与各协议的关系。
- [Conventions Template](templates/seed/CONVENTIONS.md) — CONVENTIONS.md 种子模板。最小化格式参考，在维护中首次创建时使用。
---


## How to Use This Skill

This skill uses progressive disclosure. Load the reference document matching your scenario:

| Scenario | Load |
|----------|------|
| **Creating a new journal from scratch** | **`references/protocal-init.md`** |
| **Designing the discovery contract for a new journal** | **`references/design-discovery-contract.md`** |
| Writing/reviewing INDEX.md core spec and protocol declaration | `references/spec-index.md` |
| Creating or maintaining journal conventions (design pattern instances) | `references/spec-conventions.md` |
| Creating or reviewing a project-level dashboard (secondary INDEX) | `references/patterns/dashboard.md` |
| Writing a journal entry (workflow: triage → supplement → update INDEX.md → self-check) | `references/protocal-write.md` |
| Writing a journal entry (format: summary → body → granularity → directory → lifecycle) | `references/spec-note.md` |
| **Importing existing content into the journal** | **`references/protocal-import.md`** |
| **Capturing a discussion decision immediately into a project document** | **Operating Rules below** |
| Maintaining or cleaning up the journal | `references/protocal-maintenance.md` |
| Designing or revising journal classification | **`references/design-classification.md`** |
| Researching classification patterns for a custom design | **`examples/classification-systems/`** — read summaries, decide which to load |
| Designing or revising journal tag system | **`references/design-tags.md`** |
| Writing or checking entry frontmatter format | **`references/spec-frontmatter.md`** |
If the scenario is ambiguous, load two references. Don't load all at once.

---

## Operating Principles

These principles follow from the journal's design decisions. Each exists because a design choice creates a specific operational constraint.

- **Journal serves you, not the user — don't ask for approval, for reversible operations.** You write it, you maintain it, for your future self. The user cannot effectively judge whether a directory reorganization, tag merge, or archive is correct — these depend on patterns only you see. So reversible operations (directory reorganization, tag merge, archive) do not need permission. Irreversible operations (hard deletion) require explicit user confirmation or must follow the maintenance protocol's conditions. You MAY solicit the user's perspective on ambiguous cases to learn from their judgment, but the decision and execution are yours for reversible ops.

- **Select tags from TAGS.md before writing — the tag system is self-managed.** A tag not in `<journal-root>/TAGS.md` doesn't exist for this journal. If a needed tag is missing, register it there first. Freeform tags bypass the registry and silently decay into noise.

- **Determine directory assignment before writing — the directories are the classification.** Which directory an entry lands in is a decision about what kind of thing this is. Read `references/spec-note.md`'s Directory Assignment before creating.

- **Verify actual entry state before proposing improvements — the spec is ideal, the disk is truth.** The loaded spec describes what entries should look like; actual entries may already conform. Check files before recommending changes.


- **Capture discussion decisions immediately — confirmed decisions live on a different timeline than journal entries.** When the user confirms a design decision, write it to the target project document in the same turn. Do not defer to journal. A journal summary can follow later during maintenance.

- **'Delete' in journal means move to `archive/` — never direct file removal.** Everything that looks like deletion is actually moving to `archive/`. Hard deletion only occurs during maintenance cycles, and only for archive content that has survived at least one full maintenance cycle. This replaces and supersedes any previous "check before deletion" rules — deletion is not a valid daily operation.
