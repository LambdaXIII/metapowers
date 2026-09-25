# journaling Specification

## Purpose

本域是 Agent 长期记忆的笔记本系统技能。Agent 跨 session 工作但记忆不跨 session，本技能为 agent 建立结构化的长期记忆笔记系统——有入口（INDEX.md）、有条目规范、有维护协议——解决「写了不读、写了找不到、写了变噪音、写了不维护」四个问题。设计目标是让 agent 自发形成持续演进的笔记系统：记笔记成为自然行为，系统随内容生长，每个新 session 能从先前状态继续。journal 服务于 agent 自身，不服务于用户。

## Requirements

### Requirement: 行为边界
本技能 MUST 提供：长期记忆笔记系统的协议体系（初始化、写入、导入、维护）、规则设计方法论、可改的种子方案与无依赖的便捷脚本。本技能 MUST NOT 替任何 journal 决定分类方案、标签集或目录结构——内容组织规则由各 journal 自管理；MUST NOT 自动触发维护——维护由 agent 判断或用户要求启动。journal 的可逆操作（目录重组、标签合并等）由 agent 自主决定并执行，不需要用户批准。

#### Scenario: 分类归属不由技能裁定
- GIVEN 某 journal 的规则文档定义了分类方案
- WHEN 判断一条新内容的目录归属
- THEN 依该 journal 规则裁定，本技能不预设任何强制分类

#### Scenario: 维护不自动启动
- GIVEN journal 存在条目过期或标签蔓延迹象
- WHEN 判断是否启动维护
- THEN 由 agent 自行判断或用户要求触发，不存在自动触发信号机制

### Requirement: 硬性机制边界
技能内容中仅以下五项 MAY 作为硬性机制存在：INDEX 可发现性保证（发现合约）、读取与写入的不对称加载、INDEX 作入口、RULES 作规则纪录（单入口、必读、必须存在）、笔记文件必须含 YAML 段。其余一切机制（分类、标签、字段、目录、INDEX 板块、维护信息等）MUST 仅作引导性建议表述——MUST NOT 点名 INDEX 具体板块、MUST NOT 要求必填字段、MUST NOT 断言种子目录存在。种子方案（RULES.md 初始分类、tag、字段方案）是可改默认值，不是规范；规则文档入口名 RULES.md 由机制绑定，其内容自定、可自组织为多文件。

#### Scenario: 引导性机制被写成硬性要求即违规
- GIVEN 技能内容要求「每条笔记必须填写某字段」，而该字段不在五项硬性机制内
- WHEN 检查表述
- THEN 判定违规，该机制只能作引导性建议表述

#### Scenario: 种子被当作规范即违规
- GIVEN 技能内容把种子的分类方案表述为强制要求
- WHEN 检查种子的定位
- THEN 判定违规，种子是可改默认值

### Requirement: 删除与归档边界
技能 MUST NOT 规定具体的归档设施（目录名、机制）。「删除」与「归档」在技能内容中 MUST 作为通用操作词使用，MUST NOT 指代特定目录。维护协议 MUST 保留「不直接删除」的底线做法（以移动代替删除），移动目标为临时保存目录或该 journal 规则已定义的类似设施，MUST NOT 指定目录名。

#### Scenario: 指定归档目录即违规
- GIVEN 技能内容写有「删除的条目移入 archive/ 目录」
- WHEN 检查归档设施表述
- THEN 判定违规，移动目标由 journal 规则决定，技能不指定目录名

### Requirement: 维护协议三分离
维护协议 MUST 保持三分离结构，段落形态可调整但三分离不可破坏：(1) 流程推荐化——推荐流程是默认值而非规范，agent 可理解动机后自行调整，其中 MUST NOT 出现强制措辞；(2) 红线集中化——硬性要求（「必须 / 禁止」措辞）MUST 只出现在操作规范段，作为硬性要求的唯一集中地；(3) 启发性独立化——「怎样跳出框架」的启发内容 MUST 独立成段。

#### Scenario: 推荐流程混入强制措辞即违规
- GIVEN 维护协议的推荐流程段写有「必须先做 X」
- WHEN 检查三分离
- THEN 判定违规，强制措辞只能出现在操作规范段

### Requirement: 协议设计范式
协议文档 MUST 按操作场景分两类设计：远征型（任务独立、步骤多、边界清晰，每步给出 why，强边界约束）与内嵌型（嵌入主线工作、高频率、低延迟，仅开头定位说明，不提供逐步骤 why）。新增协议 MUST 先判定场景类型，再按对应范式设计；MUST NOT 以远征型范式设计内嵌型协议。每个协议开头 MUST 描述完成状态（做完这个想达到什么状态）——远征型展开为完整节，内嵌型保留 2-3 行定位说明。任何含「先理解现状再决策」的流程 MUST 保留决策前的理解验证环节（确认数据解读无误），与交付前的质量检查区分。导入协议的准入判断 MUST 按成本递增排列：技术检查与基于已知信息的判断先于内容读取。

