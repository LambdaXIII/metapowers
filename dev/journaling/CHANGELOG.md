# Changelog




## [4.8.0] — 2026-06-29

> Base: v4.7.0. 合约同步——合约内容随技能版本迭代自动同步，防止已部署合约停滞在旧版。

### Added
- **已有合约检测**：`design-discovery-contract.md` 新增「已有合约的检测」节——初始化时先检测是否已有合约，按四维度比对最新模板，支持三种结果分支（有差异→更新建议 / 匹配→报告最新 / 未找到→正常流程）
- **合约合规检查**：`protocal-maintenance.md` Phase 0 新增 Step 11 合约过期扫描 + Phase 1 P1-S1 新增合约审查维度（启动措辞强度/读 INDEX 理由具体性/写操作范围完整性/拼写语法，共四个维度五种判定标准）
- **有意冗余的显式注释**：`design-discovery-contract.md` Step 3 新增冗余说明——contract 与 INDEX.md 协议声明行的重叠是设计选择

### Changed
- **design-discovery-contract.md Step 3**：新增格式适配声明——合约模板的 `>` 是展示格式非强制要求，实际写入需适配载体格式；从零创建时使用模板格式
- **protocal-init.md Phase 3**：新增「合约已存在的情况」分支——不重复设计，按四维度评估是否需要更新

## [4.7.0] — 2026-06-29

> Base: v4.6.0. Description 重写为约束行格式 + 正文新增信息依赖声明。

### Added
- **信息依赖声明**：SKILL.md 正文 "Before You Begin" 节——声明技能协议依赖 INDEX.md 上下文（维护信号、活跃工作区、经验陷阱），用信息缺口驱动而非命令
- **INDEX.md 价值行**：seed 模板新增"跳过意味着在信息盲区中操作"行
- **spec-index.md Protocol Declaration 第六项**：Value self-description（可选推荐）

### Changed
- **SKILL.md description 重写**：从枚举场景式（Triggers + Do NOT load）改为约束行格式——"在任何写入性操作前必须加载" + 写入操作示例。移除对 reading 的错误声称
- **design-discovery-contract.md Step 3、protocal-init.md Phase 3 回退方案**：启动指令从「首先读取」强化为「第一步」+ ⚠️ + 价值说明

### Removed
- **description 中的 Do NOT load for 段**：被约束行中的「无需为仅读取 journal 内容而加载」负边界取代
- **description 中的 Triggers 枚举段**：被「写入操作示例」取代（从白名单降级为澄清示例）

## [4.6.0] — 2026-06-29

> Base: v4.5.1. 删除操作重新定义为 archive——journal 中不存在直接删除，所有删除行为实际是 mv to archive/。

### Added
- **"删除即归档"原则**：删除操作重新定义为 `mv to archive/`，禁止直接删除 journal 文件。Operating Principles 新增此原则，旧 "Search before bulk deletion" 移除。

### Changed
- **"不请求许可"原则收紧**：仅可逆操作（archive、tag merge、reorganization）不需要审批。不可逆操作（hard deletion）需用户确认或遵守维护协议条件。
- **protocal-maintenance.md**: Phase 0 新增 Step 10 扫描 archive/；Phase 1 P1-S1 新增 archive 审查维度（恢复/保留/可硬删除三判定 + 冷却保护）；Phase 2 P2-S3 入口新增保护声明（本轮新 archive 内容禁止硬删除）；Phase 2 新增 P2-S9 执行 archive 清理。
- **protocal-init.md Phase 3 回退方案、design-discovery-contract.md Step 3 推荐方案**：写入操作增加举例（移动、修改、编写、删除等）。
- **templates/seed/INDEX.md、spec-index.md**: 协议声明行同步扩展。

### Fixed
- **inbox/README.md**: 处理节奏 "已过期/无用 → 删除" 改为 "→ 移入 archive"。


> Base: v4.4.0. 新增 CONVENTIONS 机制——可选设计模式实例注册，联通 patterns/ 设计参考和 protocol/ 操作流程。

### Added
- **`references/spec-conventions.md`**: CONVENTIONS.md 的设计原则与操作建议。三条核心原则（不重复技能规范、不与技能冲突、参考 spec-note 风格）和各协议关系。
- **`templates/seed/CONVENTIONS.md`**: 最小化种子模板，供维护中首次创建时参考格式。

