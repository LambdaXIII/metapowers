# Journal Concept

> The design philosophy behind the journaling skill — what a journal is, why it works the way it does, and the principles that govern every mechanism.

---

## What Is a Journal

An agent's **long-term memory notebook**, cross-project and global. The `index.md` is the cover; individual entries are the pages. The journal serves the agent, not the user — every write, read, maintenance, and deletion decision is the agent's to make.

> This is not a collaboration preference. It is a design constraint: the user cannot be the quality gate for journal operations, so the skill must make the agent self-sufficient.

---

## Skill Design Principles

These govern **how the skill is structured**, not how entries are written. Every mechanism (progressive disclosure, maintenance protocol, gate rules, tag registry) is shaped by them.

### Core Identity

The journal serves the agent, not the user. The user cannot judge the correctness of specific journal operations, nor needs to approve them. Every read, write, maintenance, and deletion decision is the agent's to make — carefully, with the future self in mind.

### Read/Write Asymmetry

| Direction | Design goal |
|-----------|-------------|
| **Read operations** | Minimize attention drain. The dashboard uses the mistake test. The gate activates only on matched triggers. Nothing demands attention unless it prevents a concrete mistake. |
| **Write operations** | Prospectively serve future reading. Every write decision — what to record, how much, with what tags, in what directory — is made with a future reader in mind who has no memory of this session. |

### Progressive Disclosure

The skill manifest stays lean — it is a router, not a textbook. Mechanism details live in dedicated reference files. Load only what the current scenario demands.


### Dynamic Prompt System

The journal functions as a **dynamically loaded prompt system**:

- **index.md** is the always-available entry point. It loads at every session start without needing the journaling skill. It tells the agent what's happening, what's changed, and what demands attention.
- **References and notes** load on demand. From index.md's links, the agent reads experience entries, project notes, and research files as needed.
- **The skill** loads only when the agent needs to write or maintain. Writing triggers the format rules and write procedure (note-spec.md), and the maintenance protocol (maintenance.md).

This layering is intentional:
- Reading is free — no skill dependency, no loading cost, always works.
- Writing is deliberate — it requires the skill because writing is the highest-ceremony operation.
- The skill is a tool, not a prerequisite. The journal works without it; the skill makes it work better.

> The index.md must never depend on the journaling skill for readability. The skill is a writing and maintenance tool, not a reading tool.
---

## Execution Anchors

These are the principles an agent follows during journal operations. Every mechanism exists to serve them.

### Writing Anchors — Write for the future reader

| # | Principle | What it means |
|---|-----------|---------------|
| 1 | **可复现深刻理解** | 重读时必须能复现写时的深刻理解——不只是"做了什么"，更是"为什么这样决定、排除过哪些替代方案、在什么边界条件下成立"。提示性摘要是检索工具，不是理解载体。 |
| 2 | **No redundancy** | Signal must not drown in noise. Don't record what can be rediscovered cheaply. Don't duplicate what lives elsewhere (persona, memory, project docs). |
| 3 | **Precision** | Never blur scope, domain, or project boundaries. Tags, directory placement, and cross-references must make this distinction clear. |
| 4 | **Discoverability** | Future self must find the right entry at the right moment. Tags, cross-references, the index, and the gate table are all finding aids. |
| 5 | **Retrieval efficiency** | Finding must be fast, loading must be cheap. The dashboard compresses signals to one screen. Summary lines allow relevance judgment without opening the file. |

### Reading Anchors — Read with minimal distraction

| # | Principle | What it means |
|---|-----------|---------------|
| 6 | **Minimize attention drain** | The dashboard uses the mistake test: "If this line were absent, would I make a mistake?" Lines that fail are noise. The gate activates only on matched triggers. |
| 7 | **Scene awareness, not log replay** | What matters is the current work scene, not a chronological archive. The dashboard encodes what kind of work is happening, not a list of events. |

### Mechanism Mapping

When a new mechanism is proposed, test: which of these seven principles does it serve? If unclear, the mechanism is ceremony.

