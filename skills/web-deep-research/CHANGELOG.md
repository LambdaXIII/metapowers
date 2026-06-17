# Changelog

All notable changes to this skill will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/).

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
