# Changelog

## 5.1.0
- protocal-write.md 新增「合并条目」最小指引（保留方判据、内容并入、summary 收敛、矛盾显式化、被并条目入临时保存并留关系注记、引用修复与 INDEX 同步）；protocal-maintenance.md 裁定句补合并指引指针
- protocal-operations.md 删除指引补 journal 规则未定义删除约定时的缺省回退（移入临时保存目录、同步 INDEX 登记）
- spec-rules.md 最小义务表述对齐操作参考口径（「写入/导入前必读」改「非只读操作前必读」）
- 新增 references/protocal-operations.md（非只读操作参考：操作族概述、共享原则、族义务单处定义、收录/移动/删除最小指引、维护协议层级声明）
- 移除 references/protocal-import.md（收录协议消解：P1 准入判断、REJECT/SUSPEND 控制流与协议内安全边界整体退役，防护归模型能力与平台层原则）
- protocal-write.md 吸收录入（定位与额外说明补收录表述，「判断是否值得写」承接收录价值判断，第 2 步读取规则改为引用族义务）
- protocal-maintenance.md 触发边界专项化（维护只由用户明确触发、建议专门会话执行、agent 不自行执行、提醒以维护备忘承接，补充泛化阅读认可声明）
- SKILL.md 自治域收窄至写入与用户引导下的操作、协议表重排为 Init/Write/非只读操作参考/Maintenance、删除处理原则对齐操作参考路由、Linked Files 以 protocal-operations 替换 protocal-import、description 触发动词面补收录/导入、last_updated 更新
- spec-note.md 新增 Title 建议（标题组织为命题形式，附对比例与不适用边界）
- design-discovery-contract.md 注入模板扩为六要素（journal-root 声明、定位立场、价值裁量、读取路由、加载触发与操作边界、与其他记忆机制的分工）、新增「注入文本的设计方法」节（要素框架、写作原则、宿主提示词更改权限）与快照宿主适配说明、「已有合约的检测」节四维度表升级为要素覆盖检查
- protocal-init.md Phase 3 回退方案模板同步六要素版、「合约已存在的情况」评估判据改为要素覆盖检查

## 5.0.4
- protocal-write.md 新增「如果你能够委派子代理」节：主线话题仍在继续且能委派子代理时，先将笔记写入临时目录，再委派子代理读取规则文档并按规范整理，最小化对当前话题的干扰
- 种子 INDEX.md 协议声明区新增「以本 INDEX 为线索，主动读取相关内容」引导提示，强化 INDEX 唯一入口导向
- 种子 RULES.md INDEX 结构板块明确 INDEX.md 开头保留引导提示并附 Markdown 示例，笔记文件命名补充「日期为笔记的创建日期」，种子 INDEX.md 协议声明标题层级回正

## 5.0.3
- SKILL.md 正文全量英文化（The Journal 三要素、Before You Begin、操作协议表、Scripts 段、Operating Principles 六条），实质内容与中文原版逐节对照一致
- description 保留操作范围约束结构，补充中文操作动词示例（创建/写入/编辑/移动/归档/删除/维护/整理）作为中文匹配面
- Operating Principles 中标签自管理、目录归属判断、删除处理三条中文原则译为英文

## 5.0.2
- SKILL.md Operating Principles 移除「'Delete' means move to archive/」硬性规定，删除处理改为按 journal 规则判断、技能不预设归档设施，可逆操作原则示例移除 archive
- protocal-maintenance.md「不删除任何文件」红线改为移入临时保存目录，移除「删除即归档」表述，规则区检查、.bak 初始化、过时内容处理、临时产物处理等处的 archive 引用统一改为临时保存
- script-tools.md 断链修复场景从「已归档 → 从 archive 拉回」改为「已移入临时保存 → 从临时保存目录拉回」
- SKILL-DESIGN.md 决策 #3 重写为「删除处理归 journal 规则——技能不预设归档设施」

