# web-entity-search Specification

## Purpose

本域是快速结构化实体搜索技能，填补「直接搜索」与「深度研究」之间的空白：直接搜索快但结构松散——只抓到首条结果的碎片、漏掉关键维度；深度研究全面但重——对「XX 是啥」过于奢侈。本技能只加两层东西：**维度模板**（这类实体该看哪几个关键维度——搜索时的 checklist）和**停止纪律**（≥ 2 个来源即填、填完就停）。

## Requirements

### Requirement: 行为边界
本技能 MUST 提供：单个命名实体的快速结构化搜索、关键维度覆盖、轻量置信回检。本技能 MUST NOT 提供：链式线索追踪、多实体对比、深度争议分析——这些超出本技能边界。搜索工具的选择与网页内容提取方法 MUST NOT 在本技能范围内——本技能只管「搜什么、搜多少、何时停、怎么呈现」。停止纪律 MUST 保持：≥ 2 个来源即填充维度、填完即停。实体涉及高度争议话题时 MUST 标注「controversial」即停，MUST NOT 深入评价任何一方。实体类型覆盖 MUST 保持七类：人物、公司/组织、创意作品、产品/技术、事件、概念/术语，以及不匹配任何判定线索或跨类型的兜底类。

#### Scenario: 超出边界不承接
- GIVEN 请求对某话题做多来源交叉比对的深度调查
- WHEN 对照行为边界
- THEN 属深度研究范畴，不在本技能内执行链式追踪或争议分析

#### Scenario: 争议话题即停
- GIVEN 目标实体涉及高度争议话题
- WHEN 搜索到该情况
- THEN 输出标注 controversial 并停止，不深入评价任一方

#### Scenario: 两来源即停
- GIVEN 某实体已获得 ≥ 2 个来源并填满维度
- WHEN 判断是否继续搜索
- THEN 停止搜索，进入回检与输出

### Requirement: 模板与输出形态
维度模板 MUST 位于 templates/——语义是 agent 按需读取的执行模板（搜索过程中当 checklist 使用）；references/ MUST 只承载知识类内容（搜索指引、维度表、坑位规则）。输出 MUST 是自然语言段落，MUST NOT 是表单或检查表——维度是给 agent 看的工作工具，不是交付格式；把「维度 1：✔」式检查表呈现给用户即为误解本意。

#### Scenario: 检查表不出现在交付
- GIVEN 已填完维度模板的搜索结果
- WHEN 产出交付
- THEN 呈现为自然语言结构化回答，不含检查表形态

### Requirement: 置信回检与委派纪律
置信回检 MUST 只抽样——抽查 2-3 个关键维度，发现矛盾即标注；MUST NOT 全量回检，MUST NOT 因回检重新打开搜索链路。委派子代理执行时，下发 MUST 只含任务描述；MUST NOT 读取本技能文件并转达给子代理——子代理自行加载本技能并按其流程执行。

#### Scenario: 回检不重开搜索
- GIVEN 回检某维度时发现来源间存在矛盾
- WHEN 处理该矛盾
- THEN 标注矛盾，不重新发起搜索链路

#### Scenario: 委派不转达技能内容
- GIVEN 主 agent 将实体搜索委派给子代理
- WHEN 下发任务
- THEN 只传任务描述，技能文件由子代理自行加载

### Requirement: 语言约定
SKILL.md MUST 用英文编写；references/ 与 templates/ MUST 保持中文。description MUST 含中英双触发面（中文「查一下 / 是什么」与英文 "what is X?"）。技能内容 MUST NOT 硬编码其他技能名——边界 MUST 用功能描述表达（如「链式线索追踪超出本技能范围」），MUST NOT 点名其他技能。

#### Scenario: 边界表述不点名
- GIVEN 技能内容表达与深度研究的边界
- WHEN 检查表述
- THEN 用功能描述（链式线索追踪、交叉比对等），不出现其他技能名

### Requirement: 触发语义
触发面 MUST 覆盖两类问法：「XX 是什么 / 查一下 / 搜索 / 搜一下 / 了解一下」+ 具名实体（人物、公司、作品、产品、事件、概念），以及 "what is X?" / "look up" / "search for" + 具名实体。触发判定线索 MUST 以实体的搜索结果特征为准（如人物类结果出现生卒年与职业身份），MUST NOT 依赖用户句式穷举。

#### Scenario: 中英问法均命中
- GIVEN 「查一下 DeepSeek 是什么」与 "what is Blackmagic Design?" 两个请求
- WHEN 判定触发
- THEN 两者都命中触发面，目标均为具名实体
