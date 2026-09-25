# skill-package Specification

## Purpose

本域定义 metapowers 技能组全体技能共同满足的**包形态契约**：技能包由哪些文件构成、SKILL.md 的入口形态、frontmatter 与 description 的硬性构成、references/ 的组织方式、CHANGELOG 的体例，以及发布快照与开发源的一致性。各技能域的规格约束该技能自身的行为契约；本域约束所有技能共享的形态要求，两者合并构成一个技能的完整契约。

本域的规范性范围是技能组的 7 个成员：agent-prompt-design、journaling、rehearsal、skill-exposition、skill-master、web-deep-research、web-entity-search。经规格变更加入的新技能同样受本域约束。

## Requirements

### Requirement: content/ 文件白名单
技能包内容目录 `content/` MUST 仅包含以下条目：`SKILL.md`、`references/`、`templates/`、`examples/`、`scripts/`，以及条件性存在的 `LICENSE`（见「许可证与 LICENSE 文件」要求）。`content/` 下 MUST NOT 出现任何其他文件或目录。

#### Scenario: 白名单外条目即违规
- GIVEN 某技能的 content/ 目录
- WHEN 列举该目录下的全部文件与子目录
- THEN 每个条目都是 SKILL.md、references/、templates/、examples/、scripts/、LICENSE 之一

#### Scenario: 开发侧文档不得进入 content/
- GIVEN 某技能的开发侧文档（设计记录、变更记录、研究素材等）
- WHEN 检查这些文件的存放位置
- THEN 它们位于 content/ 之外，content/ 内不出现任何对应条目

### Requirement: frontmatter 必须字段与引号规则
SKILL.md MUST 包含 YAML frontmatter。`name`、`description`、`metadata` 是必须字段；`metadata` MUST 包含子字段 `version`、`last_updated`、`author`，并在该技能采用许可证时包含 `license`。`metadata` 下所有子字段的值 MUST 以双引号包围（如 `version: "1.0.0"`、`last_updated: "2026-06-27"`）。

#### Scenario: 必须字段齐备
- GIVEN 任意技能的 SKILL.md
- WHEN 解析其 frontmatter
- THEN name、description、metadata 三个字段齐备，且 metadata 含 version、last_updated、author 子字段

#### Scenario: 无引号值即违规
- GIVEN 某 SKILL.md 的 metadata 写有 `version: 1.0.0` 或 `last_updated: 2026-06-27`
- WHEN 检查 metadata 子字段的取值形式
- THEN 判定违规：子字段值必须写作 `"1.0.0"`、`"2026-06-27"` 形式的双引号字符串

### Requirement: description 触发构成
技能的 `description` MUST 同时满足以下构成：(1) 出现技能核心名的中英双名——用户或 agent 可能用任一语言触发；(2) 触发动词贴近用户首话中实际会说的词，不用完成时态描述；(3) 同时覆盖两条触发路径的词汇命中面——用户主动提问与 agent 完成交付物后的自问；(4) 反向条件（何时不使用）MUST 限制到最关键的一条，展开判定写入 SKILL.md 正文；(5) MUST NOT 指向不存在的独立技能——references/ 下的文件不是独立技能。description 与 SKILL.md 正文 MUST NOT 重复同一信息：description 是加载器的语义匹配面，正文是触发决策依据。

#### Scenario: 单一语言核心名即违规
- GIVEN 某技能的 description 只出现中文核心名（或只出现英文核心名）
- WHEN 检查双名命中面
- THEN 判定违规，中英双名都必须出现

#### Scenario: 误指向不存在的技能即违规
- GIVEN 某技能的 description 写有「→ 用 X 技能」，而 X 不是可独立加载的技能
- WHEN 检查技能指向
- THEN 判定违规，指向只允许指向真实存在的独立技能

#### Scenario: 反向条件堆叠即违规
- GIVEN 某技能的 description 列出多条「何时不使用」的反向条件
- WHEN 检查反向条件数量
- THEN 判定违规，反向条件只保留最关键的一条，其余展开到 SKILL.md 正文

### Requirement: SKILL.md 目录树根为技能自身
SKILL.md 展示技能目录树时，根目录 MUST 是技能自身（如 `my-skill/`），MUST NOT 包含上层磁盘位置（如 `dev/my-skill/content/`、`skills/my-skill/`）。

#### Scenario: 树根不含上层路径
- GIVEN 某 SKILL.md 中展示的技能目录树
- WHEN 定位树的根节点
- THEN 根节点是技能自身目录名，其下直接是包内条目（SKILL.md、references/ 等）

### Requirement: references/ 组织规则
references/ 下参考文档 MUST 遵守以下组织约束：(1) 主文档 MUST 独立成立，MUST NOT 假设读者已读过任何其他文件；特化文档（按场景或载体分类的文档）是对主文档的补充而非替代；(2) 按需加载的参考文档 MUST NOT 绑定使用场景——是否加载由运行时 agent 按具体情况决定；(3) 按载体类型匹配的文档与按情境加载的文档 MUST 分目录存放，MUST NOT 混放；(4) 新增或移除特化文档时 MUST 同步更新主文档的路由表；参考文档的变更 MUST NOT 迫使主文档修改（路由表或引用提示变更除外）。

#### Scenario: 场景文档未注册路由表即违规
- GIVEN 主文档维护有特化文档路由表
- WHEN 新增一个场景文档而路由表未登记它
- THEN 判定违规，路由表与特化文档集合必须一致

