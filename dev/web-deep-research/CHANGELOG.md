## [2.5.1] - 2026-08-28

非功能调整（Patch）：description 补中英双触发面——核心名含中文「深度调研」、when-to-use 自然措辞（用户问法「查透 / 彻底了解 / 深挖」+ agent 自问「是否值得深挖」），删方法论阶段名（Phase 0-4、clue-chain 等转正文）；修复纯英文方法论描述导致的漏触发。SKILL-DESIGN 记录补中文面决策。

### Changed

- description 从纯英文方法论阶段描述改写为中英双触发面；反向限一条（Overkill for simple fact lookups，对应「不是快速查询」边界）

## [2.5.0] - 2026-08-23

### Added
- **workflow.md Phase 0 新增「主题制定」**：研究的对象是主题而非用户的问题——主题中立（决策型意图转为考察型）、可研究、服务于主会话话题；技能不控制研究启动决策；区分核心关切与支撑性论据（去倾向 ≠ 去维度，核心关切必须保留，支撑性论据可纳入相关维度而非升格为独立目标）
- **workflow.md Phase 3 新增「验证强度 · 来源独立性」**：差异增强（跨领域/语言/地区/利益立场的一致是强验证）与关联削弱（同机构/作者/引用源头/利益/测量方法的一致是伪验证）
- **workflow.md Phase 4 新增「输出形态」选择**：完整报告 / 决策简报 / 精选列表，内部流程不变
- **workflow.md Quality Checklist 新增「时效覆盖」检查项**：素材时间窗是否覆盖目标时间窗

### Changed
- **SKILL.md「Not for pure advice/opinion questions」改为职责边界「Not a decision-maker」**：技能研究主题、不替用户做决定；研究启动是主会话基于上下文的判断，非技能输入闸门
- **workflow.md Phase 0 产出改为固定四行格式**（实体名称/目标清单/初始问题集/范围边界），供跨会话续研恢复上下文
- **workflow.md Phase 0 新增完成检查**（指称/主题/目标/问题集/范围）
- **workflow.md Phase 2 澄清「不做真假判断」与来源权威性排序的关系**（排序属收集策略，非内容判断）
- **workflow.md Phase 3 声明「领域特化规则优先」**：领域文档采信规则优先于通用规则
- **description 补全相位清单（Phase 0/1）与 experience 资料类**，与 workflow 五类资料对齐
- **SKILL.md Content Index 新增加载说明**：workflow 必读，其余参考与模板选读
- **SKILL.md Delegation 块补充被委派执行者视角**：委派已决策，不二次委派

### Fixed
- **workflow.md Q-set「关键纪律」与 Phase 2 候选答案表述冲突**：候选答案作为独立工作产物（含依据 S 编号），不属于 Q 条目
- **workflow.md Phase 3 事实段补充「官方一手自证」规则**：机构对自身信息可低置信度消解，规模数据仍需第三方验证
- **workflow.md Phase 3 数据段补充「单来源但方法可追溯」规则**：与「来源不明数据」区分
- **workflow.md Phase 4 模板引用补全相对路径**（`../templates/report-template.md`）

## [2.4.1] - 2026-08-23

### Changed
- **SKILL.md Content Index 中文残留英文化**: `references/workflow.md`、`references/search-strategy.md`、`templates/report-template.md` 三行的 Purpose/When-to-read 描述由中文改写为英文，语义与中文原意一致

### Fixed
- **`cross-references` 语义偏移**: report-template 行「交叉比对」原误译为 `cross-references`（英文中更常指相互引用，与追踪链索引职责混淆），改为 `cross-comparison`
- **workflow 行措辞**: 「资料不被结论覆盖」→ `sources stand independent of conclusions`，与顶部 Core mechanism 措辞统一（`covered` 原译文可读为「被包含/被遮蔽」两义）
- **`web-search-protocol` 悬空引用清除**: "Not a tool selection guide" / "Not a troubleshooting guide" 两条指向不存在的技能名，改为自足表述（a separate concern）——既消除悬空引用，也符合 SKILL-DESIGN 零跨技能引用约束

## [2.4.0] - 2026-08-23

### Changed
- **问题集（Q-set）模型**：`references/workflow.md` 重构为问题驱动结构——Phase 0 目标拆解为原子问题集，Phase 1/2 循环由开放问题驱动，Phase 3 成为消解闸门（交叉验证通过才消解，单来源不构成完整消解），停止条件升级为「收束 = 问题前沿稳定化」，「不可得」（逐 Q 可得性判定）与「收束」（全局停点）明确分离
- `templates/report-template.md` —「信息空白与遗留问题」贴合 Q 模型：区分仍开放（"还开放"）/不可得/被排除的问题
- `SKILL.md` — 核心机制简介从"追踪线索链"改为"问题集驱动"，与 Q-set 模型一致