## 5.0.1
- 写入协议交付前自检四问条目化（可执行性、独立性、边界覆盖、可复现性）
- 发现合约冗余说明删除悬空引用「设计决策 #6/#20」，保留「重复是有意的」事实与约束
- 模式文档作者口吻转化为操作性表述（dashboard、layered-rules、maintenance-memo、note-tags、spec-frontmatter、spec-rules、protocal-import 多处「不要生硬照搬」「可以考虑」「自行决定」等改写）
- 种子 RULES.md 引言由「均为可改默认值」改为「非技能强制、可调整」
- SKILL-DESIGN 措辞风格约定更新为「语境归属判定 + 修复三分」，维护注意事项补充 protocal-import P1 顺序理据
- frontmatter 双版本脚本清除 7 处指向不存在写作计划的悬空引用，修正 fm_parse 边界导航与自相矛盾的 null-like 注释及不可达分支
- check-links 双版本删除 44 处悬空节编号括注、孤儿标签「(type B)」与 4 处未实现的调试日志模板，mjs「Start directory」注释与代码行为对齐

## 5.0.0
- 新增 references/design-rules.md（组织方式设计提示，合并 spec-conventions、design-classification、design-tags 三文档）
- 新增 references/design-index.md（INDEX 设计参考，与规范层 spec-index 分离）
- 新增 templates/seed/RULES.md（规则文档种子：INDEX 结构、分类、笔记元数据字段、写作约定）
- spec-note.md 新增 Link Convention 章节（链接形态规范独立成章）
- 新增 references/script-tools.md（脚本工具完整指南，替代 scripts/README.md）
- 新增 references/patterns/layered-rules.md（分层规则设计模式）
- 新增 references/patterns/note-tags.md（笔记标签模式）
- 新增 references/patterns/maintenance-memo.md（维护备忘录模式）
- 新增 references/patterns/classification-systems/about.md（分类系统集合引导）
- CLASSIFICATION.md、TAGS.md、CONVENTIONS.md 三份规则文件与 .maintenance-memo.md 收敛为 RULES.md 单一规则文档入口
- 写入协议重组为两段式（头部 4 步规范性动作 + 额外说明），删除目录/文件预设与 INDEX 同步义务，交付前自检降级为提醒
- spec-index.md 重写为极简规范层，设计内容移入新建 design-index.md，六原则降为常用板块建议
- dashboard.md 重写（摘要、核心方法、层级化与引导链路、领域 vs 分类、从自然需求生长、一种可能的做法），删除旧设计意图与内容范围等节
- protocal-import.md P2-S3 重写为规则文档抽象表述，P3-S2 删除 imported/imported_source 字段规定并消除 P2-S4 悬空引用
- protocal-init.md 重新设计为四阶段（确定位置、创建骨架、发现合约、维护接管）
- protocal-maintenance.md 调整（设计阶段审视规范维度、新增规则区检查、扫描阶段维护信息读取移除、操作规范新增 .bak 归档与骨架态完整流程）
- spec-note.md 收窄为纯方法论（删除 Directory Assignment 与 Entry Lifecycle 两节）
- SKILL.md 全文件更新（Journal 节、Core Constraint、Linked Files、Operating Principles、场景表）
- seed INDEX.md 精简为仅含协议声明
- 元数据字段方案降级为「推荐并预设」，字段设计归 journal 规则
- check-links 解析语义按 Link Convention 重写（[[foo]] 库内按名搜索、相对路径语义、status 字段与 wrong/ambiguous 计数，py/mjs 双实现逐字段一致）
- references/ 内文档互引用路径基准统一为相对当前文件
- spec-frontmatter.md tags 来源改表述为规则文档标签板块，自定义字段约定改记录于规则文档
- 分类体系目录由 examples/classification-systems/ 迁至 references/patterns/classification-systems/，examples/ 目录整体移除
- SKILL.md 精简（路由表收窄为四协议、Linked Files 极简纯链接、Scripts 节一句话、删除开头重复引用块与定位段）
- protocal-maintenance.md 相关参考补 design-index
- patterns 四文档格式统一为「摘要（定位+设计意图）+ 核心方法 + 具体节 + 一种可能的做法」
- 新增 references/spec-rules.md（规则规范层），design-rules.md 收窄为纯设计层，规则编写原则新增「自包含且完备」
- 表述一致性收敛：技能内容不再假定引导性建议之外的机制，frontmatter 脚本新增 `--required-fields` 选项
- 移除 references/spec-conventions.md、design-classification.md、design-tags.md（内容并入 design-rules.md）
- 移除 templates/seed/CONVENTIONS.md、TAGS.md、CLASSIFICATION.md（并入 templates/seed/RULES.md）
- 移除 SKILL.md 的 Inbox 条目与 Conventions Template 条目
- 移除 examples/journal-standards/ 目录
- 移除维护信号机制（写入协议步骤、维护协议读取/清除、协议声明快照、初始化触发判断及相关引用）
- 移除 references/patterns/classification-systems/journaling-default.md
- scripts/check-links.py 符号链接行为对齐 Node 实现（纯字符串规范化、文件收集跳过符号链接文件）
- protocal-import P2-S2 顺序循环消除，入口定位统一在 P3-S3，P2-S3 补规则文档缺失处理
- spec-index 协议声明维护信号快照随机制删除移除
- protocal-init 边界修复（P1「已有笔记文件」判定排除骨架文件、P3 禁令作用域澄清）
- Link Convention 内部自洽修复（共享规则集表述、库内 mdlink 选用策略、歧义判定位置、绝对路径禁用边界）
- frontmatter 两脚本帮助文本移除 TAGS.md registry 引用
- 杂项修复（SKILL.md index.md 大小写统一、种子 RULES.md 补路径归属说明、SKILL.md Discovery Contract 条目路径补全）

