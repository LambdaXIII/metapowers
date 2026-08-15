# GTD Contexts

> 按可用手段（工具、地点、精力水平）分类，而非按内容主题。传统上下文包括 @computer、@calls、@errands、@agenda、@home、@anywhere。与所有其他系统的分类维度都不同——它回答的不是"这是什么"而是"我能在这里做什么"。

**创建者**: David Allen（Getting Things Done）  
**核心分类维度**: 可用手段（工具 / 地点 / 精力状态）

## 分类维度对比

| 系统 | 问题 | 答案 |
|------|------|------|
| PARA | 这个内容需要行动吗？ | 可行动性 |
| Zettelkasten | 这个想法是什么？ | 概念 |
| Johnny Decimal | 这个编号多少？ | 固定位置 |
| **GTD Contexts** | **我在哪？我有什么工具？** | **可用手段** |

## 传统上下文

```
@computer      ← 需要用电脑做的事
@calls         ← 需要打电话
@errands       ← 需要外出办的事
@agenda        ← 需要和某人当面谈
@home          ← 只能在家做的事
@anywhere      ← 任何地方都能做的事（低精力任务）
```

## 分类规则

GTD 的上下文是**任务分类**而非**笔记分类**。上下文的作用是：

1. **批量处理**：你在电脑前时一次性处理所有 @computer 任务
2. **减少切换**：不需要不同上下文间反复切换工具
3. **精力匹配**：低精力时处理 @anywhere，高精力时处理 @computer

## Obsidian 中的 GTD 示例结构

最简 GTD 仓库（来自 [Obsidian Mate](https://obsidianmate.com/vaults) 模板）：

```
📁 0 Inbox/              ← 捕获所有输入，不处理
📁 1 Projects/           ← 项目文件
   ├── Project Alpha.md
   └── Project Beta.md
📁 2 Areas/              ← 持续责任
📁 3 Archive/            ← 已完成
📄 Daily Note.md         ← 日记，含当日任务
```

上下文通过 frontmatter `context:` 字段或标签实现，而非文件夹：

```yaml
---
title: "Review Q3 budget"
context: "@computer"
project: "Q3 Planning"
status: "next"
---
```

## 适用场景

- **任务管理为主**：你的笔记系统需要回答"我接下来做什么"
- **多上下文工作**：工作场景多样（办公室、家中、外出）
- **精力敏感型工作**：你根据不同精神状态安排不同任务

## 不适用场景

- **知识积累为主**：GTD 不回答"这个概念和另一个概念有什么关系"
- **纯学习型笔记**：学习笔记不需要上下文

## 改编要点

- GTD contexts 可以和其他系统共存——如 PARA 处理内容分类，contexts 处理执行时机
- 自定义上下文：根据你的实际场景调整（如设计师可能有 @design-tools, @research, @client-meeting）
- 精力标签（high/low energy）可以作为 context 的补充维度
- 前端代码中的 context 字段需要维护——定期清理已不使用的上下文

## 参考来源

- [FacileThings: GTD Contexts Guide](https://facilethings.com/blog/en/gtd-contexts) — 一手来源
- [Obsidian Mate: Best Obsidian Vaults](https://obsidianmate.com/vaults) — GTD 模板
- David Allen: Getting Things Done (书籍)
