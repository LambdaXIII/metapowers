# Changelog

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
