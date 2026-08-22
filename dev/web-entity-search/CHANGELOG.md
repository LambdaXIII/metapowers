## [1.3.2] — 2026-08-23

### Changed
- **SKILL.md 英文化**: 正文全量英文化（核心流程、委派建议、Content Index 七行表格、Instructions、Capability Boundaries）——实质内容与中文原版逐节对照一致
- **description 补中英双触发面**: 原 description 纯英文（pre-existing 不符合 AGENTS.md §4.6），借英文化补齐——加入中文说明句与中英触发词（「查一下 / 搜索 / 是什么 / 搜一下 / 了解一下」+ what is X? / look up / search for）

## [1.3.1] — 2026-06-17

### Fixed
- **frontmatter 结构修正**：`version`、`last_updated`、`author` 从顶层字段移至 `metadata:` 下级，值均为字符串

## [1.3.0] — 2026-06-18

### Changed
- **工作流下沉**：5 步流程从 SKILL.md 移至 `references/workflow.md`，SKILL.md 保留入口索引和 2 行指令
- **描述瘦身**：description 删除硬编码技能名和触发短语枚举，50 词
- **边界脱钩**：全文中不再出现其他技能的名称——用功能描述代替点名
- **参考资料整合**：模板中"来源"和"扩展线索"合并为一个「参考资料」章节
- 新增委派子代理建议（简介区，`>` 块引用醒目）：简单搜索强烈委派，只传任务描述不转述技能内容
- Content Index 新增 workflow.md 条目


## [1.2.0] — 2026-06-18

### Changed
- **重大结构调整：拆分为 references/（怎么搜）和 templates/（怎么呈现）**
- references/ — 搜索指引、维度表（含必填/选填/关键标记）、避坑规则。Step 2-3 使用
- templates/ — 纯输出结构带占位符（每个 5-12 行）。Step 5 使用
- SKILL.md Content Index 更新为四列表格（实体类型、判断线索、参考文件、模板文件）

## [1.1.0] — 2026-06-18

### Added
- 所有模板维度表新增「必填」列（✓ 必填 / — 选填），与已有的「关键★」列独立
- Step 3 停止条件更新：必填维度全部处理即可停止，选填维度尽力而为

## [1.0.0] — 2026-06-18

### Added
- 初始版本：5 步流程（消歧→分类→逐维填充→置信回检→输出）
- 6 种实体类型模板 + 1 兜底：人物、公司、作品、产品/技术、事件、概念/术语、通用
- 每个模板包含搜索指引、维度表（含关键标记）、输出结构、来源格式
- Content Index 机制（SKILL.md 表格为权威源，流程中不重复枚举）
