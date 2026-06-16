# 第一阶段：理解

> 理解被蒸馏技能的核心定位、设计思想和使用场景。

---

## 目标

建立对技能的全面认知，回答：这个技能是什么？为什么存在？为谁服务？如何使用？

## 为什么需要这些知识文档

技能文件（SKILL.md）通常以指令型语言编写，聚焦"怎么做"。要转化为人类可读的方法论文档，首先需要理解其背后的"为什么"和"是什么"。

三个知识文档从不同维度提供理解框架：
- **黄金圈法则**：确保从 WHY→HOW→WHAT 理解，而非仅从功能列表理解
- **冰山模型**：挖掘表层功能之下的设计模式和心智模型
- **5W1H**：全面覆盖，避免遗漏关键维度

## 如何加载知识文档

按顺序加载：
1. [frameworks/golden-circle.md](../frameworks/golden-circle.md) — 建立核心认知
2. [frameworks/iceberg-model.md](../frameworks/iceberg-model.md) — 深入理解层次
3. [frameworks/five-wh-one-h.md](../frameworks/five-wh-one-h.md) — 全面检查覆盖

加载方式：读取文件内容，提取框架要点，应用到被蒸馏技能。

## 操作步骤

### 步骤1：读取技能文件

按照技能标准的定义，技能目录包含以下文件：

- **SKILL.md**（skill-creator 标准必需）：解析 YAML frontmatter，提取 `name`（技能标识）、`description`（触发描述与核心定位）和 `metadata`（如有：version、last_updated、author）。frontmatter 中的 `description` 是技能的自述摘要，包含"做什么"和"何时使用"，是理解 WHY/WHAT 的首要来源
- **references/**（skill-creator 标准可选）：按需加载的参考文档目录
- **scripts/**、**assets/**（skill-creator 标准可选）：可执行代码与媒体资源，蒸馏过程不涉及
- **README.md**（项目规范可选）：设计意图与维护参考，如有则读取
- **CHANGELOG.md**（项目规范必需）：版本历史
- **templates/**（项目规范可选）：提示词或文档模板，如有则读取

> **注意**：skill-creator 标准仅要求 SKILL.md（含 frontmatter 的 name + description）和可选的 references/scripts/assets。README.md、CHANGELOG.md、templates/ 是本项目的追加规范。蒸馏时不可假设目标技能必定包含这些追加文件——仅有 skill-creator 标准文件时也能正常蒸馏。

### 步骤2：应用黄金圈法则

- 提取 WHY：技能存在的理由、解决的核心问题
- 提取 HOW：核心机制、实现方式
- 提取 WHAT：具体功能、输出物

### 步骤3：应用冰山模型

- 识别事件：技能做了什么（操作步骤）
- 识别模式：反复出现的行为（流程、规则）
- 识别结构：文件组织、模块依赖、数据流
- 识别心智模型：设计者的核心假设和价值观

### 步骤4：应用 5W1H

- What：技能的功能是什么？
- Why：为什么需要这个技能？
- Who：谁使用这个技能？
- When：什么时候触发？
- Where：在什么环境下工作？
- How：如何使用？

### 步骤4.5：技能类型初步识别

基于 SKILL.md 的结构特征快速判断技能类型：
- **纯指令型**：内容以步骤、规则、约束为主（程序知识+规则知识占比 > 80%），缺乏设计理由和概念解释
- **混合型**：包含一定比例的说明型内容，有设计理由或概念解释

识别方法：
- 快速扫描 SKILL.md 的章节结构：如果主要是"步骤"、"流程"、"约束"、"规则"等指令型章节，倾向于纯指令型
- 检查是否有"设计思想"、"核心概念"、"为什么"等说明型章节
- 此为初步识别，解构阶段（phase-02）将做细粒度统计

输出类型标签，供后续阶段使用。

### 步骤4.6：源一致性扫描

检查源文件之间的显式矛盾（同一事项的描述互相冲突）：

| 检查项 | 说明 |
|--------|------|
| SKILL.md 内部一致性 | 流程描述与约束声明是否矛盾 |
| SKILL.md frontmatter vs body | description 与正文定位是否一致 |
| SKILL.md vs README.md | 核心描述是否一致（仅当 README.md 存在） |
| SKILL.md vs references/ | 关键信息是否一致 |
| SKILL.md vs templates/ | 模板内容与流程描述是否一致（仅当 templates/ 存在） |
| metadata.version vs CHANGELOG.md | 版本号是否对应（仅当 metadata 存在） |

发现矛盾时的裁决策略：

| 矛盾类型 | 裁决策略 | 说明 |
|----------|----------|------|
| SKILL.md 内部矛盾 | 以约束部分为准 | 约束通常比流程更审慎 |
| frontmatter vs body 矛盾 | 以 body 为准，frontmatter description 是摘要 | body 是完整表述 |
| SKILL.md vs README.md | 以 SKILL.md 为准 | SKILL.md 是运行时主文件 |
| SKILL.md vs references/ | 以 SKILL.md 为准 | references/ 是辅助材料 |
| SKILL.md vs templates/ | 以 SKILL.md 为准 | 模板是执行辅助，可能滞后 |
| metadata.version vs CHANGELOG | 以 CHANGELOG.md 为准 | CHANGELOG 是版本权威来源 |
| 数值型矛盾 | 并列呈现，标注矛盾来源 | 数值无法自动裁决 |

### 步骤5：输出理解摘要

整合以上分析，输出理解摘要。

## 输出格式

```markdown
## 理解摘要

### 元信息
- name：...
- metadata（如有）：version=..., last_updated=..., author=...

### 黄金圈
- WHY：...
- HOW：...
- WHAT：...

### 冰山模型
- 事件：...
- 模式：...
- 结构：...
- 心智模型：...

### 5W1H
- What：...
- Why：...
- Who：...
- When：...
- Where：...
- How：...

### 技能类型
- 类型：[纯指令型 / 混合型]
- 判断依据：...

### 源一致性
- 内部一致性：[一致 / 存在矛盾：...]
- frontmatter vs body：[一致 / 存在矛盾：...]
- 与 README.md 一致性：[一致 / 不存在 / 存在矛盾：...]
- 与 references/ 一致性：[一致 / 存在矛盾：...]
- 与 templates/ 一致性：[一致 / 不存在 / 存在矛盾：...]
- metadata vs CHANGELOG：[一致 / 不存在 / 存在矛盾：...]
- 裁决结果：...
```

## 质量检查

- [ ] SKILL.md frontmatter 解析了吗？（name、description、metadata）
- [ ] 能一句话说明 WHY 吗？
- [ ] 核心机制（HOW）清晰吗？
- [ ] 具体功能（WHAT）完整吗？
- [ ] 冰山模型四个层次都覆盖了吗？
- [ ] 5W1H 六个维度都覆盖了吗？
- [ ] 理解摘要忠实于原技能吗？
- [ ] 技能类型识别了吗？
- [ ] 源一致性扫描了吗？
- [ ] 发现的矛盾有裁决策略吗？
- [ ] 项目追加文件（README.md、CHANGELOG.md、templates/）的存在性确认了吗？
