# Changelog

## 2.1.0
- batch-execution 策略重心从「效率+聚合」改为「复现保真」（多场景串行自推演给不出 N 次首次接触），子代理信息隔离是保真前提，并行是顺带收益
- batch-execution 委托边界反转：子代理只承担 P3 逐段阅读，下发限于身份/目标、入口/材料、输出格式四项，不再下发推演方法、评估维度与验证点
- batch-execution 聚合保留有效洞察（自述报告按根因归纳、呈现顺序≠修复顺序、矛盾单列），★ 打分移到主侧汇总时产出
- batch-execution 删除与 knowledge-base 场景文档的角色矩阵复述，设计职责归还场景文档
- rehearsal-guide P5 开头新增「推演止于评估」边界声明
- rehearsal-guide P3 阅读纪律新增第 3 条「标题先于正文推演」（文件名/节标题是读者最先消费的推演对象而非确定坐标框）
- 移除 batch-execution「生成修复计划」步骤与「与其他文档的关系」整节
- 移除 batch-execution 经验观察表与评估矩阵/热力图/频率三档模板（仅保留「呈现规模随发现数量走」提示）
- SKILL-DESIGN 新增「批量委派的信息隔离」设计决策

## 2.0.4
- description 触发词由 20+ 穷举收敛为高频代表，载体列举 7 项改为概括，保留中英双名/载体列举/双路径触发/反向一条五构成元素

## 2.0.3
- SKILL.md 正文新增「Delegate or continue reading」路由节（简单快速的推演委托子代理，材料复杂或需严谨评估时继续阅读完整流程）
- description 维持测试定型的五个匹配元素，不承载委托/加载类执行指令
- SKILL-DESIGN 新增「委托路由：轻推演交给子代理，重推演自己读」设计决策

## 2.0.2
- SKILL.md 正文全量英文化（触发条件、参考文件路由、目录树与中文原版实质一致）
- description 保留中英双名与中英双路径触发词，中文自问短语补回并作为主触发面之一
- 正文措辞遵循「接收方」约定，以 reader/recipient 语义称呼被模拟对象
- description 第 2 条末尾 `(English: …)` 翻译残留括号删除

## 2.0.1
- 缺陷分类法以「元语境渗漏」（Context Leak）统一「悬空参照」与「身份边界错位」两类形态，判定标准为读者身份检验
- 渗漏修复分删除/归位/转化三类穷尽（保持约束强度同档转化）
- defect-taxonomy 新增「不正确的暗示」缺陷类型（偏差方向）及两类归类判据
- guide P3 留意清单新增「元语境渗漏」「不正确的暗示」两条识别条目，P5S5 补充多处元语境渗漏错误模式示例
- P1 准备完成标志新增三条可检查完成判据（范围声明、读者画像与要素、意图清单覆盖三类来源）
- P3 留意清单新增收束步骤（每个模式必须给出「检查过、无发现 / 检查过、有发现」）
- 新增「嵌入优于收网」切换时机（材料合稿时停止逐段推演，合稿后必做全景推演）
- P4 边界尝试操作化（「上游已保证」定义为材料中显式声明，边界尝试与 P5「边界覆盖」挂钩）
- 委派条件操作化（「材料比较简单」给出可检查近似：单文件、逻辑单元 ≤ 10、读者单一、决策路径 ≤ 3）
- taxonomy 补充「重复」方向引子，与劣化/偏差/过度三向对齐
- defect-taxonomy 两类渗漏改称「元语境渗漏（悬空参照/身份边界错位）」，新增「信号词线索」，「引用类渗漏」补机械验证方法
- guide P1S3 整理后果表述改为「整理是 P2 划掉的前提，否则放过材料中的元语境渗漏」
- guide P3 元语境渗漏条目承载识别操作，信号与修复指向 taxonomy 不重复展开
- guide P3 阅读纪律与理解状态循环由逐段改为逐逻辑单元，偏离处才展开记录
- SKILL-DESIGN 追加「元语境渗漏：锚定作者身份框架 + 修复三分」「完成判据操作化」两个设计决策
- SKILL.md「三元素、四步流程」旧框架术语残留修正为「推演步骤 P1-P5、四向复现」
- SKILL.md「不合触发」第 4 条自相矛盾移出为独立「澄清」段
- SKILL.md description 中文触发词补「卡住 / 看不懂 / 新人会不会卡」，触发词前补「对象为交付物」限定
- guide 评估维度表「术语一致性」改为「术语全局统一」（消除与场景文档共 7 处同物异名）
- guide P4「建议」加粗位置修正
- guide P3 元语境渗漏条目 taxonomy 引用补 # 锚点
- 场景文档两处「身份边界错位」改称「元语境渗漏（身份边界错位）」
- taxonomy 速记泄漏示例 L0/L1/L2 改为中性示例
- 8 个场景文档尾部补「回到通用论述」收束
- 场景间文件名引用链接化
- api-design 10 处「端点」空格伪影与 doc-guide、CHANGELOG 空格伪影清理
- batch-execution 绕路路径改为同目录直接引用
- SKILL.md/guide 路由条目补 batch-execution 对 knowledge-base 角色矩阵的依赖披露
- SKILL.md 场景文档清单补「何时加载」引导
- prompt-instruction / logic-chain 评估维度表标注「在通用论述基础上扩展为 M 项」