| Principle | Manifested in |
|-----------|--------------|
| **1. 可复现深刻理解** | Summary anchoring · document self-check (executability/independence/boundary/reproducibility) · gate rules anchored in specific failure incidents · Prospective Reading Check core question |
| **2. No redundancy** | Summary anchoring (update vs create decision) · dashboard mistake test · axiom deduplication from persona/memory · "don't record what can be rediscovered cheaply" |
| **3. Precision** | Tag registry (controlled vocabulary) · directory assignment · project tags · cross-references with explicit scope |
| **4. Discoverability** | Tag registry (searchable) · cross-references & wikilinks · index.md catalog · gate table (matched triggers) · summary lines for relevance judgment |
| **5. Retrieval efficiency** | Dashboard compression (one screen) · summary anchoring · scene encoding · tag search patterns |
| **6. Minimize attention drain** | Mistake test on every dashboard line · gate activates only on matched triggers · progressive disclosure (reference files) |
| **7. Scene awareness** | Scene encoding in project work · cooling period for completed milestones · dashboard not a chronological log |

---

## Memory Positioning

### Core Insight

**The journal is the agent's home** — not a fallback storage, not a secondary option, but the agent's own long-term memory body. Everything else is auxiliary.

### Layers

| Layer | Purpose |
|-------|---------|
| **Working Memory** | Minimal, essential context — extremely important, simple, high-level, must be present every round |
| **Journal** | **The agent's long-term memory body** — experiences, states, goals, processes, relationships |
| **Structured Knowledge** | Discrete facts, cross-entity relationships |
| **Skills** | Reusable operation procedures |
| **Project Docs** | External authoritative sources — project design, not the agent's memory |

### Memory Write Filter

Content entering working memory must be filtered through other layers:
1. Not a procedure → skill or project docs
2. Not a path/fact → structured knowledge or project docs
3. Not a project state → project docs or journal
4. Not an experience/process/relationship → journal

After filtering, only "minimal essential" AND "absent this round would break" content enters working memory.

### Anti-Pattern: Project State Leaking into Working Memory

Working memory accumulates project-level state — refactoring scope, context compression details, creative preferences, project locations. These are project state, not working memory.

**The test**: if this information changes tomorrow (refactoring plan updated, project path changed, character design adjusted), will it still be valuable? No → keep out of working memory.

---

## Gate Design Principles

### The Problem

Agents exhibit a consistent failure pattern:
1. Valuable lessons, user preferences, and process rules are recorded in persistent storage
2. When a relevant task arises, the stored knowledge is **not consulted** before action
3. The default is reactive: stimulus → response, without an intermediate knowledge check
4. Corrections come only after mistakes are made

The storage layer works, but retrieval lacks a trigger mechanism.

### The Pattern: Passive Storage → Active Intercept

The two-gate model introduces **decision gates** — structured checkpoints that interrupt the default reactive flow and force review of relevant knowledge before action.

A gate has three properties:
1. **Trigger specificity**: The gate fires on a concrete, recognizable action moment. "修改项目前端代码" fires; "做好工作" does not.
2. **Mandatory review**: The gate names specific entries to read. "读 user-understanding.md 第65行" fires; "注意质量" does not.
3. **Consequence anchoring**: The gate's interrupt force comes from a remembered failure. "上次跳过了文档导致3个回归" stops; "文档先行很重要" does not.

### Gate 1: Journal Gate

**Purpose**: Ensure past lessons, user preferences, and methodology agreements are re-read before acting on related tasks.

**Location**: The journal's `index.md` — the action gate section. The cover is the one page guaranteed to be read at session startup.

**Structure**: A markdown table:
| When I am about to... | I must first read... | Skipping causes... |
|----------------------|---------------------|-------------------|

**Design constraints**:
- Max 9 rules — beyond this, scanning fatigue sets in
- Each rule created only after a concrete failure proves it necessary
- First-person verbs — self-imposed rules, not external mandates

**Startup protocol**:
```
Load index.md → scan gate table →
Match any rule → read specified entries → then act
No match → skip
```

### Gate 2: Document Gate

**Purpose**: Ensure project documentation is updated before code is written, so the user retains a verification chain.

**Location**: Project entry point document (e.g., project guide or convention file).

**When**: After consensus, before implementation planning.

**Structure**: Same three-column format, but triggers are change-type → document mappings.

### Generalization

```
[Passive knowledge store] + [Trigger table at the entry point] + [Mandatory review step in protocol]
  → Active intercept that fires before the mistake, not after
```

Any knowledge system that suffers from "wrote it, didn't read it" can adopt this pattern. The key design constraint: the gate must live at the **entry point** — the one document guaranteed to be read before action begins.

### Write Timing Protocol

The two gates cover "what to read before acting" and "what to filter before writing." A third mechanism covers **when to write**: discussion decisions must be captured into the target document **in the same round** they are produced. See SKILL.md → Operating Rules for the capture procedure.
