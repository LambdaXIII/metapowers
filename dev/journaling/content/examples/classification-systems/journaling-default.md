# Journaling 默认分类方案

> journaling 技能初始化时创建的种子结构。按主观/客观 × 长期/短期两个维度组织。初始只有 4 个目录，在维护中按需演化。

**创建者**: Ĉalio
**核心分类维度**: 主观/客观 + 长期/短期

## 种子结构

```
📁 inbox/          ← 缓冲：不确定归属的内容
📁 experience/     ← 经验（主观·长期）：个人教训、决策记录、方法论
📁 knowledge/      ← 知识（客观·长期）：外部研究、文献笔记、参考
📁 active_works/   ← 工作动态（短期）：任务进度、备忘、进行中事项
```

## 分类逻辑

| 内容性质 | 放哪 | 示例 |
|---------|------|------|
| 不确定的分类 → | `inbox/` | 尚未决定的新笔记 |
| 个人实践产出的经验 → | `experience/` | ""写前 mtime 比较防止冲突" |
| 外部来源的知识 → | `knowledge/` | "消息队列对比调研" |
| 处理中的任务 → | `active_works/` | "当前项目进度备忘" |

## 演化路径

这个种子结构在 journaling 自己的 journal 中长成了以下形态。这不是初始模板——是维护中自然演化的结果。

```
📁 inbox/          ← 零摩擦捕获缓冲
📁 active/         ← 活跃事务（从 active_works/ 拆分出来）
📁 goal/           ← 长期目标（从 active_works/ 拆分出来）
📁 experience/     ← 经验沉淀（不变）
📁 research/       ← 调研记录（从 knowledge/ 拆分出来）
📁 reference/      ← 参考资料（从 knowledge/ 拆分出来）
📁 archive/        ← 归档（按需创建）
and: workspace/    ← 主题面板（按需创建）
```

分裂触发条件：
- **active_works/ → active/ + goal/**：当"正在做的事"和"未来想做的事"在数量上都达到需要独立目录时
- **knowledge/ → research/ + reference/**：当"深度研究"和"一键参考"的查询模式明显不同时
- **archive/ 创建**：当有内容需要冷存储但不想删时。不在初始结构里
- **workspace/ 创建**：当需要跨目录的主题聚合面板时

## 与其他系统的关系

| 本技能种子 | 本技能演化形态 | PARA | Zettelkasten |
|-----------|--------------|------|-------------|
| inbox/ | inbox/ | ←（无） | inbox |
| experience/ + knowledge/ | experience/ + research/ + reference/ | Resources | notes + literature |
| active_works/ | active/ + goal/ | Projects + Areas | — |
| — | archive/ | Archive | — |

## 额外分类维度：认知价值审计

除了目录归属，每条经验类笔记还应按以下概念分类（维护时评估，不体现在目录上）：

| 分类 | 定义 | 处理 |
|------|------|------|
| **Enforcement** | 已经写入协议的硬规则 | 需验证是否仍被执行 |
| **Survival** | 自己摸索的"保命"模式 | 检查是否已过时或被标准化 |
| **Methodology** | 通用工作方法 | 跟踪是否失效 |
| **Axiom** | 不证自明的底层原则 | 不再重新判断 |

## 适用场景

- **AI agent 的长期记忆**——非人类读者
- **多 agent 共享**：需要规则清晰、免歧义
- **经验累积为主**：从项目工作和讨论中积累认知

## 改编要点

- 初始 4 目录是起点不是终点——在维护中按实际内容量演化
- `inbox/` 是必须存在的缓冲，不要试图跳过它直接分类——那正是分类瘫痪的源头
- `experience/` 和 `knowledge/` 的边界是"内部 vs 外部"——你做的 vs 别人做的
- 在需要之前不要创建新目录。空目录是噪音
- 分裂触发的信号是数量 + 查询模式，不是时间

- [技能 SKILL.md](../SKILL.md)
- [Dashboard 规范](../references/spec-index.md)
- [Writing Protocol](../references/protocal-write.md)
