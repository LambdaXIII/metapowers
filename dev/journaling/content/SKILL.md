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
  version: "5.0.2"
  last_updated: "2026-08-20"
---

# Journaling

Journal 是你的结构化长期记忆机制——跨 session 的经验、决策、研究和方法论存储。有了 journal，第二个 session 可以直接从上一个 session 结束的状态继续：读状态、接工作、避开过去的坑。

## Journal

Journal 位于 `<journal-root>`，由以下要素构成：

- **INDEX.md** — 封面与仪表盘。Journal 的唯一入口，显示当前状态信号。一切 journal 操作从这里开始。
- **规则文档（RULES.md）** — 规则单入口，定义这个 journal 的运作方式：INDEX 结构、分类、笔记元数据字段、写作约定等。内容由 journal 自定，种子提供初始方案。
- **条目** — 各条笔记。条目组织方式（目录、生命周期等）由 journal 规则定义。

---

## Before You Begin

This skill's protocols depend on `<journal-root>/INDEX.md` context — the journal's current state and operating context (what's in progress, what needs attention, what you've learned before). If you have not read INDEX.md this session, open it now.

Operating without INDEX.md means operating blind.

| 操作协议 | 适用时机 | 加载 |
|----------|---------|------|
| 初始化协议 | 创建新 journal | `references/protocal-init.md` |
| 写入协议 | 写入条目 | `references/protocal-write.md` |
| 导入协议 | 导入外部内容 | `references/protocal-import.md` |
| 维护协议 | 维护 / 整理 journal | `references/protocal-maintenance.md` |

其余参考文档按协议内引用按需加载。

## Linked Files
- [初始化协议](references/protocal-init.md)
- [Discovery Contract Design Guide](references/design-discovery-contract.md)
- [写入协议](references/protocal-write.md)
- [Note Writing Guide](references/spec-note.md)
- [Frontmatter Specification](references/spec-frontmatter.md)
- [导入协议](references/protocal-import.md)
- [维护协议](references/protocal-maintenance.md)
- [INDEX.md Specification](references/spec-index.md)
- [INDEX Design Reference](references/design-index.md)
- [Rules Specification](references/spec-rules.md)
- [Rule Design Guide](references/design-rules.md)
- [Project Dashboard Pattern](references/patterns/dashboard.md)
- [Layered Rules Pattern](references/patterns/layered-rules.md)
- [Note Tags Pattern](references/patterns/note-tags.md)
- [Maintenance Memo Pattern](references/patterns/maintenance-memo.md)
- [Classification Systems](references/patterns/classification-systems/)
- [Script Tools Guide](references/script-tools.md)
- [Templates](templates/seed/)

## Scripts

`scripts/` 目录提供零依赖便利工具（`frontmatter`、`check-links`），Python 与 Node.js 双版本。完整指南见 `references/script-tools.md`。

---

## Operating Principles

- **Journal serves you, not the user — reversible operations need no approval.** You write it, maintain it, for your future self. Directory reorganization, tag merge — these depend on patterns only you see; the decision and execution are yours.

- **标签遵循 journal 规则——标签系统由 journal 自管理。** 写前读取 journal 规则的标签相关内容；规则未定义标签时，从内容、用途等维度提炼简短词汇写入 `tags` 字段。

- **目录归属按 journal 规则判断——写前读取。** 写前读取 journal 规则文档（分类板块），判断这条内容属于哪个目录；未定义时用种子方案。目录归属是内容组织决策，归 journal 规则，不由技能规定。

- **Verify actual entry state before proposing improvements — the spec is ideal, the disk is truth.** Check files before recommending changes.

- **Capture discussion decisions immediately.** When the user confirms a design decision, write it to the target project document in the same turn. Do not defer to journal; a journal summary can follow later during maintenance.

- **删除处理按 journal 规则判断——技能不预设归档设施。** 写前读取 journal 规则的删除/归档约定；维护期间的删除按维护协议执行。
