## [5.0.3] — 2026-08-23

> Base: v5.0.2. SKILL.md 全量英文化——原中英混合形态统一为英文（结构性内容与解释性内容均英文化），实质内容与中文原版逐节对照一致；description 保留中英操作动词触发面。

### Changed
- **SKILL.md 英文化**: The Journal 三要素、Before You Begin、操作协议表、Scripts 段、Operating Principles 六条全部英文化；实质内容完整承载中文原版语义（读不加载写才加载、规则文档单入口、删除处理归 journal 规则等设计决策的表述均保留）
- **description 中英触发词**: 操作范围约束结构保持不变（决策 #5 不变量满足），补充中文操作动词示例（创建/写入/编辑/移动/归档/删除/维护/整理）作为 §4.6 中文匹配面

### Fixed
- **operating principles 中文条目英文化**: 标签自管理、目录归属判断、删除处理三条中文原则译出且语义完整

## [5.0.2] — 2026-08-20

> Base: v5.0.1. 修复 v5.0.0 重构残留——删除/归档设施归属调整：archive 目录不是技能通用要求，归属 journal 自身规则。技能原则层删除保护记述移除；维护协议保留「不直接删除」做法但不再指定 archive，推荐移入临时保存目录（规则已有类似设施时直接使用）。

### Fixed
- **SKILL.md**: Operating Principles 移除「'Delete' means move to archive/」硬性规定，改为归属声明（删除处理按 journal 规则判断，技能不预设归档设施）；可逆操作原则示例移除 archive。
- **protocal-maintenance.md**: 「不删除任何文件」红线保留但不再指定 archive 目录——删除均以移入临时保存目录代替（规则已定义类似设施时直接使用）；「删除即归档」表述移除；规则区检查、.bak 初始化、过时内容处理、临时产物处理等处的 archive 引用统一改为临时保存表述。
- **script-tools.md**: 断链修复场景「已归档但未提取关键点 → 从 archive 拉回」改为「已移入临时保存 → 从临时保存目录拉回」。
- **SKILL-DESIGN.md**: 决策 #3 重写为「删除处理归 journal 规则——技能不预设归档设施」（与决策 #2 内容自管理同构）；维护注意事项删除语义统一表述同步。

## [5.0.1] — 2026-08-16

> Base: v5.0.0. 元语境渗漏全量校正——判定标准重构为「语境归属」（这段文字对运行时读者有功能吗？读者用它吗？），16 个内容文件渗漏清除（删除/归位/转化三分），另 2 个归位目标文件（SKILL-DESIGN/CHANGELOG）同步。

### Changed
- **写入协议交付前自检条目化**: 四问全部条目适用化——「可执行性」改为未来重读能否直接使用；「独立性」检查面为脱离本 session 对话上下文与其他条目；「边界覆盖」从文档 QA 视角（空输入/错输入）转化为「结论的适用条件与失效场景」；「可复现性」保留。
- **发现合约冗余说明改写**: 删除悬空引用「对应技能设计决策 #6/#20」（SKILL-DESIGN 不随技能分发，且编号已陈旧）；保留「重复是有意的」事实与「合约设计时保留此重复」约束。
- **模式文档作者口吻转化**: 「不要生硬照搬」→「不直接照搬，按笔记库自身情况调整」（dashboard/layered-rules/maintenance-memo/note-tags 共 4 处，禁止边界保留）；「可以考虑」→「建议」（note-tags/spec-frontmatter/spec-rules，推荐强度保留）；「自行决定」→「按自身情况自行设计」（layered-rules）；「精心设计的」→「固定的」（protocal-import）。
- **种子 RULES.md 引言**: 「均为可改默认值」→「非技能强制、可调整」——作者对种子起点的自我定位转化为操作事实。
- **SKILL-DESIGN**: 措辞风格约定更新为「语境归属判定 + 修复三分」；维护注意事项补充 protocal-import P1 顺序理据（廉价优先——先零成本检查后读取内容）。