### Added
- `references/search-strategy.md`（选读）— 使用层编排策略与内容层分离：执行模式 if 链（完全委派/拆分委派/自执行）、报告落盘、多子话题整合、结论回灌；零跨技能引用、不涉及子代理调用机制
- `SKILL.md` Content Index 新增 `search-strategy.md` 路由行（有能力委派或话题不清晰时读）

## [2.3.2] - 2026-06-17

## [2.3.2] - 2026-06-17

### Fixed
- **frontmatter 结构修正**：`version`、`last_updated`、`author` 从顶层字段移至 `metadata:` 下级，值均为字符串

## [2.3.1] - 2026-06-18

### Changed
- 简介区：删除硬编码技能引用，新增委派子代理建议（`>` 块引用醒目，按上下文依赖程度自判，只传任务描述不转述技能内容）
- 边界声明改为功能描述而非点名


## [2.3.0] - 2026-06-18

### Fixed
- `references/workflow.md` — Phase 0 加载检查从硬编码 2 种文档（creative-work + person-biography）改为全面检查 Content Index 中所有匹配的领域文档
- `SKILL.md` — Instruction 1 措辞从 "any domain reference" / "load it" 改为 "any domain references" / "load all matching ones"，消除多领域课题时的歧义
- `references/creative-work.md` — 新增「类别查询与发现」章节，覆盖无具体作品名称的推荐/发现类查询（如"最近有什么好看的 XX"）
- `references/workflow.md` — Phase 0 指称确认新增"无具体实体名称（类别查询）"条目
- `references/competitive-research.md` —「避免深陷单点」增加三条可执行的停止信号（来源数量阈值 / 增量价值判断 / 空白优先）
- `references/creative-work.md` — 新增「跨文化/跨市场评价对比」章节，覆盖同一作品在不同语言市场中的接受度差异分析
- `references/controversial-topics.md` —「争议真实性」二分法扩展为三种情况，增加「分层争议」（同一话题在不同层面有不同争议性质）

## [2.2.0] - 2026-06-18

### Changed
- `references/policy-law.md` — complete restructure (full rewrite, not incremental fix)
  - **法律知识参考** (new): 法规 vs 政策区分 → 大陆/普通/混合法系 → 中国法律层级表
  - **硬约束** (new): 4 条不可妥协规则 — 条文采信 = 官方原文, 地域匹配, 时效匹配, 三维全部通过才采信
  - **条文与元信息查找** (expanded): 中国按文档类型展开详细查找路径（法律/行政法规/部门规章/地方法规/地方政策/司法解释）；其他管辖区速查表（美/欧/英/日/国际条约）
  - **启发参考** (new): 事件→法规分析思路, 司法解释配套查找, 避免逐条阅读, 纠正错误前提
  - **常见陷阱** (trimmed): 从 7 条精简为 4 条法规特有陷阱（版本混淆/文本≠执行/地方差异/翻译失真），移除通用研究卫生条目
  - Removed: 旧版五维度叙事结构（person-biography 模板不适合法规研究）、旧版来源分类（按信息生产者不适合法规的规范体系逻辑）、研究姿态章节（无信息量的废话）

## [2.1.0] - 2026-06-18

### Added
- `references/policy-law.md` — domain-specific strategies for policy and law research
  - 5-dimension structure: 本体与基本信息 → 核心内容与条款 → 立法背景与目的 → 实施与演变 → 影响与评估｜争议与批评
  - Source classification by information producer (官方来源 / 司法与行政解释 / 学界与评论界 / 行业与商业反应 / 公众与媒体讨论)
  - Identity lock gate at Phase 1 with jurisdiction, issuing body, effective date, status, legal hierarchy
  - Depth control by research goal
  - Verification traps specific to legal research (text vs enforcement gap, version confusion, translation distortion, stakeholder bias)
## [2.0.0] - 2026-06-18

### Changed
- Moved from Hermes environment skills to metapowers project for independent development
- Added `last_updated` and `author` to SKILL.md frontmatter (metapowers convention)

### Added
- `references/person-biography.md` — domain-specific strategies for public figure research
  - 5-dimension structure: 基本信息与标签 → 生平与关键节点 → 人物关系 → 外界评价 → 成果展开
  - Source classification by information need (not authority tiers)
  - Identity lock gate at Phase 1
  - Depth control by research goal

### Fixed
- `references/creative-work.md` — source classification restructured from authority tiers to "information need → where to find"
- `references/creative-work.md` — dimensions reorganized by objectivity gradient (3 tiers)
- `references/creative-work.md` — constraint mechanism for subjective dimensions (Tier 3)

## [1.1.0] - 2026-06-17

### Added
- `references/domain-reference-design-principles.md` — principles and self-check checklist for domain reference documents

### Changed
- SKILL.md Instructions: domain reference loaded before workflow (instruction order)
- Content Index: updated descriptions and when-to-read guidance

## [1.0.0] - 2026-06-15

### Added
- Initial release
- `SKILL.md` — core instructions and content index
- `references/workflow.md` — Phase 0-4 research workflow
- `references/creative-work.md` — creative work domain reference
- `templates/report-template.md` — research report template
