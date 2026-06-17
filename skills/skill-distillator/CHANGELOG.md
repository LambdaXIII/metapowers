# CHANGELOG


## v1.5 (2026-06-17)

管道硬化：添加硬门（phase gate）、内容身份验证、语言锁定和反模板机制，解决测试中发现的输出形态偏离、身份漂移和语言不一致问题。

### 新增

- [新增] SKILL.md §一：三条新约束——语言锁定、输出形态不可逆转、内容身份保真
- [新增] SKILL.md §三：管道规则（阶段不可跳过、进度声明）、各阶段进入条件与完成标志
- [新增] 所有 phase 文件：`## 进入条件` 头部，声明前置输出要求
- [新增] 所有 phase 文件：`## 阶段完成确认` 尾部，替换原有 `## 质量检查`
- [新增] phase-01 步骤1：语言检测——扫描 SKILL.md 前50行确定主要语言，贯穿全程锁定
- [新增] phase-01 输出格式：`- 语言：zh-CN / en-US / ...`
- [新增] phase-03 步骤1：形态决定后的铁律——多文件判定后禁止降级为单文件
- [新增] phase-03 步骤2：反模板检查——确认章节结构反映技能独特性
- [新增] phase-04 步骤1：身份检查——逐文件确认输出描述的是技能方法论而非技能主题
- [新增] phase-04 步骤1：反模板检查——检查章节结构是否与已蒸馏技能完全相同
- [新增] phase-05：形态合规检查（致命门，最先执行）——验证输出形态与 phase-03 判定一致
- [新增] phase-05 检查维度：身份保真、语言一致性
- [新增] phase-05 输出格式模板：身份保真和语言一致性小节
- [新增] output-structure.md：形态决定的后果说明

### 修改

- [修改] SKILL.md §三：五阶段执行流程从简单加载提示改为含进入条件、完成标志的结构化管道
- [修改] SKILL.md §一：新增 `### 约束` 小节携带三条新增约束

## v1.4 (2026-06-17)

技能探索方式对齐 skill-creator 标准：区分 skill-creator 标准文件与 metapowers 项目追加文件，补全 frontmatter 解析和 templates/ 处理。

### 新增

- [新增] phase-01 步骤1：明确区分 skill-creator 标准文件（SKILL.md、references/、scripts/、assets/）与项目追加文件（README.md、CHANGELOG.md、templates/）
- [新增] phase-01 步骤1：SKILL.md frontmatter 解析——提取 name、description、metadata
- [新增] phase-01 步骤4.6：新增 frontmatter vs body 一致性检查、templates/ 一致性检查、metadata.version vs CHANGELOG 一致性检查
- [新增] phase-01 输出格式：新增"元信息"小节
- [新增] phase-02 步骤2：知识来源扩展——含 SKILL.md frontmatter、templates/、CHANGELOG.md
- [新增] output-structure.md 文件处理规则：SKILL.md frontmatter 和 templates/ 的处理方式与输出位置
- [新增] output-structure.md 边界情况：templates/ 不存在、仅有 templates 无 references、无 CHANGELOG、无 metadata
- [新增] phase-01 质量检查：frontmatter 解析检查项、项目追加文件存在性检查项

### 修改

- [修改] phase-01 步骤1：从简单罗列"读取 SKILL.md、README.md、CHANGELOG.md"改为按标准来源分类说明
- [修改] phase-01 步骤4.6 一致性检查：新增 frontmatter vs body、templates/、metadata vs CHANGELOG 三项
- [修改] phase-01 步骤4.6 裁决策略：新增 frontmatter vs body、SKILL.md vs templates/、metadata vs CHANGELOG 三条裁决规则
- [修改] phase-01 输出格式：源一致性新增 frontmatter vs body、templates/、metadata vs CHANGELOG 三行
- [修改] phase-02 步骤2：知识类型来源从"SKILL.md、references/、examples/"扩展为按文件逐一分类
- [修改] phase-02 输出格式：知识图谱来源列从 examples/ 扩展为含 frontmatter、templates/、CHANGELOG.md
- [修改] output-structure.md 输出形态决策：第三行增加 templates/
- [修改] SKILL.md description：明确"读取技能的 SKILL.md（含 frontmatter）"
- [修改] 版本号从 v1.3 升至 v1.4

## v1.3 (2026-06-17)

项目规范对齐：DESIGN.md 更名为 README.md，与 metapowers 项目 Skill 规范保持一致。

### Changed

- [修改] DESIGN.md → README.md：所有文件内的引用同步更新
- [修改] README.md 标题从“DESIGN”改为与内容匹配的设计文档标题

