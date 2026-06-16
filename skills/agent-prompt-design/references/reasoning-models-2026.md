# 推理模型提示策略 (2026)

> **来源：** §3.2 (推理引导策略) 与 §9 (前沿模型特定策略) — Agent 系统提示词编写方法论 RESEARCH.md
> **整理日期：** 2026-06-17
> 
> 📍 本文件是 [agent-prompt-design skill](../SKILL.md) 的参考文件。主入口和决策树请见 SKILL.md。

## 目录

1. [2026 范式转变](#1-2026-范式转变)
   - [1.1 为什么旧 CoT 不再适用](#11-为什么旧-cot-不再适用)
   - [1.2 从「控制步骤」到「控制预算」](#12-从控制步骤到控制预算)
2. [新范式的三个控制维度](#2-新范式的三个控制维度)
   - [2.1 思考多少 (Reasoning Effort)](#21-思考多少-reasoning-effort)
   - [2.2 何时思考 (Tool-Call Interleaving)](#22-何时思考-tool-call-interleaving)
   - [2.3 在哪里结构化 (Output Format Constraints)](#23-在哪里结构化-output-format-constraints)
3. [DeepMind 9 步预行动推理模板](#3-deepmind-9-步预行动推理模板)
   - [3.1 模板结构](#31-模板结构)
   - [3.2 量化效果](#32-量化效果)
   - [3.3 依赖优先级排序](#33-依赖优先级排序)
   - [3.4 智能重试策略](#34-智能重试策略)
4. [什么时候不该用推理模型](#4-什么时候不该用推理模型)
   - [4.1 任务类型 vs 推理模型适用性](#41-任务类型-vs-推理模型适用性)
   - [4.2 模型级联模式（推荐）](#42-模型级联模式推荐)
   - [4.3 对推理模型执行格式化任务的要点](#43-对推理模型执行格式化任务的要点)
5. [结构化推理模板 vs 原生推理](#5-结构化推理模板-vs-原生推理)
   - [5.1 选择矩阵](#51-选择矩阵)
   - [5.2 矛盾解析](#52-矛盾解析)
6. [模型特定策略对比](#6-模型特定策略对比)
   - [6.1 Anthropic Claude 4.6](#61-anthropic-claude-46)
   - [6.2 Google DeepMind Gemini](#62-google-deepmind-gemini)
   - [6.3 OpenAI GPT-5.4](#63-openai-gpt-54)
7. [实践指南](#7-实践指南)

---

## 1. 2026 范式转变

> **核心论点：** 对于 2026 年的推理模型（Claude 4.6、GPT-5.4、Gemini 2.5 Deep Think），旧的 CoT（Chain-of-Thought）技巧已**不再有效甚至有害**。这些模型在内部已经完成推理——告诉它们"一步步思考"只会浪费推理预算，或导致推理过程污染最终答案。
>
> **新范式：** 告诉模型**思考多少**（reasoning effort）、**何时思考**（tool-call interleaving）、**在哪里结构化**（output format constraints），而非如何思考。
>
> —— *SurePrompts, "Advanced Prompt Engineering in 2026"*

### 1.1 为什么旧 CoT 不再适用

传统 CoT（Chain-of-Thought）提示技巧在 GPT-4、Claude 3 等**非推理模型**上效果显著——这些模型需要外部引导来展开推理过程。但 2026 年的推理模型发生了根本变化：

| 维度 | 非推理模型 (GPT-4, Claude 3) | 推理模型 (Claude 4.6, GPT-5.4, Gemini Deep Think) |
|------|-------------------------------|--------------------------------------------------|
| **推理能力** | 需要提示引导才展示推理 | 内置深度推理引擎，在 token 生成前已内部推理 |
| **CoT 效果** | ✅ 显著提升性能 | ❌ 无提升甚至有害 |
| **CoT 为什么有效/有害** | 引导模型展开展开的推理步骤 | 外部 CoT 与内部推理竞争注意力预算（理论基础见 [context-engineering.md §3](context-engineering.md#3-注意力预算attention-budget)），产生"推理污染" |
| **最佳策略** | 详细步骤引导 | 控制 effort 预算，不控制推理内容 |

**推理污染机制：** 当推理模型已经内部完成了逻辑推演，再用外部指令要求它"一步步思考"时，模型可能：
1. 将内部推理的错误中间状态输出到最终答案中
2. 在两种推理路径（内部 vs 外部引导）之间产生冲突
3. 消耗宝贵的**推理预算**——这些模型有固定的推理 token 上限，外部 CoT 浪费了这个预算

### 1.2 从「控制步骤」到「控制预算」

```
2024-2025 年的范式的范式：
  "我会一步步思考。首先，分析... 然后，计算... 最后..."

2026 年的范式：
  推理模型内部完成推理。
  外部提示词只控制：
  ├─ 思考多少 (reasoning effort level)
  ├─ 何时思考 (interleave with tool calls)
  └─ 在哪里结构化 (output format)
```

---

## 2. 新范式的三个控制维度

### 2.1 思考多少 (Reasoning Effort)

控制模型的推理深度，而非推理路径。

| Effort 级别 | 适用场景 | 示例设置 |
|-------------|----------|----------|
| **Low** | 简单检索、事实查询、格式化任务 | `reasoning_effort: "low"` |
| **Medium** | 常规问答、中等复杂度分析 | `reasoning_effort: "medium"` |
| **High** | 复杂推理、多步逻辑链、代码调试 | `reasoning_effort: "high"` |
| **Max** | 极端复杂问题、数学证明、深度研究 | `reasoning_effort: "max"` (Deep Think) |

**Claude 4.6 的 Adaptive Thinking 实现：**
```
在 API 调用中设置：
anthropic_beta=["thinking-adaptive"]
thinking_config={
    "type": "enabled",
    "budget_tokens": 16000,    # 推理预算上限
    "effort": "high"           # low / medium / high / max
}
```

**实践建议：**
- 不要对简单任务用高 effort——浪费 token，增加延迟
- 不要对复杂推理用低 effort——模型会跳过关键推理步骤
- 最佳实践：根据任务复杂度**动态调整** effort 级别

### 2.2 何时思考 (Tool-Call Interleaving)

控制模型在工具调用序列中何时进行深度推理。

**模式对比：**

| 模式 | 流程 | 适用场景 |
|------|------|----------|
| **Think-Then-Act** | 先推理 → 再调用工具 | 任务需要完整规划后再执行 |
| **Act-Then-Think** | 先调用工具获取信息 → 再推理 | 需要外部数据支撑的决策 |
| **Think-Act-Think** | 推理 → 工具调用 → 根据结果再次推理 | 多步 Agent 任务、研究型任务 |
| **Iterative Think-Act** | 推理 ↔ 工具调用 交替进行 | 复杂探索型任务（如代码调试） |

```
✅ 明确告诉模型何时思考的示例：

You have three reasoning modes:
1. **Plan mode** — Before starting a multi-step task, reason about the plan.
2. **Reflect mode** — After receiving tool results, reason about next steps.
3. **Execute mode** — For straightforward tool calls, no explicit reasoning needed.

Use Plan mode at task start, Reflect mode after tool results, Execute mode for simple lookups.
```

### 2.3 在哪里结构化 (Output Format Constraints)

控制输出格式（而非推理过程）——这是唯一仍然有效的"外部引导"手段。

| 约束类型 | 方法 | 示例 |
|----------|------|------|
| **格式骨架** | 预填输出骨架，让模型填充 | `{"answer": "", "reasoning_steps": [], "confidence": 0.0}` |
| **JSON Schema** | 定义严格的输出 schema | OpenAI `response_format` 参数 + JSON Schema |
| **长度限制** | 控制推理或输出的 token 预算 | `budget_tokens: 16000` 或 "答案不超过 100 字" |
| **边界声明** | 明确什么属于推理、什么属于输出 | "将内部推理放在 `reasoning` 字段，最终答案放在 `answer` 字段" |

---

## 3. DeepMind 9 步预行动推理模板

虽然对 2026 原生推理模型来说 CoT 有害，但对于**非推理模型**（或需要极端可靠性的场景），DeepMind 发布的官方结构化推理模板仍然非常有效。

### 3.1 模板结构

DeepMind 为 Gemini 3 Pro 设计的 9 步强制性预行动推理链：

```
You are a very strong reasoner and planner.
Before taking any action (tool calls OR user responses),
you MUST methodically reason about:

1. LOGICAL DEPENDENCIES:
   - Policy constraints > Operation order > Prerequisites > User preferences
   
2. RISK ASSESSMENT:
   - What happens if this action is taken?
   - Could the new state cause future issues?

3. HYPOTHESIS EXPLORATION:
   - What is the most likely root cause?
   - Prioritize by likelihood, but don't discard low-probability hypotheses.

4. OUTCOME EVALUATION:
   - Does the last observation require plan changes?
   - If initial hypotheses disproven, generate new ones.

5. INFORMATION AVAILABILITY:
   - Tools, policies, conversation history, user-provided info.

6. PRECISION & GROUNDING:
   - Verify claims by quoting exact applicable information.

7. COMPLETENESS:
   - All requirements, constraints, options, preferences incorporated.
   - Avoid premature conclusions.

8. PERSISTENCE（错误恢复策略）:
   - Transient errors → retry (up to explicit limit)
   - Other errors → change strategy, don't repeat.
   > 完整的错误恢复策略（含重试次数、策略切换的详细规则）见 [tool-design.md §6](tool-design.md#6-错误恢复策略)。

9. INHIBIT RESPONSE:
   - Only act after completing ALL reasoning above.
```

### 3.2 量化效果

DeepMind 的测试结果（2025 年 11 月发布）：

| 指标 | 改善幅度 | 说明 |
|------|----------|------|
| **多步工作流错误率** | **↓ 减少 8%** | 9 步推理模板减少了逻辑遗漏和跳跃 |
| **任务成功率** | **↑ 提升 ~5%** | 推理完备性增加带来更一致的执行 |
| **重试次数** | **↓ 显著减少** | 智能重试策略消除无意义的重复 |
| **错误模式** | **从重复失败转向策略调整** | 不再在同一错误上反复循环 |

> **为什么是 "~5%" 而不是一个精确值？** 效果因任务类型和复杂度而异——结构化推理对多步工作流的提升远大于简单任务。DeepMind 报告给出的是跨任务平均提升。

### 3.3 依赖优先级排序

模板第一步骤（Logical Dependencies）包含明确的优先级排序：

```
策略约束 (Policy constraints) > 操作顺序 (Operation order)
  > 信息前提 (Prerequisites) > 用户偏好 (User preferences)
```

这意味着：
- **策略约束**永远排在第一位——合规和边界检查不可协商
- **操作顺序**服从于策略——先确保合规，再考虑执行顺序
- **信息前提**排在操作顺序之后——在确认顺序前先检查依赖
- **用户偏好**权重最低——用户的偏好不能推翻策略或必要前提

### 3.4 智能重试策略

模板第八步骤（Persistence）区分了两种错误类型：

| 错误类型 | 示例 | 响应策略 |
|----------|------|----------|
| **瞬态错误 (Transient)** | 网络抖动、429 限流、服务暂时不可用 | **必须重试**（直到达到明确设定的重试上限） |
| **其他错误 (Other)** | 认证失败、参数错误、资源不存在 | **必须改变策略**，绝不重复相同的失败调用 |

```
✅ 实践中的重试逻辑 (伪代码)：

if error.is_transient():
    retry_count += 1
    if retry_count <= MAX_RETRIES:
        wait(backoff(retry_count))
        retry()          # 瞬态错误重试
    else:
        escalate("max retries reached")
else:
    change_strategy()    # 非瞬态错误改变策略
    # 不重复相同的失败调用
```

---

## 4. 什么时候不该用推理模型

> **来源：** SurePrompts, "Prompting Reasoning Models in 2026" (April 2026)
>
> 推理模型并非万能。选择何时使用推理模型（高 effort）与何时使用标准模型（低 effort/无推理）同样重要——甚至更重要。

### 4.1 任务类型 vs 推理模型适用性

| 任务类型 | 用推理模型？ | 原因 |
|---------|------------|------|
| 多步数学/逻辑推理 | ✅ 是 | 核心优势场景 |
| 代码调试、架构分析 | ✅ 是 | 需要深度推理 |
| 多文档综合、矛盾检测 | ✅ 是 | 推理模型在综合任务上显著优于标准模型 |
| 直接事实召回 | ❌ 否 | 标准模型更快、更便宜、准确率相当 |
| 简单分类 | ❌ 否 | 浪费推理 token |
| 格式转换（JSON↔Markdown） | ❌ 否 | 不需要推理，只需要格式遵循 |
| 低延迟对话 | ❌ 否 | 3-10× 慢于标准模型 |
| 格式化输出生成 | ⚠️ 视情况 | 格式规则复杂到需要推理→用；简单格式→不用 |

### 4.2 模型级联模式（推荐）

不要"全有或全无"——最优策略是**模型级联**（Model Cascading）：

```
用户请求
  │
  ▼
标准模型（低 effort / 无推理）
  │
  ├─ 能处理？→ 直接返回（快速、便宜）
  │
  └─ 需要推理？→ 调用推理模型（高 effort）
       ├─ 数学/逻辑子任务
       ├─ 代码分析子任务  
       └─ 多文档综合子任务
```

即：**优先使用标准模型处理简单任务，仅在需要深度推理的子任务上调用推理模型。** 这既能最大化效率，又能合理分配推理预算。

### 4.3 对推理模型执行格式化任务的要点

> ⚠️ 对推理模型执行格式化任务时，仍然需要明确格式指令和示例——只是不需要"think step by step"，而非去掉所有结构性指导。

关键区别：
- **不需要的：** "一步步思考"、"让我们逐步分析"——这些会触发冗余的内部推理过程
- **仍然需要的：** 明确的 JSON Schema 定义、输出示例、格式边界声明——这些属于"在哪里结构化"的维度（见 §2.3）

---

## 5. 结构化推理模板 vs 原生推理

### 5.1 选择矩阵

| 条件 | 使用结构化推理模板 (9-step) | 使用原生推理 (Effort Control) |
|------|-----------------------------|-------------------------------|
| **模型类型** | 非推理模型 (GPT-4, Claude 3, Gemini 1.5) | 推理模型 (Claude 4.6, GPT-5.4, Gemini Deep Think) |
| **任务复杂度** | 中等复杂度、需要明确步骤 | 高复杂度、需要深层推理 |
| **可靠性要求** | 极高（金融、医疗、法律） | 高（但允许一定灵活性） |
| **可审计性** | 需要推理过程可追溯、可检查 | 最终结果正确性 > 过程可读性 |
| **Token 预算** | 充足（模板本身消耗 tokens） | 有限（effort 控制更 token 高效） |
| **开发阶段** | 原型验证阶段、调试阶段 | 生产部署、成本优化阶段 |

### 5.2 矛盾解析：为何 CoT 对 Claude 4.6 有害，但对 Gemini Deep Think 可能有益？

这看起来是一个矛盾，但本质区别在于**推理机制的不同**：

| 维度 | Claude 4.6 | Gemini Deep Think |
|------|------------|-------------------|
| **推理方式** | **隐式推理**——内部推理 token 与生成文本分离，用户不可见 | **显式推理**——推理过程可以作为可见 token 流的一部分 |
| **CoT 影响** | 外部 CoT 与内部推理**竞争 attention 预算**，产生推理污染 | 结构化模板与 Deep Think 的**并行假设探索**机制互补 |
| **为什么会不同** | Claude 4.6 在内部已经有一套完整的推理机制；外部 CoT 是多余的噪声，反而干扰内部路径 | Deep Think 的推理机制是"探索多个假设并行验证"——结构化模板提供假设空间的组织框架 |
| **最佳实践** | 不要给推理指令。只给 effort 级别和输出格式。 | 可提供高层框架（如依赖优先级），但不要求 step-by-step。模板的价值在于**假设空间组织**，而非步骤引导。 |

**总结规律：**
- **隐式推理模型**（推理在其内部 token 空间完成）→ 控制 effort，不控制步骤
- **显式推理模型**（推理可以作为用户可见 token 流）→ 可提供**框架**，但不提供**步骤**

> 一个有用的类比：
> - **Claude 4.6** 像一个数学家在心算——你在他耳边念"先加十位，再加个位"只会干扰他
> - **Gemini Deep Think** 像一个团队在讨论——你给他们一个白板和标记笔，他们能更有效地组织思路

---

## 6. 模型特定策略对比

### 6.1 Anthropic Claude 4.6

| 维度 | 策略 |
|------|------|
| **结构** | XML 标签（`<instructions>`, `<examples>`, `<background>`）优先 |
| **推理控制** | **Adaptive Thinking** — 通过 API 参数控制 effort (low/medium/high/max) |
| **推理预算** | `budget_tokens` 参数控制推理 token 上限。不要耗尽——留出空间给输出 |
| **工具** | Tool Search（延迟加载）+ Programmatic Tool Calling（Python 编排） |
| **长上下文** | 1M token 上下文窗口；压缩旧消息保留架构决策 |
| **关键禁忌** | ❌ 不要给 Claude 4.6 "一步步思考" 或 CoT 指令 |
| **关键指令** | ✅ 只给 effort 级别 + 输出格式 + 目标描述 |

### 6.2 Google DeepMind Gemini

| 维度 | 策略 |
|------|------|
| **结构** | Markdown 标题 + 强制预行动推理链（对非推理模型） |
| **推理控制** | **Deep Think 模式** — 并行假设探索；适合需要穷举可能性的任务 |
| **系统指令** | 官方发布 9 步推理模板（见第 3 节），可直接复制到 `system_prompt` 字段 |
| **多模态** | 原生多模态（文本 + 图像 + 音频 + 视频），提示词中可直接引用 |
| **上下文** | Gemini 3.5 支持 2M token 上下文 |
| **评估** | 三维评估：能力评估 + 轨迹分析 + 最终响应评估 |

### 6.3 OpenAI GPT-5.4

| 维度 | 策略 |
|------|------|
| **结构** | `###` 或 `"""` 分隔符；指令放在提示词开头 |
| **推理控制** | 高层目标而非精确指令——像「资深同事」而非「初级同事」 |
| **安全** | 内置审核 API；至少 7 类拒绝场景；KYC 建议 |
| **工具** | Agents SDK 支持函数工具 + 主机工具 + Agent-as-Tool |
| **编排** | Manager Pattern（中心 Agent 分发任务）+ 评估驱动的模型降级 |

---

## 7. 实践指南

### 7.1 什么时候用什么策略？

```
你的模型是推理模型还是非推理模型？
├─ 推理模型 (Claude 4.6, GPT-5.4, Gemini Deep Think)
│  ├─ 任务需要深度推理？
│  │  ├─ 是 → 设置高 effort + 输出格式约束
│  │  └─ 否 → 设置低/中 effort + 直接输出
│  └─ 需要工具调用？
│     └─ 指定 Think-Act-Think 模式，而非 step-by-step
│
└─ 非推理模型 (GPT-4, Claude 3, Gemini 1.5)
   ├─ 任务需要高度可靠性？
   │  ├─ 是 → 使用 DeepMind 9 步推理模板
   │  └─ 否 → 使用传统 CoT 引导
   └─ 需要可审计推理过程？
      └─ 保留结构化推理模板的中间输出
```

### 7.2 快速决策清单

- [ ] 确定模型类型：推理模型还是非推理模型？
- [ ] 推理模型 → 是否设置了适当的 effort 级别？
- [ ] 是否避免了"一步一步思考"类 CoT 指令（对推理模型）？
- [ ] 是否明确定义了 Think-Act 模式（何时推理、何时调用工具）？
- [ ] 输出格式是否使用 JSON Schema 或预填骨架控制？
- [ ] 对非推理模型 → 9 步预行动推理链是否提供了足够的组织框架？
- [ ] 重试策略是否区分了瞬态错误和策略性失败？
- [ ] 依赖优先级是否明确（策略约束 > 操作顺序 > 信息前提 > 用户偏好）？

### 7.3 关键原则总结

```
对于推理模型 (2026)：
  × 不要告诉模型怎么思考
  × 不要使用 CoT 技巧
  ✓ 控制思考多少 (effort)
  ✓ 控制何时思考 (interleaving)
  ✓ 控制输出结构 (format)

对于非推理模型：
  ✓ 使用结构化推理模板 (9-step)
  ✓ 使用 CoT 引导
  ✓ 控制依赖优先级
  ✓ 实现智能重试策略
```

---

## 下一步

推理模型策略确定后：
- 📐 需要标准提示词结构 → [structure-design.md](structure-design.md)
- ✍️ 非推理任务的内容编写 → [content-writing.md](content-writing.md)
- 📋 直接使用推理模板 → [templates/deepmind-reasoning.md](../templates/deepmind-reasoning.md)
- 📋 回到 [SKILL.md 决策树](../SKILL.md)

## 附录：参考资料

- **SurePrompts** — "Advanced Prompt Engineering in 2026: Claude 4.6, GPT-5.4, Gemini 2.5 Deep Think"
  https://sureprompts.com/blog/advanced-prompt-engineering-2026-claude-gpt5-gemini
- **Google DeepMind** — "Gemini 3 Pro System Instructions" (Nov 2025)
  https://www.aibase.com/news/23137
- **Anthropic** — "Effective Context Engineering for AI Agents" (Sep 2025)
  https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
- **OpenAI** — "A Practical Guide to Building Agents" (2025)
  https://openai.com/business/guides-and-resources/a-practical-guide-to-building-ai-agents
