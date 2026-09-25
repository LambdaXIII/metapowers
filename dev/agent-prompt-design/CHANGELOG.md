# Changelog

## 1.0.4
- description 结构收敛为「what + when-to-use + 反向一条」，触发/不触发场景清单移入正文

## 1.0.3
- SKILL.md 正文全量英文化（内容索引、快速决策树、迭代开发流程、能力边界、适用模型），实质内容与中文原版逐节对照一致
- description 补回三条中文用户首话触发示例（「帮我写个系统提示词 / 这个 agent 需要什么指令 / 设计 agent 的 prompt」），满足中英双触发词不变量
- 删除 SKILL.md「背景资料」节（指向不在发布包内 research/ 目录的 RESEARCH.md 悬空引用）
- 决策树 operations.md「Preparing for production deployment」分支恢复「如需」条件语义（原译文丢失条件性）

## 1.0.2
- metadata.version 与 metadata.last_updated 从裸值（数字/日期）改为字符串

## 1.0.1
- D-01 版本声明虚泛：SKILL.md 适用模型从「Claude 4.x」改为「Claude 4.6+」
- D-02 从零设计主路径缺少安全：决策树「从零设计」分支增加 safety.md 为必读步骤
- D-03 工具术语歧义：决策树改为「如果需要定义工具（即 API 函数调用，非业务系统）」，tool-design.md 开头增加术语说明 blockquote
- D-04 旧模型降级指引：扩展适用模型段落，明确旧模型用户参考文件中标注适用版本的策略
- D-05 前置依赖循环：structure-design.md §2.0 增加未选定模型时的 fallback（使用 Markdown 标题）
- D-06 死引用修复：model-specific.md:192 的 `templates.md` 改为 `templates/deepmind-reasoning.md`
- D-07 决策树分支歧义：「行为异常」与「安全审查」分支之间增加导航注释（安全问题先走安全审查）
- D-08 模板自我否定：deepmind-reasoning.md 明确完整 9 步版不适用于推理模型，增加指向轻量 4 步版的导航节
- D-09 中文「注入」歧义：structure-design.md 组件 5 标题改为「动态环境信息注入」，增加术语区分 blockquote
- D-10 检查清单缺回链：safety.md §8.3 快速检查每项增加回链
- D-12 锚点风格不统一：全文 50+ 处跨文件锚点引用中英混合三种风格，记录为已知问题留待专项修复

## 1.0.0
- 初始版本，基于 RESEARCH.md（18 个来源的调查报告）构建
- 新增 SKILL.md 入口文件（内容索引、使用方法决策树、能力边界）
- 新增 references/context-engineering.md（范式转换、注意力预算、正确海拔）
- 新增 references/structure-design.md（分层结构设计、标签选型、8 大组件）
- 新增 references/content-writing.md（五条铁律、Few-Shot、角色定义、输出格式）
- 新增 references/reasoning-models-2026.md（推理模型策略变化、effort 控制、CoT 陷阱）
- 新增 references/tool-design.md（最小可行工具集、工具契约、调用协议）
- 新增 references/safety.md（安全第一阶变量、注入防御、三层边界、Kill Switch）
- 新增 references/operations.md（四支柱、版本管理、回归测试）
- 新增 references/anti-patterns.md（十大反模式、诊断流程、自查清单）
- 新增 references/model-specific.md（四厂商差异化策略、跨模型原则）
- 新增 templates/generic-agent.md（通用 Agent 系统提示词模板）
- 新增 templates/deepmind-reasoning.md（DeepMind 9 步推理模板）
- 新增 templates/three-layer-boundary.md（三层边界框架模板）
- 新增 templates/tool-calling-protocol.md（工具调用协议模板）
- 新增 README.md（设计意图与维护参考）
- 新增 RESEARCH.md（原始调查报告，保留溯源）
- 入口从 README.md 重构为 SKILL.md 入口 + README.md 设计文档
- references/templates.md（混装）拆分到 templates/ 四个独立文件
- references/safety.md 与 references/model-specific.md 大幅扩展重写