## 2.0.0
- 复现质量检查扩展为四向（新增「重复」方向，区分引用/提及与重复定义或描述）
- 新增推演步骤 P1-P5 结构（P1 准备、P2 身份转换、P3 模拟阅读、P4 回顾、P5 评估整理）
- 新增范围确定机制（起步声明 + 主动搜索焦点，阅读范围 ⊇ 推演范围，上下文材料只读不推演）
- 新增 P3 阅读机制（阅读和理解是两个动作，每段产出理解状态，最终理解状态作为 P5S1 输入）
- 新增留意之处清单（静态模式 5 条 + 动态信号 2 类）
- 新增身份边界错位概念（材料混入作者身份内容，与 Context Leak 区分）
- 「推演止于评估」定位确立（是否修改、如何修改、是否通过不在推演技能范畴）
- 新增委派并行推演执行策略（单推演者委派子代理代读、多场景批量执行）
- defect-taxonomy 新增三类缺陷（重复呈现/冗余定义、身份边界错位、过度承诺/强度放大）
- 通用技能设计方法论固化到 AGENTS.md（§4.6 description 规范、§4.7 references 组织原则，§2.7 补「开发速记不泄漏」）
- guide P5S3 严重程度格式示例补充计划文档与知识库
- guide 路由表 plan 条目维度描述改为实际维度名
- 通用论述全量重写（三元素+四步流程改为 P1-P5，三节合并入「推演是什么」，移除局限性与「快速/零成本」定位词）
- 术语统一：客体 → 读者（通用语境），场景特化称呼保留（执行者/模型/操作者/调用者/执行引擎）
- 10 篇参考文档全量重写（场景文档改为自由组织的载体特化补充）
- defect-taxonomy 按四向复现重新组织，脚手架残留从 Context Leak 拆分
- SKILL-DESIGN 全量重写为方向锚定版（删除历史性内容，新增三个设计定位与推演止于评估）
- AGENTS.md §2.5/§4.2 SKILL-DESIGN 定位强化（锚定设计方向，不是历史记录）
- 委派推演三处层次化（guide 策略推荐、prompt-instruction 执行方法、batch-execution 批量执行）
- 各场景文档评估维度表标注「额外提示，非硬性指标」
- plan-rehearsal 与 design-doc-rehearsal 边界声明修正
- logic-chain「唯一模拟对象非人」断言修正为「唯一模拟无理解、无判断、纯机械精确执行」
- doc-guide 常见问题 Q2 与「嵌入优于收网」执行策略对齐
- batch-execution 术语修正（测试用例→推演场景）、补打分机制与聚合呈现说明、补异常处理
- 移除通过标准（doc-guide 单文档/全流程、plan）——推演止于评估
- 移除局限性与同体模拟论述
- 移除三元素、四步流程、边界刨、逐帧跟、清空、作者视角步骤等旧框架术语与概念
- 移除 guide 完整示例节
- 移除「每个维度必须有记录」等硬性表述，改为提示性
- 移除 doc-guide 常见问题 Q1（推演 vs 审阅）
- 移除 design-doc 微型示例，knowledge-base 大示例表压缩为角色矩阵节选
- 移除各场景文档「看作者视角/设定阅读身份/显式清空」三步重复模板

