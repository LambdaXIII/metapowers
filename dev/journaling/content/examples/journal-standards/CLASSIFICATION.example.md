# Classification

> 本文档记录当前 journal 的分类规则。
>
> 初始种子是 4 个目录（inbox / experience / knowledge / active_works），以下结构是在维护中逐步演化而成的成熟形态。
>
> 关于分类设计的完整方法论，见 `references/design-classification.md`。

## 快速参考

| 目录 | 放什么 | 不放什么 | 一句话判断 |
|------|--------|---------|-----------|
| `inbox/` | 不确定归属的内容 | 已明确分类的条目 | 放这里会后悔吗？不会就放 |
| `experience/` | 个人实践的教训、决策、方法 | 外部研究、正在做的事 | 这是我做的还是别人做的？ |
| `research/` | 对外部事物的调研、分析 | 自己的实践心得 | 这是我从外部学来的吗？ |
| `reference/` | 即用参考：配置、速查表 | 需要深度理解的内容 | 这是我下次还需要查的吗？ |
| `active/` | 进行中的任务、被阻塞项 | 已完成、未来的事 | 这件事现在是否需要行动？ |
| `goal/` | 长期目标、待讨论的想法 | 正在做的事 | 如果删掉这行，我的工作会失去方向吗？ |
| `archive/` | 已完成/非活跃的历史内容 | 当前仍在参考的内容 | 一个月内还会需要它吗？ |

## 演化历史

| 阶段 | 结构 | 触发条件 |
|------|------|---------|
| 初始化 | inbox / experience / knowledge / active_works | — |
| 第一次分裂 | knowledge → research + reference | knowledge/ 超过 20 条，查询模式分化为"深度阅读"和"即用查找" |
| 第二次分裂 | active_works → active + goal | active_works/ 中既有"正在做的事"也有"将来想做的事"，互相干扰 |
| 第三次分裂 | 新增 archive | 第一条内容完成并确认不再活跃 |

## 跨域内容处理

- 一条经验（experience/）引用外部研究：在 body 中用 `Related:` 链接 research/ 下的相关条目
- 一条研究（research/）包含个人应用心得：在 body 中用 `## 应用` 节标注，不改变目录归属
