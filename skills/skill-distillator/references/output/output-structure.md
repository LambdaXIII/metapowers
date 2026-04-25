# 输出结构定义

> 蒸馏技能的输出文档结构、文件定义和处理规则

---

## 输出形态决策

| 原始技能结构 | 输出形态 |
|-------------|----------|
| 只有 SKILL.md，且 < 400 行 | 单文件 |
| 只有 SKILL.md，但 ≥ 400 行 | 多文件 |
| 有 SKILL.md + 其他文件（references/、examples/、DESIGN.md 等） | 多文件 |

---

## 多文件目录结构

```
<output-dir>/
├── README.md                    # L1: 概览层（Tutorials）
│   ├── 一句话定义
│   ├── 适用场景
│   ├── 快速开始
│   └── 文档导航
├── methodology/                 # L2-L3: 方法论层
│   ├── core-concepts.md         # Explanation: 核心概念
│   ├── workflow.md              # How-to: 工作流程
│   └── decision-rules.md        # Reference: 决策规则
├── reference/                   # L3: 参考层
│   ├── guide-xxx.md             # Reference: 各参考文档人类可读版
│   └── examples.md              # Tutorials: 典型示例
└── meta/                        # L4: 深度层
    ├── changelog.md             # 版本历史
    └── design-notes.md          # 设计笔记
```

---

## 单文件输出结构

当原始技能只有 SKILL.md 且 < 400 行时，输出为单个文件：

```markdown
# [技能名称]

> [一句话定义]

---

## 适用场景
...

## 核心概念
...

## 工作流程
...

## 决策规则
...

## 设计笔记
（如有 DESIGN.md，补充设计思想）
```

**章节说明**：
- 按渐进式披露组织：概览 → 概念 → 流程 → 规则 → 设计
- 仍然应用 Diátaxis 分类逻辑，但合并到同一文件的不同章节
- 视角转换原则不变
- 纯指令型技能的"核心概念"和"设计笔记"章节可能内容极少，可合并为"背景与概念"章节

---

## 各文件定义

### README.md

**目标**：让读者 2 分钟内了解这个技能

**内容**：
- **一句话定义**：技能是什么
- **适用场景**：什么时候用这个技能
- **快速开始**：最简单的使用方式
- **文档导航**：引导读者去哪个文件找什么

**来源**：SKILL.md 中的"核心定位"、"触发决策规则"

---

### methodology/core-concepts.md

**目标**：解释技能的核心概念和设计思想（Explanation）

**内容来源**：
- SKILL.md 中的"核心定位"、"指导思想"
- DESIGN.md 中的"核心思想"

**处理原则**：
- 解释"为什么这样设计"
- 保留核心概念的定义
- 去除执行指令性质的内容，转为说明型表达

---

### methodology/workflow.md

**目标**：说明技能的工作流程（How-to）

**内容来源**：
- SKILL.md 中的流程章节
- references/ 中的方法论文档

**处理原则**：
- 说明每一步的目的和逻辑
- 保留关键决策点
- 从"指令型"转为"说明型"

---

### methodology/decision-rules.md

**目标**：说明技能的决策规则和边界（Reference）

**内容来源**：
- SKILL.md 中的"触发决策规则"、"边界与约束"
- DESIGN.md 中的"关键决策"

**处理原则**：
- 明确什么情况下应该/不应该使用
- 说明约束条件及其理由

---

### reference/guide-xxx.md

**目标**：人类可读版参考资料（Reference）

**内容来源**：references/ 目录下的各文件

**处理原则**：
- **不是简单复制**，而是视角转换（指令→说明）
- 从"Agent参考"转为"人类参考"
- 保留完整内容，转换表达方式
- 清晰的内容直接摘取，指令型内容转为说明型

---

### reference/examples.md

**目标**：典型示例汇总（Tutorials）

**内容来源**：
- examples/ 目录
- SKILL.md 中的示例

**处理原则**：
- 选择 2-3 个最有代表性的示例
- 每个示例包含：场景描述 + 输入 + 输出 + 关键点说明
- 展示典型用法，而非罗列所有

---

### meta/changelog.md

**目标**：版本历史

**内容来源**：CHANGELOG.md

**处理原则**：
- 保留版本号、日期、变更摘要
- 去除过细的实现细节

---

### meta/design-notes.md

**目标**：设计笔记

**内容来源**：DESIGN.md

**处理原则**：
- 保留设计初衷和关键决策
- 说明"为什么这样设计"

---

## 文件处理规则

| 源文件/目录 | 处理方式 | 输出位置 | 处理原则 |
|------------|----------|----------|----------|
| SKILL.md | 拆解为核心概念、工作流程、决策规则 | methodology/ + README.md | 提取 WHY/HOW/WHAT |
| DESIGN.md | 提取设计思想和关键决策 | meta/design-notes.md + methodology/core-concepts.md | 深入心智模型层 |
| CHANGELOG.md | 整理为版本历史 | meta/changelog.md | 保留摘要 |
| references/ | 每个文件转换为人类可读版 | reference/guide-xxx.md | 视角转换，保留完整内容 |
| examples/ | 选择典型示例汇总 | reference/examples.md | 选择 2-3 个典型 |

---

## 边界情况处理

| 情况 | 处理方式 |
|------|----------|
| 技能没有 references/ | 跳过 reference/ 目录生成 |
| 技能没有 examples/ 且 SKILL.md 中无可提取示例 | 不生成 examples.md，在 README.md 导航中说明该文件不存在 |
| 技能没有 DESIGN.md | 仅从 SKILL.md 推断设计思想，输出中标注"设计笔记基于推断" |
| DESIGN.md 存在但内容空洞（可提取的元认知知识 < 5 条） | 视同"不存在"，从 SKILL.md 推断设计思想，输出中标注"设计笔记部分基于推断" |
| references/ > 10个 | 按核心能力域分组，每组一个 guide 文件（能力域来自解构阶段的能力清单） |
| 技能版本为 1.0（无变更历史） | changelog.md 可简化或标注"初始版本" |

---

## Diátaxis 类型映射

| 输出文件 | Diátaxis 类型 | 用户意图 |
|----------|---------------|----------|
| README.md | Tutorials | "带我快速了解" |
| methodology/workflow.md | How-to Guides | "如何执行流程" |
| reference/guide-xxx.md | Reference | "我需要查细节" |
| methodology/core-concepts.md | Explanation | "为什么这样设计" |
| reference/examples.md | Tutorials | "给我看例子" |
