# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).



## [1.5.0] - 2026-07-19

### Changed

- 第四步从「打分」重设计为「评估整理」——包含五个子步骤：4a 意图对照、4b 发现归类（含实际效果/预期效果/缺陷类型四要素）、4c 严重程度判定、4d 修复优先级与覆盖检查、4e 错误模式提取
- 严重程度格式从 ★ 1-5（默认）改为 阻塞/缺陷/建议（通用格式），仅知识库保留 ★ 1-5 作为跨版本测量工具并显式标注
- 全部 7 个场景文档的 step 4 重构：去除 4a-4e 副标题，改为"参照通用论述 + 载体特有要求"结构，每场景补充 2-3 个载体特有错误模式
- design-doc-rehearsal：原「推演执行」末尾的汇总段提取为独立评估整理节
- doc-guide-rehearsal：通过标准从 ★ 阈值（无 ≤2★）改为阻塞级判定（无 阻塞 级发现）
- rehearsal-guide.md 示例从 ★ 表格改为阻塞/缺陷/建议格式
- 通用论述严重程度格式表、SKILL.md 引用措辞、batch-execution.md 术语全员对齐（打分 → 评估整理/评估维度）
- SKILL-DESIGN.md：决策 #7 从「打分维度的动态选择」重写为「评估整理环节的设计」，从历史叙事改为设计决策说明（为什么不用打分）



## [1.4.0] - 2026-07-08

### Added

- L0 通用论述：新增「0. 作者视角」步骤——推演前以作者身份明确目标读者、设计意图和前置假设
- L0 通用论述：新增「维护者须知」节——记录目录分组理由和开发速记边界
- prompt-instruction-rehearsal：新增「推演前：锁定作者视角」节——提示词场景特化的意图回溯比对
- prompt-instruction-rehearsal：新增「委派推演（推荐）」节——子代理阅读机制和提示词模板

### Changed

- L0 通用论述：「清空」步骤重写为包含身份设定和显式约束声明的操作流程
- prompt-instruction-rehearsal：「清空」重写为「准备与清空」——三步操作（设定身份 → 清空 → 锁定评估者位置）
- prompt-instruction-rehearsal：常见陷阱新增「混淆客体」和「跳过作者视角直接清空」
- doc-guide-rehearsal、interaction-rehearsal、api-design-rehearsal、logic-chain-rehearsal：清空深化为三步（回看作者视角 + 设定阅读身份 + 显式清空）+ L0 引用
- design-doc-rehearsal、knowledge-base-rehearsal：新增清空步骤，适配各自方法结构
- SKILL-DESIGN：新增「文档定位」段，明确本文件与其他文档的边界
- SKILL-DESIGN：移除决策 #5（原版 references 裁剪与迁移）和 #6（原版触发条件的去敏）→ 操作日志移入 CHANGELOG v1.0.0
- SKILL-DESIGN：新增「目录分组」决策（决策 #2）和「开发速记边界」决策（决策 #6）
- SKILL-DESIGN：决策重新排序（按架构→组织→操作→专项），措辞风格约定去芜存菁
- SKILL.md：重写描述为结构化格式——触发条件 + 何时使用（4 场景）+ 何时不使用（3 排除），从内部术语转为面向 agent 的操作语言
- defect-taxonomy：新增 Context Leak（上下文泄漏）缺陷条目——三种子类型的信号识别和修复模式
- L0 作者视角：新增 Context Leak 动机说明——跳过步骤 0 的典型后果
- 修复 5 处 Context Leak 实例：L0 超前引用×2、logic-chain 脚手架残留×1、prompt-instruction 速记泄漏×1、knowledge-base 编号冲突×1
- 版本号 1.3.0 → 1.4.0

## [1.3.0] - 2026-07-08

### Changed

