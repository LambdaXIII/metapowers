# Journal Tag Registry

> Controlled vocabulary for journal entry tags.
> Tags must come from this table. New tags: register here first, then use.
> During maintenance, entries with unregistered tags are flagged for remediation.

## Project Tags

> Project tags are optional. Register your own project tags here when your journal contains entries tied to specific projects. Keep the list lean — each tag must earn its place.

| Tag | Scope |
|-----|-------|
| _(register your project tags here)_ | _Add: tag name → one-line project description_ |

## Activity Tags

| Tag | Meaning |
|-----|---------|
| `design-decision` | 设计决策、架构选择 |
| `research` | 调研、信息搜集与分析 |
| `debugging` | 调试、问题排查 |
| `migration` | 环境/技术栈/数据迁移 |
| `implementation` | 实现、编码落地 |
| `planning` | 计划制定、路线图 |
| `documentation` | 文档编写、修缮 |
| `review` | 审查、评估、验收 |

## Domain Tags

| Tag | Scope |
|-----|-------|
| `architecture` | 系统架构、组件设计 |
| `screenwriting` | 编剧创作 |
| `frontend` | 前端/UI |
| `tool-system` | 工具链、开发工具 |
| `profile-design` | Agent Profile 设计 |
| `workflow` | 工作流程、方法论 |
| `environment` | 运行环境、操作系统 |
| `agent-design` | Agent 架构设计（compaction、prompt工程、工具系统） |
| `patent` | 专利申请、专利挖掘、查新 |

## Meta Tags

| Tag | Meaning |
|-----|---------|
| `journal` | Journal 自身维护 |
| `skill` | Skill 开发/维护 |
| `methodology` | 方法论提炼、范式总结 |
| `lesson` | 教训、经验总结 |

## Rules

1. **Must come from this table.** Every tag on a journal entry must appear here.
2. **Register before use.** If a genuinely needed tag is missing, add it to the appropriate category BEFORE using it in an entry.
3. **During maintenance:** scan all entries for unregistered tags. Decision branches:
   - Worth keeping → register it here (see Tag Worthiness Criteria in maintenance.md)
   - Synonym of existing tag → replace with the canonical tag, don't register
   - Vague but common (e.g., `misc`, `general`, `notes`) → remove from all entries, don't register — regardless of use count
   - One-off / too narrow → remove from entry frontmatter, don't register
4. **Keep it lean.** ~20 tags is the target. Each new registration must earn its place.

## Change Log

| Date | Action | Tag | Reason |
|------|--------|-----|--------|
| 2026-06-18 | added | change log | This section — to track tag evolution over time |
