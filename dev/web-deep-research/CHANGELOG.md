# Changelog

## 2.5.1
- description 从纯英文方法论阶段描述改写为中英双触发面（核心名含中文「深度调研」、用户问法「查透/彻底了解/深挖」+ agent 自问双路径，删方法论阶段名），反向限一条（Overkill for simple fact lookups）

## 2.5.0
- workflow.md Phase 0 新增「主题制定」（主题中立、可研究、服务于主会话话题，区分核心关切与支撑性论据）
- workflow.md Phase 3 新增「验证强度 · 来源独立性」（跨领域/语言/地区/利益立场一致是强验证，同机构/作者/引用源头一致是伪验证）
- workflow.md Phase 4 新增「输出形态」选择（完整报告 / 决策简报 / 精选列表）
- workflow.md Quality Checklist 新增「时效覆盖」检查项（素材时间窗是否覆盖目标时间窗）
- SKILL.md「Not for pure advice/opinion questions」改为职责边界「Not a decision-maker」（技能研究主题、不替用户做决定）
- workflow.md Phase 0 产出改为固定四行格式（实体名称/目标清单/初始问题集/范围边界）
- workflow.md Phase 0 新增完成检查（指称/主题/目标/问题集/范围）
- workflow.md Phase 2 澄清「不做真假判断」与来源权威性排序的关系
- workflow.md Phase 3 声明「领域特化规则优先」
- description 补全相位清单（Phase 0/1）与 experience 资料类
- SKILL.md Content Index 新增加载说明（workflow 必读，其余参考与模板选读）
- SKILL.md Delegation 块补充被委派执行者视角（委派已决策，不二次委派）
- workflow.md Q-set「关键纪律」与 Phase 2 候选答案表述冲突修正（候选答案为独立工作产物，不属于 Q 条目）
- workflow.md Phase 3 事实段补充「官方一手自证」规则
- workflow.md Phase 3 数据段补充「单来源但方法可追溯」规则
- workflow.md Phase 4 模板引用补全相对路径（`../templates/report-template.md`）

## 2.4.1
- SKILL.md Content Index 中文残留英文化（workflow.md、search-strategy.md、report-template.md 三行 Purpose/When-to-read 改写为英文）
- report-template.md 行「交叉比对」误译 `cross-references` 改为 `cross-comparison`
- workflow 行措辞「资料不被结论覆盖」改为 `sources stand independent of conclusions`
- web-search-protocol 两条指向不存在技能名的悬空引用清除，改为自足表述（a separate concern）

## 2.4.0
- references/workflow.md 重构为问题驱动的 Q-set 模型（Phase 0 目标拆解为原子问题集、Phase 3 成为消解闸门、停止条件升级为问题前沿稳定化、「不可得」与「收束」明确分离）
- templates/report-template.md「信息空白与遗留问题」贴合 Q 模型（区分仍开放/不可得/被排除的问题）
- SKILL.md 核心机制简介从「追踪线索链」改为「问题集驱动」
- 新增 references/search-strategy.md（选读：执行模式 if 链、报告落盘、多子话题整合、结论回灌）
- SKILL.md Content Index 新增 search-strategy.md 路由行

## 2.3.2
- frontmatter 结构修正（version、last_updated、author 从顶层字段移至 metadata 下级，值均为字符串）

## 2.3.1
- 简介区删除硬编码技能引用，新增委派子代理建议（按上下文依赖程度自判，只传任务描述不转述技能内容）
- 边界声明改为功能描述而非点名

## 2.3.0
- references/workflow.md Phase 0 加载检查从硬编码 2 种文档改为全面检查 Content Index 中所有匹配的领域文档
- SKILL.md Instruction 1 措辞改为复数（any domain references / load all matching ones），消除多领域课题歧义
- references/creative-work.md 新增「类别查询与发现」章节（无具体作品名称的推荐/发现类查询）
- references/workflow.md Phase 0 指称确认新增「无具体实体名称（类别查询）」条目
- references/competitive-research.md「避免深陷单点」增加三条可执行停止信号（来源数量阈值 / 增量价值判断 / 空白优先）
- references/creative-work.md 新增「跨文化/跨市场评价对比」章节
- references/controversial-topics.md「争议真实性」二分法扩展为三种情况（增加「分层争议」）

## 2.2.0
- references/policy-law.md 整体重写（新增法律知识参考与 4 条硬约束、展开条文与元信息查找路径、新增启发参考、常见陷阱精简为 4 条、移除旧五维度叙事结构与旧来源分类）

## 2.1.0
- references/policy-law.md 新增政策与法律研究领域策略（五维度结构、按信息生产者分类来源、Phase 1 身份锁定、按研究目标控深度、法律研究特有验证陷阱）

## 2.0.0
- 从 Hermes 环境技能迁入 metapowers 项目独立开发
- SKILL.md frontmatter 新增 last_updated 与 author（metapowers 约定）
- 新增 references/person-biography.md（公众人物研究领域策略：五维度结构、按信息需求分类来源、Phase 1 身份锁定、按研究目标控深度）
- references/creative-work.md 来源分类从权威层级重构为「信息需求 → 去哪找」
- references/creative-work.md 维度按客观性梯度重组（3 层）
- references/creative-work.md 主观维度（Tier 3）增加约束机制

## 1.1.0
- 新增 references/domain-reference-design-principles.md（领域参考文档原则与自查清单）
- SKILL.md Instructions 调整为领域参考先于 workflow 加载
- Content Index 描述与 when-to-read 指引更新

## 1.0.0
- 初始发布
- 新增 SKILL.md（核心指令与内容索引）
- 新增 references/workflow.md（Phase 0-4 研究工作流）
- 新增 references/creative-work.md（创作类领域参考）
- 新增 templates/report-template.md（研究报告模板）
