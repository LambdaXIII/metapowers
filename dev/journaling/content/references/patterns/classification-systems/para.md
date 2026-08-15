# PARA Method

> 按可行动性组织信息，而非按主题。所有内容归入四个顶层容器：Projects（有时间限制的项目）、Areas（持续责任）、Resources（参考资料）、Archives（已归档）。最广泛推荐的 Obsidian 起点方案。

**创建者**: Tiago Forte  
**核心分类维度**: 可行动性（该内容现在需要行动？还是未来可能有用？还是已完成？）

## 核心结构

```
📁 Projects/        ← 有截止日期和明确交付物的活跃工作
📁 Areas/           ← 持续的责任领域，无截止日期（健康、财务、家庭）
📁 Resources/       ← 参考资料，当前不活跃但可能有用
📁 Archive/         ← 已完成或非活跃的项目和领域
```

## 分类规则

每条笔记只属于一个目录。区分规则：

| 情况 | 归属 | 示例 |
|------|------|------|
| 有截止日期 + 具体交付物 | Projects | "Q3 市场分析报告" |
| 持续负责，无结束日期 | Areas | "健康"、"财务规划" |
| 感兴趣，当前无行动 | Resources | "Python 机器学习教程" |
| 已结束 / 不再活跃 | Archive | 已完成的项目 |
| 不确定 | 临时放入 Resources | — |

## 真实案例：Obsidian 混合模板

来自 [Studio Obsidian](https://studio-obsidian.com/obsidian-folder-structure/) 的推荐结构：

```
📁 00 - Inbox        ← 先捕获，再分类
📁 01 - Projects     ← 有截止日期的活跃工作
📁 02 - Areas        ← 持续的生活领域
📁 03 - Notes        ← 永久原子想法（Zettelkasten 补充）
📁 04 - Resources    ← 参考答案
📁 05 - Templates    ← 笔记模板
📁 06 - Attachments  ← 图片、PDF、文件
📁 07 - Archive      ← 已完成/非活跃
📄 Home.md           ← 主索引（MOC）
📄 Daily / YYYY-MM-DD ← 日记
```

## 适用场景

- **内容创作者 / 自由职业者**：他们有明确的 deliverables 和项目周期
- **初学者**：PARA 提供了一个清晰的结构起点，减少"怎么组织"的空白
- **输出导向的人**：需要快速找到当前工作所需的信息

## 不适用场景

- **知识工作者**：以概念探索为主的工作流中，Project/Area 边界频繁模糊
- **纯学习 / 研究型**：缺乏对概念之间关系的表达能力——PARA 不解决"A 概念和 B 概念有什么联系"的问题
- **AI 增强的工作流**：PARA 假设人类读者，AI 需要 frontmatter 契约和渐进式摘要结构

## 改编要点

- 可以添加 `Inbox/` 作为捕获缓冲（PARA 原始设计中没有明确 inbox，但几乎所有实践者都加了）
- `Areas/` 和 `Resources/` 的边界可以根据实际内容灵活调整——核心是保持 Project/非Project 的分界清晰
- 对 AI 读者，PARA 的四个目录不足以表达内容之间的关系，需要补充 frontmatter 字段和链接

## 参考来源

- [Forte Labs: The PARA Method](https://fortelabs.com/blog/para) — 一手来源
- [TheOwlLogic: How to Organize Your Obsidian Vault](https://theowllogic.com/obsidian-folder-structure)
- [Wasita: Four Folders Won't Hold](https://wasita.net/blog/four-folders-wont-hold/) — PARA 对 AI 工作流的不足
