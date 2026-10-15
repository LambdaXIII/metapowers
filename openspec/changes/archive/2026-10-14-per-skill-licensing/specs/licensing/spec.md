# Spec Delta

## Purpose

本域定义仓库级许可政策：全局许可证声明的吊销、许可信息的唯一载体，以及各技能许可证选择的登记与变更约束。

## ADDED Requirements

### Requirement: 无全局许可证声明
仓库不设根 LICENSE 文件，不以仓库级声明（README 徽章、根许可证文件等）作为任何技能的许可来源。技能的许可信息唯一载体是该技能 SKILL.md 的顶层 `license` 字段（Agent Skills 开放标准字段）。README 以一句声明将许可指向各技能标注，并说明仓库其他内容（规格、开发文档等）保留所有权利。

#### Scenario: 根 LICENSE 不存在
- GIVEN 仓库根目录
- WHEN 检查是否存在 LICENSE 文件
- THEN 不存在任何根级 LICENSE 文件

#### Scenario: README 不做仓库级许可背书
- GIVEN README.md 与 README.en.md
- WHEN 检查其许可相关表述
- THEN 无 MIT 徽章或等效的仓库级许可声明，许可声明指向各技能 SKILL.md 的 `license` 字段，并包含仓库其他内容保留所有权利的说明

### Requirement: 各技能许可证登记
各技能的 SPDX 许可证选择固定如下，为结构性不变量：

| 技能 | SPDX 标识 |
|---|---|
| skill-master | CC-BY-NC-SA-4.0 |
| rehearsal | CC-BY-NC-SA-4.0 |
| journaling | CC-BY-NC-SA-4.0 |
| agent-prompt-design | MIT |
| skill-exposition | MIT |
| web-deep-research | MIT |
| web-entity-search | MIT |

变更任一技能的许可证须经变更提案流程修订本登记，不直接修改。

#### Scenario: 技能 license 字段与登记一致
- GIVEN 任一技能的 SKILL.md
- WHEN 解析其顶层 `license` 字段
- THEN 字段值为本登记中该技能的 SPDX 标识

#### Scenario: 未登记技能不得发布
- GIVEN 一个不在登记表中的新技能
- WHEN 其进入发布流程
- THEN 其许可证已通过变更提案登记于本表

