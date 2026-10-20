# Tasks

## 1. 撤销发布 agent-prompt-design（独立 chore 提交）

- [x] 1.1 删除 `skills/agent-prompt-design/` 发布快照（开发版 `dev/agent-prompt-design/` 与其 spec 零改动）
- [x] 1.2 README 同步：安装示例（:54）移除 `--skill agent-prompt-design` 一行；技能目录条目（:64-66）标注「（开发中）」；「6 个生产级技能」（:34）计数修正
- [x] 1.3 `skills.sh.json` 的 metapowers 组移除 agent-prompt-design（确认点＝本提案评审，AGENTS.md 分组纪律；若评审否决则保留成员、跳过 1.4 并回退 delta）
- [x] 1.4 与 skill-grouping delta（5→4 成员）保持一致，作为同一逻辑变更一并入 chore 提交

## 2. rehearsal 修复 → 2.2.2（独立 fix 提交）

- [x] 2.1 定位词退出正文：SKILL.md:32 的 `quick`/`fast`、defect-taxonomy.md:4 的「快速」改中性表述（贴合 spec 语言与指称约定）
- [x] 2.2 SKILL.md:41 加载器机制句（the description is what the loader matches against）改写为面向读者的触发判断句
- [x] 2.3 出处/免责/叙事剥离：defect-taxonomy.md:4,6 来源与免责句、:12/70/143/171 四段「归类理由」改判定说明或删；knowledge-base-rehearsal.md:116-118 具体分数与 :127「某设计方法论文档知识库（节选）」出处注记；doc-guide-rehearsal.md:140-147 FAQ 两问并入正文去 FAQ 形态
- [x] 2.4 路由补齐：rehearsal-guide.md:238-243「补充参考」补 `agent-paired-reading.md`（带一句适用条件）；:113 锚点改可解析（去 `#…` 或改文件级链接）；SKILL.md:74 章节名与通用论述实际标题「场景特化参考」对齐；其余 6 份场景文档补「不适用 → 对应场景文档」反向路由；defect-taxonomy.md:2 补「假设已读通用论述」前提句统一体例
- [x] 2.5 欠载落值：defect-taxonomy.md:27「新增的特定路径」补参照基准；:130 示例文件名改可解析或标注示例占位
- [x] 2.6 SKILL.md 双清单合一：Reference files 清单承载路由（含加载时机），Directory tree 去逐文件注释只留结构，消除同批文件两处罗列
- [x] 2.7 defect-taxonomy §修复模式的「📍 本文件是……」处方补适用边界（仅开给被推演的知识库产物，技能自身文档不套用）
- [x] 2.8 `metadata.version` 2.2.1 → 2.2.2，`dev/rehearsal/CHANGELOG.md` 记一句话条目，独立提交

## 3. skill-exposition 修复 → 1.0.2（独立 fix 提交）

- [x] 3.1 extraction×5（workflow/knowledge/rule/example/rationale-content.md:3）头部 blockquote 收敛：保留「按需加载」时机与括号内路由指向，删「本文只讲……」自述与「由你自行发挥」口吻
- [x] 3.2 自述与口吻清理：exposition-guide.md:3「本文档是……独立站住」删（保留「需先读本文件」路由语义）；:114/129/137 与 general/readability.md:3 的「自行发挥/均由你判断」改「确保……」效果目标句（贴合 spec 边界模型）；:139「本次调用的交付物」等调用侧机制改中性表述
- [x] 3.3 8 模式选型判据上提：在 SKILL.md 参考区或 exposition-guide 加一张模式选择小表（模式 / 组织轴与适用特征 / 何时不选，信息从各 pattern 已有的「适用情况＋与 X 的差异」上提，不新写方法论）；8 份 pattern 头部注解体例统一（组织轴一句话＋按需加载，learning-path 标注默认）
- [x] 3.4 术语收敛：面向教学对象的「读者」按 spec 统一为「学习者」（按受影响概念清单逐处核对上下文，泛指处保留）
- [x] 3.5 路由单处承载：SKILL.md:53「see routing table below」与实际形态一致（改为清单指称）；exposition-guide 文末路由表与 SKILL.md 清单分工明确（去重复定义）；SKILL.md 入口补一句完成判据（对照 guide §5 效果清单自查）
- [x] 3.6 其余自述句清理：general/traps.md:3、general/readability.md:3、general/multi-skill.md:3、structure/pattern-learning-path.md:3（范围/适用信息保留，「本文」主体表述删）
- [x] 3.7 `metadata.version` 1.0.1 → 1.0.2，`dev/skill-exposition/CHANGELOG.md` 记一句话条目，独立提交

## 4. skill-master 修复 → 1.0.1（独立 fix 提交）

