# Dashboard (INDEX.md) Specification

**INDEX.md is the notebook cover — the sole entry point into the journal.**

The journal is a dynamically loaded prompt system:
- Reading it requires no skill — INDEX.md is always accessible without loading journaling.
- Writing to it requires loading the journaling skill's references.
- From INDEX.md, the agent sees the full picture in one glance and follows links into detailed notes.

INDEX.md must be:
- **Concise enough** — dashboard, not document. One glance should tell the state.
- **Complete enough** — no signal is missing. The agent should never need a second pass.
- **Self-sufficient** — it works without any skill loaded, and tells the agent when to load one.
---

## What is INDEX.md?

**定义**：INDEX.md 是 journal 的 dashboard 和唯一入口点。它不是目录列表，而是状态信号面板——一眼看清 journal 的当前状态。

**Role**：
- **Entry point**：所有 journal 操作的起点。读到 INDEX.md 即了解整个 journal 的结构和状态。
- **State dashboard**：经验摘要、专项工作、最近变更——三节编码了 journal 内"现在什么重要"的信号，不是"曾经发生过什么"的日志。
- **Maintenance carrier**：协议声明节告知何时加载 skill，维护信号项提示何时触发维护。

**Type Identification**：文件顶部为 `## 协议声明` 节（新版），或包含 `> ⚠️ 本 journal 由 journaling 技能管理`（旧版，下一个维护周期自动转换为新版）。此协议声明是初始化时写入的，用于类型识别——区分 journal 的仪表盘和恰好同名的其他 INDEX.md 文件。



## Design Principles

These principles were derived from a real dashboard degradation event (2026-05-29), during which the INDEX.md transitioned from a signal-emitting cover to a chronological log. They explain why the sections below have the shape they do.

| # | Principle | Core question | What it prevents |
|---|-----------|--------------|-----------------|
| 1 | **犯错测试** | "如果下次启动时没有这一行，我会不会犯错？" | 仪表盘退化为"日志"，信号被已完成记录淹没 |
| 2 | **一行一域** | 一个项目能压缩成一行吗？ | 结构性漂移：一个项目占据多行 |
| 3 | **场景编码** | 这一行编码了工作场景还是状态标签？ | 状态标签伪装成场景信号 |
| 4 | **必要性审计 (分类保留为维护逻辑)** | 这条经验属于哪一类（enforcement/survival/axiom）？ | 有价值的支撑条目在扁平列表中被无差别删除 |
| 5 | **会话冷却** | 完成的里程碑有 2 次机会被看到吗？ | 信号在消费前消失 |
| 6 | **不同衰变率** | 各区域的淘汰节奏匹配其内容生命周期吗？ | 快衰和慢衰内容共用同一套规则 |

Each principle's rationale is embedded in the sections they govern. If you encounter a rule whose "why" is unclear, trace it back to this table. These principles shape INDEX.md's design. The specific organization format is not mandated — your INDEX.md evolves with your journal.

---
## 协议声明（必含）

文件顶部。以 `## 协议声明` 标题开始，以下内容以列表形式依次列出：
- ⚠️ 本 journal 由 `journaling` 技能管理
- 个性化规则：[CLASSIFICATION.md]（目录分类）· [TAGS.md]（标签注册）· [CONVENTIONS.md]（约定特例）
- 维护信号：<signal snapshot>（例：经验摘要含 axiom(2) · 最近变更 9/7 · 维护备忘 12/10 · active_works/ 积灰）
- Journal root（可选，初始化时记录）
- 价值自述（可选，推荐）
- 读此文件不需要加载 skill · 写入或维护时（含任何写入、移动、删除操作）必须加载 journaling
---

## Recommended Organization

INDEX.md 的具体组织由每个 journal 自行演化，没有固定的章节模板。从协议声明开始，随着条目增加逐渐自然生长出适合自己项目的结构。

如果 INDEX.md 在当前组织方式下感觉不够用（信号不清晰、专项工作堆积、变更列表过长），参见 `references/protocal-maintenance.md` P1-S2（设计目标组织方式）中的 Pattern 选择维度。

关于为特定项目/领域创建独立的次级 INDEX，参见 `references/patterns/dashboard.md`。

