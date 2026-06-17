---
name: web-deep-research
description: >-
  Deep research: clue-chain tracing (Phase 2, no judgment) →
  cross-reference by information type (Phase 3: facts→confidence,
  knowledge→combination, opinions→disputes, data→methodology) →
  deliver report with sources independent of conclusions (Phase 4).
  Use when thorough investigation matters more than speed.
metadata:
  version: "2.3.2"
  last_updated: "2026-06-17"
  author: "Ĉalio"
---

# Web Deep Research

Information is a network, not a list. The first search result is a clue, not an answer.

**Core mechanism:** Before any search, clarify what you're actually researching (Phase 0). Then trace clue chains — collect, read, summarize, connect, record URLs (Phase 2 — no judgment yet). In Phase 3, cross-reference everything by information type: facts get confidence assessment, knowledge gets systematic combination, opinions get dispute analysis, data gets methodology tracing. Discoveries that raise new questions loop back to Phase 2. Phase 4 delivers a complete research report where source materials stand independent of conclusions — readers can judge without reading conclusions.

> **Delegation:** This skill involves multiple search phases and many tool calls.
> Consider delegating to a sub-agent when the research topic is self-contained —
> the sub-agent can execute Phase 0–4 independently without blocking the main conversation.
> If the topic depends heavily on conversation context (prior decisions, nuanced
> user preferences discussed earlier), keep the research in the main agent where
> full context is available. Judge based on how much the research needs to know
> about what came before it.
>
> When delegating, pass only the task description — do **not** read this skill's
> files and relay their content to the sub-agent. The sub-agent should load the
> skill itself and follow its workflow.

For simple fact lookups where a quick answer suffices, this methodology is overkill — a direct search without the Phase structure will serve better.

## Content Index

| File | Purpose | When to read |
|------|---------|--------------|
| `references/workflow.md` | Phase 0（话题确认）→ Phase 1（线索起点）→ Phase 2（纯收集，记录URL）→ Phase 3（按资料性质评估：事实→置信度，知识→组合，意见→争议，数据→溯源）→ Phase 4（整理报告，资料不被结论覆盖） | **Always** |
| `references/creative-work.md` | Domain-specific strategies for film, anime, games, books | When researching creative works — ideally before or alongside Phase 0 |
| `references/person-biography.md` | Domain-specific strategies for public figures | When researching people — ideally before or alongside Phase 0 |
| `references/policy-law.md` | Domain-specific strategies for policies, laws, regulations | When researching policies or laws — ideally before or alongside Phase 0 |
| `references/academic-research.md` | Strategies for academic and highly specialized topics | When researching academic or highly specialized topics — ideally before or alongside Phase 0 |
| `references/controversial-topics.md` | Strategies for polarizing or controversial topics | When researching polarizing or controversial topics |
| `references/historical-events.md` | Strategies for historical events | When researching historical events |
| `references/competitive-research.md` | Strategies for competitive and market landscape research | When researching competitors, market landscapes, or doing comparative product/company analysis |
| `templates/report-template.md` | 研究报告模板，结论前置。章节以名称定位（无编号）：研究概要→研究结论→资料来源→交叉比对→追踪链索引→信息空白→参考资料→元知识。结论可向后追溯至来源URL | Before writing the report |

## Instructions

1. Make a preliminary judgment: does the research topic match any domain references listed in the Content Index? If so, load all matching ones now. If unsure, skip — you can load one later if you discover a match during research
2. Read `references/workflow.md` and follow Phase 0 → Phase 1 → Phase 2 → Phase 3 → Phase 4. Phase 2 collects + records URLs (no judgment). Phase 3 evaluates by information type. Phase 4 compiles the report — sources independent of conclusions

## What This Skill Is NOT

- **Not a tool selection guide** — that's web-search-protocol's job
- **Not a troubleshooting guide** — "what if extraction fails" belongs to web-search-protocol
- **Not a lightweight quick-search** — this methodology is overkill for simple lookups
- **Not for pure advice/opinion questions** — "how should I...?" without a research dimension is consulting, not research. But if the question involves "what frameworks exist", "what do studies say", "what are best practices for", or any multi-source investigation, it IS research regardless of how the user phrases it

This skill solves ONE problem: **"I need to research this topic thoroughly — how do I systematically uncover the truth?"**