### Changed
- **`protocal-write.md`**: 新增 "Before Writing: Check Journal Conventions" 节——写入前最后一步加载 CONVENTIONS.md（若存在），检查是否命中 scope。
- **`protocal-import.md`**: 新增 P2-S5 "检查 Journal Conventions"——P3 执行前加载 CONVENTIONS.md。P3 入口增加 convention 后续操作提示。
- **`SKILL.md`**: Linked Files 和场景表新增 spec-conventions.md 和 templates/seed/CONVENTIONS.md 条目。
- **`SKILL-DESIGN.md`**: 新增决策 #13 CONVENTIONS 机制。

## [4.5.1] — 2026-06-29

> Base: v4.5.0. 维护协议重设计——五阶段结构对齐新流程，三规则平等对待，涟漪修正 11 文件。

### Changed
- **`protocal-maintenance.md`**: 五阶段重设计。Phase 1 改为审查→设计→定规→计划四步（P1-S1/2/3/4，三规则平等参考），P1-S1 新增格式审查；Phase 2 执行先改三规则再改条目（P2-S1→S8）；Phase 3 双向质量检验（P3-S1 回顾微调 + P3-S2 条目验证）；Phase 4 Step 1 改为 INDEX.md 全量重写（按 spec）。Phase 0 新增 Step 9 收集 convention 数据。
- **`protocal-write.md`**: "Before Writing: Check Journal Conventions" 改写为 "Before Writing: Check Journal Rules"，三规则平等提及+各自要求。
- **`protocal-import.md`**: P2-S3/S4/S5 合并为统一 P2-S3 "检查 Journal Rules"，三规则平等加载。
- **`spec-index.md`**: 移除 "Relationships" 节和 "Self-management reference" 子弹。修复 "Recommended Organization" 中旧 Phase 引用。
- **`templates/seed/INDEX.md`**: 移除 self-management reference 行。
- **`examples/journal-standards/INDEX.example.md`**: 同上移除 self-management reference 行。
- **`protocal-init.md`**: 发现链图示更新，移除 INDEX.md 对 CLASSIFICATION/TAGS 的引用。
- **`design-tags.md`**: 维护引用更新为 P1-S3。移除 "INDEX.md 的协议声明行指向它" 过时关系表述。
- **`design-classification.md`**: 移除 "INDEX.md 的协议声明行指向它" 过时关系表述。
- **`spec-conventions.md`**: "最后一步加载" → "与其他规则文件一起前置加载"，协议关系表同步更新。
- **`SKILL.md`**: Linked Files 维护协议描述更新，版本号 4.5.0 → 4.5.1。

- **`SKILL-DESIGN.md`**: 决策 #2 重写（新五阶段）、新增决策 #14（三规则平等）/ #15（设计目标先行）/ #16（双向检查）/ #17（跨版本防格式漂移）。决策 #13 描述微调（与 #14 对齐）。
## [4.4.0] — 2026-06-29

> Base: v4.3.2. Phase 3 设计发现合约拆分为两层——协议保留"方案讨论"概览（载体类型、核心任务），详细发现流程独立为新参考文件。

### Added
- **`references/design-discovery-contract.md`**: 发现合约设计的系统化四步流程——Step 1 清查 / Step 2 评估 / Step 3 推荐 / Step 4 呈报。含三类注入机制清查清单、三问题过滤评估表（带示例）、推荐方案构成模板、用户呈报模板。

### Changed
- **`protocal-init.md` Phase 3**: `### 合约发现流程`（完整 Step 1-4）→ `### 方案讨论`（载体概览 + 核心任务概述 + 引用链接）。`### 回退方案` 整理为有序列表。
- **SKILL.md**: Linked Files 和场景表新增 `references/design-discovery-contract.md` 条目。
- **SKILL-DESIGN.md 决策 #7**: Phase 3 演化记录从"替换"更新为"协议流与参考分离"。

## [4.3.2] — 2026-06-29

> Base: v4.3.1. 修正上一版本的错误合并——`patterns/` 不应是独立顶层目录，应是 `references/` 的子目录。还原 dashboard 的推荐模式定位。

### Added
- **`references/patterns/dashboard.md`**: 恢复 `references/patterns/` 子目录结构。dashboard 作为推荐模式（非硬规范）存放在此。

