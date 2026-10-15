# Spec Delta

## MODIFIED Requirements

### Requirement: 许可证与 LICENSE 文件
采用标准 SPDX 许可证标识（如 MIT、Apache-2.0、GPL 系列、CC 系列等）的技能不在 content/ 内放置 LICENSE 文件，仅在顶层 `license` 字段标识 SPDX 标识符。采用非标准、自定义或非公开引用许可证的技能在 content/ 内包含 LICENSE 文件（许可证原文），并在顶层 `license` 字段引用该许可证名称。未选择任何许可证的技能可省略 `license` 字段，含义为保留所有权利。

#### Scenario: 标准许可证无需 LICENSE 文件
- GIVEN 采用 MIT 许可证的技能
- WHEN 检查 content/ 与顶层 license 字段
- THEN content/ 内无 LICENSE 文件，license 字段的值为 "MIT"

#### Scenario: 自定义许可证必须携带原文
- GIVEN 采用自定义许可证的技能
- WHEN 检查 content/ 与顶层 license 字段
- THEN content/ 内存在包含许可证原文的 LICENSE 文件，license 字段引用该许可证
