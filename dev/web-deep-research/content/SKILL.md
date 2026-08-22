---
name: web-deep-research
description: >-
  Deep research: topic-setting (Phase 0) → clue starting points (Phase 1) →
  clue-chain tracing (Phase 2, no judgment) → cross-reference by
  information type (Phase 3: facts→confidence, knowledge→combination,
  opinions→disputes, data→methodology, experience→transferability) →
  deliver report with sources independent of conclusions (Phase 4).
  Use when thorough investigation matters more than speed.
metadata:
  version: "2.5.0"
  last_updated: "2026-08-23"
  author: "Ĉalio"
---

# Web Deep Research

Information is a network, not a list. The first search result is a clue, not an answer.

**Core mechanism:** Before any search, clarify what you're actually researching (Phase 0). Then chase the open question set (Q-set): trace the clues that can support each open question, collect, read, summarize, connect, record URLs (Phase 2 — no judgment yet). In Phase 3, cross-reference everything by information type: facts get confidence assessment, knowledge gets systematic combination, opinions get dispute analysis, data gets methodology tracing. Discoveries that raise new questions loop back to Phase 2. Phase 4 delivers a complete research report where source materials stand independent of conclusions — readers can judge without reading conclusions.

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
>
> If you are the delegated executor reading this: the delegation decision is
> already made — do not re-delegate; load the skill and run the workflow yourself.

For simple fact lookups where a quick answer suffices, this methodology is overkill — a direct search without the Phase structure will serve better.

## Content Index

| File | Purpose | When to read |
|------|---------|--------------|
| `references/workflow.md` | Phase 0 (confirm the topic) → Phase 1 (clue starting points) → Phase 2 (pure collection, record URLs) → Phase 3 (evaluate by material type: facts→confidence, knowledge→combination, opinions→disputes, data→trace methodology) → Phase 4 (compile the report; sources are stand independent of conclusions) | **Always** |
| `references/search-strategy.md` | Orchestration strategy for using this skill: execution modes (delegate / split / self-run), report persistence, multi-subtopic integration, feeding conclusions back | When delegation is viable, or the topic is unclear |
| `references/creative-work.md` | Domain-specific strategies for film, anime, games, books | When researching creative works — ideally before or alongside Phase 0 |
| `references/person-biography.md` | Domain-specific strategies for public figures | When researching people — ideally before or alongside Phase 0 |
| `references/policy-law.md` | Domain-specific strategies for policies, laws, regulations | When researching policies or laws — ideally before or alongside Phase 0 |
| `references/academic-research.md` | Strategies for academic and highly specialized topics | When researching academic or highly specialized topics — ideally before or alongside Phase 0 |
| `references/controversial-topics.md` | Strategies for polarizing or controversial topics | When researching polarizing or controversial topics |
| `references/historical-events.md` | Strategies for historical events | When researching historical events |
| `references/competitive-research.md` | Strategies for competitive and market landscape research | When researching competitors, market landscapes, or doing comparative product/company analysis |
| `templates/report-template.md` | Research report template, conclusions first. Sections are located by name (unnumbered): research summary → conclusions → sources → cross-comparison → clue-chain index → information gaps → references → meta-knowledge. Conclusions can be traced back to source URLs | Before writing the report |

> Loading note: `references/workflow.md` is **required** (Always). All other
> references and the template are **optional** — load by topic match and need.

## Instructions

1. Make a preliminary judgment: does the research topic match any domain references listed in the Content Index? If so, load all matching ones now. If unsure, skip — you can load one later if you discover a match during research
2. Read `references/workflow.md` and follow Phase 0 → Phase 1 → Phase 2 → Phase 3 → Phase 4. Phase 2 collects + records URLs (no judgment). Phase 3 evaluates by information type. Phase 4 compiles the report — sources independent of conclusions

## What This Skill Is NOT

- **Not a tool selection guide** — choosing search tools is a separate concern
- **Not a troubleshooting guide** — extraction-failure handling is a separate concern
- **Not a lightweight quick-search** — this methodology is overkill for simple lookups
- **Not a decision-maker** — this skill researches a topic; it does not make the user's decision. A delegated decision-shaped question ("should I...") becomes a neutral researchable topic ("should we adopt X" → "X vs the current stack: differences, tradeoffs, evidence") — the topic carries no lean, and the conclusion supports the delegating conversation's decision rather than making it. Whether and when to start research is the main agent's call from conversation context — not this skill's input gate

This skill solves ONE problem: **"I need to research this topic thoroughly — how do I systematically uncover the truth?"**