### Changed
- **SKILL.md 引用路径**: `references/dashboard.md` → `references/patterns/dashboard.md`（Linked Files 两处 + 场景表一处）。
- **SKILL-DESIGN.md `patterns/` 节**: 从"已合并至 references/"重写为"references/patterns/ 子目录设计说明"。
- **protocal-maintenance.md、spec-index.md 引用路径**: `references/dashboard.md` → `references/patterns/dashboard.md`。

### Removed
- **`references/dashboard.md`**: 扁平位置的 dashboard 参考文件已移除（移至 `references/patterns/`）。




## [4.3.1] — 2026-06-27

> Base: v4.3.0. `patterns/` 目录合并至 `references/`，修正非标准技能结构。所有引用路径同步更新。

### Changed
- **`patterns/dashboard.md` → `references/dashboard.md`**: 移至标准 `references/` 目录。更新 SKILL.md、README.md、protocal-maintenance.md、spec-index.md 中全部引用路径。

- **`patterns/` 目录**: 合并后删除。README.md 中原 `## patterns/ 目录` 节替换为合并说明。

## [4.3.0] — 2026-06-27

> Base: v4.2.0. Import protocol redesigned from 6-step English procedure to full 3-phase Chinese protocol with REJECT/SUSPEND control flow. README expanded with design decisions #8-#12.

### Redesigned
- **`protocal-import.md` 全篇重写**：6 步英文指令 → 三阶段中文协议（P1 准入判断 / P2 策略判断 / P3 执行）。新增 REJECT/SUSPEND 控制流信号、用户交互式暂停机制。删除 import 的 write-style adaptation 步骤（adjust body、proceed）。

### Added
- **`README.md` 设计决策 #8-#12**：Protocol 操作模式分化（远征型/内嵌型）、目标前置、理解验证≠质量检查、加法胜于减法、模板分离时机。
- **`protocal-write.md` 定位节**：目标前置风格的开端描述，定位为内嵌型协议。
- **`protocal-maintenance.md` 目标节 + 理解验证提示 + 加法模式提示**：远征型协议完成状态描述，Phase 0→1 边界理解验证，Phase 2 加法操作模式。
- **`design-tags.md` 约定标签（Seed Tags）子节**：文档化 `imported` 标签含义、生命周期和角色。
- **`templates/seed/TAGS.md` `imported` 标签**：注册种子标签。

### Fixed
- **`protocal-import.md` P3-S2 步骤编号引用错误**：P2-S3→P2-S4（frontmatter 验证）、P2-S4→P2-S2（摘要来源）、P2-S3→P2-S4（标签来源）。

### Removed
- **`protocal-import.md` 设计泄漏**：总体要求安全设计理由说明、P1-S0 注释规则设计哲学。

## [4.2.0] — 2026-06-27

> Base: v4.1.1. 发现链从附录提升为目标态展开——明确它是三阶段初始化的共同保证效果，而非 Phase 3 的附属信息。

### Changed
- **`protocal-init.md` 发现链定位修正**：从"附录：发现链（信息参考）"移至初始化目标 → 可发现态，作为三阶段共同保证的链路展开。不再是"仅作参考"。
- **`design-tags.md` Type Identification 措辞修正**："此行首" → "这些标识"。
- **`protocal-init.md` 补充占位符替换提示**：复制种子文件后替换 INDEX.md 中的 YYYY-MM-DD 和 <初始化原因>。

All notable changes to the journaling skill.



## [4.1.1] — 2026-06-27

> Base: v4.1.0. Init protocol restructure — move from bloated 7-step flow to clear 3-phase structure with type identification.

### Redesigned
- **`protocal-init.md` 全篇重写**：7 步流程 → 三阶段（确定位置 / 初始化内容 / 设计发现合约）。Pre-check 分支逻辑并入 Phase 2 通用检查流程。移除"设计模式"和 bootstrap entry。种子目录不再主动创建——由写入操作按需催生。Phase 3 标记为"禁止自行执行"。

