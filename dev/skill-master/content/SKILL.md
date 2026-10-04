---
name: skill-master
description: |
  Skill master (技能): guidance for any work whose object is a skill —
  making one from a practice, using and judging one, repairing one, or
  choosing between them. Use when asked to design, write, modify, review,
  troubleshoot, quickly test (推演 / 验一下 / 走通), or evaluate (评估 /
  怎么样 / 哪个更好) a skill, or whenever a skill itself is the question.
  An agent asks after building or using one: 「这个技能别人能不能照着做完」
  「这个技能用下来帮没帮上忙」. Not for rewriting skill content as prose.
license: "MIT"
metadata:
  version: "1.0.0"
  last_updated: "2026-09-15"
  author: "LambdaXIII"
---

# Skill Master


Skill Master is the method for working on skills, from the maker's side and the user's: turning a practice into one, repairing one that misbehaves, finding what is wrong with one you maintain, deciding whether to use one you have not tried, checking a cold agent can actually use one, looking back on one you have just used, and writing the text any of that needs.

It is not a template to fill in and not a checklist to run. What it carries is the reasoning behind the choices — what belongs in a skill at all, which file a piece of content goes into, why a sentence should be cut. Read the file that matches what you are holding. Every file here is written to be read once, cold, by an agent with nothing else in hand.

### What a skill is

A skill is a directory an agent loads to gain a capability. The loader reads two fields — `name` and `description` — and holds them in context for the whole session. When a task matches, the loader pulls in the body of `SKILL.md` in full. Anything deeper is read only after something already loaded points at it.

Three consequences follow from that, and everything in this skill assumes them:

- **Layer is cost.** Text in `SKILL.md` is paid on every match. Text behind a link is paid only when followed. Where you put a piece of content decides which of those happens.
- **A reference is a load path.** Following a link *is* the read. A link to nothing means that knowledge cannot be reached, and nothing reports it.
- **Any file may be read on its own.** The reader was not in the conversation that produced it and has nothing else in hand. A file has to carry enough for the reader to act on it alone.

### What makes one good

Four tests, applied to every sentence and every file:

- **Useful（有用）** — delete it and the reader behaves differently. If nothing changes, it is a no-op; cut it.
- **Complete（全面）** — the branches and failure modes the reader will actually hit are covered. A cold reader who hits an uncovered case has nothing to fall back on.
- **Accurate（准确）** — every claim traces to a mechanism or to practice. Skill text is used as authority, so a wrong claim becomes a wrong action and nobody re-checks it.
- **Clear（清晰）** — the reader has no one to ask. Ambiguity gets filled in silently, and a wrong fill-in is never reported.

Review judges a skill by these four; pre-use evaluation weighs them for the task at hand, and post-use insights test them against what actually happened. A modification has failed if it breaks any of them.

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