## 4.10.0
- 新增 scripts/check-links.py 与 scripts/check-links.mjs（Journal 链接检查双版本脚本，API、行为、输出格式完全一致）
- scripts/README.md 新增 check-links 章节
- content/SKILL.md 新增 Scripts 节
- content/references/protocal-maintenance.md 追加 check-links 内联提醒与 frontmatter check 提醒
- content/scripts/README.md 追加 check-links 使用场景与最佳实践，文件清单更新
- SKILL-DESIGN.md 新增决策 #23（脚本引导的三层披露设计）
- content/references/protocal-maintenance.md 元语境渗漏清理（删除全部「作者现身」句）
- content/references/protocal-maintenance.md 维护完成形态重构为「INDEX 可用性 + 维护信息清零」，术语泛化为「笔记库维护信息」
- content/references/protocal-maintenance.md INDEX 幻影行泛化为「INDEX 的重要性」
- content/references/protocal-maintenance.md 推演修复 8 项（红线明确、收尾闭环、交付检查改指相关参考、相关参考补链接、memo 术语统一等）
- content/SKILL.md Linked Files 维护协议描述「默认值可调整」改为「执行路径可调整」
- content/references/protocal-write.md Maintenance Signals 节旧阶段引用改指维护协议扫描阶段
- content/references/spec-note.md 目录分配启发性修正（Default Directories 改为 Seed Directories，四目录定位为种子结构）
- 移除维护触发信号机制（dashboard staleness、tag sprawl、memo accumulation 等 compound signals 判定）
- 移除「一些值得借鉴的整理思路」节，三个条目拆散为独立小节
- 移除「维护备忘的价值」小节，并入「笔记库维护信息」
- scripts/check-links 修复 wikilink 路径解析（markdown 链接相对源文件目录、wikilink 相对 journal-root）

## 4.9.0
- SKILL.md 新增 Journal 节（笔记库结构要素），锚定术语「INDEX」「个性化规则文件」
- INDEX.md 协议声明区新增个性化规则文件指引（三文件链接 + 用途标注）
- 术语「个性化规则文件」正式定义为 CLASSIFICATION.md、TAGS.md、CONVENTIONS.md 的统称
- CONVENTIONS.md 优先级规则明确：存在时覆盖其他两份规则文件
- SKILL-DESIGN.md 新增 Decision #15（INDEX.md 协议声明使用标题节而非引用块）
- INDEX.md 协议声明区格式从引用块改为「## 协议声明」标题 + 列表（含旧版兼容锚点）
- SKILL.md 顶部 intro 拆分为「journaling 技能的价值」与「Journal 的结构」两层
- spec-conventions.md「不冲突」原则改为「允许偏离，需说明理由」
- 全文零散称呼（三规则/自管理文件/制度文件）统一为「个性化规则文件」
- patterns/dashboard.md ASCII 图节点名称随 INDEX.md 格式同步更新
- 联动更新 15 个文件（spec-index、protocal-init、protocal-maintenance、protocal-write、protocal-import、spec-conventions、design-tags、design-discovery-contract、seed/INDEX、INDEX.example、examples/README、SKILL-DESIGN、CHANGELOG 等）
- 移除「三份规则文件平等并列，不设先后依赖顺序」的表述