### Added
- **`templates/seed/`**：三个种子文件模板（INDEX.md、CLASSIFICATION.md、TAGS.md）。协议不再内嵌初始模板——引用此目录取用。`seed/` 子目录强调版本身份，文件名不加前缀——复制使用时无需改名。
- **`spec-index.md` — `What is INDEX.md?`** 节：包含 Role、Type Identification 和与其他骨架文件的关系。
- **`design-classification.md` — `What is CLASSIFICATION.md?`** 节：同上。
- **`design-tags.md` — `What is TAGS.md?`** 节：同上。

### Changed
- **`README.md` Section 7**：从"最小种子 + 设计模式"重写为"三阶段明确分工"。
- **`SKILL.md` Linked Files**：新增 `templates/seed/` 引用行，Journal Initialization 描述更新。


## [4.1.0] — 2026-06-26

> Base: v4.0.0 (last committed). All intermediate versions (4.1.x–4.3.x) were uncommitted session artifacts — consolidated here.

### Redesigned
- **`README.md` 完整重写**：从"技能维护参考"重新定位为"独立的设计锚定文档"（不被运行时加载）。结构从 10 节精简至 7 条真实设计决策。删除闸门模型、虚构的七执行锚点、已删除文件的幽灵残留。修正 12 处事实错误。
- **`SKILL.md` Operating Rules → Operating Principles**：12 条行为指令 → 6 条设计原则，每条以设计决策为根。人称统一为"你"。移除的规则重分配到 reference 文件。
- **Journal 概念重新定义**：Journal 是 Agent 的长期记忆笔记本，不是项目日志。读不需要加载 skill。四种子目录（inbox/experience/knowledge/active_works/）。
- **`patterns/dashboard.md` 重写**：从 INDEX 板块模式 → 项目/领域级次级 INDEX 设计参考。
- **`.maintenance-memo.md` 生命周期重新设计**：初始化不创建空文件。Phase 0 不清空——Phase 4 完成后清理。`protocal-write.md` Maintenance Signals 是日常写入 memo 的入口。

### Added
- **`references/spec-note.md`** — 笔记编写指南，从 protocal-write 独立。
- **`patterns/dashboard.md`** + **`patterns/` 目录**。
- **`protocal-write.md` Maintenance Signals**：日常操作通向维护循环的 memo 写入入口。
- **`protocal-maintenance.md` Phase 4 Step 4**、Phase 0 memo 上下文段落、技能升级触发信号。
- **`examples/classification-systems/`**、**`references/design-classification.md`**、**`references/design-tags.md`**、**`references/spec-frontmatter.md`**、**`examples/journal-standards/`**。

### Changed
- **闸门引用清理（6 文件 23 处）**：闸门概念从 journaling 设计层移除。替换为 agent operating rule / custom section tables / self-regulation rules。
- **`protocal-write.md` 精简**：纯工作流程，格式指南移至 spec-note.md。
- **`spec-index.md` 重组**：核心规范 = 协议声明 + 设计原理。
- **维护协议重写**：五阶段框架、信号合并优先级。
- **`protocal-init.md` 步骤重编号**：Step 5→4, 6→5, 7→6（删除 Step 4 创建空 memo）。
- **`protocal-import.md`** 增加 tagging 检查。
- **读/写非对称明确化**：读取 INDEX.md 不需要加载 skill。

### Removed
- **闸门概念从 journaling 设计层移除**（CHANGELOG 历史记录保留）。
- **`README.md` §9 "七执行锚点"**、**§10 "内存定位"**。
- **`protocal-init.md` Step 4 "创建维护备忘录"**。
- **DAILY-OPS 文件** → 拆分为 protocal-write + spec-note。

### Fixed
- **C4 敏感信息验证**：0 泄露。
- **memo 鸡和蛋问题**：protocal-write.md Maintenance Signals 解决——日常写条目时即可了解并写入 memo。

## [3.3.0] — 2026-06-25

