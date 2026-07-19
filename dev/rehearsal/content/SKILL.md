---
name: rehearsal
description: |
  写完任何给别人用的内容后触发。丢掉作者身份，模拟一个不知道你意图的接收方，
  从头走一遍完整接触路径——逐段读、逐操作，记录每个停顿、误解和想放弃的地方。

  **何时使用**：
  - 写完系统提示词或任务指令 → 检查模型会不会误解模糊约束
  - 写完文档、教程、操作指南 → 确认新人能不能按步骤执行
  - 设计完 API 或交互流程 → 验证调用者/用户能否顺利完成任务
  - 任何要交给「不知道你脑子里在想什么的人」的内容，发布之前

  **何时不使用**：
  - 纯代码逻辑验证 → 不涉及接收方体验，用 logic-chain-rehearsal
  - 已有真实用户反馈数据 → 用反馈比模拟更准
  - 只改了几个错别字或格式 → 不需要完整的推演流程
metadata:
  version: "1.5.0"
  last_updated: "2026-07-19"
  author: "xiii_1991"
  license: "MIT"
---

# Rehearsal（推演）

## 这是什么

**Rehearsal（推演）= 暂停作者身份，完整走一遍另一个视角的「首次接触 → 理解 → 决策」链路。**

它和载体无关——可以推演文档、代码、UI 流程、API 设计、指令集等任何交付物。
它和客体也无关——客体可以是 AI 模型、真实用户、读者、学生、顾客、新人同事。

## 为什么有效

作者有一个致命盲区：**你知道"应该得到什么结论"，所以你看不到"得不到的人会在哪里卡住"。**
Rehearsal 就是强制切除"设计者知识"——假装不知道，走一遍，哪里卡住了哪里就有问题。

## 触发条件

适用于任何「给别人看/用」的产物的交付前检查：

- 文档、教程、指南、README
- UI 界面、CLI 命令系列、表单流程
- 操作手册、运行指引、风格指南
- API 或接口设计
- 配置模板、代码示例、教学材料

## 如何推演

**阅读通用论述文档并按照其中的流程进行推演：**

→ [rehearsal-guide.md](references/rehearsal-guide.md) — 含推演方法的完整阐述（原理、三元素、四步流程、评估维度）和场景特化参考索引。

## 参考文件

**必读入口：**

- [rehearsal-guide.md](references/rehearsal-guide.md) — 通用论述，完整方法 + 场景特化参考

**场景文档（按需参考）：**

- [文档/指南质量验证推演](references/scenarios/doc-guide-rehearsal.md) — 单文档推演 + 全流程跨文档推演，五维度评估标准
- [设计方法论文档验证推演](references/scenarios/design-doc-rehearsal.md) — 四维验证框架：逻辑正确、线索清晰、前后一致、可复现深刻理解
- [多场景知识库验证推演](references/scenarios/knowledge-base-rehearsal.md) — 多角色×多路径推演，适配决策树分支消费模式
- [提示词/指令集推演](references/scenarios/prompt-instruction-rehearsal.md) — 双维度推演（内容表达层 + 逻辑执行层），委派推演机制
- [交互流程推演](references/scenarios/interaction-rehearsal.md) — 操作链路的首次可执行性、困惑点密度、放弃率预估维度
- [API 设计推演](references/scenarios/api-design-rehearsal.md) — 命名一致性、默认值合理性、错误信息可操作性、缺失端点覆盖维度
- [逻辑链路推演](references/scenarios/logic-chain-rehearsal.md) — 控制流正确性、边界条件覆盖、状态一致性等维度

**按需参考：**

- [batch-execution.md](references/supplementary/batch-execution.md) — 推演场景 ≥ 5 个时使用并行执行模式
- [defect-taxonomy.md](references/supplementary/defect-taxonomy.md) — 发现缺陷时用于归类与定位


## 目录树

```
rehearsal/
├── SKILL.md
└── references/
    ├── rehearsal-guide.md
    ├── scenarios/
    │   ├── doc-guide-rehearsal.md
    │   ├── design-doc-rehearsal.md
    │   ├── knowledge-base-rehearsal.md
    │   ├── prompt-instruction-rehearsal.md
    │   ├── interaction-rehearsal.md
    │   ├── api-design-rehearsal.md
    │   └── logic-chain-rehearsal.md
    └── supplementary/
        ├── batch-execution.md
        └── defect-taxonomy.md
```
