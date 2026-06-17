# Changelog

All notable changes to this skill will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/).

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
