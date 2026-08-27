---
name: agent-prompt-design
description: |
  Design Agent system prompts (系统提示词 / agent prompt): structure, content
  writing, tool protocols, safety hardening, operations. Use when the user
  asks for a system prompt or an Agent instruction set — 「帮我写系统提示词 /
  这个 agent 需要什么指令 / 设计 agent 的 prompt」/ "write a system prompt" —
  or wants an existing Agent's instruction conflicts, tool overload, or
  security holes diagnosed. Not for ordinary one-off prompts.

metadata:
  version: "1.0.4"
  last_updated: "2026-08-23"
  author: "Ĉalio"
---

# agent-prompt-design: Agent System Prompt Design Methodology

> From structure design to safety hardening — take Agent system prompts from "it works" to "it is reliable".

---

## Content Index

### Core references (load on demand)

| File | Topic | When to load |
|------|-------|-------------|
| [references/context-engineering.md](references/context-engineering.md) | Paradigm shift (Prompt Eng → Context Eng), attention budget, right altitude | Understanding the theoretical foundation; behavior degradation in long Agent conversations |
| [references/structure-design.md](references/structure-design.md) | Layered structure, tag selection, the 8 major components | Designing the structure of a system prompt from scratch |
| [references/content-writing.md](references/content-writing.md) | The five iron rules, Few-Shot, role definition, output format | Writing instruction body text; diagnosing vague/contradictory instructions |
| [references/reasoning-models-2026.md](references/reasoning-models-2026.md) | Reasoning-model strategy shifts, effort control, CoT traps | Target model is Claude 4.6+ / GPT-5.x / Gemini Deep Think |
| [references/tool-design.md](references/tool-design.md) | Minimal viable tool set, tool contracts, calling protocol | Designing tools; Agent over-calls or misses tools |
| [references/safety.md](references/safety.md) | Safety as first-order variable, injection defense, three-layer boundary | Before production deployment; security review; Agent touches untrusted external content |
| [references/operations.md](references/operations.md) | Four pillars, version management, regression testing, iteration process | Team collaboration; long-term maintenance; CI/CD integration |
| [references/anti-patterns.md](references/anti-patterns.md) | Ten anti-patterns + diagnostic process + self-check checklist | Agent behavior anomalies; reviewing existing prompts |
| [references/model-specific.md](references/model-specific.md) | Four-vendor differentiation strategies + cross-model principles | Tuning for a specific model; migrating across models |

### Templates (copy and use)

| File | Content | When to use |
|------|---------|-------------|
| [templates/generic-agent.md](templates/generic-agent.md) | Generic Agent system prompt template (fill-in-the-blank) | Starting point for most scenarios |
| [templates/deepmind-reasoning.md](templates/deepmind-reasoning.md) | DeepMind 9-step forced pre-action reasoning template | High-reliability, complex, multi-step Agents |
| [templates/three-layer-boundary.md](templates/three-layer-boundary.md) | Three-layer boundary framework template | Embeddable into the generic template or standalone |
| [templates/tool-calling-protocol.md](templates/tool-calling-protocol.md) | Tool-calling protocol template | For the tool-usage section of a system prompt |

---

## How to Use

### Quick decision tree

```
What is your situation?
│
├── Designing a system prompt from scratch
│   → structure-design.md (structural framework)
│   → content-writing.md (writing instruction body)
│   → tool-design.md (if tools need defining — i.e. API function calls, not business systems)
│   → safety.md (safety is a design starting point, not a deployment afterthought)
│   → templates/ pick a starting template
│
├── Existing Agent, abnormal behavior
│   → anti-patterns.md (diagnose against the ten anti-patterns)
│   → locate the problem → load the matching reference and fix
│   → verify the fix with the self-check checklist
│
│   (if the anomaly relates to safety → run the "Safety Review" branch below first, then diagnose)
├── Preparing for production deployment / security review
│   → safety.md (required: injection defense + three-layer boundary)
│   → operations.md (if team collaboration and version management are needed)
│
├── Tuning for a specific model
│   → model-specific.md (compare differences across the four vendors)
│   ├── target is a reasoning model → read reasoning-models-2026.md first
│   ├── target is NOT a reasoning model → skip reasoning-models-2026.md
│
├── Migrating prompts from model A to model B
│   → model-specific.md (compare the two: tag preferences, reasoning strategy, safety features)
│   → tags need changing → structure-design.md §2
│   → re-check the iron rules → content-writing.md
│   → check and adapt the tool protocol → tool-design.md
│   ├── target is a reasoning model → reasoning-models-2026.md
│   → regression testing → operations.md §3 (at least 20 test cases)
│   → security review → safety.md §6 (recalibrate the three-layer boundary)
│   ✅ After migration, self-check: tags, iron rules, tools, reasoning strategy, security boundary — all five dimensions covered
│
│   **Migration checklist (complete in order):**
│   □ 1. Tag structure → compare via model-specific.md + adjust via structure-design.md §2
│   □ 2. Instruction writing → re-check the five iron rules in content-writing.md
│   □ 3. Tool protocol → check function-call compatibility in tool-design.md
│   □ 4. Reasoning strategy → reasoning-models-2026.md (if applicable)
│   □ 5. Regression testing → operations.md §3 (at least 20 cases)
│   □ 6. Security boundary → recalibrate the three-layer boundary in safety.md §6
│
├── Want to understand the theoretical foundation
│   → context-engineering.md
│
└── Long-term maintenance / multi-person collaboration
    → operations.md
```

### Iterative development process

```
Strongest model + simplest prompt
    ↓
Establish baseline performance (Evals)
    ↓
Observe failure modes → add instructions/examples only for those failures
    ↓
Regression testing (replay historical interactions) → confirm no degradation
    ↓
Cost/latency optimization
    ↓
Continuous monitoring + iteration
```

---

## Capability Boundaries

### What it provides

- ✅ **Structure design** principles for system prompts (layering, tag selection, 8 major components)
- ✅ **Content writing** methodology (five iron rules, Few-Shot, role definition, output format)
- ✅ **Reasoning model** (2026) specific strategies (effort control, CoT traps)
- ✅ **Tool definition** standards (minimal viable tool set, calling protocol, error recovery)
- ✅ **Safety protection** strategies (injection defense, three-layer boundary, production checklist)
- ✅ **Operations management** process (four pillars, versioning, regression testing)
- ✅ **Differentiation strategies** for four frontier vendors (Anthropic / Google / OpenAI / xAI)
- ✅ Ready-to-copy **templates**
- ✅ **Anti-pattern diagnosis** + troubleshooting workflow

### What it does NOT provide

- ❌ Domain-specific business logic (e.g. "what a financial-service agent should say")
- ❌ Code implementation (e.g. API calls, integration code)
- ❌ Training-level guidance — model fine-tuning, RLHF, etc.
- ❌ Localization advice for non-English models

### Supported models

Covers Claude 4.6+, Gemini 3.x, GPT-5.x / o-series, Grok 4.x, and frontier models of comparable capability. For older models (GPT-3.5, Claude 2, etc.): this skill's core strategies target 2026 frontier models. Users of older models should consult the version-tagged strategies in each reference file; untagged strategies default to frontier models.
