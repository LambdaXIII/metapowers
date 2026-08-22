---
name: web-entity-search
description: >-
  Answer "what is X?" questions by searching the web for named entities —
  回答「XX 是什么」：通过网络搜索给出结构化、经过置信度检查的回答。
  Triggers: 「查一下 / 搜索 / 是什么 / 搜一下 / 了解一下」+ a named entity
  (person, company, work, product, event, concept); or "what is X?" /
  "look up" / "search for" a named entity.
metadata:
  version: "1.3.2"
  last_updated: "2026-08-23"
  author: "Ĉalio"
---

# Web Entity Search

Answer "what is X?" — via web search, produce a structured answer with confidence checking.
Not a research report, no chain tracing. Just a thin layer that adds framework and discipline over a direct search.

**Core flow:** disambiguation → classification → fill dimensions per template → confidence re-check → output per template.

> **Delegation advice:** This skill is simple structured search; strongly recommend delegating a sub-agent to load this skill and execute independently — avoids occupying the main agent's context and keeps the search uninterrupted. Topics are usually self-contained and rarely depend on conversation history.
> When delegating, pass only the task description — do **not** read this skill's files and relay them to the sub-agent. Let the sub-agent load the skill itself and follow the workflow inside the Skill.

Which specific search tool to use and how to extract web content are outside this skill's scope — this skill only governs "what to search, how much, when to stop, how to present".

## Content Index

| Entity type | Judgment clue | Reference file (how to search) | Template file (how to present) |
|-------------|--------------|--------------------------------|--------------------------------|
| Person | Search results show birth/death dates, occupation/identity | `references/person.md` | `templates/person.md` |
| Company / organization | Search results show founding date, industry, products | `references/company.md` | `templates/company.md` |
| Creative work | Search results show creator, release date, genre tags | `references/creative-work.md` | `templates/creative-work.md` |
| Product / technology | Search results show developer, feature description, version | `references/product-tech.md` | `templates/product-tech.md` |
| Event | Search results show time/place, participants | `references/event.md` | `templates/event.md` |
| Concept / term | Search results show definition, domain, theoretical origin | `references/concept-term.md` | `templates/concept-term.md` |
| Fallback | None of the above clues match, or entity spans multiple types | `references/general.md` | `templates/general.md` |

- **references/** — search guidance, dimension tables (with required/optional/key markers), pitfall rules. Load after Step 2 classification; guides Step 3 dimension filling
- **templates/** — pure output structures with placeholders. Load at Step 5; fill in the blanks
- `references/workflow.md` — the **full 5-step flow** (disambiguation→classification→filling→re-check→output). Required reading

## Instructions

1. Read `references/workflow.md`, execute Step 1 → Step 5
2. After Step 2 classification, load the matching reference and template files per the Content Index

## Capability Boundaries

- **Provides**: fast structured search for a single named entity, key-dimension coverage, light confidence checking
- **Does not provide**: chain clue tracing, multi-entity comparison, in-depth controversy analysis — these belong to deep research, beyond this skill's boundary
- **If the entity involves highly controversial topics**: mark "controversial" and stop — do not deeply evaluate either side
