---
name: agent-prompt-design
description: |
  Agent 系统提示词设计方法论——覆盖从结构设计、内容编写、工具协议、安全加固到运营管理的全流程。

  **何时触发**：
  - 用户说"帮我写个系统提示词"、"这个 agent 需要什么指令"、"设计 agent 的 prompt"
  - 需要从零设计 Agent 的系统提示词
  - 诊断已有 Agent 的行为问题（指令冲突、工具过载、安全漏洞）
  - 为生产环境加固 Agent 的安全边界
  - 讨论 prompt engineering 或 agent instruction 最佳实践

  **何时不触发**：
  - 编写普通一次性提示词（非 Agent 持久指令）→ 不需要完整方法论
  - 创建新 Skill 封装 → 用 skill-creator
  - 纯代码实现问题 → 本技能关注提示词文本设计

metadata:
  version: 1.0.0
  last_updated: 2026-06-17
  author: Ĉalio
---

# agent-prompt-design：Agent 系统提示词设计方法论

> 从结构设计到安全加固——让 Agent 系统提示词从「能跑」到「可靠」。

---

## 内容索引

### 核心参考（按需加载）

| 文件 | 主题 | 何时加载 |
|------|------|---------|
| [references/context-engineering.md](references/context-engineering.md) | 范式转换（Prompt Eng → Context Eng）、注意力预算、正确海拔 | 理解理论基础；Agent 长对话中行为退化 |
| [references/structure-design.md](references/structure-design.md) | 分层结构、标签选型、8 大组件 | 从零开始设计系统提示词的结构 |
| [references/content-writing.md](references/content-writing.md) | 五条铁律、Few-Shot、角色定义、输出格式 | 编写指令正文；诊断模糊/矛盾指令 |
| [references/reasoning-models-2026.md](references/reasoning-models-2026.md) | 推理模型策略变化、effort 控制、CoT 陷阱 | 目标为 Claude 4.6+ / GPT-5.x / Gemini Deep Think |
| [references/tool-design.md](references/tool-design.md) | 最小可行工具集、工具契约、调用协议 | 设计工具；Agent 滥调/漏调工具 |
| [references/safety.md](references/safety.md) | 安全第一阶变量、注入防御、三层边界 | 生产部署前；安全审查；Agent 接触不可信外部内容 |
| [references/operations.md](references/operations.md) | 四支柱、版本管理、回归测试、迭代流程 | 团队协作；长期维护；CI/CD 集成 |
| [references/anti-patterns.md](references/anti-patterns.md) | 十大反模式 + 诊断流程 + 自查清单 | Agent 行为异常；审查已有提示词 |
| [references/model-specific.md](references/model-specific.md) | 四厂商差异化策略 + 跨模型原则 | 针对特定模型调优；跨模型迁移 |

### 模板（复制使用）

| 文件 | 内容 | 何时使用 |
|------|------|---------|
| [templates/generic-agent.md](templates/generic-agent.md) | 通用 Agent 系统提示词模板（填空式） | 大多数场景的起点 |
| [templates/deepmind-reasoning.md](templates/deepmind-reasoning.md) | DeepMind 9 步强制预行动推理模板 | 高可靠性复杂多步 Agent |
| [templates/three-layer-boundary.md](templates/three-layer-boundary.md) | 三层边界框架模板 | 可嵌入通用模板或独立使用 |
| [templates/tool-calling-protocol.md](templates/tool-calling-protocol.md) | 工具调用协议模板 | 嵌入系统提示词的工具使用部分 |

### 背景资料

| 文件 | 内容 | 何时加载 |
|------|------|---------|
| [RESEARCH.md](RESEARCH.md) | 原始调查报告（18 个来源、完整引用） | 追溯方法论来源或深入特定引用 |

---

## 使用方法

### 快速决策

```
你的情况是什么？
│
├── 从零设计系统提示词
│   → structure-design.md（结构框架）
│   → content-writing.md（编写指令正文）
│   → tool-design.md（如果需要工具）
│   → templates/ 选起点模板
│
├── 已有 Agent，行为异常
│   → anti-patterns.md（十大反模式诊断）
│   → 定位问题 → 加载对应 reference 修复
│   → 用自查清单验证修复效果
│
├── 准备生产部署 / 安全审查
│   → safety.md（必读：注入防御 + 三层边界）
│   → operations.md（如需团队协作和版本管理）
│
├── 针对特定模型调优
│   → model-specific.md（对比四厂商差异）
│   ├── 目标是推理模型 → 先看 reasoning-models-2026.md
│   ├── 目标是非推理模型 → 跳过 reasoning-models-2026.md
│
├── 从模型 A 迁移提示词到模型 B
│   → model-specific.md（对比两家差异：标签偏好、推理策略、安全特性）
│   → 标签需改 → structure-design.md §2
│   → 复查铁律 → content-writing.md
│   → 工具协议检查和适配 → tool-design.md
│   ├── 目标是推理模型 → reasoning-models-2026.md
│   → 回归测试 → operations.md §3（至少 20 个测试用例）
│   → 安全审查 → safety.md §6（三层边界需重新校准）
│   ✅ 迁移完成后自查：标签、铁律、工具、推理策略、安全边界五维全覆盖
│
├── 想深入理解理论基础
│   → context-engineering.md
│
└── 长期维护 / 多人协作
    → operations.md
```

### 迭代开发流程

```
最强模型 + 最简提示词
    ↓
建立基线性能（Evals）
    ↓
观察失败模式 → 仅针对失败添加指令/示例
    ↓
回归测试（回放历史交互）→ 确认无退化
    ↓
成本/延迟优化
    ↓
持续监控 + 迭代
```

---

## 能力边界

### 提供什么

- ✅ 系统提示词的**结构设计**原则（分层、标签选型、8 大组件）
- ✅ **内容编写**方法论（五条铁律、Few-Shot、角色定义、输出格式）
- ✅ **推理模型**（2026）的专项策略（effort 控制、CoT 陷阱）
- ✅ **工具定义**规范（最小可行工具集、调用协议、错误恢复）
- ✅ **安全防护**策略（注入防御、三层边界、生产清单）
- ✅ **运营管理**流程（四支柱、版本化、回归测试）
- ✅ 四家前沿厂商（Anthropic / Google / OpenAI / xAI）的**差异化策略**
- ✅ 可直接复制使用的**模板**
- ✅ **反模式诊断** + 排查工作流

### 不提供什么

- ❌ 特定领域的业务逻辑（如"金融客服 agent 应该说什么"）
- ❌ 代码实现（如 API 调用、集成代码）
- ❌ 模型微调、RLHF 等训练层面指导
- ❌ 非英语模型的本地化建议

### 适用模型

覆盖 Claude 4.x、Gemini 3.x、GPT-5.x / o-series、Grok 4.x 及同等能力的前沿模型。对旧模型（GPT-3.5、Claude 2 等）部分策略不适用。