## 1.6.1
- plan-rehearsal.md 清空补充新增「状态传递假设」清除项
- plan-rehearsal.md 链路段「边读边执行」洞察转化为逐帧跟阶段可操作检查指令（随机选非起始步骤验证上下文独立性）
- rehearsal-guide.md 路由表 plan-rehearsal 条目从全列 9 维简化为 3 项核心维度 + 计数
- SKILL.md 参考列表 plan-rehearsal 条目同步简化

## 1.6.0
- description 重写以修复加载失败问题（核心名仅现于反向语境、首句非用户提问用语、场景枚举过窄、缺 agent 自问触发维度）
- 新 description 结构：一句话精简定义 + 12 类交付物枚举 + 中英双语用户触发语与 agent 自问两条触发路径 + 单条反向条件
- SKILL.md 正文新增「触发条件」节（合触发/不合触发/边界判定三层），纠正「纯代码逻辑验证 → 用 logic-chain-rehearsal」的反向误导
- SKILL-DESIGN.md 追加「description 作为加载器匹配面」设计原则

## 1.5.0
- 第四步从「打分」重设计为「评估整理」（五个子步骤：意图对照、发现归类、严重程度判定、修复优先级与覆盖检查、错误模式提取）
- 严重程度格式从 ★ 1-5（默认）改为阻塞/缺陷/建议，仅知识库保留 ★ 1-5 作为跨版本测量工具
- 全部 7 个场景文档 step 4 重构为「参照通用论述 + 载体特有要求」结构，每场景补充 2-3 个载体特有错误模式
- design-doc-rehearsal 原「推演执行」末尾汇总段提取为独立评估整理节
- doc-guide-rehearsal 通过标准从 ★ 阈值（无 ≤2★）改为阻塞级判定（无阻塞级发现）
- rehearsal-guide.md 示例从 ★ 表格改为阻塞/缺陷/建议格式
- 通用论述严重程度格式表、SKILL.md 引用措辞、batch-execution.md 术语全员对齐（打分 → 评估整理）
- SKILL-DESIGN 决策 #7 重写为「评估整理环节的设计」（从历史叙事改为设计决策说明）

## 1.4.0
- L0 通用论述新增「0. 作者视角」步骤（推演前明确目标读者、设计意图和前置假设）
- L0 通用论述新增「维护者须知」节（目录分组理由和开发速记边界）
- prompt-instruction-rehearsal 新增「推演前：锁定作者视角」节
- prompt-instruction-rehearsal 新增「委派推演（推荐）」节（子代理阅读机制和提示词模板）
- L0「清空」步骤重写为包含身份设定和显式约束声明的操作流程
- prompt-instruction-rehearsal「清空」重写为「准备与清空」三步操作
- prompt-instruction-rehearsal 常见陷阱新增「混淆客体」与「跳过作者视角直接清空」
- doc-guide、interaction、api-design、logic-chain 四场景清空深化为三步 + L0 引用
- design-doc、knowledge-base 两场景新增清空步骤
- SKILL-DESIGN 新增「文档定位」段（本文件与其他文档的边界）
- SKILL-DESIGN 移除决策 #5、#6（操作日志移入 CHANGELOG v1.0.0）
- SKILL-DESIGN 新增「目录分组」（决策 #2）与「开发速记边界」（决策 #6）决策，决策按架构→组织→操作→专项重新排序
- SKILL.md 描述重写为结构化格式（触发条件 + 4 个何时使用场景 + 3 个何时不使用排除）
- defect-taxonomy 新增 Context Leak（上下文泄漏）缺陷条目（三种子类型的信号识别和修复模式）
- L0 作者视角新增 Context Leak 动机说明（跳过步骤 0 的典型后果）
- 修复 5 处 Context Leak 实例（L0 超前引用×2、logic-chain 脚手架残留×1、prompt-instruction 速记泄漏×1、knowledge-base 编号冲突×1）

