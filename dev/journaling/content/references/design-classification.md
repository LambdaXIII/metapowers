# Classification Design Guide

> 本文件提供设计 journal 分类体系的方法论框架。它不提供"正确答案"——而是通过 5 步诊断流程，帮助你从现有内容推导出最适合当前需求的分类方案。
>
> 使用场景：
> - 初始化时目标目录已有内容但不是 managed journal → 按此指导设计自定义分类
> - 分类不适配（维护审计或日常感知）→ 通过此框架重新设计
> - 手动触发——当前分类持续感觉"不对"


## What is CLASSIFICATION.md?

**定义**：CLASSIFICATION.md 是 journal 的目录规则手册——记录当前生效的分类规则：每个目录放什么、不放什么、如何判断。

**Role**：
- **Classification anchor**：日常写入时的目录分配依据——"这个内容属于哪个目录"由 CLASSIFICATION.md 中的规则回答。
- **Evolution record**：分类规则随 journal 内容增长而演化。CLASSIFICATION.md 的变更历史记录了规则如何从种子结构逐步适配实际内容。
- **Shared reference**：维护时 agent 读取 CLASSIFICATION.md 了解"当前规则是什么"，而不是依赖记忆。

**Type Identification**：`# Classification` 标题 + `| 目录 | 放什么 | 不放什么 | 一句话判断 |` 四列快速参考表格。此表格是初始化时从模板写入的，用于区分 journal 的 CLASSIFICATION.md 和恰好同名的其他文件。

**Relationships**：
- `INDEX.md` 的协议声明行指向它（`分类规则 → CLASSIFICATION.md`）。
- `TAGS.md` 提供跨目录的次分类轴——目录是主分类轴，标签是次分类轴。
- 没有 CLASSIFICATION.md 时，4 目录种子结构是隐式分类。CLASSIFICATION.md 将其显式化。

---

## When to Design Classification

- **Initialization in design mode** — target path has existing content that is not a managed journal
- **Maintenance audit** — classification audit during maintenance flags issues requiring redesign
- **Manual trigger** — when the current classification feels persistently wrong

---

## Design Framework

以下流程是诊断式的——你的内容决定分类，而不是分类决定你的内容。每个步骤引用可参考的分类体系示例（`examples/classification-systems/`），代理只需阅读示例摘要即可判断是否进一步查看。


### Step 1: Scan — Understand Your Existing Content

在创建任何目录之前，先理解你有哪些内容。

**操作：**

1. 列出目标路径下所有.md 文件（排除 INDEX.md 等元文件）
2. 对每个文件，读取 frontmatter 和前三行，记录：
   - 文件目的（记录了一个什么事件/决策/发现）
   - 内容性质（经验教训、外部研究、参考资料、目标描述、活跃任务）
   - 大致创建日期和使用频率
3. 按自然相似性分组——不要强行套分类，先看哪些内容感觉"属于一起"

**参考示例：**

- `examples/classification-systems/para.md` — PARA 按可行动性分类，适合分析内容的目的性（这是待办事项还是参考资料？）
- `examples/classification-systems/journaling-default.md` — Journaling 默认 7 目录按生命周期分类，适合分析内容在"捕获→活跃→沉淀→归档"链条上的位置

**输出：** 一个未命名的内容簇列表，每簇 3-15 个文件。

---

### Step 2: Identify Natural Clusters

分析 Step 1 的内容簇，提炼它们共享的属性。

**操作：**

1. 对每个内容簇，回答三个问题：
   - **共性**：这些文件共享什么？相同的主题？相同的目的？相同的活性状态？
   - **区分性**：这个簇和另一个簇的主要差异是什么？这个差异是稳定的还是情境依赖的？
   - **边界案例**：什么内容会同时属于两个簇？如果不存在这样的内容，可能分类过细
2. 评估分类维度——你的簇是按照什么维度自然聚合的：

| 可能的维度 | 说明 | 查看示例 |
|-----------|------|---------|
| 可行动性 | 按"现在是否需要行动"分组 | `examples/classification-systems/para.md` |
| 概念/主题 | 按"这个想法是什么"分组 | `examples/classification-systems/zettelkasten.md` |
| 可用手段 | 按"在什么场景下使用"分组 | `examples/classification-systems/gtd-contexts.md` |
| 有限编号空间 | 按固定槽位分组 | `examples/classification-systems/johnny-decimal.md` |
| 生命周期阶段 | 按内容成熟度（捕获→处理→沉淀）分组 | `examples/classification-systems/journaling-default.md` |

> 一个内容簇可能有多个维度同时成立。选择**最稳定**的那个——如果可行动性会随时间变化，而主题不会，那么按主题更稳定。

