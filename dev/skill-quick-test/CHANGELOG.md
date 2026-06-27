# Changelog

All notable changes to skill-quick-test will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/).


## [1.4.3] — 2026-06-17

### Changed
- **Context 模板字段标注可选**：execution-light.md 两个模板中的使用场景、模拟背景、入口路径字段增加 `← 可选` 标注，边界测试和错误模式测试可跳过这些字段
- **报告格式嵌入 context 模板**：execution-light.md 两个模板的推演指引中，将松散的自然语言输出描述替换为结构化报告格式。子代理在 context 中直接看到格式规范，无需额外读取 scenario-card.md
- **Baseline 报告格式**：为 baseline 模板设计了专用报告格式（决策路径/困惑犹豫/断裂点/与有技能时的差异），与技能加载单元的报告格式区分
- **委派模拟 → 能力模拟**：将原来只覆盖子代理委派的"委派模拟"扩展为统一的"能力模拟"机制，覆盖三种外部能力：子代理委派（扮演角色）、工具调用（推演结果）、脚本执行（读源码推演逻辑）。SKILL.md、execution-light.md、execution-full.md、scenario-card.md 四处同步更新

### Fixed
- **计划闸门约束升级**：execution-full.md 计划闸门从"建议性"（跳过→质量下降）改为"硬性"（【铁律】…禁止调用 delegate_task），增加子代理完成后的闸门验证步骤

## [1.4.4] — 2026-06-17

### Fixed
- **报告格式提升为硬约束**：execution-light.md 两个模板中，报告格式从"推演指引"内嵌内容提升为独立的"报告格式（硬约束）"节。明确禁止 JSON/纯文本格式，要求每个章节必须出现（即使为空）。解决子代理返回格式不统一的问题
- **Full 模式写入权限覆盖**：execution-full.md 明确说明 Full 模式下 Light 模式的"禁止写入任何文件"约束被替换为"允许写入 reports/ 目录"，消除两处约束的冲突
- **中止检查扩展至启动失败**：execution-light.md 的"委派后中止检查"从仅覆盖"推演中止"扩展为同时覆盖"启动失败"（429、超时等）。SKILL.md 失败行为节同步更新

## [1.4.2] — 2026-06-17

### Added
- **SKILL.md 步骤详解表**：流程概览下方增加各步骤的输入/输出/参考文件表，帮助主代理快速定位
- **Light/Full 差异对照表**：两种模式的适用条件、测试计划、子代理输出、数据来源一表对比
- **呈现原则**：核心约束新增输出控制节，中间步骤不主动展示，只在用户确认节点输出简洁测试用例列表
- **覆盖闸门 + 用户确认**：scenario-design.md 增加步骤 6 引用、覆盖闸门（步骤 2-6 全通过才放行）、用户确认（含预期效果的测试用例列表格式）
- **步骤 5 覆盖标准注释**：明确场景数 ≥ 2 是硬要求，不满足时应补充或说明原因
- **回链**：scenario-design.md、error-patterns.md、execution-light.md、execution-full.md 末尾增加返回主入口链接

### Changed
- **核心约束分类标签**：隔离铁律/加载规则/委派模拟/失败行为各加 emoji 分类标识
- **scenario-card.md 去重**：删除与 execution-light.md 重复的 context 模板（委派提示词），只保留报告格式，context 模板统一指向 execution-light.md
- **scoring-rubric.md 回链修正**：错误的"下一步 → summarization.md"改为"被 summarization.md 步骤 5 调用"
- **summarization.md 步骤 5 措辞**：明确打分是可选步骤，由调用者决定是否执行
- **execution-full.md 报告命名**：明确为 `S01-U1.md` 格式，消除与 test-plan.md 的命名矛盾
- **test-plan.md 命名统一**：`S01-a/S01-b` → `S01-U1/S01-U2`，与 execution-full.md 对齐
- **参考文件索引**：场景设计描述更新为步骤 2-6
- **术语统一**：被测Skill → 被测技能