## 4.8.1
- design-discovery-contract.md 已有合约检测的搜索范围从 omp 特定路径改为通用配置层级描述（运行时配置文件 > 项目根配置 > 用户级配置 > 全局默认路径）

## 4.8.0
- design-discovery-contract.md 新增「已有合约的检测」节（四维度比对最新模板、三种结果分支）
- protocal-maintenance.md Phase 0 新增合约过期扫描，Phase 1 新增合约审查维度（四维度五种判定标准）
- design-discovery-contract.md Step 3 新增有意冗余的显式注释（contract 与 INDEX.md 协议声明行重叠是设计选择）
- design-discovery-contract.md Step 3 新增格式适配声明（模板 `>` 为展示格式，写入需适配载体格式）
- protocal-init.md Phase 3 新增「合约已存在的情况」分支（不重复设计，按四维度评估是否更新）

## 4.7.0
- SKILL.md 正文新增 Before You Begin 节（声明技能协议依赖 INDEX.md 上下文的信息依赖声明）
- seed INDEX.md 模板新增价值行（跳过意味着在信息盲区中操作）
- spec-index.md Protocol Declaration 新增第六项 Value self-description（可选推荐）
- SKILL.md description 从枚举场景式重写为约束行格式（写入性操作前必须加载 + 写入操作示例）
- design-discovery-contract.md Step 3 与 protocal-init.md Phase 3 回退方案的启动指令强化为「第一步」
- 移除 description 中的 Do NOT load for 段（由约束行负边界取代）
- 移除 description 中的 Triggers 枚举段（由写入操作示例取代）

## 4.6.0
- Operating Principles 新增「删除即归档」原则（删除操作定义为 mv to archive/，禁止直接删除 journal 文件）
- 「不请求许可」原则收紧（仅可逆操作免审批，不可逆操作需用户确认或遵守维护协议条件）
- protocal-maintenance.md 新增 archive 扫描步骤、archive 审查维度、本轮新 archive 保护声明与 archive 清理步骤
- protocal-init.md Phase 3 回退方案与 design-discovery-contract.md Step 3 推荐方案的写入操作增加举例
- templates/seed/INDEX.md、spec-index.md 协议声明行同步扩展
- inbox/README.md 处理节奏「已过期/无用 → 删除」改为「→ 移入 archive」
- 新增 references/spec-conventions.md（CONVENTIONS.md 的设计原则与操作建议）
- 新增 templates/seed/CONVENTIONS.md 最小化种子模板
- protocal-write.md 新增 Before Writing: Check Journal Conventions 节（写入前加载 CONVENTIONS.md 检查是否命中 scope）
- protocal-import.md 新增 P2-S5 检查 Journal Conventions（P3 执行前加载）
- SKILL.md Linked Files 和场景表新增 spec-conventions.md 与 templates/seed/CONVENTIONS.md 条目
- SKILL-DESIGN.md 新增决策 #13（CONVENTIONS 机制）

## 4.5.1
- protocal-maintenance.md 五阶段重设计（审查→设计→定规→计划四步、执行先改三规则、双向质量检验、INDEX 全量重写，Phase 0 新增 convention 数据收集）
- protocal-write.md「Check Journal Conventions」改写为「Check Journal Rules」（三规则平等提及）
- protocal-import.md P2-S3/S4/S5 合并为统一「检查 Journal Rules」
- spec-index.md 移除 Relationships 节与 Self-management reference 子弹，修复旧 Phase 引用
- templates/seed/INDEX.md 移除 self-management reference 行
- examples/journal-standards/INDEX.example.md 移除 self-management reference 行
- protocal-init.md 发现链图示更新，移除 INDEX.md 对 CLASSIFICATION/TAGS 的引用
- design-tags.md 维护引用更新为 P1-S3，移除「INDEX.md 的协议声明行指向它」过时表述
- design-classification.md 移除「INDEX.md 的协议声明行指向它」过时表述
- spec-conventions.md「最后一步加载」改为「与其他规则文件一起前置加载」，协议关系表同步更新
- SKILL.md Linked Files 维护协议描述更新，版本号更新为 4.5.1
- SKILL-DESIGN.md 决策 #2 重写（新五阶段），新增决策 #14–#17，决策 #13 描述微调

