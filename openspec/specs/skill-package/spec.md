# skill-package Specification

## Purpose

本域定义所有技能在**开发过程中**的包形态规格。每个技能的开发内容位于 `dev/<name>/content/`，本域规定该目录的结构、SKILL.md 的 frontmatter 形态、开发侧 CHANGELOG 的体例与许可证的放置规则。发布快照（`skills/<name>/`）与发布动作不属于本域，其要求记于 AGENTS.md 的发布流程。

## Requirements

### Requirement: 开发包结构
每个技能的开发内容以 `dev/<name>/content/` 为根，目录结构固定如下：

```text
content/
├── SKILL.md         # 必需，技能入口
├── references/      # 参考文档：按需加载的方法论知识
├── templates/       # 模板：可直接复制使用的产出物
├── examples/        # 示例
├── scripts/         # 脚本
└── LICENSE          # 仅采用自定义许可证的技能需要（见「许可证与 LICENSE 文件」）
```

`SKILL.md` 之外的条目按技能实际需要存在，可省略。content/ 下不出现上述结构之外的文件或目录。开发侧文档（设计记录、变更记录、研究素材等）位于 content/ 之外。

#### Scenario: 结构外条目即违规
- GIVEN 某技能的 content/ 目录
- WHEN 列举该目录下的全部文件与子目录
- THEN 每个条目都属于上述结构，无额外条目

#### Scenario: 开发侧文档不进 content/
- GIVEN 某技能的设计记录、变更记录或研究素材
- WHEN 检查其存放位置
- THEN 它们位于 content/ 之外

### Requirement: SKILL.md frontmatter 形态
每个 SKILL.md 以如下形态的 YAML frontmatter 开篇：

```yaml
---
name: "journaling"            # 必需：技能名
description: "..."            # 必需：加载器的语义匹配面
license: "MIT"                # 采用许可证时必需（Agent Skills 开放标准顶层字段）
metadata:
  version: "5.0.4"            # 必需
  last_updated: "2026-06-27"  # 必需
  author: "..."               # 必需
---
```

`name`、`description`、`metadata` 是必须字段；采用许可证的技能含顶层 `license` 字段（Agent Skills 开放标准定义的可选顶层字段，取值规则见「许可证与 LICENSE 文件」），许可证信息不写入 `metadata`。`metadata` 下所有子字段的值以双引号包围。

#### Scenario: 必须字段齐备
- GIVEN 任意技能的 SKILL.md
- WHEN 解析其 frontmatter
- THEN name、description、metadata 三个字段齐备，且 metadata 含 version、last_updated、author 子字段

#### Scenario: 无引号值即违规
- GIVEN 某 SKILL.md 的 metadata 写有 `version: 5.0.4`
- WHEN 检查 metadata 子字段的取值形式
- THEN 判定违规：子字段值写作 `"5.0.4"` 形式的双引号字符串

### Requirement: 开发根即技能根
开发版本中 `dev/<name>/content/` 就是技能自身的根目录。技能内容不把仓库的开发层或发布层路径（如 `dev/<name>/content/`、`skills/<name>/`）表述为技能自身结构的一部分。

#### Scenario: 技能内容不含仓库层路径
- GIVEN 某技能内容中展示的技能目录树或路径引用
- WHEN 定位其根节点或路径前缀
- THEN 根节点是技能自身（或 content/ 内的条目），不出现 dev/、skills/ 等仓库层路径

### Requirement: 许可证与 LICENSE 文件
采用标准开源许可证（SPDX 常见标识，如 MIT、Apache-2.0、GPL 系列等）的技能不在 content/ 内放置 LICENSE 文件，仅在顶层 `license` 字段标识 SPDX 标识符。采用非标准、自定义或非公开引用许可证的技能在 content/ 内包含 LICENSE 文件（许可证原文），并在顶层 `license` 字段引用该许可证名称。未选择任何许可证的技能可省略 `license` 字段，含义为保留所有权利。

#### Scenario: 标准许可证无需 LICENSE 文件
- GIVEN 采用 MIT 许可证的技能
- WHEN 检查 content/ 与顶层 license 字段
- THEN content/ 内无 LICENSE 文件，license 字段的值为 "MIT"

#### Scenario: 自定义许可证必须携带原文
- GIVEN 采用自定义许可证的技能
- WHEN 检查 content/ 与顶层 license 字段
- THEN content/ 内存在包含许可证原文的 LICENSE 文件，license 字段引用该许可证

### Requirement: CHANGELOG 一句话体例
`CHANGELOG.md` 以 `# Changelog` 开篇，版本号标题（`## <版本号>`）按降序排列；每个版本下每条变更一行，写清哪个对象发生了什么变更。尚未确定版本号的变更归入置顶的「未定版」节，版本号确定后归入对应版本标题。CHANGELOG 不包含日期、`[Unreleased]` 标记、Keep a Changelog 前言或链接定义，也不包含介绍、原因、原理、背景类叙述。

#### Scenario: 条目一句话写清对象与变更
- GIVEN 某技能的 CHANGELOG.md
- WHEN 检查其条目
- THEN 每条变更占一行，指明变更对象与变更内容，无任何背景叙述

#### Scenario: 带日期的版本标题即违规
- GIVEN 某 CHANGELOG.md 的版本标题写有发布日期，或以 [Unreleased] 标记未定版条目
- WHEN 检查体例
- THEN 判定违规：版本标题只有版本号且降序排列，未定版条目归入置顶「未定版」节
