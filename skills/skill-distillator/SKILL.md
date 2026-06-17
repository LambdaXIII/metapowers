---
name: skill-distillator
description: |
  将Agent技能文档转化为人类可读的方法论文档。读取技能的SKILL.md（含frontmatter的name/description/metadata）、references/、README.md等文件，输出结构化的方法论文档（README + methodology/ + reference/ + meta/）。

  **何时使用**：
  - 用户说"整理技能文档"、"生成方法论"、"把技能输出为文档"
  - 需要理解某个技能的设计思想和决策逻辑
  - 技能知识沉淀、团队传承、文档化归档

  **何时不使用**：
  - 创建新技能 → 用 skill-creator
  - 询问技能用法 → 直接回答
  - 测试技能效果 → 用 cx-skill-test
  - 用户无明确文档化意图

  **核心能力**：五阶段转化（理解→解构→编排→表达→质检）、类型自适应（纯指令型/混合型）、推断边界标注、源一致性检测。
metadata:
  version: 1.5
  last_updated: 2026-06-17
  author: LambdaXIII
  email: xiii_1991@163.com
license: LICENSE.md
---

# skill-distillator：技能文档蒸馏器

> 将技能的"执行文档"转化为"阅读文档"，降低人类理解成本。

---

## 一、边界与约束

### 只读

- 技能源文件目录
- 项目文件

### 可写

- 仅用户指定的输出目录

### 约束

- **语言锁定**：输出语言必须与源技能的 SKILL.md 正文主要语言一致。在 phase-01 识别后锁定，phase-05 验证。
- **输出形态不可逆转**：phase-03 判定为多文件后，phase-04 必须生成多文件。中途降级为单文件 = 流程违规。
- **内容身份保真**：输出文档必须描述技能本身的方法论（而非技能处理的主题）。身份漂移在 phase-04 检查，phase-05 验证。

### 禁止

- 修改被蒸馏技能的源文件
- 修改项目文件
- 调用记忆库技能

---

## 二、核心定位

### 解决什么问题？

技能文件为 Agent 优化，人类阅读成本高。本技能提供：

- **结构化转化**：将分散的技能文件转化为系统的方法论文档
- **视角转换**：从"指令型"转为"说明型"
- **知识沉淀**：便于技能传承和团队协作

### 核心原则

- **五阶段转化**：理解 → 解构 → 编排 → 表达 → 质量检查
- **渐进式披露**：L1概览 → L2摘要 → L3详情 → L4深度
- **智能转换**：清晰则摘取，指令型则转换，简略则丰富
- **类型自适应**：纯指令型授权推断，混合型选择性转换
- **推断边界**：可推断则标注依据，不可推断则标注原因

---

## 三、执行流程

**管道规则**：
- 每个阶段的输出是下一阶段的输入——**不可跳过**。
- 每完成一个阶段，必须在对话中声明：`阶段[N]完成，进入阶段[N+1]。`
- Phase-03 的输出（文档大纲）必须在 Phase-04 步骤1 中被引用。缺失 = 硬停止，回退到 Phase-03。

### 第一阶段：理解

**进入条件**：无前置条件——这是强制起点。

加载参考文件，理解技能核心：
- [phases/phase-01-understanding.md](references/phases/phase-01-understanding.md)：详细操作步骤、输出格式、质量检查
- [frameworks/golden-circle.md](references/frameworks/golden-circle.md)：黄金圈法则
- [frameworks/iceberg-model.md](references/frameworks/iceberg-model.md)：冰山模型
- [frameworks/five-wh-one-h.md](references/frameworks/five-wh-one-h.md)：5W1H

**操作概要**：读取技能文件 → 应用理解框架 → 识别技能类型 → 扫描源一致性 → 语言识别 → 输出理解摘要

**完成标志**：理解摘要完整 + 语言标签已记录 + `阶段完成确认` 全部通过。

### 第二阶段：解构

**进入条件**：Phase-01 理解摘要已完成，`阶段完成确认` 已通过。

加载参考文件，拆解技能结构：
- [phases/phase-02-deconstruction.md](references/phases/phase-02-deconstruction.md)：详细操作步骤、输出格式、质量检查
- [frameworks/functional-decomposition.md](references/frameworks/functional-decomposition.md)：功能分解
- [frameworks/knowledge-types.md](references/frameworks/knowledge-types.md)：知识类型分析

**操作概要**：分析能力结构 → 识别知识类型 → 输出能力清单 + 知识图谱

**完成标志**：能力清单可独立理解 + 知识图谱覆盖所有类型 + `阶段完成确认` 全部通过。

### 第三阶段：编排