### Fixed
- **frontmatter 双版本悬空引用清除**: 「plan §2.1 decision table」等 7 处引用指向不存在的写作计划，删除或改为实际导航；英文 docstring 中的中文速记转为英文表述；fm_parse 边界导航修正为「empty input → {}; unsupported YAML → error」；自相矛盾的「null-like keep as string」注释及其暴露的不可达分支（重复的 null 判断）一并删除。
- **check-links 双版本注释清理**: 44 处悬空节编号括注（§2/§3/§5/§8/§9/§10——指向不存在的写作计划）删除（描述性文字保留）；孤儿标签「(type B)」删除（代码与 spec-note 均无 type A/B 分类）；4 处未实现的调试日志模板（2 种模板 × 双版本）与 1 处与行为不符的草稿注释删除；mjs「Start directory」注释与代码行为对齐（目录→自身，否则→父目录）；变更历史括注「Path.resolve() previously expanded them」删除（历史已在 v5.0.0 Fixed 记录）。

## [5.0.0] — 2026-08-15

> Base: v4.10.0. 大规模重设计——机制归属收敛（四件套 → RULES.md 单入口）、规范性动作统一收敛到协议层、INDEX 约束收敛 + spec/design 拆分、spec-note 纯方法论化、写入协议重组、check-links 符号链接行为对齐。

### Added
- **`references/design-rules.md`**: 组织方式设计提示（合并 spec-conventions / design-classification / design-tags 三文档）——组织方式定位、读写关系线索（读/写/规则分量平衡）、设计模式参考（patterns/ 引导）。规范层见 spec-rules.md。
- **`references/design-index.md`**: INDEX 设计参考（设计层，与规范层 spec-index 分离）——常用板块建议（六原则降格为启发）、三个示例板块、组织方式建议、dashboard 指引。
- **`templates/seed/RULES.md`**: 规则文档种子——节序：INDEX 结构（极简可执行规则）/ 分类（4 目录）/ 笔记元数据字段 / 写作约定。头部声明仅定位与"可改默认值"两行；标签注册表不预置（tags 并入元数据字段，注册表为庞杂时扩展）。
- **spec-note.md Link Convention 章节**: 链接形态规范独立成章——两种形态选用策略、解析语义五条、WRONG/EXTERNAL/歧义分类、路径基准约束（笔记间链接禁用绝对路径、外部文件建议绝对路径）。
- **`references/script-tools.md`**: 脚本工具完整指南（替代 scripts/README.md——scripts/ 目录按规范仅含脚本）——frontmatter/check-links 命令参考、输出格式、链接解析语义、符号链接行为。
- **`references/patterns/layered-rules.md`**: 分层规则设计模式——规则内容分层：RULES 承载无条件遵循的规则，条件性遵循的规则分入规则子集（独立文件），RULES 引用处说明适用加载条件。外置判定=条件性遵循，不由体量决定。
- **`references/patterns/note-tags.md`**: 笔记标签模式——tags 字段与标签格式（简短词汇、可嵌套、多维度、单一字段）；扩展建议：维度提炼规范、庞杂时启用标签注册表（先注册后使用）。
- **`references/patterns/maintenance-memo.md`**: 维护备忘录模式——独立文档记录延后操作（不被 INDEX 感知、仅在规则中规范；准确但不具体；不延后必要操作；处理即删；单一文件）。
- **`references/patterns/classification-systems/about.md`**: 分类系统集合引导——pattern 架构（摘要/核心方法/每模式抓手段），替代表格索引。

