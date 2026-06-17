# Changelog


## [1.0.2] - 2026-06-17

### Fixed
- **D-13 frontmatter 元数据类型修正**：`metadata.version` 和 `metadata.last_updated` 从裸值（数字/日期）改为字符串，确保技能运行时解析正确

## [1.0.1] - 2026-06-17

### Fixed
- **D-01 版本声明虚泛**：SKILL.md 适用模型从"Claude 4.x"改为"Claude 4.6+"，匹配实际内容覆盖范围
- **D-02 从零设计主路径缺少安全**：决策树"从零设计"分支增加 safety.md 为必读步骤（安全是设计起点，不是部署终点）
- **D-03 工具术语歧义**：SKILL.md 决策树中"如果需要工具"改为"如果需要定义工具（即 API 函数调用，非业务系统）"；tool-design.md 开头增加术语说明 blockquote
- **D-04 旧模型降级指引**：扩展适用模型段落，明确旧模型用户应参考文件中标注了适用版本的策略
- **D-05 前置依赖循环**：structure-design.md §2.0 增加未选定模型时的 fallback（使用 Markdown 标题）
- **D-06 死引用修复**：model-specific.md:192 `templates.md` → `templates/deepmind-reasoning.md`
- **D-07 决策树分支歧义**："行为异常"与"安全审查"分支之间增加导航注释，安全相关问题先走安全审查
- **D-08 模板自我否定**：deepmind-reasoning.md 明确完整 9 步版不适用于推理模型，增加推理模型导航节指向轻量 4 步版
- **D-09 中文"注入"歧义**：structure-design.md 组件 5 标题从"动态系统信息注入"改为"动态环境信息注入"，增加术语区分 blockquote
- **D-10 检查清单缺回链**：safety.md §8.3 快速检查每项增加 (→ §X.Y) 回链
- **D-12 锚点风格不统一**：记录为已知问题。全文 50+ 处跨文件锚点引用使用中英混合/纯中文/纯英文三种风格，统一需全量回归测试，留待下次专项修复

## [1.0.0] - 2026-06-17

### Added

- 初始版本，基于 RESEARCH.md（18 个来源的调查报告）构建
- **SKILL.md**：入口文件，含内容索引、使用方法决策树、能力边界
- **references/context-engineering.md**：范式转换、注意力预算、正确海拔
- **references/structure-design.md**：分层结构设计、标签选型、8 大组件
- **references/content-writing.md**：五条铁律、Few-Shot、角色定义、输出格式
- **references/reasoning-models-2026.md**：推理模型策略变化、effort 控制、CoT 陷阱
- **references/tool-design.md**：最小可行工具集、工具契约、调用协议
- **references/safety.md**：安全第一阶变量、注入防御、三层边界、Kill Switch
- **references/operations.md**：四支柱、版本管理、回归测试
- **references/anti-patterns.md**：十大反模式 + 诊断流程 + 自查清单
- **references/model-specific.md**：四厂商差异化策略 + 跨模型原则
- **templates/generic-agent.md**：通用 Agent 系统提示词模板
- **templates/deepmind-reasoning.md**：DeepMind 9 步推理模板
- **templates/three-layer-boundary.md**：三层边界框架模板
- **templates/tool-calling-protocol.md**：工具调用协议模板
- **README.md**：设计意图与维护参考（给人读）
- **RESEARCH.md**：原始调查报告（保留溯源）

### Changed

- 原先 `README.md` 作为入口 → 重构为 `SKILL.md` 入口 + `README.md` 设计文档
- 原先 `references/templates.md`（混装）→ 拆分到 `templates/` 四个独立文件
- 原先 `references/safety.md`、`references/model-specific.md` → 大幅扩展重写
