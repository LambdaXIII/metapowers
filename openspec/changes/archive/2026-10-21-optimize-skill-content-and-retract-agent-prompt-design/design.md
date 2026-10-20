# Design

## Context

五技能（rehearsal / skill-exposition / skill-master / web-deep-research / web-entity-search）已完成逐个诊断，病灶归四类：**渗入**（文档自述、出处注记、历史叙事、编辑者口吻）、**欠载**（指代未定、完成条件缺位、度量单位不一、异常出口缺失）、**结构化石**（命名/切分冻结写作演化史）、**路由不齐**（加载时机注解缺失、断链、指针漏写），另有一批与各自 spec 的表述冲突。诊断清单按技能列入 tasks.md。约束：AGENTS.md「规格与技能内容冲突时规格赢——改内容」；设计内容分离；原子修改（整文件重写先备份）；一提交一逻辑变更；用户基线「不求完美，只求尽量优化」。动机见 proposal.md - Why。

## Goals / Non-Goals

**Goals:**
- 渗入类清零（自述、出处注记、历史叙事、口吻），欠载类落值（单处定义、引用别处），路由闭环（何时读什么在 SKILL.md 单处承载、指针可达、断链归零）。
- spec 表述冲突全部以修内容收敛，各技能域规格零改动。
- agent-prompt-design 发布面干净撤销（快照、README、分组），开发版与其规格零改动。
- 五个被调整技能各出一个 patch 版本与一句话 CHANGELOG 条目，可随用户发起的发布流程独立上线。

**Non-Goals:**
- journaling：已由 `rework-journaling-reader-journey`（5.1.2）覆盖，本批不重复诊断。
- `dev/agent-prompt-design/` 与 `openspec/specs/agent-prompt-design/`：一字不动。
- 除 `skill-grouping` 外的任何规格改动；有争议的 spec 口径（web-deep-research description 方法措辞、「硬约束单独成文」解读）只报不改，留独立提案。
- 发布动作本身（其余技能快照刷新、main `--no-ff` 合并）：由用户发起，不在本变更执行。

## Decisions

1. **修复转化口径**（四类病灶各自的处理法，全批统一）：
   - 渗入 → 先归位后删除：有承载功能的信息（术语定义、加载时机、读者前提）翻成读者语境的表述归入正文或路由，其余（出处注记、整理日期、免责、「由你自行发挥」口吻、跨文档「出发点一致」叙事）直接删。信息无辜，表述有罪。
   - 欠载 → 单处落值：给判定值、指代、完成标志、度量单位一个名字和一处定义，别处引用。**fix 边界**：只补既有设计意图内的值（如「最大并发数」默认值、委派场景无用户通道时按已知推荐路径不阻塞）；凡属新增行为语义的点不做，宁缺勿扩。
   - 结构化石 → 名实对齐：命名与切分向领域职责看齐，改名同步全部引用面（SKILL.md 路由行、文内链接）。
   - 路由 → SKILL.md 单处承载「何时读什么」，参考文档间互相指路但不重复职责描述。
2. **📍/头部声明行裁定**：判据是**路由由加载指引承载时，文内职责声明是复述（漂移面）；文档允许直接进入时，导航回链是收束**。落法：
   - web-deep-research（10 处）与 web-entity-search（8 处）：统一收敛为一行 `[← 回 SKILL.md](../SKILL.md)`——保留导航回链（直接落进单个文件的读者需要回主入口），删除职责短语与装饰（职责由 SKILL.md Content Index 单处承载；已见漂移实证：web-entity-search 参考文件 H1 自称「模板」与其职责矛盾）。一次改全，不留半删半留。
   - rehearsal：8 份场景文档头部「场景文档 — 配合推演通用论述参考使用……」保留（承载读者前提与使用方式），只给 defect-taxonomy 补齐缺失的前提句以统一体例；defect-taxonomy §修复模式 的「📍 本文件是……」处方保留（它开给**被推演的知识库产物**，那些文件允许直接进入，声明行是收束），补一句适用边界防机械套用到技能自身。
   - agent-prompt-design 的「📍 本文件是……」不动（开发版零改动）。
3. **spec 冲突一律修内容**：定位词退出 rehearsal 正文、「验证」退出 skill-master 正文、skill-exposition 正文「读者」按其 spec 术语收敛为「学习者」、web-entity-search 删除「一手来源可单源直填」的放宽（其 spec 停止纪律为 ≥2 来源）。规格是契约权威，本次不改规格迁就内容。
4. **search-strategy.md 改名 `orchestration.md`**：文件名 fossilize 了旧职责（搜索策略），实际职责是编排策略，SKILL.md 的 Purpose 已写 "Orchestration strategy"。改名同步 SKILL.md Content Index 与文内引用（引用面小，改前 grep 全量确认）。备选「只改标题不改名」被否：名实不符是诊断点名的中危病灶，文件名是路由信号，留着就是留病灶。
5. **版本与提交纪律**：patch +1 清单 = rehearsal 2.2.2、skill-exposition 1.0.2、skill-master 1.0.1、web-deep-research 2.5.3、web-entity-search 1.3.4（版本号不在过程中递增，随各技能修复完成的那次提交一起改；CHANGELOG 一句话条目同提交入「未提交」区）。提交切分：撤销发布独立 chore 提交（含 skill-grouping delta 折回与 skills.sh.json/README 同步），五技能各一个 fix 提交，互不混装。分支：`rework-journaling-reader-journey` 合并回 dev 后，从 dev 起 `fix/optimize-skill-content-and-retract-agent-prompt-design`。
6. **skills.sh.json 分组移除的确认点**：AGENTS.md 要求分组变更经用户确认——以 proposal 评审为确认点；若评审否决此项，则 skills.sh.json 保留成员、skill-grouping delta 回退为原枚举（快照删除与 README 撤销不受影响）。
7. **验收口径**（tasks 的验证面，三层分开）：
   - 机械面：病灶签名 grep 归零（「本文件/本文档是/此文件/本协议定义/整理日期/来源：/由你自行发挥/仅作参考」在 content/ 内零命中，示例引文除外逐条核）、断链检查（改名与回链修复后全量链接可解析）、四点 spec 冲突复核。
   - 冷读面：每技能一轮冷读推演（用 rehearsal 自身的场景文档推演技能内容——它就是这类工作的量具），只修高/中危发现，低危记入 CHANGELOG 或留观。
   - 一致性面：术语统一按受影响概念清单扫引用面（不只扫关键词）；frontmatter 与 CHANGELOG 体例合规；`openspec validate --all` 全绿，skill-grouping delta 与 skills.sh.json 实际成员一致。

## Risks / Trade-offs

- 术语统一（skill-exposition「读者→学习者」等）波及面广，逐文件替换有误伤风险——按概念清单人工核对上下文，泛指「读者」确需区分处保留。
- web-entity-search 回撤「一手来源直填」使官方一手信息也需第二来源确认，效率换合规——要放宽语义应走独立提案改规格，不在本 fix 夹带。
- 五技能并发修改共用一套口径，若口径本身有偏将被放大——口径（尤其 📍 裁定）在 proposal 评审时一并确认。
- 删除 `skills/agent-prompt-design/` 后 dev 与发布短暂漂移，直至用户发起发布——可接受：快照本就是可再生产出，恢复发布只需正常发布流程。
