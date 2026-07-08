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
  version: "1.4.0"
  last_updated: "2026-07-08"
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

→ [rehearsal-guide.md](references/rehearsal-guide.md) — 含推演方法的完整阐述（原理、三元素、四步流程、打分维度）和场景分流路由表。

## 参考文件

**必读入口：**

- [rehearsal-guide.md](references/rehearsal-guide.md) — 通用论述，完整方法 + 场景路由表

**场景文档（载体匹配时必读）：**

- [doc-guide-rehearsal.md](references/scenarios/doc-guide-rehearsal.md) — 文档/指南的推演操作指导
- [design-doc-rehearsal.md](references/scenarios/design-doc-rehearsal.md) — 设计方法论文档的推演操作指导
- [knowledge-base-rehearsal.md](references/scenarios/knowledge-base-rehearsal.md) — 知识库推演操作指导
- [prompt-instruction-rehearsal.md](references/scenarios/prompt-instruction-rehearsal.md) — 提示词/指令集的推演操作指导
- [interaction-rehearsal.md](references/scenarios/interaction-rehearsal.md) — 交互流程的推演操作指导
- [api-design-rehearsal.md](references/scenarios/api-design-rehearsal.md) — API 接口契约的推演操作指导
- [logic-chain-rehearsal.md](references/scenarios/logic-chain-rehearsal.md) — 逻辑链路的推演操作指导

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