## 4.4.0
- 新增 references/design-discovery-contract.md（发现合约四步流程：清查、评估、推荐、呈报）
- protocal-init.md Phase 3「合约发现流程」替换为「方案讨论」概览，回退方案整理为有序列表
- SKILL.md Linked Files 和场景表新增 references/design-discovery-contract.md 条目
- SKILL-DESIGN.md 决策 #7 更新为「协议流与参考分离」

## 4.3.2
- 新增 references/patterns/dashboard.md（恢复 references/patterns/ 子目录结构）
- SKILL.md 引用路径从 references/dashboard.md 改为 references/patterns/dashboard.md（Linked Files 两处 + 场景表一处）
- SKILL-DESIGN.md patterns/ 节重写为 references/patterns/ 子目录设计说明
- protocal-maintenance.md、spec-index.md 引用路径同步更新
- 移除扁平位置的 references/dashboard.md

## 4.3.1
- patterns/dashboard.md 移至标准 references/ 目录，SKILL.md、README.md、protocal-maintenance.md、spec-index.md 引用路径全部更新
- patterns/ 目录合并后删除，README.md 原「patterns/ 目录」节替换为合并说明

## 4.3.0
- protocal-import.md 全篇重写为三阶段中文协议（P1 准入判断、P2 策略判断、P3 执行），新增 REJECT/SUSPEND 控制流与交互式暂停机制
- README.md 新增设计决策 #8–#12
- protocal-write.md 新增目标前置风格的定位节
- protocal-maintenance.md 新增目标节、理解验证提示与加法模式提示
- design-tags.md 新增约定标签（Seed Tags）子节
- templates/seed/TAGS.md 注册 imported 种子标签
- protocal-import.md 修正 P3-S2 步骤编号引用错误
- 移除 protocal-import.md 的设计泄漏内容（总体要求设计理由说明、P1-S0 注释规则设计哲学）

## 4.2.0
- protocal-init.md 发现链从附录提升为初始化目标 → 可发现态的共同保证
- design-tags.md Type Identification 措辞修正（「此行首」改为「这些标识」）
- protocal-init.md 补充复制种子文件后的占位符替换提示（YYYY-MM-DD 与初始化原因）

## 4.1.1
- protocal-init.md 全篇重写为三阶段结构（确定位置、初始化内容、设计发现合约），种子目录不再主动创建，Phase 3 标记为禁止自行执行
- 新增 templates/seed/ 三个种子文件模板（INDEX.md、CLASSIFICATION.md、TAGS.md）
- spec-index.md 新增 What is INDEX.md? 节（Role、Type Identification、与其他骨架文件的关系）
- design-classification.md 新增 What is CLASSIFICATION.md? 节
- design-tags.md 新增 What is TAGS.md? 节
- README.md Section 7 从「最小种子 + 设计模式」重写为「三阶段明确分工」
- SKILL.md Linked Files 新增 templates/seed/ 引用行，Journal Initialization 描述更新

