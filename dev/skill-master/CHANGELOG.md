# Changelog

All notable changes to this skill will be documented in this file.

格式遵循 [Keep a Changelog](https://keepachangelog.com/)；版本号在功能完成后统一确定，开发期间不逐次递增。

## [Unreleased]

### Added

- 初始化技能骨架：SKILL.md 入口（极简形态：触发条件 + 路由引导）与
  references/skill-master-guide.md 方法主文档占位

- 三工作论述成文：skill-design.md 重写为八节论述（锚定 / 材料从哪来 /
  组织与打包 / 编写 / 披露 / 验证 / 推荐路径 / Gotchas）；
  skill-modify.md、skill-review.md 由提纲扩写为论述（含审查的两种输入
  形态与七个审查维度）
- 新增 documents/ 四册：essay-writing（论述型编写）、workflow-writing
  （工作流型编写）、template-writing（模板编写）、writing-craft（编写
  手艺共享层）；新增 scripts/ 两册：script-design（脚本设计论述）、
  scripting-craft（脚本手艺）；新增 general/ 两册：standards（开放标准
  规范册）、disclosure（披露设计论述）

### Changed

- 架构定为多 guide 任务分流：按任务类型（设计 / 修改 / 调试 / 审查）各自
  成册，SKILL.md 改为纯路由入口；新增共享编写手艺层 writing-craft.md（次级命名），任务分册以 skill-<task> 命名
- skill-design.md 由提纲充实为论述正文；结构与材料的分册（通用组织规范、
  类型结构分册、材料提炼）仅在本档内预留拟定文件名，未创建文件
- 新增 references/design/structure-general.md《技能组织通用规范》：先技能
  开放标准规范条目（目录结构、frontmatter、渐进式披露、校验），后实践
  沉淀的组织经验（SKILL.md 入口化、主文档独立站住、路由分派与兜底）；
  skill-design.md 结构节登记为实际可读分册
- 新增类型特化结构分册三篇（素材取自 journal Skill Dev 域，体例与
  structure-general 衔接，读者默认先读通用分册，不重复其条目）：
  references/design/structure-knowledge.md《知识型技能结构》、
  structure-operation.md《操作型技能结构》、structure-template.md
  《模板型技能结构》；skill-design.md 结构节路由表由拟定转为实际文件
  并补「何时读」
- 四篇 structure 分册经 journal Skill Dev 域全量经验研读与仓库已发布技能
  组织形态对照后重新整理定稿：structure-general 扩充规模治理（臃肿/沉积
  诊断、类型分流、该拆信号）、支撑文件归属与指针纪律、术语单一权威，
  经验层条目与仓库实践对齐；三类型分册判别总判据去重（统一回指
  structure-general「类型分流」，混合路由单一权威位置），操作型补流程
  编排并行/串行/回环标注，各册引言体例统一
- SKILL.md 重写为「前提 + 路由」：前提《什么是一个好的技能》加载即得
  （内容质量四标准 + 四个可检查特征）；路由表改为三工作论述加共享册
  （writing-craft、standards、disclosure）；「技能调试」不再作为独立
  工作——行为与预期不符路由到审查工作的症状排查形态；description 仅
  把调试措辞改为排查，占位保留（定稿待披露论述，属后续工作）

### Removed

- references/design/ 四册结构分册（structure-general / -knowledge /
  -operation / -template）：技能类型框架已否弃（SKILL-DESIGN 决策 2）；
  其开放标准转述由 general/standards.md 承接，结构与编写知识由
  documents/ 三形态册承接
- 旧位置 references/writing-craft.md：移至 documents/writing-craft.md
  并扩写为论述
- skill-master-guide.md 单一主文档占位（由任务分册与共享手艺层取代）
