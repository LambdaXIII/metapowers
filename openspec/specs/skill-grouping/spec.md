# skill-grouping Specification

## Purpose

本域定义技能包组的声明形态与本仓库现行的包组。技能包组通过仓库根的 `skills.sh.json` 声明，用于 skills.sh 发布站点的分组展示。存在包组不代表所有技能都必须登记入组，也不排除未来声明其他包组；新增技能是否入组经确认后更新（流程见 AGENTS.md）。

## Requirements

### Requirement: 包组以 skills.sh.json 声明
技能包组通过仓库根的 `skills.sh.json` 声明：每个包组是 `groupings` 数组的一个条目，含 `title`、`description` 与 `skills` 成员清单。未登记进任何包组的技能不出现在 `groupings` 中。

#### Scenario: 包组信息与声明文件一致
- GIVEN 仓库中的技能包组集合
- WHEN 解析 skills.sh.json 的 groupings
- THEN 每个包组的标题、描述与成员清单与声明文件完全一致

### Requirement: 现行包组 metapowers
本仓库当前声明一个名为 `metapowers` 的技能包组，其 skills 清单恰为以下 5 个技能：agent-prompt-design、journaling、rehearsal、skill-exposition、web-deep-research。skill-master 与 web-entity-search 不属于该组。

#### Scenario: 成员清单与声明一致
- GIVEN skills.sh.json 中 title 为 metapowers 的包组
- WHEN 比对其 skills 清单与本条枚举
- THEN 两者完全一致，无多余成员、无缺失成员