**进入条件**：Phase-02 解构结果已完成，`阶段完成确认` 已通过。

加载参考文件，组织文档结构：
- [phases/phase-03-organization.md](references/phases/phase-03-organization.md)：详细操作步骤、输出格式、质量检查
- [frameworks/diataxis.md](references/frameworks/diataxis.md)：Diátaxis框架
- [frameworks/pyramid-principle.md](references/frameworks/pyramid-principle.md)：金字塔原理
- [frameworks/progressive-disclosure.md](references/frameworks/progressive-disclosure.md)：渐进式披露

**操作概要**：确定输出形态 → 应用 Diátaxis 分类 → 设计渐进式披露层级 → 输出文档大纲

**完成标志**：输出形态已判定 + 文件清单完整 + 反模板检查通过 + `阶段完成确认` 全部通过。

### 第四阶段：表达

**进入条件**：Phase-03 文档大纲已完成，`阶段完成确认` 已通过。Phase-01 的语言标签可用。

加载参考文件，转化为可读文档：
- [phases/phase-04-expression.md](references/phases/phase-04-expression.md)：详细操作步骤、输出格式、质量检查
- [writing/three-c-principles.md](references/writing/three-c-principles.md)：3C原则
- [writing/style-guide.md](references/writing/style-guide.md)：风格指南
- [writing/instructional-to-explanatory.md](references/writing/instructional-to-explanatory.md)：指令→说明转换

**操作概要**：按技能类型调整策略 → 逐文件身份检查 → 按大纲生成各文件 → 应用风格指南 → 完成视角转换 → 输出最终文档

**完成标志**：所有文件已生成 + 每文件身份检查通过 + 输出形态与 Phase-03 判定一致 + `阶段完成确认` 全部通过。

### 第五阶段：质量检查

**进入条件**：Phase-04 所有输出文件已生成，`阶段完成确认` 已通过。Phase-03 的文档大纲可用。

加载参考文件，交付前自我评估：
- [phases/phase-05-quality-check.md](references/phases/phase-05-quality-check.md)：详细操作步骤、检查维度、停止规则

**操作概要**：
1. 形态合规检查（最先，不通过即回退）
2. 逐文件检查（完整性、准确性、可读性、一致性、渐进式披露、身份保真、语言一致性）
3. 发现问题 → 修复 → 重新检查该文件
4. 连续两轮完整检查无修改 → 停止

**完成标志**：形态合规通过 + 所有维度通过或已达第5轮 + `阶段完成确认` 全部通过。蒸馏完成——可交付。

---

## 四、与其他技能的关系

| 技能 | 关系 | 说明 |
|------|------|------|
| skill-creator | 对偶 | creator 封装，distillator 解构 |
| cx-skill-test | 协作 | 测试验证技能效果，distillator 整理技能文档 |

---

## 五、目录结构

### 技能目录

```
skill-distillator/
├── SKILL.md                    # 主文件（本文件）
├── README.md                   # 设计意图与维护参考
├── CHANGELOG.md                # 版本历史
├── LICENSE.md                  # 许可协议
└── references/
    ├── frameworks/             # 理解框架（8个）
    │   ├── golden-circle.md
    │   ├── iceberg-model.md
    │   ├── five-wh-one-h.md
    │   ├── functional-decomposition.md
    │   ├── knowledge-types.md
    │   ├── diataxis.md
    │   ├── pyramid-principle.md
    │   └── progressive-disclosure.md
    ├── writing/                # 写作指南（3个）
    │   ├── three-c-principles.md
    │   ├── style-guide.md
    │   └── instructional-to-explanatory.md
    ├── output/                 # 输出结构定义（1个）
    │   └── output-structure.md
    └── phases/                 # 执行阶段（5个，每文件含"阶段完成确认"门）
        ├── phase-01-understanding.md
        ├── phase-02-deconstruction.md
        ├── phase-03-organization.md
        ├── phase-04-expression.md
        └── phase-05-quality-check.md
```

### 输出目录

```
<output-dir>/
├── README.md                    # L1: 概览层（Tutorials）
├── methodology/                 # L2-L3: 方法论层
│   ├── core-concepts.md         # Explanation: 核心概念
│   ├── workflow.md              # How-to: 工作流程
│   └── decision-rules.md        # Reference: 决策规则
├── reference/                   # L3: 参考层
│   ├── guide-xxx.md             # Reference: 各参考文档精炼版
│   └── examples.md              # Tutorials: 典型示例
└── meta/                        # L4: 深度层
    ├── changelog.md             # 版本历史
    └── design-notes.md          # 设计笔记
```