## 4.1.0
- README.md 完整重写为独立设计锚定文档（10 节精简至 7 条真实设计决策，修正 12 处事实错误）
- SKILL.md Operating Rules 改为 Operating Principles（12 条行为指令改 6 条设计原则）
- Journal 概念重新定义为 Agent 的长期记忆笔记本（读不加载 skill，四种子目录）
- patterns/dashboard.md 重写为项目/领域级次级 INDEX 设计参考
- .maintenance-memo.md 生命周期重新设计（初始化不创建空文件，Phase 4 完成后清理）
- 新增 references/spec-note.md（笔记编写指南，从 protocal-write 独立）
- 新增 patterns/dashboard.md 与 patterns/ 目录
- protocal-write.md 新增 Maintenance Signals（日常写入通向维护循环的 memo 入口）
- protocal-maintenance.md 新增 Phase 4 Step 4、Phase 0 memo 上下文段落与技能升级触发信号
- 新增 examples/classification-systems/、references/design-classification.md、design-tags.md、spec-frontmatter.md、examples/journal-standards/
- 闸门引用清理（6 文件 23 处，闸门概念移出 journaling 设计层）
- protocal-write.md 精简为纯工作流程，格式指南移至 spec-note.md
- spec-index.md 重组为核心规范 = 协议声明 + 设计原理
- 维护协议重写为五阶段框架、信号合并优先级
- protocal-init.md 步骤重编号（删除创建空 memo 步骤）
- protocal-import.md 增加 tagging 检查
- 读/写非对称明确化（读取 INDEX.md 不需要加载 skill）
- 移除闸门概念（journaling 设计层）
- 移除 README.md §9「七执行锚点」与 §10「内存定位」
- 移除 protocal-init.md Step 4「创建维护备忘录」
- 移除 DAILY-OPS 文件（拆分为 protocal-write + spec-note）
- C4 敏感信息验证 0 泄露
- memo 鸡和蛋问题由 protocal-write.md Maintenance Signals 解决

## 4.0.0
- initialization.md 重写为发现合约模型（Step 0–7 结构，含载体判定标准、插入指引、验证标准与回退路径）
- index-spec.md 重组（设计哲学、The Six Sections 改 Sections、协议声明扩为 4 项、闸门降级为可选示例、行为闸门上限 9 条、附录删除）
- daily-ops.md 解散，内容并入 note-spec.md、SKILL.md Operating Rules 与 maintenance.md
- note-spec.md 集成完整写入流程（Before Writing、Importing、Supplementing、Frontmatter、Body、After Writing、Before Delivery）
- journal-concept.md 新增 Dynamic Prompt System 节（三层模型：index.md → notes → skill）
- 移除 daily-ops.md 文件
- Startup Protocol 从 41 行精简至 11 行（保留三要素）
- initialization.md Step 0 新增 Pre-Check 决策树（5 种目标路径状态，绝不覆盖现有内容）
- README.md 更新初始化模板描述
- 清除全部 daily-ops.md 交叉引用（Decision Capture 与 Trace-back 移至 SKILL.md，Cascade Rename 移至 maintenance.md）
- maintenance.md 与 note-spec.md 标签规则矛盾统一为「activity tag or meta tag, project tags optional」
- bootstrap entry 模板标签从未注册的 [journaling, meta] 改为 [journal, skill]

## 3.3.0
- 14 个 reference 文件精简为 7 个（移除 4 个非 journaling 文件，合并 3 个内容重叠文件）
- 新增 journal-concept.md（设计哲学文档：定义、执行锚点、机制映射、记忆定位、闸门设计理论）
- index-spec.md 重组（新增设计原则 6 条表、Workspace Dashboard 模式与 REAP/推演方法论附录，AGENTS.md 解耦为「项目入口」）
- daily-ops.md 强化（Action Gate 前设计理由、Decision Capture 时机协议、工具名去耦合）
- SKILL.md 更新（Linked Files 与场景表减至 7 个 reference，版本号更新为 3.3.0）
- 移除 design-principles.md、memory-layer-strategy.md、dashboard-design-principles.md、two-gate-model.md（内容并入 journal-concept、index-spec、daily-ops）
- 移除 concept-vs-operation.md、doc-crossref.md、environment-migration.md、cross-instance-sync.md（非 journaling 相关）
- initialization.md 移除 ~/.hermes/jornal/ 框架特定路径，HERMES_HOME 改为 AGENT_DATA_DIR
- maintenance.md search_files 引用改为通用描述
- note-spec.md 交叉引用从 design-principles.md 改为 journal-concept.md
- README.md 更新 AGENTS.md 引用（→「项目入口」）与过期文件名
- daily-ops.md 第 136 行交叉引用从 design-principles.md 改为 journal-concept.md
- daily-ops.md 工具名（搜索、搜索会话记录、读取文件、编辑工具）替换为通用动作描述
- index-spec.md 范围路由表 AGENTS.md 改为「项目入口」

