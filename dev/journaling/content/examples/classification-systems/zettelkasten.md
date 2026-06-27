# Zettelkasten

> 以原子笔记和密集链接为基础的知识积累系统。每条笔记包含一个核心想法，通过链接网络而非文件夹层级表达概念之间的关系。适合以知识探索和写作为目标的使用者。

**创建者**: Niklas Luhmann（原始），现代数字版由社区演进  
**核心分类维度**: 概念（一个笔记 = 一个概念，通过链接表达概念间关系）

## 核心原则

1. **原子性（Atomicity）**：每条笔记只包含一个核心想法
2. **自主性（Autonomy）**：每条笔记独立可理解，不依赖上下文
3. **链接为主（Connectedness）**：通过链接表达概念结构，而非文件夹
4. **累积（Accumulation）**：笔记价值随数量增长（网络效应）

## 原始 vs 现代

| 方面 | 原始 Luhmann（1960s） | 现代数字版 |
|------|---------------------|-----------|
| 物理介质 | 纸质索引卡（90,000 张） | 数字文件 |
| 分类 | Folgezettel 编号系统（层级分支） | 链接 + 标签 |
| 盒子 | 文献盒（书目笔记）+ 主盒（想法） | 单个 vault |
| 元结构 | Structure Notes / Hub Notes | MOC / Index Notes |
| 文件命名 | 编号（如 21/3a26c1） | 概念名（如 "atomic-notes.md"） |

**关键事实**：原始 Luhmann 系统并非"无文件夹"——Folgezettel 编号本质上是树状层级分类。现代数字版才去掉了编号，完全依赖链接。

## 目录结构示例

```
📁 inbox/            ← 未处理的原始想法
📁 notes/            ← 主体：所有原子笔记，扁平存储
📁 structure/        ← Structure Notes / MOC / Index
📁 literature/       ← 文献笔记（外部来源的重新表述）
📁 attachments/      ← 图片、PDF
```

或更简化的：

```
📂 /
  ├── atomic-notes.md        ← 主体笔记，全部在根目录
  ├── zettel-structure.md    ← Structure note：整体结构概览
  ├── zettel-moc-concepts.md ← MOC：相关概念的索引
  ├── ...
```

## 适用场景

- **学术研究 / 深度写作**：需要长期积累和发现概念关系的场景
- **探索性思考**：不确定最终输出是什么，但需要持续积累
- **网络化知识**：内容之间的关联比内容本身的位置更重要

## 不适用场景

- **任务管理**：Zettelkasten 不处理"接下来该做什么"
- **快速捕获**：原子笔记的要求在有时间压力时会变成负担
- **需要严格分类**：如果你必须知道"这条笔记在哪"，Zettelkasten 会让检索更像探险

## 改编要点

- 现代实践中，Zettelkasten 通常不替代文件夹，而是和扁平目录 + MOC 配合使用
- 可以保留 `inbox/` 作为临时缓冲，定期处理为原子笔记
- 文献笔记和主笔记的分离是 Luhmann 的关键设计——这两者的目的不同，虽然可以放在一起，但要清楚区分

## 参考来源

- [Ernest Chiang: 原始 Zettelkasten 方法深度分析](https://www.ernestchiang.com/en/posts/2025/niklas-luhmann-original-zettelkasten-method/)
- [Wikipedia: Zettelkasten](https://en.wikipedia.org/wiki/Zettelkasten)
- [Andy Matuschak: Evergreen notes](https://notes.andymatuschak.org/Evergreen_notes) — 概念相近但独立的系统