### Changed
- **四件套 → RULES.md 单入口**: CLASSIFICATION.md/TAGS.md/CONVENTIONS.md 三份 journal 侧规则文件与 .maintenance-memo.md 机制收敛为单一规则文档（RULES.md）——技能强制 5 条义务 + 4 条提醒；写入/维护/收录协议只面对一个入口；读 INDEX 时不感知、写时才加载。
- **写入协议重组**: 两段式（头部 4 步规范性动作 + 额外说明）——triage → 读 journal 规则 → frontmatter+body → 可发现链路检查。目录/文件预设全部删除（inbox 兜底句、.maintenance-memo.md 硬编码、Required fields 写死列表）；INDEX 同步义务（三义务 + status guard）移除，落为价值陈述；交付前自检降级为提醒。
- **INDEX 约束收敛 + spec/design 拆分**: spec-index.md 重写为极简规范层——三个 must 合并为一个、协议声明删除个性化规则行、INDEX 具体格式归属移交 journal 规则（RULES.md INDEX 结构板块）；设计内容（六原则/板块建议/组织建议）全部移入新建 design-index.md，六原则从"设计约束"改定性为"常用板块建议"。
- **dashboard.md 重写**: 摘要（定位+设计意图）/ 核心方法（领域级次级 INDEX）/ 层级化与引导链路（渐进式披露）/ 领域 vs 分类 / 从自然需求生长（生长/消散解绑/命名）/ 一种可能的做法——删除设计意图、内容范围表、创建信号表、设计原则等旧节。
- **protocal-import.md 调整**: P2-S3 重写为规则文档抽象表述（删除三文件指名与优先级）；P3-S2 删除 imported/imported_source 字段规定并消除 P2-S4 悬空引用；发现路径表述抽象化（不点名 INDEX.md）。
- **protocal-init.md 重新设计**: 四阶段（P1 确定位置+已有内容检查 / P2 创建骨架两个种子 / P3 发现合约含可发现态验证 / P4 维护接管条件触发）；旧三件套保留原样由维护协议接管；占位符替换步骤与类型识别流程删除。
- **protocal-maintenance.md 调整**: 设计阶段审视对象改为规范维度（参考 design-rules）；新增规则区检查（挂靠设计阶段）；扫描阶段维护信息读取移除（维护信号机制整体删除，见 Removed）；INDEX 核对与交付检查合规依据改为 journal 规则；操作规范新增 .bak 归档与骨架态完整流程；相关参考列表更新。
- **spec-note.md 收窄为纯方法论**: 删除 Directory Assignment 与 Entry Lifecycle 两节（目录判断替代路径已由 RULES 机制建立）——零目录、零文件名、零规范性动作；Granularity 时间方向表述改为纯写作技巧（`## Future` 节）。
- **SKILL.md 全文件更新**: Journal 节（规则文档单入口）、Core Constraint（技能定义协议、journal 规则定义内容组织）、Linked Files（design-index/design-rules 新增、三旧文档与 Inbox/Conventions Template 移除）、Operating Principles 两条改写、场景表同步。
- **seed INDEX.md 精简**: 仅含协议声明（删除个性化规则行、板块占位、初始化占位行）。
- **元数据字段方案降级**: 字段规定从协议硬编码（Required fields 写死列表）降级为"推荐并预设"（种子 RULES.md 元数据字段板块），字段设计归 journal 规则；frontmatter.py check 脚本自定义字段集支持归 #8 单独处理。
- **check-links 解析语义实现按 Link Convention 重写**: `[[foo]]` 库内按名搜索（多匹配报歧义）、`[[foo.md]]`/`[foo.md]` 相对当前文件 + 各自 fallback、`./`/`../` 前缀相对当前文件、路径无前缀相对 journal-root；链接输出新增 `status` 字段（internal/external/wrong/ambiguous），summary 新增 `wrong`/`ambiguous` 计数——双实现（py/mjs）逐字段一致。
- **引用路径基准统一**: references/ 内文档互引用统一为相对当前文件（裸文件名或 `../` 前缀）——修复 protocal-maintenance 相关参考列表 dashboard 死链、design-index/script-tools/examples 悬空引用；SKILL.md 等根目录文档保持 `references/` 前缀（相对技能根）。
- **spec-frontmatter.md 规则文档表述**: tags 来源/规则从 TAGS.md 改为规则文档标签板块；自定义字段约定记录位置改规则文档；示例节补充自定义标签先注册说明。
- **分类体系目录迁移**: `examples/classification-systems/` → `references/patterns/classification-systems/`——分类体系是设计模式参考（与 patterns/dashboard 同性质）而非示例；目录内 README 与 examples/README 删除（README 非合法条目），examples/ 目录整体移除；design-rules/SKILL.md 引用路径同步更新。
- **SKILL.md 精简**: 路由表收窄为四协议（操作协议 | 适用时机 | 加载）；Linked Files 极简纯链接（18 条）；Scripts 节一句话；Operating Principles 标签原则更新（种子标签集移除，规则未定义时按维度自行提炼）；开头重复引用块与定位段删除。
- **protocal-maintenance.md**: 相关参考补 design-index（路由表收窄后的唯一孤儿文件）。
- **patterns 四文档格式统一**: 核心维度行删除（与摘要重复，无独立信息）；定稿形态统一为摘要（定位+设计意图）+ 核心方法 + 具体节 + 一种可能的做法。
- **RULES 规范/设计分层（spec-rules 新增）**: 新建 `references/spec-rules.md`（规范层——规则编写的原则 5 条；规则设计的提醒四节：放置与检索、INDEX 的结构、约定、维护信息——独立启发、不预设机制，技能最小义务之外组织方式由 journal 自行决定）；design-rules.md 收窄为纯设计层（设计方法/Pitfalls/建议的板块/参考体系），与 INDEX 体系的 spec-index/design-index 结构对称。规则编写原则删除"参考 spec-note 风格"（规则文档是规范不是笔记，参考笔记写作方法论属旧 spec-conventions 继承残留），新增"自包含且完备"原则（规则内容不得引用笔记条目、技能内容等不稳定外部来源）——种子 RULES.md 相应移除技能文档引用。

