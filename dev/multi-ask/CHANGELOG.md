# Changelog

## 未定版

- 初始化技能开发框架（dev/multi-ask/ 目录、CHANGELOG、SPEC）
- SPEC.md：新增技能设计规格
- script-contract.md：新增脚本工件契约（DSL、校验清单、命令行、答卷 JSON、拼装格式）
- scripts/multi_ask.py：新增问卷校验、交互收卷、拼装脚本（validate / show / assemble）
- scripts/multi_ask.py：交互页与拼装答卷不再向用户显示任何 id
- scripts/multi_ask.py：选项行新增 `[x] ` 推荐标记（推荐≠预选，交互页显推荐签但不预勾，推荐不入答卷）
- scripts/multi_ask.py：推荐标识改为行首五角星装饰（不参与排版），内容宽度 +50%，提交条压至 1/3 高且按钮与内容同宽
- scripts/multi_ask.py：交互页视觉重做为暖纸朱砂样式
- SKILL.md：新增技能入口与脚本使用说明
- SKILL.md、script-contract.md：拼装答卷格式同步去除 id 标记，id 可见性约束入契约