### Fixed
- **边界测试必须委派子代理**：scenario-design.md 步骤 3 删除"不需要子代理推演"，改为"仍须委派子代理执行，避免主代理的上下文偏见影响结果"。所有测试单元——无论简单或复杂——均须通过独立子代理执行。

## [1.4.1] — 2026-06-17

### Fixed
- **入口路径不再应用于 baseline 单元**：baseline agent 不加载技能，不存在"从哪个文件进入"的问题。入口路径（正门/侧门/回访/引用跳转）仅用于加载技能的单元。
- **scenario-design.md**：等价类表中入口路径标注"仅加载技能的单元"，增加约束说明 baseline 只给"用户想达成什么"不给入口路径；场景卡片入口路径标注"仅 a 单元，baseline 不填"。
- **execution-light.md**：拆分为两个独立 context 模板——技能加载单元模板（含入口路径）和 Baseline 模板（无入口路径、禁止定位技能文件）。

## [1.4.0] — 2026-06-17

### Changed
- **子代理 context 模板重设计**：增加框架声明和硬约束（禁止联网），消除"教义吞噬测试目标"的缺陷
- **推演指引内嵌化**：清空→逐步骤跟随→边界刨直接写入 context，不再依赖外部技能
- **新增"模拟背景"字段**：主代理准备领域知识，子代理据此推演替代真实搜索
- **"目标"改为"用户想达成什么"**：与框架声明对齐，子代理明确测试文档
- **execution-light.md**：context 模板全量重写
- **execution-full.md**：追加文件写入权限说明
- **scenario-card.md**：同步新格式，去 tuiyan 引用
- **SKILL.md**：加载规则去 tuiyan 依赖，子代理资源表清空

### Removed
- **assets/tuiyan-fallback.md**：推演指引已内嵌

## [1.3.0] — 2026-06-17

### Added
- **ISTQB 六步测试设计方法论**：等价类划分 + 边界测试 + 决策逻辑覆盖 + 端到端用例 + 错误模式检查
- **references/scope-analysis.md**：重写为步骤 1，提取输入空间（功能域/路径集/决策点/能力边界）+ 委派需求检测
- **references/scenario-design.md**：重写为步骤 2-5，每步双产出（设计动作 + 覆盖标准）
- **references/error-patterns.md**（新）：步骤 6，13 条反模式清单，随测试经验累积增长
- **委派模拟规则**：测试子代理遇到委派指令时自己扮演被委派角色继续推演
- **assets/tuiyan-fallback.md**：Persona → 使用场景

### Changed
- **Persona 完全移除**：所有文件中的 Persona 概念替换为使用场景（需求明确度/目标类型/背景上下文）
- **模式判定重置**：复杂测试场景 ≥ 2 或总测试数 ≥ 5 → Full
- **覆盖检查闸门化**：从建议变为步骤 2-5 完成后的硬闸门
- **SKILL.md**：流程概览增加覆盖检查和错误模式节点，核心约束重写，参考文件索引更新
- **execution-light.md**：context 模板 Persona→使用场景，增加委派模拟节，适用条件更新
- **execution-full.md**：context 引用和适用条件更新，增加委派模拟引用
- **scenario-card.md**：报告格式去 Persona，路径追踪增加委派模拟标注
- **summarization.md**：增加 📍 归属声明，多单元对比聚焦主 vs baseline
- **test-plan.md**：去掉 Persona 字段

### Removed
- **references/test-design-methodology.md**：中间设计文档，内容已落实到正式文件中

## [1.2.0] — 2026-06-17

### Changed
- 测试策略重设计：Persona → 使用场景，两层策略（简单 + 复杂）
- 模式判定重置、scope-analysis 输出格式、scenario-design 完整重写
- test-plan.md 去 Persona，增简单测试列表
- SKILL/execution/summarization 全量去 Persona

## [1.1.0] — 2026-06-17

### Fixed
- 打分错位：子代理不再打分
- Full 模式计划闸门化

### Added
- 加载规则、失败行为、致命错误检查、推演中止报告格式

## [1.0.0] — 2026-06-17

### Added
- 初始版本