- **表述一致性收敛（仅 5 条硬性可假定存在）**: 全量语义检查——技能内容不再假定真实场景中存在引导性建议之外的机制。SKILL.md Before You Begin 重写（不再点名 INDEX 具体板块）；spec-frontmatter Required Fields 降级为种子预设字段方案（硬性仅"必须有 YAML frontmatter 段"——字段集由 journal 规则定义，tags 不再强制"至少选一个"）；frontmatter 脚本新增 `--required-fields`（journal 规则定义了不同字段集时覆盖默认种子四字段，check/replace 双实现同步）；design-index 被引用关系、design-discovery-contract 检查维度与合约模板、protocal-init 回退方案引用块与版本号示例、protocal-write 交叉引用、protocal-maintenance 交付检查、spec-note project tag、SKILL.md 与 script-tools 示例路径均去板块/目录/标签/字段假定。

### Removed
- **references/spec-conventions.md / design-classification.md / design-tags.md**: 内容并入 design-rules.md。
- **templates/seed/CONVENTIONS.md / TAGS.md / CLASSIFICATION.md**: 并入 templates/seed/RULES.md。
- **SKILL.md Inbox 条目 / Conventions Template 条目**: 种子不再预设 inbox 目录与 CONVENTIONS 模板。
- **examples/journal-standards/**: 删除（INDEX/分类/标签示例——旧拆分模型残留，"standard"命名与"结构由 journal 自定"哲学冲突；示例价值由 design-rules 板块示例与 classification-systems 覆盖）。
- **维护信号机制**: 写入协议维护信号步骤、维护协议维护信息读取/清除与"笔记库维护信息"节、INDEX 协议声明维护信号快照（spec-index 与种子 INDEX）、初始化维护信号触发判断与相关引用（protocal-init/design-discovery-contract/SKILL.md）整体移除——机制不再存在。spec-rules"维护信息"节（最后保留形式）随之删除，主题由 patterns/maintenance-memo.md 模式承载。
- **`references/patterns/classification-systems/journaling-default.md`**: 删除——操作记录无模式价值（种子解释自包含于种子模板、演化原则已由维护协议覆盖、认知价值审计为错位维度）；about.md 抓手 7→6、design-rules 免责说明随残留断言消失。

### Fixed
- **`scripts/check-links.py` 符号链接行为对齐**: Path.resolve() 全部替换为纯字符串规范化（不追踪符号链接，与 Node path.resolve() 对齐）——journal-root 本身为符号链接时保持用户路径视角；文件收集跳过符号链接文件（与 Node Dirent.isFile() 一致）；存在性检查保持跟随符号链接（指向存在即有效）；scripts/README.md 声明补充到文件收集层。
- **protocal-import P2-S2 顺序循环消除**: "按 journal 规则确定发现入口位置"从 P2-S2 移除（规则在 P2-S3 才读取），入口定位统一在 P3-S3；P2-S3 补规则文档缺失处理（复制种子补齐），与写入协议一致。
- **spec-index 协议声明维护信号快照移除**: 维护信号机制整体删除（见 Removed），"全程不变"加注保留（结构不变，其中值为快照，随维护更新）。
- **protocal-init 边界修复**: P1"已有笔记文件"判定排除骨架文件（避免重初始化误触发 P4）；P3 禁令作用域澄清（仅限发现合约建立）。
- **Link Convention 内部自洽修复**: 共享规则集表述、库内 mdlink 选用策略、两处"相对当前文件"措辞统一、分类体系与语义表对应完整（WRONG/EXTERNAL/歧义补判定位置）、EXTERNAL 与库内绝对路径禁用边界说明。
- **frontmatter 帮助文本残留清理**: 两脚本 `--journal-root` 帮助描述移除 TAGS.md registry 引用（该校验未实现，标记预留）。
- **杂项**: SKILL.md `index.md` 大小写统一；种子 RULES.md 头部补 `references/…` 路径归属说明（指向技能文档）；SKILL.md Discovery Contract 条目路径补全。

## [4.10.0] — 2026-08-11

> Base: v4.9.0. 新增 check-links 脚本 + 维护协议四节重构 + 元语境渗漏清理 + 分类启发性修正。

### Added
- **`scripts/check-links.py` + `scripts/check-links.mjs`**: Journal 链接检查双版本脚本——提取全部 markdown/wikilink 链接、检查目标存在性、分析入链/出链关系。零第三方依赖，纯只读。两版本 API、行为、输出格式完全一致。支持 --absolute / --relative-to / --file 聚焦 / --journal-root 手动指定等选项。
- **`scripts/README.md`**: 新增 `## check-links` 章节——快速开始、命令参考、输出格式说明、支持的链接格式、常用场景、错误处理、限制说明。

### Changed
- **`content/SKILL.md`**: 新增 `## Scripts` 节——列出 frontmatter/check-links 脚本用途、关键用法场景示例。
- **`content/references/protocal-maintenance.md`**: P3-S2-dim3 追加 check-links 内联提醒，P0-S7 表后追加 frontmatter check 提醒。
- **`content/scripts/README.md`**: 追加 check-links 使用场景（4 种）和最佳实践（6 条），文件清单更新为含 check-links 文件。
- **`SKILL-DESIGN.md`**: 新增决策 #23——脚本引导的三层披露设计（SKILL.md 节 + 协议内联网格 + README 完整指南）。
- **`content/references/protocal-maintenance.md` 元语境渗漏清理**：删除全部"作者现身"句——"供你理解""帮助你跳出框架""设计它的目的是让你""你可以根据笔记库的实际情况调整""供你参考。它们是启发，不是清单"等。作者语境（写作要求、设计意图、态度、许可、对文本的自我定位）不再泄漏进正文；约束层次改由结构（操作规范/推荐流程/补充论述分区）与措辞（必须/禁止 vs 陈述句）传达。判定依据：正文中是否有作者的声音。
- **`content/references/protocal-maintenance.md` 维护完成形态重构**：重构为两点——INDEX 可用性（引导入口作用 + 维护后展示最新状态）+ 维护信息清零。后续术语泛化：维护信号 → 维护纪录 → **笔记库维护信息**（汇集日常工作中发现的待处理问题，主要来源 `.maintenance-memo.md`，不限于其他渠道）。
- **`content/references/protocal-maintenance.md` INDEX 幻影行泛化**："INDEX 中的幻影行"（具体检查技巧）→ "INDEX 的重要性"（引导入口作用 + 最终可用性，叙述柔和化）；"摸底不依赖 INDEX 展示"并入"怎样跳出框架"的独立判断姿态。
- **`content/references/protocal-maintenance.md` 推演修复（8 项）**：设计阶段与操作规范红线"写入 journal"明确为"更新到相应的规范文件（CLASSIFICATION.md / TAGS.md / CONVENTIONS.md）"；细粒度收尾补收尾闭环（更新 INDEX 反映新状态、清除维护信息中已解决的问题）；交付检查"即读取/写入协议"改为"见相关参考"；相关参考补 protocal-write/spec-note/spec-frontmatter 三个链接；扫描阶段 memo 术语统一为"维护备忘"并补位置（`<journal-root>`）与存在性（如不存在则跳过）；对比检查补基线来源（如维护前的文件清单快照）；流程一览补衔接句"重组与细粒度收尾是设计确认后的执行部分"；设计阶段补"若规范仍适合现状，确认后直接进入重组"。
- **`content/SKILL.md`**: Linked Files 维护协议描述同步——"默认值可调整"→"执行路径可调整"（"默认值"字样随元语境清理从正文移除）。
- **`content/references/protocal-write.md`**: Maintenance Signals 节旧阶段引用（Phase 0 Step 0）→ 指向维护协议扫描阶段（新四阶段结构）。
- **`content/references/spec-note.md` 目录分配启发性修正**：Directory Assignment 引言翻转——第一认知从"条目放在四个默认目录之一"改为"四个目录是种子结构、起点而非固定分类法；权威目录列表是 `<journal-root>/CLASSIFICATION.md`，随维护演化；种子目录是演化前的基线"；标题 "Default Directories" → "Seed Directories"。内容未动，仅语气调整（强化"分类可演化"暗示，弱化"固定分法"暗示）。

### Removed
- **维护触发信号机制**：旧版维护信号（dashboard staleness / tag sprawl / memo accumulation 等）与 compound signals 优先级判定整体移除
- **"一些值得借鉴的整理思路"节**：改名联动/临时产物/维护备忘价值三个条目拆散为独立小节，"供你参考。它们是启发，不是清单"随节消失
- **"维护备忘的价值"小节**：并入"笔记库维护信息"（核心洞察保留：日常积累往往比一次扫描更能暴露长期问题）

### Fixed
- **`scripts/check-links.py` + `check-links.mjs`**: 修复 wikilink 路径解析——markdown 链接相对于源文件目录，wikilink 相对于 journal-root（Obsidian 规范）。新增 `link_type`/`journal_root` 参数到 `link_resolve`/`linkResolve`，双版本同步修改。
## [4.9.0] — 2026-06-30

> Base: v4.8.1. 表述优化——术语统一、优先级澄清、INDEX.md 格式规范化。

### Added
- SKILL.md 新增 `## Journal` 节，描述 journal 笔记库的结构要素，锚定术语"INDEX"、"个性化规则文件"
- INDEX.md 协议声明区新增个性化规则文件指引——三文件链接 + 用途标注，作为必含内容
- 术语"个性化规则文件"正式定义为 CLASSIFICATION.md、TAGS.md、CONVENTIONS.md 的统称
- CONVENTIONS.md 的优先级规则明确：存在时覆盖其他两份规则文件
- SKILL-DESIGN.md 新增 Decision #15：INDEX.md 协议声明使用标题节而非引用块

### Changed
- INDEX.md 协议声明区格式从 `>` 引用块改为 `## 协议声明` 标题 + 列表（含旧版兼容锚点）
- SKILL.md 顶部 intro 拆分为"journaling 技能的价值"与"Journal 的结构"两层，区分清晰
- spec-conventions.md "不冲突"原则改为"允许偏离，需说明理由"
- 全文"三规则/自管理文件/制度文件"等零散称呼统一为"个性化规则文件"
- patterns/dashboard.md ASCII 图中节点名称随 INDEX.md 格式同步更新
- 联动更新 15 个文件：spec-index.md、protocal-init.md、protocal-maintenance.md、protocal-write.md、protocal-import.md、spec-conventions.md、design-tags.md、design-discovery-contract.md、templates/seed/INDEX.md、examples/journal-standards/INDEX.example.md、examples/README.md、SKILL-DESIGN.md、CHANGELOG.md

### Removed
- 移除"三份规则文件平等并列，不设先后依赖顺序"的表述——已由个性化规则文件概念和优先级设计替代






## [4.8.1] — 2026-06-29

> Base: v4.8.0. 去除平台路径硬编码——`design-discovery-contract.md` 的"已有合约检测"搜索范围误将 omp 环境路径（`.omp/agent/`）写入技能内容，违反「技能无硬性依赖」原则。

### Fixed
- **design-discovery-contract.md 已有合约检测**：将搜索范围从 omp 特定路径（`.omp/agent/RULES.md` 等）改为通用描述——「agent 运行时配置文件（按注入优先级从高到低）> 项目根配置文件 > 用户级配置目录 > 全局默认路径」，不绑定具体平台

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
