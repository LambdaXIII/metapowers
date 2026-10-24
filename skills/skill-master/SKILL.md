---
name: skill-master
description: |
  Skill master: guidance for any work whose object is a skill — making
  one from a practice, using and judging one, repairing one, or choosing
  between them. Use when asked to design, write, modify, review,
  troubleshoot, quickly test, or evaluate a skill, or whenever a skill
  itself is the question. An agent asks after building or using one:
  "can someone follow this and finish the job?" / "did this skill
  actually help?" Not for rewriting skill content as prose.
license: "CC-BY-NC-SA-4.0"
metadata:
  version: "1.0.3-beta"
  last_updated: "2026-10-24"
  author: "LambdaXIII"
---

# Skill Master


Skill Master is the method for working on skills, whether using them or making them. Whatever the work, the skill it targets is judged by the same four criteria: Useful（有用）, Complete（全面）, Accurate（准确）, Clear（清晰）.

## How to use it

Start from what is in your hands. The situations split by which side of the skill you are on: its user, or its maker.

### When you are using skills

**You are deciding whether to use a skill you have not used — or picking one from several candidates.** The assessment draws on a few directions of evidence — the content itself, where it comes from, how actively it is kept up, what others say, how it fits your task, what you already have covering the same ground, what adopting it costs. Fast and rough is the design; how to act on the assessment is a decision after it. → [Evaluating a skill you have not used](references/skill-pre-assessment.md)

**You have just used a skill on a task and want to record what the use actually showed — what held up, what fell short, what was wrong.** The evidence is the task process itself, still fresh; what comes out is a record of insights, each tied to something that happened. → [Evaluating a skill you have just used](references/skill-post-assessment.md)

### When you are making skills

**You have a practice, or a body of knowledge, and want it to become a skill.** Design is the whole path: whether it is worth making, what it is for, how the material gets organized into files, how the text gets written, how it gets delivered. This is also the entry when a skill exists but its structure itself has to move — its positioning, its name, its scope boundaries. → [Designing a skill](references/skill-design.md)

**A skill exists, something in it needs to change, and the change fits inside the structure already there.** Modification is not a small design. Its own problem is that every edit travels: along reference chains, across layers, into places the edit never named. → [Modifying a skill](references/skill-modify.md)

**You maintain a skill and need to find what is wrong with it before fixing it.** Finding what is wrong means setting what the skill claims against what it actually does. The output is a defect list, each item with a location and a reason — the input modification consumes. → [Finding what is wrong with a skill](references/skill-review.md)

**A skill misbehaves — it does not trigger, it triggers on the wrong tasks, its output is off.** Symptom tracing is the fast path of review, not a work of its own: trace the symptom back down the trigger chain, and the repair it points to is a modification job. → [Finding what is wrong with a skill](references/skill-review.md)

**You want to know whether a skill actually works — whether a cold agent can understand it, walk its flow, and finish the task.** That is its own work: quick testing. It does not execute the skill — sub-agents rehearse "if I followed this guidance, what would happen" and report where they stall. It judges *is it enough*, not *is it right* — that division belongs to review. Where a rehearsal stalls is often a specific defect class showing through, so the output doubles as a modification job list. → [Quick-testing a skill](references/skill-quick-test.md)

**You are writing or rewriting the entry file itself** — the one file every match pays for in full, the one that decides whether the rest is ever reached. → [Writing the entry file](references/documents/skill-md-writing.md)

**You are writing or rewriting skill text.** Any of the four kinds of work puts you here. Sentence-level and structure-level craft, shared by every file form. → [Writing skill text](references/documents/writing-craft.md)

By the kind of thing you are writing:

- **The reader is missing judgement, not steps** — where the boundaries are, how a trade-off is weighed, which way to think in a given case. → [Essay form](references/documents/essay-writing.md)
- **The reader knows the goal and fails on the process** — skipped steps, wrong order, a wrong turn at a decision point. → [Workflow form](references/documents/workflow-writing.md)
- **The reader has the material and cannot assemble it** — the value is a stable output shape. → [Template form](references/documents/template-writing.md)
- **You are weighing whether a piece of content should be a script at all.** "This skill needs a script" is a symptom, not a requirement: three different causes hide behind it and their fixes do not overlap. → [To script or not](references/scripts/script-design.md)
- **You have decided it should be a script.** It runs where you cannot see it — interpreter version, dependencies, external commands, working directory, path separators, none of it assumable. → [Writing skill scripts](references/scripts/scripting-craft.md)

Entered by need rather than by situation:

- **How to structure a skill's files — where a piece of content goes, how the layers and references are organized.** → [Designing a skill's structure](references/general/structure.md)
- **What the open standard and the runtime environment require, and how to verify compliance before delivery.** → [Keeping a skill package compliant](references/general/standards.md)
- **Naming, `description`, trigger surface — anything about getting matched rather than being good once loaded.** → [Getting a skill matched](references/general/disclosure.md)

## Not this skill

- Rewriting skill content as prose for people to read. Exposition, not skill work.
- Staging real executions of a skill to test it. Quick testing rehearses without executing, and post-evaluation only looks back at a use that already happened in the course of work — neither stages anything.
- Typos, punctuation, and formatting on their own. Not one of the kinds of work above.

## Beta

This skill is in beta. If you hit a problem or have a suggestion while using it, open an issue at https://github.com/LambdaXIII/metapowers/issues.