## 1.3.0
- 移除技能内容中全部 L0/L1/L2 层级代号，改用自然语言表述（必读入口、场景文档、补充参考）
- 参考文件按目录分组（scenarios/ 7 个场景文档、supplementary/ 2 个补充参考）
- SKILL.md 参考区从表格改为分组列表，目录树反映新子目录结构
- rehearsal-guide.md 路由表分为「场景路由表」和「补充参考」两段
- 所有文件头部代号替换为自然语言描述，交叉引用路径适配新目录结构
- SKILL-DESIGN.md 术语同步至自然语言表述

## 1.2.0
- 新增场景文档 prompt-instruction-rehearsal.md（提示词/指令集推演，含双重定位原则与双层观察框架）
- 新增场景文档 interaction-rehearsal.md（交互流程推演，合并 UI + CLI 两种模式）
- 新增场景文档 api-design-rehearsal.md（API 接口契约推演，严格限定在接口层面）
- 新增场景文档 logic-chain-rehearsal.md（逻辑链路推演，泛化至代码/配置/规则/数据管道）
- L0 新增「推演者定位」通用原则节
- L0 打分维度表新增逻辑链路载体类型，UI 流程扩展为交互流程
- L0 路由表扩充至 7 个 L1 文件
- SKILL.md 参考文件表和目录树扩展至 10 个文件

## 1.1.0
- 参考文件按 L0/L1/L2 三级重组（SKILL.md 简化为极简入口，通用方法迁移至 L0 rehearsal-guide.md）
- doc-guide-validation.md 改名为 doc-guide-rehearsal.md（L1），移除旧 L1/L3 层级术语
- design-doc-validation.md 改名为 design-doc-rehearsal.md（L1），更新交叉引用文件名
- knowledge-base-validation.md 改名为 knowledge-base-rehearsal.md（L1），旧 L3 术语替换为 L0/L1/L2 体系
- batch-execution.md、defect-taxonomy.md 分类为 L2 并添加 L2 文件头
- SKILL.md 中「与其他方法的区别」「局限」「示例」完整迁移至 L0
- 移除空目录 templates/、examples/、scripts/

## 1.0.0
- 初始版本，从 Hermes `tuiyan` 技能通用化导出
- 中文「推演」方法论重构为通用 `rehearsal` 技能，去除所有平台特化内容
- 保留核心三元素（客体、载体、链路）和四步流程（清空、逐帧跟、边界刨、打分）及已验证原则
- 触发条件从 Hermes 项目特化重写为通用载体分类
- 子代理执行参考从 `delegate_task` 机制通用化为抽象「并行协作者」模式
- 参考文件迁移与裁剪（doc-guide-validation、design-doc-validation 保留去敏，skill-validation 通用化为 knowledge-base-validation，batch-subagent-execution 保留为 batch-execution，skill-defect-taxonomy 保留为 defect-taxonomy，document-qa-pattern 不纳入）
- 移除 document-qa-pattern.md 参考文件
- 移除所有引用 Scriptum、Steward Agent、Hermes 的示例和上下文
- 移除 Skill、SKILL.md 等 Hermes 特有概念内容（通用文档中替换为「指令集」等术语）