**参考示例：**

- `examples/classification-systems/moc-lyt.md` — MOC 解决"一个内容属于多个簇"的问题，当你的簇不是正交时可以作为补充手段
- `examples/classification-systems/evergreen.md` — Evergreen Notes 不按文件夹分类，完全依赖链接和命名，适合内容簇之间关系比位置更重要的场景

**输出：** 3-7 个候选分类，每个分类有清晰的定义和边界条件。

---

### Step 3: Name & Define Categories

为每个候选分类命名并写正式定义。

**命名标准：**

- 名称反映分类的内部一致性（"活跃事务"比"Misc"好一万倍）
- 名称暗示什么内容应该放进去（"参考资料"暗示"不需要行动"）
- 名称说明什么内容不应该放进去（通过命名反例暗示边界）

**定义结构：**

```
## [分类名称]

目的：[句描述这个分类存在的理由]
包含：[明确说明什么类型的内容]
不包含：[明确排除什么类型的内容]
判断测试：[一句话问自己——"这个文件属于[分类名称]吗？"]
示例：[1-2 个真实文件标题]
```

**粒度控制：**

- 如果你需要 2 层以上文件夹，考虑是否是分类过细
- 如果你经常在想"这个该放哪"，考虑是否分类边界不够清晰
- 允许一个"不确定"兜底位置（如 Inbox）——它不丢人，它是设计的一部分

**参考示例：**

每个示例文件都包含分类定义部分，展示了不同系统如何定义边界：
- `examples/classification-systems/para.md` 有 PARA 的"区分规则"表
- `examples/classification-systems/journaling-default.md` 有 7 目录的"分类逻辑"表

**输出：** 3-7 个命名好的分类定义。

---

### Step 4: Test Orthogonality & Coverage

验证你的分类是否满足两个核心质量指标。

**正交性（Orthogonality）：** 一条内容不应该可以合理地放在两个分类中。

测试方法：随机抽取 10 条内容，尝试把它们放到两个不同的分类中。如果 >3 条感觉合理，你的分类不是正交的。

- 不友好的正交性测试：检查是否有内容同时在 A 和 B 中都"感觉对"
- 友好的正交性解释：有些内容天然跨域。对于这些内容，不要试图强行塞入一个分类，而是：
  - 接受它属于主要分类，用标签/链接表达跨域关系
  - 或者创建 MOC（index note）跨分类聚合，而不是改变分类本身

**覆盖度（Coverage）：** 所有现有内容都能放入至少一个分类。

测试方法：遍历 Step 1 扫描的所有文件，为每条内容指派分类。

- 如果有内容找不到归属，需要新增分类或扩展现有分类的定义
- 如果 >90% 的内容集中在 1-2 个分类，分类可能太粗，考虑是否需要拆分
- 如果每个分类只有 1-2 条内容，分类可能太细——考虑是否需要合并

**参考示例：**

- `examples/classification-systems/johnny-decimal.md` 展示了"有限槽位"的设计哲学——每个新分类都消耗一个永远不重用的 ID，这个约束本身就迫使正交性
- `examples/classification-systems/moc-lyt.md` 展示了当正交性不可能时如何用 MOC 弥补

**输出：** 分类正交性评估 + 覆盖度评估。标记跨域内容和未覆盖内容。

---

### Step 5: Document — Write CLASSIFICATION.md

将验证后的分类写入 CLASSIFICATION.md，作为 Journal 日常操作的参考文档。

**格式：**

```markdown
# Classification

> 本文件记录当前 journal 的分类规则。封面提供快速参考，后续章节提供每条规则的详细定义和判断标准。
> （此文件在维护时重新评估，日常操作不读取全文）

## 快速参考

| 目录 | 放什么 | 不放什么 | 一句话判断 |
|------|--------|---------|-----------|
| [目录名] | [简短描述] | [排除] | [测试问题] |

## 分类定义

逐一列出每个目录的完整定义（从 Step 3 复制）。

## 跨域内容

列出跨域内容的处理方式（链接、标签、MOC 引用）。

## 规则变更历史

记录分类规则的修改（日期 + 原因）。
```

**写入条件：** CLASSIFICATION.md 只在以下情况更新：
- 初始化时设计模式完成（首次写入）
- 维护审计诊断出需要修改
- 手动触发的重新设计

**参考示例：**

- `examples/classification-systems/journaling-default.md` — 默认 7 目录的完整定义，可以作为 CLASSIFICATION.md 的参考格式

**输出：** `CLASSIFICATION.md` 文件（位于 journal 根目录）。

