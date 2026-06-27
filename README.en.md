[中文](README.md) | English

# metapowers

[![License](https://img.shields.io/badge/license-MIT-blue)](LICENSE)

> An agent skill development workshop — a set of universal Skills and the engineering standards that produce them.

---

## Table of Contents

- [Background](#background)
- [Features](#features)
- [Installation](#installation)
- [Skills](#skills)
- [Project Structure](#project-structure)
- [Design Philosophy](#design-philosophy)
- [Contributing](#contributing)
- [License](#license)

---

## Background

AI agents acquire domain expertise through **skills** — a SKILL.md file and a few reference documents are enough to give an agent mastery of prompt design, deep research, knowledge distillation, and more.

But skill quality varies wildly. Some skills are filled with the designer's inner monologue instead of executable instructions. Some bump a major version over a typo fix. Some have design intent scattered across chat sessions, impossible to trace.

metapowers solves these problems — it provides a set of battle-tested **universal skills** and an **engineering standard** ([AGENTS.md](AGENTS.md)) that keeps every skill consistently high-quality.

---

## Features

- **6 production-grade skills** — covering prompt design, deep research, knowledge distillation, skill testing, entity search, and long-term memory
- **Development/release separation** — `dev/` is the workshop, `skills/` is the showroom; design docs never ship to runtime
- **Design anchoring** — every skill has a SKILL-DESIGN.md recording design intent and key tradeoffs, preventing architectural drift
- **Strict documentation discipline** — skill content is unambiguous, self-contained, and never depends on conversation context
- **Versioning standards** — Patch/Minor/Major with clear criteria, determined only when the feature is complete

---

## Installation

Install the full metapowers skill set:

```bash
npx skills add LambdaXIII/metapowers
npx skills add LambdaXIII/metapowers -g # recommended: global install
```

Or install individual skills:

```bash
npx skills add LambdaXIII/metapowers --skill agent-prompt-design
npx skills add LambdaXIII/metapowers --skill skill-quick-test
npx skills add LambdaXIII/metapowers --skill skill-distillator
npx skills add LambdaXIII/metapowers --skill web-deep-research
npx skills add LambdaXIII/metapowers --skill web-entity-search
npx skills add LambdaXIII/metapowers --skill journaling
```

---

## Skills

### agent-prompt-design

A methodology for designing agent system prompts. Covers structure design, content writing, tool protocols, security hardening, and operations. Highlights: security as a design starting point; reasoning-model era (2026) strategies; a ten-anti-pattern diagnostic system.

### skill-quick-test

Rapid skill validation through parallel sub-agent reasoning. ISTQB six-step test design + capability simulation + strict isolation discipline.

### skill-distillator

Distills skill execution documents into human-readable methodology documents. Five-stage transformation pipeline with automatic skill type detection and adaptive conversion strategies.

### web-deep-research

Systematic deep web research. Clue-chain tracing + cross-referencing by information type (confidence scoring for facts, combination for knowledge, dispute analysis for opinions, methodology tracing for data).

### web-entity-search

Fast structured entity search that fills the gap between direct search and deep research. Covers 7 entity types. Core discipline: stop at ≥ 2 sources.

### journaling

A notebook system for agent long-term memory. Structured notes + maintenance protocols + progressive disclosure. The journal serves the agent itself.

---

## Project Structure

```
metapowers/
├── dev/                    # Development workspace
│   └── <skill-name>/
│       ├── content/        # Skill content (= release package)
│       ├── SKILL-DESIGN.md # Design anchor document
│       ├── CHANGELOG.md    # Change log
│       ├── test-space/     # Test cases
│       └── research/       # Reference materials
├── skills/                 # Release directory
│   └── <skill-name>/       # Copied from dev/<name>/content/
└── AGENTS.md               # Engineering standards
```

---

## Design Philosophy

**Universality first** — only skills that work for a different person on a different project.

**Independent, with recommendations** — each skill stands alone. Skills may recommend each other in descriptions, but never form hard dependencies.

**Development and release separated** — `dev/` keeps design docs and change logs; `skills/` ships clean skill packages only.

**Design before code** — write SKILL-DESIGN.md to anchor the design direction, then write the `content/` implementation.

---

## Contributing

1. **Verify universality** — would this skill work for someone else, on a different project?
2. **Follow the standards** — build directory structure, frontmatter, SKILL-DESIGN, and CHANGELOG per [AGENTS.md](AGENTS.md)
3. **One branch, one change** — each feature branch corresponds to one logical change
4. **Show the diff** — let maintainers see the full change before committing
5. **Discuss first** — not sure if it fits? Open an Issue

---

## License

[MIT](LICENSE)
