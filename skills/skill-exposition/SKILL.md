---
name: skill-exposition
description: |
  Skill exposition (技能阐述): turn a skill (or specified aspects of it, or
  multiple skills) into human-readable expository text that lets humans learn
  the skill by reading.

  Triggers: 「阐述技能 / 整理技能文档 / 生成方法论 / 把技能输出为文档 / 学会某个技能」;
  or when an agent needs to distill skill knowledge into human-readable
  material to pass it on.

  Does NOT trigger: reviewing, evaluating, testing, or creating skills.
metadata:
  version: "1.0.1"
  last_updated: "2026-08-23"
  author: "LambdaXIII"
  license: "MIT"
---

# Skill Exposition

> Turn a skill (or specified aspects of it, or multiple skills) into human-readable expository text that lets humans learn the skill by reading.

## What this is

Skills are executable methodology carriers designed for agents — their content exists as instructions, so humans cannot directly learn, pass on, or critique them. This skill turns skill content into **expository teaching material**: complete and faithful (no distortion, no omission, no degradation), organized for learning.

The deliverable lets humans learn to use the skill. What humans do after learning — applying it, designing better skills — is the result of learning, not part of this skill's scope.

**Behavior boundaries**: read source files only, never modify; do not execute or test the skill being expounded; do not judge whether the skill is good or bad.

## Trigger conditions

This section expands the description's trigger conditions — the description is what the loader (the skill loading/matching mechanism) matches against; the clauses below let the agent decide after loading whether to start this exposition.

**Triggers** (any one suffices):

- The user's first message contains verbs such as 「阐述 / 整理成文档 / 生成方法论 / 输出为文档 / 学会」, and the target is a skill (or aspects of a skill, or multiple skills)
- The user provides a skill directory (containing SKILL.md) or skill content and asks for human-readable expository text
- As an agent, right after completing or encountering a skill, asking yourself "how do I teach this skill to others" / "how do I distill its knowledge into human-readable material"

**Does NOT trigger**:

- The user wants skill-quality review, evaluation, or testing — that is a review-type responsibility (e.g. the domain of skill-quick-test), not exposition
- The user wants to create a new skill — that is skill-creator's domain
- The target is not a skill (content without SKILL.md, such as ordinary documents or codebases) — this skill only expounds skills

**Edge cases**: when unsure, trigger by default — producing expository text loses nothing even if imperfect; skipping it leaves the skill's knowledge sealed inside executable instructions where humans cannot learn it.

## How to use

1. Read [exposition-guide.md](references/exposition-guide.md) — the general guide, required reading. Contains the full method: sorting → pitfalls → organizing → effect mentions
2. Load reference files on demand (see routing table below) — judge for yourself, load anytime, they offer heuristics rather than requirements

## Reference files

**Required entry:**

- [exposition-guide.md](references/exposition-guide.md) — general guide, full method, self-contained

**Content-extraction reminders (on demand, load while sorting):**

- [extraction/workflow-content.md](references/extraction/workflow-content.md) — when encountering workflow-type content
- [extraction/knowledge-content.md](references/extraction/knowledge-content.md) — when encountering knowledge-base-type content
- [extraction/rule-content.md](references/extraction/rule-content.md) — when encountering rule/decision-type content
- [extraction/example-content.md](references/extraction/example-content.md) — when encountering example-type content
- [extraction/rationale-content.md](references/extraction/rationale-content.md) — when encountering design-thinking-type content

**Structure-pattern handbook (on demand, load while organizing):**

- [structure/pattern-learning-path.md](references/structure/pattern-learning-path.md) — learning-path pattern (default; outline included in the general guide)
- [structure/pattern-golden-circle.md](references/structure/pattern-golden-circle.md) — principle-first pattern (WHY→HOW→WHAT)
- [structure/pattern-knowledge-types.md](references/structure/pattern-knowledge-types.md) — group-by-knowledge-type pattern
- [structure/pattern-progressive-disclosure.md](references/structure/pattern-progressive-disclosure.md) — progressive-disclosure pattern (overview→detail)
- [structure/pattern-iceberg.md](references/structure/pattern-iceberg.md) — understanding-depth layering pattern (phenomenon→principle)
- [structure/pattern-scenario-driven.md](references/structure/pattern-scenario-driven.md) — reader-scenario/problem-driven pattern
- [structure/pattern-5w1h.md](references/structure/pattern-5w1h.md) — six-dimension coverage pattern
- [structure/pattern-functional-decomposition.md](references/structure/pattern-functional-decomposition.md) — capability-tree pattern

**General tips (on demand, loadable at any point):**

- [general/traps.md](references/general/traps.md) — pitfalls in depth (manifestations, examples, self-checks)
- [general/adjustments.md](references/general/adjustments.md) — adjustment advice for edge cases
- [general/readability.md](references/general/readability.md) — readability enhancement (register shifts, pyramid principle, etc.)
- [general/multi-skill.md](references/general/multi-skill.md) — multi-skill scenarios (batch / cross-skill integration)

## Directory tree

```
skill-exposition/
├── SKILL.md
└── references/
    ├── exposition-guide.md
    ├── extraction/               # content-extraction reminders (5)
    │   ├── workflow-content.md
    │   ├── knowledge-content.md
    │   ├── rule-content.md
    │   ├── example-content.md
    │   └── rationale-content.md
    ├── structure/                # structure-pattern handbook (8)
    │   ├── pattern-learning-path.md
    │   ├── pattern-golden-circle.md
    │   ├── pattern-knowledge-types.md
    │   ├── pattern-progressive-disclosure.md
    │   ├── pattern-iceberg.md
    │   ├── pattern-scenario-driven.md
    │   ├── pattern-5w1h.md
    │   └── pattern-functional-decomposition.md
    └── general/                  # general tips (4)
        ├── traps.md
        ├── adjustments.md
        ├── readability.md
        └── multi-skill.md
```