---

## Verification Checklist

设计完成后，检查以下各项是否满足。全部通过后再投入使用。

### 覆盖率
- [ ] 每条现有内容都能放入至少一个分类
- [ ] 分类总数 ≤ 7 ± 2（认知负荷上限）
- [ ] 深层嵌套 ≤ 2 层

### 边界清晰度
- [ ] 每对相邻分类有明确的边界区分规则
- [ ] 有一个兜底位置（Inbox/Unsorted/Misc）处理无法立即分类的内容
- [ ] 跨域内容有明确的处理策略（主分类 + 链接/MOC/标签）

### 长期可持续性
- [ ] 分类预期能在未来 6 个月内不被推翻（但你可以在 6 个月后修改它）
- [ ] 分类的数量不会随着内容增长而自动膨胀——新内容不自动要求新分类
- [ ] 分类规则可以写进 CLASSIFICATION.md 的一次性短文档中

### 与实际使用的关系
- [ ] 分类维度反映了你实际查询笔记的方式（你找笔记时是按什么条件找的）
- [ ] 日常写入不需要阅读分类定义——直觉测试就够了
- [ ] 最大分类的内容量不会大到检索困难（如果某个分类 >200 条，考虑是否需要内部子结构或 MOC）

---

## Common Pitfalls

从真实用户实践中提取的常见错误模式。

### 1. 分类瘫痪

> "深层嵌套的文件夹让找笔记变成了一场寻宝——几个月后你根本不记得笔记在哪里。"

**表现**：每次写笔记时花大量时间决定放哪，最终放在不对的地方或干脆不写。

**预防**：inbox 缓冲 + 简单规则（见 journaling-default 的"分类逻辑"表）+ 容忍偶尔的分类错误。

**修复**：维护时批量修正，日常不追究。

### 2. 分类法崇拜（完美文件夹结构陷阱）

> "他们花了几周完善他们的设置，把每样东西都连接到每样东西，直到他们的系统看起来像是由正在崩溃的人设计的蜘蛛网。"

**表现**：花在调整系统上的时间超过实际使用笔记的时间。陷入"如果我的分类再完美一点，我的生产力就会提升"的幻觉。

**预防**：分类设计是迭代的——先用不完美的分类开始，在维护中逐步改进。分类的最终验证是"我能否找到想要的笔记"，而不是"我的分类是否美丽"。

### 3. 标签通胀

> "#dog 还是 #dogs？#pets 还是 #mammals？"

**表现**：不受控的标签逐渐退化为噪声。同义、近义、层级混乱的标签数量超过有效使用阈值。

**预防**：维护 tag registry（受控词汇表），定期合并冗余标签。标签是跨切面分类手段，不是主分类的替代。

### 4. 单一系统教条

> "我尝试 PARA、Zettelkasten 和其他系统，六个月都放弃了。"

**表现**：盲目遵循某一方法论的所有规则，而不考虑自己的实际内容和工作流。

**预防**：参考示例中的"改编要点"（每个示例文件末尾都有这个章节）——所有系统都是起点，不是终点。你的分类应该从内容推导，而不是从方法论推导。

### 5. Projects vs. Areas 的模糊边界

**表现**：无法区分"有时限的任务"和"持续的责任"，导致内容在这两个分类间反复移动。

**预防**：如果你使用 Project/Area 维度，接受边界模糊是常态而非异常。维护 CLASSIFICATION.md 中"跨域内容"章节，记录你的判断标准。

### 6. 衰退信号

**标志**：持续感觉分类"不对"、内容积累后查询成本上升、或者你在写笔记时开始跳过分类步骤直接扔到 inbox。

**行动**：触发分类审计，运行以上 5 步流程重新评估。

---

## Referenced Example Files

本文件引用的所有示例见 `examples/classification-systems/`。每个文件以摘要开头，代理可以先读摘要判断是否需要全文：

| 文件 | 一句话摘要 |
|------|-----------|
| `para.md` | 按可行动性分四个容器（Project/Area/Resource/Archive），适合项目驱动型内容 |
| `zettelkasten.md` | 按概念分原子笔记 + 链接网络，适合知识积累与发现 |
| `johnny-decimal.md` | 按有限编号空间（10×10 槽位），适合需要跨工具一致分类 |
| `moc-lyt.md` | 按导航优先（索引笔记替代文件夹），适合大型笔记库 |
| `evergreen.md` | 按演化概念（笔记随时间生长），适合长期知识写作 |
| `journaling-default.md` | 主观/客观 × 长期/短期（4 目录种子 → 可演化），AI agent 日记的起点和演化参考 |