#### Scenario: 主文档依赖他文档即违规
- GIVEN 某主文档开头写「如前所述」「基于某某文档的结论」
- WHEN 检查其自包含性
- THEN 判定违规，主文档必须独立成立、不假设读者已加载任何其他文件

### Requirement: SKILL.md 入口化
SKILL.md MUST 承载且仅承载三项职责：(1) frontmatter 的 description 提供加载器语义匹配面；(2) 正文承载展开版触发判定（合触发 / 不合触发 / 边界判定）；(3) 正文路由引导——必读的主方法文档，以及按需参考文档的路由表（文件 / 用途 / 何时加载）。SKILL.md MUST NOT 承载完整的方法论述、执行流程细节或检查清单展开——这些位于 references/ 下的主文档，按需加载。

#### Scenario: 正文混入方法论长文即违规
- GIVEN 某 SKILL.md 的正文包含完整方法论述或执行流程细节
- WHEN 检查入口化职责
- THEN 判定违规，此类内容必须位于 references/ 下的主文档

#### Scenario: 缺触发判定或路由即违规
- GIVEN 某 SKILL.md 的正文只有简介
- WHEN 检查三项职责的落点
- THEN 判定违规，触发判定与路由引导必须在正文中各就其位

### Requirement: 技能独立性
技能的设计与运行 MUST 独立成立：MUST NOT 硬性依赖其他技能、仓库特定文件或运行环境特定信息；MUST NOT 在技能内容中硬编码当前开发环境的路径、工具名等信息。技能之间只 MAY 通过 description 或「与其他技能的关系」互相推荐。

#### Scenario: 硬性依赖即违规
- GIVEN 某技能内容写有「必须先运行 X 技能」或「假设仓库根存在某文件」
- WHEN 检查依赖形态
- THEN 判定违规，技能必须独立运行，技能间只允许推荐关系

#### Scenario: 硬编码环境信息即违规
- GIVEN 某技能内容含本机路径、密钥或特定环境工具名
- WHEN 检查环境绑定
- THEN 判定违规，此类信息不得写入技能内容

### Requirement: 许可证与 LICENSE 文件
采用标准开源许可证（SPDX 常见标识，如 MIT、Apache-2.0、GPL 系列等）的技能 MUST NOT 在 content/ 内放置 LICENSE 文件，仅在 `metadata.license` 标识 SPDX 标识符。采用非标准、自定义或非公开引用许可证的技能 MUST 在 content/ 内包含 LICENSE 文件（许可证原文），并在 `metadata.license` 引用该许可证名称。未选择任何许可证的技能 MAY 省略 `license` 子字段，含义为保留所有权利。

#### Scenario: 标准许可证无需 LICENSE 文件
- GIVEN 采用 MIT 许可证的技能
- WHEN 检查 content/ 与 metadata.license
- THEN content/ 内无 LICENSE 文件，metadata.license 的值为 "MIT"

#### Scenario: 自定义许可证必须携带原文
- GIVEN 采用自定义许可证的技能
- WHEN 检查 content/ 与 metadata.license
- THEN content/ 内存在包含许可证原文的 LICENSE 文件，metadata.license 引用该许可证

### Requirement: CHANGELOG 一句话体例
`CHANGELOG.md` MUST 以 `# Changelog` 开篇，版本号标题（`## <版本号>`）按降序排列；每个版本下每条变更一行，写清哪个对象发生了什么变更。尚未确定版本号的变更 MUST 归入置顶的「未定版」节，版本号确定后归入对应版本标题。CHANGELOG MUST NOT 包含日期、`[Unreleased]` 标记、Keep a Changelog 前言或链接定义，MUST NOT 包含介绍、原因、原理、背景类叙述。

#### Scenario: 条目必须一句话写清对象与变更
- GIVEN 某技能的 CHANGELOG.md
- WHEN 检查其条目
- THEN 每条变更占一行，指明变更对象与变更内容，无任何背景叙述

#### Scenario: 带日期的版本标题即违规
- GIVEN 某 CHANGELOG.md 的版本标题写有发布日期，或以 [Unreleased] 标记未定版条目
- WHEN 检查体例
- THEN 判定违规：版本标题只有版本号且降序排列，未定版条目归入置顶「未定版」节

### Requirement: 发布快照一致性
发布快照 `skills/<name>/` MUST 与开发源 `dev/<name>/content/` 完全一致：不缺少 content/ 中的任何文件，不包含 content/ 之外的任何文件，文件内容逐字节相同。

#### Scenario: 快照与开发源逐文件相同
- GIVEN 发布后的 skills/<name>/ 与对应的 dev/<name>/content/
- WHEN 逐文件比对两个目录树
- THEN 两边文件集合与内容完全相同

### Requirement: 技能组成员
技能组 MUST 恰好包含以下 7 个成员：agent-prompt-design、journaling、rehearsal、skill-exposition、skill-master、web-deep-research、web-entity-search。新技能 MUST 经规格变更更新本条、成为技能组成员之后，才 MAY 初始化其开发目录。哪些技能在组内本身是规格内容，不是惯例。

#### Scenario: 成员清单与规格枚举一致
- GIVEN 仓库中的技能集合
- WHEN 与本条枚举比对
- THEN 两者完全一致，无多余成员、无缺失成员

#### Scenario: 未入规格不得先建目录
- GIVEN 计划新增技能 X，且本条尚未包含 X
- WHEN 检查开发目录
- THEN dev/X/ 尚未初始化，本条更新之后方可初始化
