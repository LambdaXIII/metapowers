# Proposal

## Why

读者旅程 × 元语境双向失配的逐技能诊断显示：journaling 之外的技能残留同类病灶——文档自述与出处注记（写作语境痕迹留进载体）、欠载判定值（指代、完成条件、度量单位未落笔）、路由不齐（加载时机注解缺失或断链）。其中 agent-prompt-design 病灶最重，用户裁定撤销其发布、开发版原样保留；其余技能按「设计不改、内容尽量优化」收敛为一批 fix 迭代。

## What Changes

- **BREAKING** 撤销发布 agent-prompt-design：删除 `skills/agent-prompt-design/` 发布快照；README 安装示例移除该技能、技能目录条目标注「（开发中）」、生产级计数同步；`skills.sh.json` 的 metapowers 包组移除该成员（按 AGENTS.md 分组纪律，此项以本提案为确认点，评审时可否决）。开发版 `dev/agent-prompt-design/` 与 `openspec/specs/agent-prompt-design/` 一字不动。
- 五个技能逐个内容优化（各自独立提交，均不改行为设计）：
  - **rehearsal**（2.2.1 → 2.2.2）：定位词退出正文（贴合 spec 语言约定）；加载器机制句改写为读者判断句；出处注记与免责叙事剥离；路由补齐（「补充参考」清单补漏、锚点可解析化、八份场景文档反向路由体例统一、supplementary 头部前提句对齐）。
  - **skill-exposition**（1.0.1 → 1.0.2）：extraction 五份头部「本文只讲……由你自行发挥」收敛为加载时机＋效果目标句；通用论述自述（「本文档是……独立站住」）删除；8 个结构模式的选型判据上提为一张选择指引、头部注解体例统一；「读者」按 spec 术语收敛为「学习者」；路由收敛为单处承载。
  - **skill-master**（1.0.0 → 1.0.1）：summary-report / scenario-card 两份模板补具名指针（深层断链修复）；「本文件讲/对应/收」式宣布自述删除（范围声明保留，贴合自家 spec 措辞风格）；仓库层路径与「验证」一词退出正文（贴合 spec 术语）；测试临时目录记法三处统一；「最大并发数」落值；skill-quick-test 重复双表合并。
  - **web-deep-research**（2.5.2 → 2.5.3）：workflow 重复小节标题删除；search-strategy 名实对齐；自述导语与跨文档「出发点一致」叙事清理；报告章节与模板对齐；领域文档 When-to-read 注解补齐；「重要 Q」判据落值。
  - **web-entity-search**（1.3.3 → 1.3.4）：8 处「回 SKILL.md」断链修复（多退一级）；references 七份「XX模板」H1 去化石命名、general.md「此模板用于」串味清理；references/templates 复述漂移三处统一；「结果/轮」度量单位统一、「最相关」等判据落值。
- 📍/头部声明行统一裁定落地：保留「← 回 SKILL.md」导航回链、删除职责短语（职责由 SKILL.md 路由单处承载，消除漂移面），web-deep-research 与 web-entity-search 一次改全；rehearsal 场景文档头部声明行保留（承载使用前提），仅统一缺失的前提句。
- 各被调整技能：`metadata.version` patch +1，`dev/<skill>/CHANGELOG.md` 各记一句话条目。web-entity-search 与 web-deep-research 的内容修改同步刷新发布快照与否，随统一发布流程走（用户发起）。

## Capabilities

### New Capabilities

（无——本变更不引入新行为能力。）

### Modified Capabilities

- `skill-grouping` —— 「现行包组 metapowers」成员清单移除 agent-prompt-design（5 → 4），与 skills.sh.json 声明保持一致。这是撤销发布唯一的契约面变更；其余修改均为内容/表述/路由级，按「规格赢、改内容贴合规格」处理，各技能域规格不动。

## Impact

- 发布面（BREAKING）：`skills/agent-prompt-design/` 消失，`npx skills add LambdaXIII/metapowers --skill agent-prompt-design` 不再可用；README、skills.sh.json 随之同步。
- 开发面：dev/agent-prompt-design 与其规格零改动，技能开发可在其上继续，未来重新发布走正常发布流程。
- 五技能修改全部为表述/路由/欠载级，行为契约不变；诊断中发现的规格冲突（定位词入正文、「验证」术语、spec 术语「学习者」、内容多出「一手来源直填」例外）一律修内容贴合规格。
- 发布动作（快照刷新 + main `--no-ff` 合并）由用户发起，不在本变更内自动执行。
- journaling 不在本批：`rework-journaling-reader-journey`（5.1.2）已覆盖同惯性修复。
- 只报不改、留待独立提案的争议口径：web-deep-research description 方法措辞是否越界、spec「硬约束单独成文」的解读。