## v1.1 (2026-04-24)

边界场景增强，基于5种边界场景推演评估。

### 新增

- [新增] 技能类型识别：纯指令型/混合型两类（phase-01 步骤4.5）
- [新增] 源一致性扫描：检查源文件矛盾，定义裁决策略（phase-01 步骤4.6）
- [新增] 知识分布评估：统计知识类型占比，标记分布特征（phase-02 步骤2.5）
- [新增] 类型自适应编排：纯指令型技能合并 core-concepts.md（phase-03）
- [新增] 类型自适应策略：纯指令型授权推断，混合型选择性转换（phase-04）
- [新增] 推断边界定义：可推断/不可推断/兜底规则，统一标注 `[推断: 依据]`（phase-04）
- [新增] 决策规则表转换规范：条件→动作 转为 场景→行为→理由（phase-04）
- [新增] 转换模式4：检查清单 → 定义+检测方法（instructional-to-explanatory.md）
- [新增] 转换模式5：决策规则表 → 场景-行为-理由表（instructional-to-explanatory.md）
- [新增] "清晰则摘取"判断标准：语态/可读性/完整性三维度（instructional-to-explanatory.md）
- [新增] 边界情况：DESIGN.md 存在但内容空洞、references/ > 10个分组（output-structure.md）
- [新增] 源一致性检查维度（phase-05）
- [新增] 类型自适应检查：纯指令型/混合型针对性检查项（phase-05）
- [新增] 单文件输出质量检查模板（phase-05）

### 修改

- [修改] examples.md 无来源时：从"标记为无示例"改为"不生成文件 + README.md 说明"（output-structure.md）
- [修改] L3 检查措辞：从"能按文档执行吗"改为"能理解执行逻辑吗"（phase-05）
- [修改] 智能转换检查项：从2项细化为4项（phase-05）
- [修改] SKILL.md 核心原则：增加"类型自适应"和"推断边界"
- [修改] SKILL.md 操作概要：阶段1增加类型识别和一致性扫描，阶段4增加类型自适应

### 设计决策

- 技能类型简化为两类（纯指令型/混合型），不设"已可读型"
- 推断标注统一为 `[推断: 依据]` 格式
- 推断兜底规则：无法确定时不推断
- DESIGN.md 空洞判断标准：可提取的元认知知识 < 5 条

## v1.0 (2026-04-24)

初始版本，基于最佳实践调查设计。

### 新增

- [新增] 五步执行框架：理解 → 解构 → 编排 → 表达 → 质量检查
- [新增] 技能文件结构：SKILL.md + DESIGN.md + CHANGELOG.md + references/
- [新增] references/frameworks/：8个独立方法论文件
  - 黄金圈法则、冰山模型、5W1H
  - 功能分解、知识类型分析
  - Diátaxis框架、金字塔原理、渐进式披露
- [新增] references/writing/：3个写作指南文件
  - 3C原则、风格指南、指令→说明转换
- [新增] references/output/：输出结构定义
- [新增] references/phases/：5个执行阶段文件
  - phase-01-understanding：理解阶段操作指南
  - phase-02-deconstruction：解构阶段操作指南
  - phase-03-organization：编排阶段操作指南
  - phase-04-expression：表达阶段操作指南
  - phase-05-quality-check：质量检查阶段操作指南
- [新增] 输出文档结构：README + methodology/ + reference/ + meta/
- [新增] 文件处理规则：明确各源文件的处理方式和输出位置
- [新增] 边界情况处理：无 references/、无 examples/、无 DESIGN.md 等情况
- [新增] 质量检查机制：强制阶段，连续两轮无修改停止
- [新增] 智能转换原则：清晰则摘取，指令型则转换，简略则丰富
- [新增] 输出形态决策：仅 SKILL.md 且 <400行 → 单文件；否则 → 多文件

### 设计决策

- 采用多文件目录结构（而非单文件）
- references/ 视角转换（从"Agent参考"转为"人类参考"，保留完整内容）
- examples/ 选择 2-3 个典型示例（而非全部罗列）
- 内容风格从"指令型"转为"说明型"
- 应用 Diátaxis 框架按用户意图组织内容
- 知识拆分到独立 reference 文件，SKILL.md 只保留流程和引用
- 阶段文档独立为 phases/ 文件，包含目标、知识加载、操作步骤、质量检查
- 质量检查作为强制阶段，确保输出可靠性
- 触发规则放在 frontmatter，正文聚焦执行流程