- 移除技能内容中全部 L0/L1/L2 层级代号，改用自然语言表述（必读入口、场景文档、补充参考）
- 参考文件按目录分组：`scenarios/`（7 个场景文档）、`supplementary/`（2 个补充参考）
- SKILL.md 参考区从表格改为分组列表；目录树反映新子目录结构
- `rehearsal-guide.md` 路由表分为「场景路由表」和「补充参考」两段
- 所有文件头部代号替换为自然语言描述；交叉引用路径适配新目录结构
- SKILL-DESIGN.md 术语同步至自然语言表述
- 版本号 1.2.0 → 1.3.0

## [1.2.0] - 2026-07-08

### Added

- 新增 L1 场景文档 `prompt-instruction-rehearsal.md`：提示词/指令集推演，含双重定位原则和内容表达+逻辑执行双层观察框架
- 新增 L1 场景文档 `interaction-rehearsal.md`：交互流程推演，合并 UI + CLI 两种模式
- 新增 L1 场景文档 `api-design-rehearsal.md`：API 接口契约推演，严格限定在接口层面
- 新增 L1 场景文档 `logic-chain-rehearsal.md`：逻辑链路推演，泛化至代码/配置/规则/数据管道

### Changed

- L0 新增「推演者定位」通用原则节
- L0 打分维度表新增逻辑链路载体类型；UI 流程扩展为交互流程
- L0 路由表扩充至 7 个 L1 文件
- SKILL.md 参考文件表和目录树扩展至 10 个文件
- 版本号 1.1.0 → 1.2.0

## [1.1.0] - 2026-07-08

### Changed

- 参考文件按 L0/L1/L2 三级重组：SKILL.md 简化为极简入口（触发条件 + 核心指令 → L0），通用方法迁移至 L0 `rehearsal-guide.md`
- 原 `doc-guide-validation.md` → `doc-guide-rehearsal.md`（L1），移除旧 L1/L3 层级术语
- 原 `design-doc-validation.md` → `design-doc-rehearsal.md`（L1），更新交叉引用文件名
- 原 `knowledge-base-validation.md` → `knowledge-base-rehearsal.md`（L1），旧 L3 术语替换为 L0/L1/L2 体系
- `batch-execution.md`、`defect-taxonomy.md` 分类为 L2，添加 L2 文件头
- 原 SKILL.md 中「与其他方法的区别」「局限」「示例」完整迁移至 L0
- 版本号 1.0.0 → 1.1.0

### Removed

- 空目录 `templates/`、`examples/`、`scripts/`

## [1.0.0] - 2026-07-08

### Added

- 初始版本。从 Hermes `tuiyan` 技能通用化导出。
  - 将中文"推演"方法论重构为通用 `rehearsal` 技能，去除所有平台特化内容
  - 保留核心三元素（客体、载体、链路）和四步流程（清空、逐帧跟、边界刨、打分）
  - 保留嵌入优于收网、边界范围约束等已验证原则
  - 保留打分维度动态选择机制

### Changed

- 触发条件从 Hermes 项目特化重写为通用载体分类
- 子代理执行参考从 `delegate_task` 机制通用化为抽象"并行协作者"模式
- 参考文件迁移与裁剪：
  | 原文件 | 处理 |
  |--------|------|
  | doc-guide-validation.md | 保留，去敏（移除 Steward Agent、Scriptum 引用） |
  | design-doc-validation.md | 保留，去敏（移除 L1/L3 层级引用） |
  | skill-validation.md | 通用化为 knowledge-base-validation.md（去除 Skill 概念） |
  | batch-subagent-execution.md | 保留为 batch-execution.md，去敏（去除 delegate_task） |
  | skill-defect-taxonomy.md | 保留为 defect-taxonomy.md，去敏 |
  | document-qa-pattern.md | 不纳入（内容已被覆盖） |
- 去除 Hermes 项目特定的触发条件条目（Skill 重构验证等），保留通用载体分类触发信号

### Removed

- `document-qa-pattern.md` 参考文件——内容是前 4 个参考文件的英语复述 + 项目记录
- 所有引用 Scriptum、Steward Agent、Hermes 的示例和上下文
- 所有引用 Skill、SKILL.md 等 Hermes 特有概念的内容（在通用文档中替换为"指令集"等术语）