#### Scenario: 新协议未判型即落笔
- GIVEN 计划新增一个协议文档
- WHEN 检查设计过程
- THEN 先判定远征型 / 内嵌型，再按对应范式编写

#### Scenario: 协议开头缺完成状态即违规
- GIVEN 某协议文档的开头
- WHEN 检查完成状态描述
- THEN 开头说明完成后的目标状态：远征型为完整节，内嵌型为 2-3 行定位说明

#### Scenario: 理解验证缺失即违规
- GIVEN 某流程含「先理解现状再决策」环节
- WHEN 检查流程构成
- THEN 决策前存在理解验证（确认数据解读无误），与交付前质量检查分立

### Requirement: 信息依赖结构
技能 MUST 以信息缺口驱动 agent 行动，MUST NOT 依赖惩罚条款——内容中 MUST NOT 出现「违反的代价」类表述。三层信息依赖结构 MUST 保持各层职责：description 声明操作边界（什么操作需要本技能）；SKILL.md 正文声明信息依赖（需要 INDEX.md 中的什么）；INDEX.md 自述价值（包含什么、跳过它的代价）。

#### Scenario: 惩罚条款即违规
- GIVEN 技能内容写有「若跳过 INDEX.md 将导致 XX 后果」类惩罚表述
- WHEN 检查驱动方式
- THEN 判定违规，行动依据必须来自信息缺口而非惩罚条款

### Requirement: 语言与措辞约定
SKILL.md MUST 用英文编写；references/ MUST 保持中文。journal 路径 MUST 以 `<journal-root>` 参数化指称，示例 MUST 使用通用占位符，MUST NOT 回填特定项目名或硬编码路径。Operating Principles 追加新规则时 MUST 用指令式措辞，MUST NOT 夹带历史溯源——历史案例属于 journal 经验条目，不属于技能规范。SKILL.md 的路由表与 Linked Files 两个位置 MUST 同步维护，新增或移除 reference 文件时两处同时更新。

#### Scenario: 硬编码路径即违规
- GIVEN 某技能内容含具体项目路径或项目名
- WHEN 检查通用性
- THEN 判定违规，路径必须写作 `<journal-root>` 形式

#### Scenario: 路由两处失步即违规
- GIVEN 新增了一个 reference 文件
- WHEN 检查 SKILL.md
- THEN 路由表与 Linked Files 都登记了该文件

### Requirement: 元语境渗漏控制
技能的文字载体 MUST 只承载文字语境——操作事实、约束边界、结构导航、判断依据；MUST NOT 出现写过程语境——写作要求、设计意图、写作态度、对文本的自我定位、写作过程状态。判定标准是语境归属（这段文字对运行时读者有功能吗），MUST NOT 以「是否作者现身」等形式判定。发现写过程语境时 MUST 三选一修复：删除（任何读者都不用）、归位（对另一载体的读者有功能——设计意图归开发侧文档、变更历史归 CHANGELOG）、转化（当前读者有功能但形态是写过程的，转为操作事实陈述，如「可以考虑 X」→「可 X」）。

#### Scenario: 写作要求混入即违规
- GIVEN 技能内容含「本技能统一使用术语 A 而非 B」类写作约定
- WHEN 检查语境归属
- THEN 判定违规：该约定对运行时读者无功能，须删除或归位到开发侧文档

#### Scenario: 写过程形态可转化保留
- GIVEN 技能内容含「可以考虑 X」的建议句
- WHEN 检查语境归属
- THEN 该句对运行时读者有功能但形态是写过程的，转为「可 X」的形式

### Requirement: 触发语义
触发边界 MUST 是操作范围约束而非场景枚举：凡对 journal-root 的写入性操作（创建、写入、编辑、移动、归档、删除、维护、整理、写入设计决策等）MUST 加载本技能，读取访问 MUST NOT 要求加载。description MUST 保持「操作范围约束 + 写入操作示例」结构，MUST NOT 退回场景白名单；MUST 保留中英操作动词触发面。INDEX.md 的协议声明行 MUST 标注「读此文件不需要加载 skill · 写入或维护时必须加载」；本技能 MUST NOT 为读取增加加载要求。

#### Scenario: 新说法的写入操作同样受约束
- GIVEN 用户以新措辞要求把某决策写入 journal 文件
- WHEN 判定是否加载
- THEN 该操作落入 journal-root 写入范围，必须加载本技能

#### Scenario: 只读访问不加载
- GIVEN 本 session 只需浏览 INDEX.md 与查阅条目
- WHEN 判定是否加载
- THEN 不加载本技能

#### Scenario: 协议声明行保持标注
- GIVEN journal 的 INDEX.md
- WHEN 检查协议声明行
- THEN 标注「读此文件不需要加载 skill · 写入或维护时必须加载」