### Redesigned
- **14 reference files → 7**: Removed 4 non-journaling files (concept-vs-operation, doc-crossref, environment-migration, cross-instance-sync). Merged 3 content-overlapping files (design-principles + memory-layer-strategy + two-gate-model → journal-concept; dashboard-design-principles → index-spec). Result: 7 single-responsibility references.
- **journal-concept.md (new)**: Design philosophy document — definition, 7 execution anchors (preserved anchor #1-#7 numbering), mechanism mapping, memory positioning (generalized), gate design theory. Single source for all "why".
- **index-spec.md restructured**: Added Design Principles section (6 principles table), inline-injected derivations into each section, added Workspace Dashboard Pattern and REAP/推演 methodology appendix. Decoupled AGENTS.md → "project entry point".
- **daily-ops.md strengthened**: Added gate design rationale before Action Gate Scanning Procedure. Added timing protocol rationale to Decision Capture section. All tool names decoupled (search_files/read_file/session_search/patch → generic Chinese descriptions).
- **SKILL.md updated**: Linked Files reduced to 7 references. Scenario table reduced to 7 rows matching the 7 references. Version → 3.3.0.

### Removed
- design-principles.md, memory-layer-strategy.md, dashboard-design-principles.md, two-gate-model.md — content absorbed into journal-concept.md, index-spec.md, and daily-ops.md.
- concept-vs-operation.md, doc-crossref.md, environment-migration.md, cross-instance-sync.md — not journaling-related.

### Fixed
- **initialization.md**: Removed `~/.hermes/jornal/` (framework-specific). Kept `~/.agents/jornal/` as universal discovery convention. Added non-default path note explaining framework config requirement. Replaced HERMES_HOME with AGENT_DATA_DIR.
- **maintenance.md**: Decoupled search_files references to generic descriptions.
- **note-spec.md**: Cross-reference fixed (design-principles.md → journal-concept.md).
- **README.md**: Updated AGENTS.md reference (→ "project entry point") and outdated file name.

### Changed
- **daily-ops.md** line 136: Cross-reference updated from design-principles.md to journal-concept.md.
- **daily-ops.md** traces: Tool names replaced with generic action descriptions (搜索, 搜索会话记录, 读取文件, 编辑工具).
- **index-spec.md**: AGENTS.md → "project entry point" in scope routing table.

---

## [4.0.0] — 2026-06-25

### Redesigned
- **initialization.md rewritten**: Discovery contract model replaces 5-step search chain. Step 0-7 structure: Step 0 (confirm journal root), Step 1 (directory structure), Step 2 (initial index.md), Step 3 (establish discovery contract — meta-instructions + startup protocol separated), Step 4 (maintenance memo), Step 5 (tag registry), Step 6 (bootstrap entry), Step 7 (verify). Carrier identification criteria (3 standards), insertion guidance, verification criteria, fallback paths, and self-test.
- **index-spec.md restructured**: Added design philosophy (dynamically loaded prompt system). "The Six Sections" → "Sections". Protocol Declaration expanded from 3 to 4 items (added maintenance trigger hints with action prompt + optional journal root). Action Gate and Write Gate demoted from required sections to optional examples. Appendix deleted. Behavioral Gate max 9 rule added.
- **daily-ops.md dissolved**: File deleted. Content absorbed into note-spec.md (Before Writing, After Writing, Before Delivery, Over-generalization guard), SKILL.md Operating Rules (Decision Capture tiers + Trace-back), and maintenance.md (Cascade Rename).
- **note-spec.md integrated**: Complete write procedure in reading order — Before Writing (triage), Importing Existing Content (copy → modify copy → never touch source), Supplementing Existing Entries (same-session vs cross-session), Frontmatter, Summary Anchoring, Body (over-generalization + shelf life), Granularity, Directory, Lifecycle, After Writing (update index.md), Before Delivery (self-check).
- **journal-concept.md expanded**: Added "Dynamic Prompt System" section (3-layer model: index.md → notes → skill).

### Removed
- **daily-ops.md**: Content absorbed into note-spec.md, SKILL.md, and maintenance.md.

### Changed
- **Startup Protocol slimmed**: 从 41 行（身份声明 + 记忆协调表 + Reading/Writing 四节）精简至 11 行。保留三要素：journal 是什么、为什么必须读、位置在哪。写入指引交给 index.md 协议声明行，不再重复。
- **initialization.md Step 0**: 新增 Pre-Check 决策树，覆盖 5 种目标路径状态（不存在/空/有协议声明index.md/无协议声明index.md/无index.md但有内容）。核心约束：绝不覆盖现有内容，不确定时向用户展示发现。
- **README.md**: Updated description of initialization template (六节骨架 → four core sections, gates not pre-populated).
- **Cross-references**: All daily-ops.md references removed from current files. Decision Capture + Trace-back relocated to SKILL.md Operating Rules. Cascade Rename relocated to maintenance.md.

### Fixed
- **maintenance.md vs note-spec.md tag rule contradiction**: maintenance.md Phase 3 Step 4 要求"每条至少一个项目标签 + 活动标签"，与 note-spec.md "活动标签或元标签至少一个，项目标签可选"矛盾。统一为 `activity tag or meta tag, project tags optional`。
- **bootstrap entry 使用未注册标签**：initialization.md Step 6 模板 `tags: [journaling, meta]` 中两个标签均不在 tag-registry 中。改为 `[journal, skill]`。

---
## [3.2.1] — 2026-06-25
### Fixed
- **initialization.md Prerequisites rewritten**: "Check the framework's configuration" (a hanging reference for zero-context agents) replaced with a 4-step decision process: (1) check for existing journal, (2) check framework env vars/config, (3) choose stable location by constraints, (4) confirm with user if uncertain. Includes platform-specific path examples and a "Record the Path" section that mandates writing the journal root into index.md protocol declaration and bootstrap entry.
- **initialization.md index.md template**: Added `Journal root: <chosen-path>` line to the protocol declaration block.
- **initialization.md Phase 6 verify**: Added check items for journal root recording in index.md and bootstrap entry.
- **initialization.md Post-Initialization**: Added "How Future Sessions Find the Journal" section explaining the discovery loop.
- **daily-ops.md Session Startup**: Added pre-check guard — if journal root is unknown, redirect to initialization.md discovery process before proceeding. Resolves the "no initialization guard" defect (agents entering via daily-ops.md with no existing journal hit a dead end).

---

## [3.2.0] — 2026-06-25

### Redesigned
- **Pitfalls → Operating Rules**: 12 pitfall entries rewritten as 8 directive rules. Historical case溯源 (dates, skill names, specific incidents) removed — the lessons are absorbed into the rules, the cases belong in journal entries. 4 pitfalls relocated: concept-vs-operation pointer removed (reference is self-describing), gate-rule cap audit moved to maintenance.md, recent-changes trim moved to daily-ops.md, write-gate forced-scan note moved to daily-ops.md and index-spec.md.
- **Write gate repositioned as living document**: index-spec.md Section 6 no longer prescribes specific self-questions. Instead it defines the design framework — the Agent creates and updates the gate content in index.md based on actual memory pollution failures. daily-ops.md "Before Writing to Memory or User Profile" section rewritten to reference the journal's living gate rather than reproducing fixed content. maintenance.md Phase 1 adds Step 8 (gate audit) and per-section write-gate audit procedure.
- **Action gate repositioned as living document**: index-spec.md Section 5 opening rewritten to clarify that the design framework is fixed but the actual rules are Agent-maintained. Per-section audit in maintenance.md expanded with gate-rule count check.

### Added
- **references/initialization.md**: Full initialization protocol for creating a new journal from scratch. Six phases: directory structure, initial index.md template (with empty gate tables and protocol declaration), maintenance memo, tag registry initialization, bootstrap entry, verification checklist. Includes post-initialization growth guide.
- **SKILL.md**: Initialization trigger added to description. Routing table row and Linked Files entry added for initialization.md.

---

## [3.1.0] — 2026-06-25

### Migrated
- **Skill migrated from runtime to project**: Copied from the Hermes runtime environment (`note-taking/journaling/`) into the metapowers project (`skills/journaling/`). The project version is now the development source; the runtime version remains as an independent installed copy.
- **Frontmatter normalized**: `version`/`author` moved into `metadata` block per project convention. `metadata.hermes.*` (Hermes-specific tags and related_skills) removed. `license` field removed. `last_updated` field added.
- **README.md added**: Design rationale document created per project convention (was absent in runtime version).

### Decoupled (environment-specific → generic)
- **Path parameterization**: All `~/.agents/journal/` hard-coded paths replaced with `<journal-root>/` or functional descriptions ("the journal root", "index.md").
- **Framework concepts generalized**: `SOUL.md` → "agent startup protocol"; `hermes skills list/uninstall` → "list installed skills"/"framework uninstall"; `HERMES_HOME` → "agent framework config directory"; `hermes-backup` → generic "platform-dependent scripts".
- **Project names desensitized**: `Scriptum` → "项目 A" (in examples) or "a project" (in prose); `kuiq` → "项目 B"; `Ĉalio` → "the user"; `鸣愿传说` → "某创作项目".
- **Tag registry cleaned**: Project-specific tags (`hermes-ops`, `scriptum`, `kuiq`, `metapowers`, `hermes-plugin`) removed. Structure preserved with placeholder for users to register their own.
- **Journal content links removed**: Links to `~/.agents/journal/experience/2026-06-25-journaling-skill-review.md` (a private journal entry) replaced with cross-references to skill-internal references.
- **Relative path to journal content removed**: `../../experience/2026-05-20-journal-gate-mechanism.md` in dashboard-design-principles.md replaced with link to `references/two-gate-model.md`.
- **Maintenance memo path**: `../.maintenance-memo.md` → `.maintenance-memo.md` with clarifying note that the file lives at journal root, not inside skill directory.

### Generalized (Hermes-specific reference files)
- **cross-instance-sync.md**: `~/.hermes/skills/` → `<agent-skills-dir>`; `MEMORY.md/USER.md` → "memory and user profile files"; `存前自问` → "the write gate self-check".
- **environment-migration.md**: `~/.hermes/` → `<agent-home>/`; `HERMES_HOME` → "agent framework config"; `hermes-backup` → generic scripts; `fact_store` commands → "your framework's fact search tool"; `config.yaml` specific fields → generic "agent framework config".
- **skill-audit-methodology.md**: `hermes skills list` → "list all installed skills"; `config.yaml skills.disabled` → "framework config disable"; `$HERMES_HOME/archived-skills/` → "archive directory outside skills tree"; `clawhub` source merged into `hub`/`official`.

### Retained (intentionally kept)
- **Tool names** (`search_files`, `read_file`, `patch`, `session_search`, `skill_view`): Common agent tool names with equivalents in most frameworks.
- **Memory/user profile concepts**: Universal agent memory system concepts, not Hermes-specific.
- **Windows/WSL path examples in cross-instance-sync.md**: Generic cross-platform migration examples.

---

## [3.1] — 2026-06-25 (pre-migration)

### Changed
- **design-principles.md**: Anchor #1 rewritten from "Accuracy & completeness" to "可复现深刻理解" — the core writing principle is now about reproducing deep understanding on re-read, not just information completeness. Mechanism mapping table updated to match.
- **note-spec.md**: Added "The summary is not the understanding" section after Summary Anchoring Principle — the summary decides whether to open, the body must deliver understanding. Added distinction between substantive edits (check summary) and minor edits (skip check).
- **daily-ops.md**: Prospective Reading Check now leads with the core question from Anchor #1. Strengthened "Self-contained?" to require deep understanding, not just comprehension.
- **daily-ops.md**: Added "Before Writing to MEMORY or USER PROFILE" section — conditional write gate check (triggers on borderline cases, not on obvious hard constraints).
- **daily-ops.md**: Added "Capture Tiers" — immediate-tier vs paragraph-tier decision capture.
- **daily-ops.md**: Session Startup now notes maintenance signals without forcing mandatory action.
- **daily-ops.md**: Added "Over-generalization signals" quick reference — concrete language patterns that trigger scope check.

### Merged
- **dashboard-pattern.md** → merged into **dashboard-design-principles.md** (template + when-to-create criteria).

### Removed
- **dashboard-pattern.md** — content absorbed into dashboard-design-principles.md.

---

## [3.0] — 2026-06-18

Major design revision after full maintenance session:
- Two-level design structure separation (design principles → reference, execution anchors → SKILL.md)
- Tag registry (controlled vocabulary, 4 categories ~20 tags)
- Prospective reading check (5 questions before writing)
- Over-generalization as independent guard
- Progressive disclosure: SKILL.md back to router role
- Inbox/ directory + write gate for journal entries
- Entry lifecycle model + status field
- Maintenance memo mechanism (.maintenance-memo.md)
- Concept-vs-operation diagnostic framework added

---

## [2.0] — 2026-05-23

- Four-phase maintenance protocol
- Summary anchoring with three checkpoints

---

## [1.0] — 2026-05-20

- Action Gate mechanism (two-gate model)
- SOUL.md startup protocol gate scanning
- Five-layer memory strategy
