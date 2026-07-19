---
name: rehearsal
description: |
  推演(rehearsal)：以客体身份通读检查交付物的方法。

  适用于一切「给别人看 / 用」的交付物：
  - 文档、教程、操作指南、README、计划文档
  - 系统提示词、Agent 指令、任务指令、提示词模板
  - API 设计、UI 交互流程、CLI 命令系列、表单、操作手册
  - 知识库、教学材料、代码示例、规则集

  **触发场景**（任一即触发）：
  - 用户说以下之一触发（中英都行）：「推演 / rehearsal / 通读 / 验一下 / 检查 / 确保理解 / 充分理解 / 不误解 / 能不能走通 / 过一遍 / 走一遍 / 模拟接收方视角 / simulate a reader / first-contact / dry-run / walk through / sanity-check / verify for a newcomer / will users get stuck」
  - 刚写完上列任一类交付物，自问「能不能被没有上下文的人读懂」「交付出去会不会卡住」「我自己看不出问题但别人会卡在哪」（或英文自问 can a newcomer follow this / will readers get stuck / is this readable without my context）
  - 在载体的相关产出阶段做交付前质量验证（不限上述清单——凡是最终给别人看 / 用的产物都适用）

  仅修改错别字、错标点、纯格式调整时不触发。
metadata:
  version: "1.6.0"
  last_updated: "2026-07-19"
  author: "xiii_1991"
  license: "MIT"
---

# Rehearsal（推演）

## 这是什么

**Rehearsal（推演）= 丢掉作者身份，完整走一遍另一个视角的「首次接触 → 理解 → 决策」链路。**

它和载体无关——可以推演文档、代码、UI 流程、API 设计、指令集等任何交付物。
它和客体也无关——客体可以是 AI 模型、真实用户、读者、学生、顾客、新人同事。

## 为什么有效

作者有一个致命盲区：**你知道"应该得到什么结论"，所以你看不到"得不到的人会在哪里卡住"。**
Rehearsal 就是强制切除"设计者知识"——假装不知道，走一遍，哪里卡住了哪里就有问题。

## 触发条件

本节是 description 触发条件的展开版——description 负责被加载器命中，下方条款供 agent 加载后决定是否启动本次推演 / 复查触发是否合理、是否漏触发。

**合触发**（任一成立即触发）：

- 用户首话出现「推演 / 验一下 / 走一遍 / 过一遍 / 检查能不能看懂 / 能不能走通 / 新人会不会卡 / 读者看懂吗 / 接收方会卡在哪」等动词或短语，且目标是一部交付给他人看 / 用的产物
- 用户首话出现「写完 / 设计完 / 改完 + 任一类交付物」表示要交付前自检：文档、教程、指南、README、计划文档、系统提示词、Agent 指令、任务指令、提示词模板、API 设计、UI 交互流程、CLI 命令系列、表单、操作手册、知识库、教学材料、代码示例、规则集
- 作为 agent，**刚完成**上列任一类交付物、即将交付给用户 / 读者 / 调用方之前，自问「能不能被没有上下文的人读懂」「交付出去会卡住吗」「我自己看不出问题但别人会卡在哪」时
- 用户提供了具体交付物并请求对其做质量验证 / 可用性评估 / 读者友好度检查

**不合触发**：

- 仅修改错别字、错标点、纯格式调整——一次性无内容变化的修订，不改变接收方理解路程
- 已有真实用户反馈数据，本技能是模拟，反馈比模拟更准——优先处理反馈数据，rehearsal 仅做补充视角
- 重复推演同一未变更交付物——上轮已发现的问题清单仍在，再次推演只是把同一条问题再发现一遍；应改后再推
- 纯粹代码运行时逻辑验证（不需模拟「人」的视角） → 此类任务可单独参照 references/scenarios/logic-chain-rehearsal.md 的执行指导，**但本技能仍正常触发**——logic-chain-rehearsal 是本技能 references 下的场景文档，而非另一技能；当交付物同时含文档 + 代码示例时，文档推演与逻辑链路推演一并做

**边界判定**：如果拿不准要不要触发，默认触发——推演发现不到问题不造成损失，漏推演却可能让交付物带着本可发现的问题出去。

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
