# Design

## Context

现状（动机见 proposal.md - Why）：

- 根目录 `LICENSE` 为 MIT，Copyright (c) 2026 Cxalio；README.md / README.en.md 各有一处 MIT 徽章与「许可」节。
- dev 侧 7 个技能中：rehearsal 与 skill-master 顶层 `license: "MIT"`，skill-exposition 顶层 `license: "MIT"`；agent-prompt-design、journaling、web-deep-research、web-entity-search 无 `license` 字段。
- skill-package 规格已有「许可证与 LICENSE 文件」要求，但措辞为「标准**开源**许可证」，对 CC 系列（标准 SPDX 标识但非 OSI 开源许可）存在语义缝隙。
- 发布快照 `skills/` 与 dev 存在既有偏差（如 skill-exposition 快照把 license 写入 metadata），由发布流程在下次发布时从 dev 整体重建。

## Goals / Non-Goals

**Goals:**

- 吊销仓库级 MIT 声明；许可信息唯一载体为各技能 SKILL.md 顶层 `license` 字段
- 7 个技能 dev 侧 license 字段与登记表一致
- 许可证选择登记进 `licensing` 规格，成为结构性不变量
- README 声明简短，不解释开放标准机制（技能标注 license 字段本身即 Agent Skills 开放标准，无需向读者科普）

**Non-Goals:**

- 不改 `skills/` 发布快照（已确认随下次发布重建；快照的既有偏差同样在发布时消除）
- 不为 CC-BY-NC-SA-4.0 附 LICENSE 原文（标准 SPDX 标识，按 skill-package 规格只写字段）
- 不改动 AGENTS.md 的发布流程条款
- 不处理技能内容中除 frontmatter 外的任何文本

## Decisions

1. **CC 标识写作 `CC-BY-NC-SA-4.0`**：SPDX 官方标识符为 `CC-BY-NC-SA-4.0`（连字符分隔），作为 `license` 字段值。CC 官方的「CC BY-NC-SA 4.0」（空格式）是许可证名称的展示写法，不是 SPDX 标识。
2. **skill-package 的措辞改为「标准 SPDX 许可证标识」并列举示例含 CC 系列**：原「标准开源许可证」限定会把 CC-BY-NC-SA-4.0 错误推向「自定义许可证须附原文」分支。只改限定词，两个场景原样保留。
3. **`licensing` 为独立能力而非并入 `skill-package`**：skill-package 定义的是「任一技能包都适用」的通用形态约束；「本仓库各技能选了哪个许可证」是本仓库的登记事实，换一个使用 skill-package 规格的项目结论完全不同，二者生命周期不同，混置会污染通用契约。
4. **登记表用表格而非逐场景**：7 个技能 × 逐场景会产生 7 条重复场景，表格即结构不变量的精确表达；行为面只留两条穷尽性场景（一致、未登记不得发布）。
5. **版本递增与 CHANGELOG**：license 字段变更定级为 patch，五个受影响技能在本变更中直接递增 patch 并定版，CHANGELOG 条目归入新版本节（用户裁定，覆盖「版本号功能完成后再统一确定」的默认纪律）。last_updated 同步置为递增当日。skill-exposition 无变更不递增；skill-master 未发布、无对外版本基线，license 字段照改但不递增版本、不加 CHANGELOG 条目。

## Risks / Trade-offs

- **发布前窗口期**：dev 已吊销 MIT 声明但快照仍带旧 MIT 标注，对外存在短暂不一致。已确认接受，下次发布即消除。
- **NC 条款的商业边界灰色地带**：CC BY-NC-SA 4.0 的「非商业」无精确法律定义，是该许可证的公认弱点；用户已在讨论中知悉并选择接受。
- **README 删除徽章**：外部链接 README 徽章的第三方页面会短暂显示失效徽章，无实质影响。
