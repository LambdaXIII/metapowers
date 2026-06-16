# 第三阶段：编排

> 将解构后的内容组织为结构化的文档大纲。

---

## 目标

确定输出文档的形态和结构，为表达阶段提供清晰的蓝图。

## 为什么需要这些知识文档

解构阶段得到了零散的能力单元和知识单元，需要：
- **Diátaxis 框架**：按用户意图分类内容（Tutorials/How-to/Reference/Explanation）
- **金字塔原理**：确保内容组织有逻辑、有层次
- **渐进式披露**：设计 L1-L4 阅读层级，让读者按需深入

## 如何加载知识文档

按顺序加载：
1. [frameworks/diataxis.md](../frameworks/diataxis.md) — 确定文档类型
2. [frameworks/pyramid-principle.md](../frameworks/pyramid-principle.md) — 组织内容逻辑
3. [frameworks/progressive-disclosure.md](../frameworks/progressive-disclosure.md) — 设计阅读层级

加载方式：读取文件内容，提取分类标准和组织原则，应用到解构结果。

## 操作步骤

### 步骤1：确定输出形态

根据原始技能结构判断：

| 原始技能结构 | 输出形态 |
|-------------|----------|
| 只有 SKILL.md，且 < 400 行 | 单文件 |
| 只有 SKILL.md，但 ≥ 400 行 | 多文件 |
| 有 SKILL.md + 其他文件（references/、examples/、README.md 等） | 多文件 |

### 步骤2：应用 Diátaxis 分类

将解构后的知识点按用户意图分类：
- **Tutorials**：入门引导（README.md、examples.md）
- **How-to Guides**：操作指导（workflow.md）
- **Reference**：细节查阅（decision-rules.md、guide-xxx.md）
- **Explanation**：原理解释（core-concepts.md、design-notes.md）

**根据技能类型调整大纲**

纯指令型技能的特殊处理：
- core-concepts.md 可能无法生成有意义内容（缺乏设计理由和概念解释）
- 处理方式：将 core-concepts.md 的内容合并到 workflow.md 的"设计背景"章节，不单独生成空文件
- 在文档大纲中标注"core-concepts.md 合并至 workflow.md"

混合型技能：使用标准大纲，不做调整。

### 步骤3：应用金字塔原理

- 每个文档先写结论/摘要
- 上层概括下层，下层支撑上层
- 同层内容归类分组，逻辑递进

### 步骤4：设计渐进式披露层级

- **L1 概览**（30秒）：README.md 的一句话定义 + 适用场景
- **L2 摘要**（2分钟）：methodology/core-concepts.md 的核心概念
- **L3 详情**（10分钟）：methodology/ 和 reference/ 的完整内容
- **L4 深度**（按需）：meta/ 的设计笔记和版本历史

### 步骤5：输出文档大纲

## 输出格式

```markdown
## 文档大纲

### 输出形态
[单文件 / 多文件]

### 文件清单

| 文件 | Diátaxis 类型 | 内容来源 | 阅读层级 |
|------|---------------|----------|----------|
| README.md | Tutorials | SKILL.md 核心定位 | L1 |
| methodology/core-concepts.md | Explanation | SKILL.md + README.md | L2 |
| methodology/workflow.md | How-to | SKILL.md 流程 | L3 |
| ... | ... | ... | ... |

### 内容映射

| 解构结果 | 输出文件 | 处理方式 |
|----------|----------|----------|
| 核心能力 | README.md + core-concepts.md | 提取 WHY/HOW/WHAT |
| 程序知识 | workflow.md | 步骤说明 |
| 规则知识 | decision-rules.md | 明确约束 |
| ... | ... | ... |
```

## 质量检查

- [ ] 输出形态判断合理吗？
- [ ] 每个文件都有明确的 Diátaxis 类型吗？
- [ ] L1-L4 层级清晰吗？
- [ ] 所有解构结果都有输出目标吗？
- [ ] 内容映射忠实于原技能吗？
- [ ] 技能类型是否影响了大纲设计？
- [ ] 纯指令型技能的 core-concepts.md 处理方案是否合理？
