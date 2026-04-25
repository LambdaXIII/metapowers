# Diátaxis 框架

> 基于用户意图的文档分类：Tutorials / How-to Guides / Reference / Explanation

---

## 核心概念

| 类型 | 用户意图 | 核心问题 | 写作方式 |
|------|----------|----------|----------|
| **Tutorials** | "带我入门" | 如何开始？ | 手把手教学，从0到1 |
| **How-to Guides** | "帮我完成任务" | 如何达成目标？ | 步骤导向，解决具体问题 |
| **Reference** | "我需要查细节" | 具体参数是什么？ | 完整、精确、可检索 |
| **Explanation** | "帮我理解" | 为什么这样设计？ | 概念解释，背景说明 |

**关键原则**：按用户意图分类，而非按作者思维分类。

---

## 在技能文档中的应用

### 映射关系

| 输出文件 | Diátaxis 类型 | 用户意图 |
|----------|---------------|----------|
| README.md | Tutorials | "带我快速了解这个技能" |
| methodology/workflow.md | How-to Guides | "如何执行这个流程" |
| reference/guide-xxx.md | Reference | "我需要查某个细节" |
| methodology/core-concepts.md | Explanation | "为什么这样设计" |
| reference/examples.md | Tutorials | "给我看具体例子" |

### 判断方法

面对一段内容，问自己：用户读这段时想做什么？

- 想"跟着做一遍" → Tutorials
- 想"解决某个问题" → How-to Guides
- 想"查某个参数" → Reference
- 想"理解原理" → Explanation

---

## 检查清单

- [ ] 每个文档都有明确的 Diátaxis 类型吗？
- [ ] 类型判断基于用户意图而非内容主题？
- [ ] Tutorials 是否从0开始、可跟随执行？
- [ ] How-to 是否聚焦具体任务、步骤清晰？
- [ ] Reference 是否完整精确、便于检索？
- [ ] Explanation 是否解释"为什么"而非"怎么做"？
