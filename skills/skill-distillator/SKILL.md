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
  version: 1.4
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

执行流程分五阶段，每阶段按需加载对应参考文件：

### 第一阶段：理解

加载参考文件，理解技能核心：
- [phases/phase-01-understanding.md](references/phases/phase-01-understanding.md)：详细操作步骤、输出格式、质量检查
- [frameworks/golden-circle.md](references/frameworks/golden-circle.md)：黄金圈法则
- [frameworks/iceberg-model.md](references/frameworks/iceberg-model.md)：冰山模型
- [frameworks/five-wh-one-h.md](references/frameworks/five-wh-one-h.md)：5W1H

**操作概要**：读取技能文件 → 应用理解框架 → 识别技能类型 → 扫描源一致性 → 输出理解摘要

### 第二阶段：解构

加载参考文件，拆解技能结构：
- [phases/phase-02-deconstruction.md](references/phases/phase-02-deconstruction.md)：详细操作步骤、输出格式、质量检查
- [frameworks/functional-decomposition.md](references/frameworks/functional-decomposition.md)：功能分解
- [frameworks/knowledge-types.md](references/frameworks/knowledge-types.md)：知识类型分析

**操作概要**：分析能力结构 → 识别知识类型 → 输出能力清单 + 知识图谱

### 第三阶段：编排

加载参考文件，组织文档结构：
- [phases/phase-03-organization.md](references/phases/phase-03-organization.md)：详细操作步骤、输出格式、质量检查
- [frameworks/diataxis.md](references/frameworks/diataxis.md)：Diátaxis框架
- [frameworks/pyramid-principle.md](references/frameworks/pyramid-principle.md)：金字塔原理
- [frameworks/progressive-disclosure.md](references/frameworks/progressive-disclosure.md)：渐进式披露

**操作概要**：确定输出形态 → 应用 Diátaxis 分类 → 设计渐进式披露层级 → 输出文档大纲

### 第四阶段：表达

加载参考文件，转化为可读文档：
- [phases/phase-04-expression.md](references/phases/phase-04-expression.md)：详细操作步骤、输出格式、质量检查
- [writing/three-c-principles.md](references/writing/three-c-principles.md)：3C原则
- [writing/style-guide.md](references/writing/style-guide.md)：风格指南
- [writing/instructional-to-explanatory.md](references/writing/instructional-to-explanatory.md)：指令→说明转换

**操作概要**：按技能类型调整策略 → 按大纲生成各文件 → 应用风格指南 → 完成视角转换 → 输出最终文档

### 第五阶段：质量检查

加载参考文件，交付前自我评估：
- [phases/phase-05-quality-check.md](references/phases/phase-05-quality-check.md)：详细操作步骤、检查维度、停止规则

**操作概要**：
1. 逐文件检查（完整性、准确性、可读性、一致性、渐进式披露）
2. 发现问题 → 修复 → 重新检查该文件
3. 连续两轮完整检查无修改 → 停止

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
    └── phases/                 # 执行阶段（5个）
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
