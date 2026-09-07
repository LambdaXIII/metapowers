---
name: skill-master
description: |
  Skill master (技能编写): for work on agent skills — deciding whether a
  practice is worth making into one, how to organize and word it, why one
  misbehaves, whether one is good enough. Use when asked to design, write,
  modify, review, or troubleshoot a skill, or when an agent asks
  「这个技能别人能不能照着做完」. Not for rewriting skill content as prose.
metadata:
  version: "0.2.0"
  last_updated: "2026-09-07"
  author: "LambdaXIII"
  license: "MIT"
---

# Skill Master


Skill Master is the method for making skills: turning a practice into one, repairing one that misbehaves, judging one that already exists, and writing the text any of that needs.

It is not a template to fill in and not a checklist to run. What it carries is the reasoning behind the choices — what belongs in a skill at all, which file a piece of content goes into, why a sentence should be cut. Read the part that matches what you are holding. Every file here is written to be read once, cold, by an agent with nothing else in hand.

### What a skill is

A skill is a directory an agent loads to gain a capability. The loader reads two fields — `name` and `description` — and holds them in context for the whole session. When a task matches, the loader pulls in the body of `SKILL.md` in full. Anything deeper is read only after something already loaded points at it.

Three consequences follow from that, and everything in this skill assumes them:

- **Layer is cost.** Text in `SKILL.md` is paid on every match. Text behind a link is paid only when followed. Where you put a piece of content decides which of those happens.
- **A reference is a load path.** Following a link *is* the read. A link to nothing means that knowledge cannot be reached, and nothing reports it.
- **Any file may be read on its own.** The reader was not in the conversation that produced it and has nothing else in hand. A file has to carry enough for the reader to act on it alone.

### What makes one good

Four tests, applied to every sentence and every file:

- **Useful** — delete it and the reader behaves differently. If nothing changes, it is a no-op; cut it.
- **Complete** — the branches and failure modes the reader will actually hit are covered. A cold reader who hits an uncovered case has nothing to fall back on.
- **Accurate** — every claim traces to a mechanism or to practice. Skill text is used as authority, so a wrong claim becomes a wrong action and nobody re-checks it.
- **Clear** — the reader has no one to ask. Ambiguity gets filled in silently, and a wrong fill-in is never reported.

Review judges a skill by these four. A modification has failed if it breaks any of them.

## How to use it

Start from what is in your hands.

**You have a practice, or a body of knowledge, and want it to become a skill.** Design is the whole path: whether it is worth making, what it is for, how the material gets organized into files, how the text gets written, how it gets delivered. This is also the entry when a skill exists but its structure itself has to move — its positioning, its name, its scope boundaries. → [Designing a skill](references/skill-design.md)

**A skill exists, something in it needs to change, and the change fits inside the structure already there.** Modification is not a small design. Its own problem is that every edit travels: along reference chains, across layers, into places the edit never named. → [Modifying a skill](references/skill-modify.md)

**You need a verdict on a skill that already exists.** Review reads the text dimension by dimension and produces a defect list, each item with a location and a reason. → [Reviewing a skill](references/skill-review.md)

**A skill misbehaves — it does not trigger, it triggers on the wrong tasks, its output is off.** Not a fourth kind of work. Tracing a symptom back to its cause is the second input shape of review; the repair that trace recommends is then a modification job. → [Reviewing a skill](references/skill-review.md)

**You want to know whether a skill works, not whether it reads well.** That judgement belongs to design, not to review. Review is a static read of the text. A walkthrough gives a cold agent the documents and a real task and watches where it stalls. The two answer different questions — is it right, versus is it enough. Where a walkthrough stalls is often a specific dimension failing, which makes it usable as an input to review. → [Designing a skill](references/skill-design.md)

**You are writing or rewriting skill text.** Any of the three kinds of work puts you here. Sentence-level and structure-level craft, shared by every file form. → [Writing skill text](references/documents/writing-craft.md)

By the kind of thing you are writing:

- **The reader is missing judgement, not steps** — where the boundaries are, how a trade-off is weighed, which way to think in a given case. → [Essay form](references/documents/essay-writing.md)
- **The reader knows the goal and fails on the process** — skipped steps, wrong order, a wrong turn at a decision point. → [Workflow form](references/documents/workflow-writing.md)
- **The reader has the material and cannot assemble it** — the value is a stable output shape. → [Template form](references/documents/template-writing.md)
- **You are weighing whether a piece of content should be a script at all.** "This skill needs a script" is a symptom, not a requirement: three different causes hide behind it and their fixes do not overlap. → [To script or not](references/scripts/script-design.md)
- **You have decided it should be a script.** It runs where you cannot see it — interpreter version, dependencies, external commands, working directory, path separators, none of it assumable. → [Writing skill scripts](references/scripts/scripting-craft.md)

Two more, entered by need rather than by situation:

- **Directory layout, frontmatter, machine validation before delivery.** → [Packing a skill](references/general/standards.md)
- **Naming, `description`, trigger surface — anything about getting loaded rather than being good once loaded.** → [Designing disclosure](references/general/disclosure.md)

## Not this skill

- Rewriting skill content as prose for people to read. Exposition, not skill work.
- Running a skill to see whether it executes. That is test work; review reads text and does not load or execute the skill under judgement.
- Typos, punctuation, and formatting on their own. Not one of the kinds of work above.

## Contents

- `SKILL.md` — this file: what this is, how to use it, this index
- `references/`
  - [skill-design.md](references/skill-design.md) — designing a skill, end to end
  - [skill-modify.md](references/skill-modify.md) — modifying a skill
  - [skill-review.md](references/skill-review.md) — reviewing a skill, including symptom tracing
  - `documents/` — writing text
    - [writing-craft.md](references/documents/writing-craft.md) — craft shared by every form
    - [essay-writing.md](references/documents/essay-writing.md) — essay form
    - [workflow-writing.md](references/documents/workflow-writing.md) — workflow form
    - [template-writing.md](references/documents/template-writing.md) — template form
  - `scripts/` — writing code
    - [script-design.md](references/scripts/script-design.md) — whether to script, and how to design one
    - [scripting-craft.md](references/scripts/scripting-craft.md) — script craft
  - `general/` — applies across kinds
    - [standards.md](references/general/standards.md) — packing specification
    - [disclosure.md](references/general/disclosure.md) — disclosure design