## 3.2.1
- initialization.md Prerequisites 重写为 4 步决策过程（含平台路径示例与 Record the Path 节）
- initialization.md index.md 模板协议声明新增 Journal root 行
- initialization.md Phase 6 verify 新增 journal root 记录检查项
- initialization.md 新增 Post-Initialization「How Future Sessions Find the Journal」节
- daily-ops.md Session Startup 新增 journal root 未知时的 pre-check 守卫

## 3.2.0
- Pitfalls 重写为 8 条 Operating Rules（历史案例溯源移除，4 条 pitfall 迁移至相应文件）
- Write gate 重新定位为活文档（index-spec.md Section 6 定义设计框架，maintenance 新增闸门审计）
- Action gate 重新定位为活文档（index-spec.md Section 5 框架固定、规则 Agent 维护，maintenance 扩展分节审计）
- 新增 references/initialization.md（六阶段完整初始化协议，含初始化后成长指引）
- SKILL.md description 加入初始化触发，路由表与 Linked Files 新增 initialization.md 条目

## 3.1.0
- 技能从 Hermes runtime（note-taking/journaling/）迁入 metapowers 项目（skills/journaling/）
- frontmatter 规范化（version/author 移入 metadata，移除 hermes 标签与 license，新增 last_updated）
- 新增 README.md 设计文档
- 路径参数化（硬编码 ~/.agents/journal/ 改为 <journal-root>/ 与功能描述）
- 框架概念通用化（SOUL.md、hermes 命令、HERMES_HOME、hermes-backup 改为通用表述）
- 项目名脱敏（Scriptum、kuiq、Ĉalio、鸣愿传说等改为通用指称）
- 标签注册表清除项目特定标签（hermes-ops、scriptum、kuiq、metapowers、hermes-plugin）
- 私有 journal 内容链接移除，改为技能内部互引
- dashboard-design-principles.md 中相对 journal 路径链接改为 references/two-gate-model.md
- 维护备忘路径改为 .maintenance-memo.md 并说明其位于 journal 根
- cross-instance-sync.md Hermes 特定表述通用化（skills 目录、MEMORY/USER、存前自问）
- environment-migration.md Hermes 特定表述通用化（~/.hermes/、HERMES_HOME、fact_store、config.yaml）
- skill-audit-methodology.md Hermes 命令与路径通用化（hermes skills list、archived-skills、clawhub）

## 3.1
- design-principles.md 锚点 #1 重写为「可复现深刻理解」，机制映射表同步更新
- note-spec.md 新增「The summary is not the understanding」节与实质/次要编辑区分
- daily-ops.md Prospective Reading Check 改以锚点 #1 核心问题开头，强化「Self-contained?」要求
- daily-ops.md 新增「Before Writing to MEMORY or USER PROFILE」条件写入门检查
- daily-ops.md 新增 Capture Tiers（即时条目 vs 段落条目）
- daily-ops.md Session Startup 记录维护信号但不强制行动
- daily-ops.md 新增 Over-generalization signals 快速参考
- dashboard-pattern.md 并入 dashboard-design-principles.md（模板 + 何时创建判据）
- 移除 dashboard-pattern.md

## 3.0
- 设计结构两层分离（设计原则 → reference，执行锚点 → SKILL.md）
- 新增标签注册表（受控词表，4 类约 20 标签）
- 新增前瞻性阅读检查（写入前 5 问）
- 新增过度泛化独立守卫
- 渐进式披露：SKILL.md 回到路由角色
- 新增 Inbox/ 目录与写入门
- 新增条目生命周期模型与 status 字段
- 新增维护备忘机制（.maintenance-memo.md）
- 新增概念与操作诊断框架

## 2.0
- 新增四阶段维护协议
- 新增摘要锚定与三个检查点

## 1.0
- 新增 Action Gate 机制（双闸门模型）
- 新增 SOUL.md 启动协议闸门扫描
- 新增五层记忆策略
