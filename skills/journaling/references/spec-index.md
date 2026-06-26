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
## Protocol Declaration (Required)


Top of file. Five items:
- **Skill association**: `> ⚠️ 本 journal 由 `journaling` 技能管理`
- **Read/write rule**: 读 INDEX.md 不需要加载 skill；写入或维护时必须加载 journaling skill
- **Self-management reference**: `> 分类规则 → \`CLASSIFICATION.md\` · 标签系统 → \`TAGS.md\``. Links to the journal's classification rules and tag registry. CLASSIFICATION.md exists only when the journal has evolved beyond the seed structure — when absent, the 4‑directory seed is the implicit classification. TAGS.md always exists after initialization.
- **Maintenance trigger reminders** (dynamic snapshot + action hint): After each maintenance Phase 1, rewrite this line to reflect the current state. Format: `维护信号：<signals found>`. Example: `维护信号：经验摘要含 axiom(2) · 最近变更 9/7 · 维护备忘 12/10 · active_works/ 积灰`. An empty line = no signals. When 2+ signals are at threshold or memo exceeds 10 items, consider running a full maintenance pass — load journaling skill → `references/protocal-maintenance.md`.
- **Journal root** (optional, recorded during initialization): `> Journal root: <path>`. Used for multi-session discovery verification.

---

## Recommended Organization

INDEX.md 的具体组织由每个 journal 自行演化，没有固定的章节模板。从协议声明开始，随着条目增加逐渐自然生长出适合自己项目的结构。

如果 INDEX.md 在当前组织方式下感觉不够用（信号不清晰、专项工作堆积、变更列表过长），参见 `references/protocal-maintenance.md` Phase 1 Step 1 中的 Dashboard 组织审查步骤。

关于为特定项目/领域创建独立的次级 INDEX，参见 `patterns/dashboard.md`。

