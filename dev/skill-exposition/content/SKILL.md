---
name: skill-exposition
description: |
  技能阐述（skill-exposition）：将一个技能（或其中指定的某些方面、或多个技能）转化为人类可读的说明文，让人类通过阅读材料学会这项技能。

  触发：「阐述技能 / 整理技能文档 / 生成方法论 / 把技能输出为文档 / 学会某个技能」；或 agent 需要把技能知识沉淀、传承给人类读者时。

  不触发：审查、评价、测试或创建技能。
metadata:
  version: "1.0.0"
  last_updated: "2026-08-08"
  author: "LambdaXIII"
  license: "MIT"
---

# Skill Exposition（技能阐述）

> 将一个技能（或其中指定的某些方面、或多个技能）转化为人类可读的说明文，让人类可以通过阅读材料学会这项技能。

## 这是什么

技能是为 agent 设计的可执行方法论载体——它的内容以指令形态存在，人类无法直接学习、传承、批判。本技能把技能内容转化为**说明文教学材料**：内容完整忠实（不歪曲、不省略、不劣化），组织利于学习。

交付物让人类学会使用该技能。人类学会后可以应用它、设计更好的技能——这是学习的结果，不属于本技能范畴。

**行为边界**：只读源文件、不修改；不执行、不测试被阐述的技能；不评价技能好坏。

## 触发条件

本节是 description 触发条件的展开版——description 负责被加载器（技能的加载/匹配机制）命中，下方条款供 agent 加载后决定是否启动本次阐述。

**合触发**（任一成立即触发）：

- 用户首话出现「阐述 / 整理成文档 / 生成方法论 / 输出为文档 / 学会」等动词，且对象是一个技能（或技能的部分方面、多个技能）
- 用户提供了技能目录（含 SKILL.md）或技能内容，要求产出人类可读的说明文
- 作为 agent，刚完成或接触到某个技能，自问「这个技能怎么教给别人」「怎么把它的知识沉淀成人类可读的材料」时

**不合触发**：

- 用户想要的是技能质量审查、评价、测试——那是审查类职责（如 skill-quick-test 的领域），不是阐述
- 用户想要创建新技能——那是 skill-creator 的领域
- 对象不是技能（不含 SKILL.md 的内容，如普通文档、代码库）——本技能只阐述技能

**边界判定**：拿不准时默认触发——产出说明文即使不完美也没有损失；漏阐述则技能知识继续被封存在执行指令里，人类仍然无法学习。

## 如何使用

1. 阅读 [exposition-guide.md](references/exposition-guide.md)——通用论述，必读。含完整方法：梳理 → 陷阱 → 组织 → 效果提及
2. 按需加载参考文件（见下方路由表）——自行判断，随时加载，提供启发而非必读

## 参考文件

**必读入口：**

- [exposition-guide.md](references/exposition-guide.md) — 通用论述，完整方法，自包含

**内容提取提醒（按需，梳理时加载）：**

- [extraction/workflow-content.md](references/extraction/workflow-content.md) — 遇到工作流程型内容时
- [extraction/knowledge-content.md](references/extraction/knowledge-content.md) — 遇到知识库型内容时
- [extraction/rule-content.md](references/extraction/rule-content.md) — 遇到规则/决策型内容时
- [extraction/example-content.md](references/extraction/example-content.md) — 遇到案例型内容时
- [extraction/rationale-content.md](references/extraction/rationale-content.md) — 遇到设计思想型内容时

**结构模式手册（按需，组织时加载）：**

- [structure/pattern-learning-path.md](references/structure/pattern-learning-path.md) — 学习路径模式（默认，通用论述内已含概要）
- [structure/pattern-golden-circle.md](references/structure/pattern-golden-circle.md) — 原理优先模式（WHY→HOW→WHAT）
- [structure/pattern-knowledge-types.md](references/structure/pattern-knowledge-types.md) — 按知识类型分组模式
- [structure/pattern-progressive-disclosure.md](references/structure/pattern-progressive-disclosure.md) — 分层披露模式（概览→细节）
- [structure/pattern-iceberg.md](references/structure/pattern-iceberg.md) — 理解深度分层模式（现象→原理）
- [structure/pattern-scenario-driven.md](references/structure/pattern-scenario-driven.md) — 读者场景/问题导向模式
- [structure/pattern-5w1h.md](references/structure/pattern-5w1h.md) — 六维覆盖模式
- [structure/pattern-functional-decomposition.md](references/structure/pattern-functional-decomposition.md) — 能力树模式

**通用提示（按需，全程可加载）：**

- [general/traps.md](references/general/traps.md) — 陷阱专项展开（表现、例子、自查）
- [general/adjustments.md](references/general/adjustments.md) — 边界情况调整建议
- [general/readability.md](references/general/readability.md) — 可读性强化（语体转换、金字塔原则等）
- [general/multi-skill.md](references/general/multi-skill.md) — 多技能场景专项（批量/跨技能整合）

## 目录树

```
skill-exposition/
├── SKILL.md
└── references/
    ├── exposition-guide.md
    ├── extraction/               # 内容提取提醒（5）
    │   ├── workflow-content.md
    │   ├── knowledge-content.md
    │   ├── rule-content.md
    │   ├── example-content.md
    │   └── rationale-content.md
    ├── structure/                # 结构模式手册（8）
    │   ├── pattern-learning-path.md
    │   ├── pattern-golden-circle.md
    │   ├── pattern-knowledge-types.md
    │   ├── pattern-progressive-disclosure.md
    │   ├── pattern-iceberg.md
    │   ├── pattern-scenario-driven.md
    │   ├── pattern-5w1h.md
    │   └── pattern-functional-decomposition.md
    └── general/                  # 通用提示（4）
        ├── traps.md
        ├── adjustments.md
        ├── readability.md
        └── multi-skill.md
```
