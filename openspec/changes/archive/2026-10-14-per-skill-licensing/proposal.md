# Proposal

## Why

仓库当前以根 LICENSE（MIT）作为全局许可证声明，但技能将各自选用不同许可证，全局声明会给未标注技能错误地默认套上 MIT，与实际意图冲突；同时 7 个技能中 4 个缺少 `license` 字段，权利状态未标注。需要吊销全局声明、改为按技能逐一标注，并把各技能的许可证选择固定进规格。

## What Changes

- **BREAKING** 删除根 `LICENSE` 文件，吊销仓库级 MIT 全局许可证声明（仓库其他内容转为保留所有权利）
- README.md / README.en.md：移除 MIT 徽章，「许可」节改写为指向各技能 `license` 字段的简短声明 + 仓库其他内容保留所有权利
- 各技能 dev 侧 SKILL.md 顶层 `license` 字段（Agent Skills 开放标准字段，标准 SPDX 标识只写字段、不附 LICENSE 原文）：
  - skill-master、rehearsal、journaling：`"CC-BY-NC-SA-4.0"`（更严格：署名—非商业—相同方式共享；skill-master 与 rehearsal 从现有 `"MIT"` 改为该值）
  - agent-prompt-design、web-deep-research、web-entity-search：补 `"MIT"` 字段
  - skill-exposition：现值 `"MIT"` 不变
- 五个受影响技能各递增 patch 版本（metadata.version + last_updated），CHANGELOG 以新版本节收一条一句话条目；skill-exposition 无变更、skill-master 未发布，均不递增
- 规格落点：
  - 新增 `licensing` 能力规格：承载仓库级许可政策（无全局许可证声明；各技能的 SPDX 许可证选择为结构不变量，逐一列出）
  - `skill-package` 规格微调：「许可证与 LICENSE 文件」中「标准开源许可证」改为「标准 SPDX 许可证标识」，使 CC 系列等标准标识符的处理（只写字段、不附原文）语义无歧义
- 不改 `skills/` 发布快照：快照随下次发布从 dev 重新拷贝（已与用户确认）

## Capabilities

### New Capabilities

- `licensing` — 仓库级许可政策：全局声明的吊销、各技能 SPDX 许可证选择的登记

### Modified Capabilities

- `skill-package` — 「许可证与 LICENSE 文件」措辞：标准 SPDX 标识涵盖 CC 系列，消除「开源」限定造成的语义缝隙
