# agent-prompt-design Specification

## Purpose

本域是 Agent 系统提示词（agent prompt）设计方法论技能。Agent 系统提示词是持久的行为宪法，需要考虑跨多轮对话的一致性、工具调用协议的稳定性、安全边界的完整性与版本化运营——这与面向单次 LLM 调用的提示词编写是不同品类，两者互补而非替代。本技能覆盖从结构设计、内容编写、工具协议、安全加固到运营管理的完整方法论，安全视为设计起点而非部署后补。

## Requirements

### Requirement: 行为边界
本技能 MUST 提供以下范围的方法论：系统提示词的结构设计、内容编写、推理模型（2026）策略、工具定义标准、安全防护、运营管理（版本化与回归测试）、四家前沿厂商的差异化策略、反模式诊断，以及可直接复制的模板。本技能 MUST NOT 提供：垂直领域业务逻辑文案、代码实现、训练级指导（微调、RLHF 等）、非英语模型的本地化建议。模型覆盖范围面向 2026 前沿模型（Claude 4.6+、Gemini 3.x、GPT-5.x / o 系列、Grok 4.x 及同级能力模型）；旧模型场景由参考文档的版本标注策略承担，未标注的策略默认面向前沿模型。

#### Scenario: 范围外请求不被承接
- GIVEN 用户要求本技能产出「金融客服 agent 的具体业务话术」或 API 集成代码
- WHEN 对照行为边界
- THEN 该请求超出本技能范围，不产出对应内容

#### Scenario: 未标注策略按前沿模型解释
- GIVEN 某参考文档中的策略未带模型版本标注
- WHEN 判断其适用模型
- THEN 该策略默认面向前沿模型，旧模型场景查该文档的版本标注策略

### Requirement: 专题文件独立与按需加载
references/ 下的参考文档 MUST 每文件聚焦一个主题、按需加载。以下专题 MUST 独立成文件，MUST NOT 埋入其他主题文档：推理模型策略（reasoning-models-2026）、安全（safety）、反模式诊断（anti-patterns）。templates/ 与 references/ MUST 分离：模板是可直接复制使用的产出物，参考文档是方法论知识，两类 MUST NOT 混放。SKILL.md MUST 以快速决策树引导按需定位文件，MUST NOT 引导线性通读全部参考文档。开发侧素材（研究资料等）MUST NOT 进入技能内容，MUST NOT 被技能内容链接。

#### Scenario: 三大专题各就其位
- GIVEN references/ 目录
- WHEN 检查推理模型、安全、反模式诊断三类内容的位置
- THEN 三者各自位于独立文件，不混入其他主题文档

#### Scenario: 模板与参考不混放
- GIVEN templates/ 与 references/ 两个目录
- WHEN 检查文件归属
- THEN templates/ 内只有可直接复制使用的产出物，references/ 内只有方法论知识文档

#### Scenario: 开发侧素材不出现在技能内容中
- GIVEN 某技能内容文件
- WHEN 检查其中的链接与引用
- THEN 不出现指向开发侧素材（研究资料等）的链接或引用

### Requirement: SKILL.md 形态
本技能的 SKILL.md MUST 保持极简形态：仅包含内容索引、使用方法（快速决策树）与能力边界清单（提供 / 不提供），MUST NOT 承载方法论正文。

#### Scenario: 正文无方法论正文
- GIVEN 本技能的 SKILL.md
- WHEN 检查正文构成
- THEN 只含内容索引、使用方法与能力边界，方法论内容位于 references/ 与 templates/

### Requirement: 语言与措辞约定
SKILL.md（含 frontmatter 之外的入口正文）MUST 用英文编写，是本技能唯一的英文入口；references/ 与 templates/ MUST 保持中文。description MUST 保留中英双语触发示例。

#### Scenario: 入口与正文语言各归其位
- GIVEN 本技能的 SKILL.md 与 references/ 文档
- WHEN 检查编写语言
- THEN SKILL.md 为英文，references/ 与 templates/ 为中文，description 含中英双语触发示例

### Requirement: 触发语义
本技能的触发面 MUST 覆盖两类请求：(1) 系统提示词或 Agent 指令集的编写与设计请求；(2) 既有 Agent 的指令问题诊断请求——指令冲突、工具过载、安全漏洞。反向条件为：普通一次性提示词（ordinary one-off prompt）编写不触发本技能。

#### Scenario: 诊断请求同样触发
- GIVEN 用户报告某 Agent 存在指令冲突或工具过载问题
- WHEN 判定触发
- THEN 属于本技能触发面，进入诊断路径

#### Scenario: 一次性提示词不触发
- GIVEN 用户只要求写一段单次调用的提示词
- WHEN 判定触发
- THEN 不触发本技能
