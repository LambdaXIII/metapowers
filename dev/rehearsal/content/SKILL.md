---
name: rehearsal
description: |
  Rehearsal (推演): a method of reading a deliverable from the reader's
  perspective to check it.

  Applies to any deliverable made for others to read / use:
  - Documents, tutorials, guides, READMEs, plan documents
  - System prompts, Agent instructions, task instructions, prompt templates
  - API designs, UI interaction flows, CLI command series, forms, operation manuals
  - Knowledge bases, teaching materials, code examples, rule sets

  **Triggers** (any one suffices):
  - The user says any of the following about a deliverable (Chinese or English):
    「推演 / rehearsal / 通读 / 验一下 / 检查 / 确保理解 / 充分理解 / 不误解 /
    能不能走通 / 卡住 / 看不懂 / 新人会不会卡 / 过一遍 / 走一遍 /
    模拟接收方视角 / simulate a reader / first-contact / dry-run /
    walk through / sanity-check / verify for a newcomer / will users get stuck」
  - Right after producing any of the deliverables above, asking yourself
    「能不能被没有上下文的人读懂 / 交付出去会不会卡住 / 我自己看不出问题但别人会卡在哪」,
    or "can a newcomer follow this / will readers get stuck / what will others
    get stuck on that I can't see"
  - After producing anything meant for others to read / use, rehearsing it
    before delivery (not limited to the list above — applies to any final
    deliverable for others)

  Does NOT trigger for typo/punctuation/format-only fixes.
metadata:
  version: "2.0.2"
  last_updated: "2026-08-23"
  author: "xiii_1991"
  license: "MIT"
---

# Rehearsal

## What this is

**Rehearsal = dropping the author identity and walking the full "first contact → understanding → decision" chain from another perspective.**

It is independent of the carrier — you can rehearse documents, code, UI flows, API designs, instruction sets, or any deliverable. It is also not limited to a particular reader — the reader can be an AI model, a real person, a student, a customer, a new colleague.

## Why it works

The author has a fatal blind spot: **you know "what conclusion should be drawn", so you cannot see "where someone who fails to draw it gets stuck".** Rehearsal forces the removal of "designer knowledge" — pretend you don't know, walk through it, and wherever you get stuck is where the problem is.

## Trigger conditions

This section expands the description's trigger conditions — the description is what the loader matches against; the clauses below let the agent decide after loading whether to start this rehearsal / verify whether the trigger is reasonable or whether something was missed.

**Triggers** (any one suffices):

- The user's first message contains verbs or phrases such as 「推演 / 验一下 / 走一遍 / 过一遍 / 检查能不能看懂 / 能不能走通 / 新人会不会卡 / 读者看懂吗 / 接收方会卡在哪」, and the target is a deliverable for others to read / use
- The user's first message indicates pre-delivery self-check of a deliverable ("写完 / 设计完 / 改完 + any deliverable type"): documents, tutorials, guides, READMEs, plan documents, system prompts, Agent instructions, task instructions, prompt templates, API designs, UI interaction flows, CLI command series, forms, operation manuals, knowledge bases, teaching materials, code examples, rule sets
- As an agent, **right after completing** any deliverable of the types above and before delivering it to the user / reader / caller, asking yourself "can someone without context understand this", "will it get stuck when delivered", "what will others get stuck on that I can't see"
- The user provides a specific deliverable and asks for quality verification / usability assessment / reader-friendliness checking

**Does NOT trigger**:

- Only typo, punctuation, or pure formatting fixes — one-off revisions with no content change, which do not change the reader's comprehension path
- Real user feedback data already exists — this skill is a simulation; feedback is more accurate than simulation — handle feedback data first, rehearsal only adds a supplementary perspective
- Re-rehearsing the same unchanged deliverable — the issue list from the last round is still there; rehearsing again just re-discovers the same issues; rehearse after changing

**Clarification** (the following is **not** a non-trigger):

- Pure code runtime-logic verification (no need to simulate a "person's" perspective) — rehearse per `references/scenarios/logic-chain-rehearsal.md`. logic-chain-rehearsal is a scenario document under this skill's references, not another skill; do not fail to trigger this skill because "no human simulation is needed". When a deliverable contains both documentation and code examples, do both the document rehearsal and the logic-chain rehearsal.

**Edge cases**: if unsure whether to trigger, trigger by default — a rehearsal that finds nothing costs nothing, but skipping one may let a deliverable go out with problems that could have been found.

## How to rehearse

**Read the general guide and follow its process:**

→ [rehearsal-guide.md](references/rehearsal-guide.md) — full account of the method (principles, rehearsal steps P1–P5, four-direction reproduction, evaluation dimensions) plus an index of scenario-specific references.

## Reference files

**Required entry:**

- [rehearsal-guide.md](references/rehearsal-guide.md) — general guide, full method + scenario-specific references

**Scenario documents (load on demand)**: matched by rehearsal carrier type — full routing and decision criteria in the "Scenario-specific references" section of [rehearsal-guide.md](references/rehearsal-guide.md).

- [Document/guide quality rehearsal](references/scenarios/doc-guide-rehearsal.md) — single-document rehearsal + full-process cross-document rehearsal, five-dimension evaluation criteria
- [Design-methodology document rehearsal](references/scenarios/design-doc-rehearsal.md) — four-dimension verification framework: logical correctness, clear thread, internal consistency, reproducible deep understanding
- [Multi-scenario knowledge base rehearsal](references/scenarios/knowledge-base-rehearsal.md) — multi-role × multi-path rehearsal, adapted to decision-tree branching consumption patterns
- [Prompt/instruction-set rehearsal](references/scenarios/prompt-instruction-rehearsal.md) — two-dimension rehearsal (content-expression layer + logic-execution layer), delegation mechanism
- [Interaction-flow rehearsal](references/scenarios/interaction-rehearsal.md) — dimensions: first-attempt executability of the operation chain, confusion-point density, abandonment-rate estimation
- [API design rehearsal](references/scenarios/api-design-rehearsal.md) — dimensions: naming consistency, default-value reasonableness, error-message actionability, missing-endpoint coverage
- [Logic-chain rehearsal](references/scenarios/logic-chain-rehearsal.md) — dimensions: control-flow correctness, boundary-condition coverage, state consistency
- [Plan document rehearsal](references/scenarios/plan-rehearsal.md) — 9 evaluation dimensions including execution-path completeness, dependency visibility, exception coverage

**Load on demand:**

- [batch-execution.md](references/supplementary/batch-execution.md) — parallel-execution mode when rehearsal scenarios ≥ 5 (role-matrix design in the knowledge-base scenario document)
- [defect-taxonomy.md](references/supplementary/defect-taxonomy.md) — for classifying and locating defects once found


## Directory tree

```
rehearsal/
├── SKILL.md
└── references/
    ├── rehearsal-guide.md
    ├── scenarios/
    │   ├── doc-guide-rehearsal.md
    │   ├── design-doc-rehearsal.md
    │   ├── knowledge-base-rehearsal.md
    │   ├── prompt-instruction-rehearsal.md
    │   ├── interaction-rehearsal.md
    │   ├── api-design-rehearsal.md
    │   ├── logic-chain-rehearsal.md
    │   └── plan-rehearsal.md
    └── supplementary/
        ├── batch-execution.md
        └── defect-taxonomy.md
```
