# INDEX.md Specification

**INDEX.md 是 journal 的封面——唯一入口。**

journal 是动态加载的提示系统：

- 读取它不需要加载 skill——不加载 journaling 也能访问 INDEX.md
- 写入它需要加载 journaling 技能的 references
- 从 INDEX.md，agent 一眼看到 journal 全貌，并沿链接进入详细笔记

INDEX.md 必须：不加载技能时即可一览 journal 全貌，并提供进一步检索的依据。

---

## 协议声明（必含）

文件顶部。以 `## 协议声明` 标题开始，以下内容以列表形式依次列出（由种子提供，全程不变——结构不变，其中值为快照，随维护更新）：

- ⚠️ 本 journal 由 `journaling` 技能管理
- Journal root（可选，初始化时记录）
- 价值自述（可选，推荐）
- 读此文件不需要加载 skill · 写入或维护时（含移动、归档、删除操作）必须加载 journaling

---

## 归属

INDEX.md 的具体格式（板块选择、同步节奏、维护规则）由 journal 自身规则规范——见 journal 规则文档的 INDEX 结构板块。

归属链：INDEX 格式的唯一权威在 journal 规则；design-index.md 是纯设计参考，其"具体格式由 journal 规则规范"为反向指针，非循环依赖。

INDEX 设计参考（板块建议/组织方式）见 `design-index.md`。