- [x] 4.1 深层断链修复：summarization.md「报告输出」节、scenario-design.md「场景卡片格式」处补具名指针指向 `templates/summary-report.md` / `templates/scenario-card.md`（带触发条件）；skill-quick-test.md:92 泛指目录句改逐文件指针三要素写法
- [x] 4.2 宣布式自述删（贴合自家 spec 措辞风格，范围声明保留）：skill-md-writing.md:5、disclosure.md:5、structure.md:3、standards.md:3、scope-analysis.md:7、scenario-design.md:5、scoring-rubric.md:121
- [x] 4.3 开发侧知识与禁用术语退出正文：standards.md:11/:32「本仓库/本技能的开发环境」改中性示例、`content/` 换技能根表述；skill-quick-test.md:7/8/69「验证」换工作定名（贴合 spec 术语表述）
- [x] 4.4 欠载落值与记法统一：测试临时目录三处（skill-quick-test.md:53、execution-full.md:25/27、summarization.md:12）统一为「`SKILL_TEST_DIR` + `<temp-dir>/round-<id>/` + 默认 `<cwd>/.quick-tests/`」一套写法；execution-light.md:174「最大并发数」给可判定值与默认批次策略
- [x] 4.5 重复与自相矛盾消减：skill-quick-test.md 顶部「六步测试设计」表与底部「方法目录」表合一（一份文件只出现一次）；error-patterns.md E4 回链约定收窄为「叶子方法文件须带回链」，与 structure.md:9「根不被指向」对齐，并按裁定对齐各册尾注
- [x] 4.6 scoring-rubric.md:87 落点修复：templates/test-plan.md 补承载定制维度的字段或措辞改指实际字段；「打分/评分」统一为一处（按 spec 术语）
- [x] 4.7 `metadata.version` 1.0.0 → 1.0.1，`dev/skill-master/CHANGELOG.md` 记一句话条目，独立提交

## 5. web-deep-research 修复 → 2.5.3（独立 fix 提交）

- [x] 5.1 workflow.md:292 重复小节标题「三层编号体系」删除
- [x] 5.2 `references/search-strategy.md` 改名 `references/orchestration.md`（改前 grep 全量引用面）：SKILL.md Content Index 行、文内链接、文件 H1 与职责表述同步名实
- [x] 5.3 自述与叙事清理：search-strategy.md:5-9 自述块（保留与 Content Index 一致的加载时机）、workflow.md:5-8「本技能的驱动结构是……」导语直入正文、person-biography.md:63 跨文档「出发点一致」叙事删（保留本地理由）
- [x] 5.4 欠载落值：workflow.md:184-185「重要 Q」判定标准与「低置信度消解」切换条件；:282-286 三类交付形态补显式选择判据
- [x] 5.5 流程与模板对齐：report-template.md 补「后续建议」节（或删 workflow 该节，二选一以模板为准）；「资料来源（与摘要）」「交叉比对（与发现）」章节命名统一；SKILL.md:53 template 行补「未采用来源」节；SKILL.md:50-52 三行 When-to-read 补与其余领域文档一致的 Phase-0 加载时机注解
- [x] 5.6 📍 声明行 10 处收敛为一行 `[← 回 SKILL.md](../SKILL.md)`（删职责短语与装饰，按 design 裁定）
- [x] 5.7 `metadata.version` 2.5.2 → 2.5.3，`dev/web-deep-research/CHANGELOG.md` 记一句话条目，独立提交

## 6. web-entity-search 修复 → 1.3.4（独立 fix 提交）

- [x] 6.1 断链修复：8 个 `references/*.md:3` 回链 `../../SKILL.md` → `../SKILL.md`（与 6.6 同处一次改全）
- [x] 6.2 命名化石与串味清理：references 七份 H1 去「模板」二字（与 templates 孪生拉开身份差，如 `# 人物` → `# 人物搜索指引`）；general.md:5-12「此模板用于……」用途宣布块删除，其中分类兜底判据归位 workflow Step 2 / SKILL.md Content Index 兜底行，「专用模板」指代明确到文件族
- [x] 6.3 references/templates 复述漂移统一三处：creative-work「类型/题材」必填性（维度表与模板首句二选一对齐）、concept-term「为什么重要」必填 vs 省略许可（与 workflow.md:71「不跳过」一致）、person「活跃期」在模板句式补名位；company「成立/起源」与 creative-work 创作者分媒介两处低危顺手对齐
- [x] 6.4 欠载落值：workflow.md:15-16 委派场景无用户通道时按 SKILL.md 推荐路径择最可能指代继续并注明推断（不阻塞）；:26「最相关」给判定标准、「一轮快速搜索」给度量；:28 重判回边加约束；:40/43「结果/轮」度量单位统一；templates/event.md:7「则标注」落值为具体标法
- [x] 6.5 workflow.md:42「一手来源可单源直填」例外删除，贴合 spec 停止纪律（≥2 来源即填充）；如需放宽走独立提案
- [x] 6.6 📍 声明行 8 处收敛为一行 `[← 回 SKILL.md](../SKILL.md)`（按 design 裁定）
- [x] 6.7 `metadata.version` 1.3.3 → 1.3.4，`dev/web-entity-search/CHANGELOG.md` 记一句话条目，独立提交

## 7. 验收与收尾

- [x] 7.1 机械面验收：病灶签名 grep 在五技能 content/ 内归零（自述/出处注记/整理日期/口吻词；示例引文逐条核豁免）；改名与回链后全量链接可解析；四点 spec 冲突（定位词、「验证」、「学习者」术语、「一手来源直填」）复核归零；frontmatter 与 CHANGELOG 体例合规
- [x] 7.2 冷读面验收：五技能各一轮冷读推演（用 rehearsal 场景文档推演技能内容），只修高/中危发现，低危记 CHANGELOG 或留观
- [x] 7.3 一致性核对：skill-grouping delta 成员枚举与 skills.sh.json 实际清单一致；`openspec validate --all` 全绿
- [x] 7.4 向用户展示完整 diff，获明确同意后合并（`--no-ff` 回 dev）；其余技能快照刷新与 main 合并属发布流程，由用户发起
- [x] 7.5 经用户确认后归档本 change（`/openspec-archive-change` 把 skill-grouping delta 折回主树）
