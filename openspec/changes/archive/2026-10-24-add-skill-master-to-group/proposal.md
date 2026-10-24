# Proposal: metapowers 包组纳入 skill-master

## Why

skill-master 以 v1.0.3-beta 完成首次发布（用户 2026-10-24 发起），作为技能工作元技能与库内其余技能同属 skills.sh 展示面。分组变更的确认点（AGENTS.md §7）：用户在发布指令中确认 skill-master 登记入 metapowers 包组。

## What Changes

- `skills.sh.json` 的 metapowers 包组 skills 清单 4 → 5：新增 skill-master
- `README.md` / `README.en.md`：skill-master 摘除「（开发中）」标记（英文版为新增条目）、生产级计数 5 → 6、按需安装清单补 skill-master

## Impact

- 受影响规格：skill-grouping（「现行包组 metapowers」Requirement 枚举更新）
- 受影响文件：`skills.sh.json`、`README.md`、`README.en.md`
- 不受影响：`dev/` 下任何技能内容；其余规格
