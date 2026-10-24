# skill-grouping Delta

## MODIFIED Requirements

### Requirement: 现行包组 metapowers
本仓库当前声明一个名为 `metapowers` 的技能包组，其 skills 清单恰为以下 5 个技能：journaling、rehearsal、skill-exposition、skill-master、web-deep-research。web-entity-search 与 agent-prompt-design 不属于该组。

#### Scenario: 成员清单与声明一致
- GIVEN skills.sh.json 中 title 为 metapowers 的包组
- WHEN 比对其 skills 清单与本条枚举
- THEN 两者完全一致，无多余成员、无缺失成员
