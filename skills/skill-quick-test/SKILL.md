---
name: skill-quick-test
description: Quickly test a skill's usability by parallel rehearsal with sub-agents — verifying that an Agent can correctly understand the skill, walk through its flow, and complete tasks in different usage scenarios. Complements skill-creator's functional testing; does not replace it. 通过子代理并行推演（parallel rehearsal）快速测试技能可用性——验证 Agent 能否理解技能、走通流程、完成任务。触发：「推演 / 测试 / 验一下 / 快速验证 / 走通」一个技能。
metadata:
  version: "1.4.5"
  last_updated: "2026-08-23"
  author: "Ĉalio"
---

# Skill Quick Test

Quickly test a skill's usability by **parallel rehearsal with sub-agents**.

> **Prerequisite:** the runtime must support sub-agent delegation (`delegate_task`). If the current environment lacks this capability, this skill cannot be used.

---

## When to use

- New skill, quick usability verification before submission
- After modifying a skill, regression-verify the fix
- Multi-round iteration, tracking quality trends
- Comparing against baseline (behavior difference with vs without loading the skill)

**This skill vs skill-creator testing:**

| | skill-creator testing | skill-quick-test |
|---|---|---|
| What it tests | Functional correctness (loads, executes) | Usability (Agent understands, walks through, completes tasks) |
| How it tests | Structured verification process | Rehearsal: simulating the full chain of an Agent using the skill |
| Complementarity | Neither can replace the other | — |

---

## Flow overview

                                             │                          │               │
                    steps 1-5 coverage all pass      Light: complex <2 & total <5  ≥2 aborts → terminate
                    step 6 error-pattern check      Full:  complex ≥2 or total ≥5  otherwise → summarize
```
                            │                            │                 │
                   steps 1-5 coverage all pass     Light: complex <2 & total <5  ≥2 aborts → terminate
                   step 6 error-pattern check     Full:  complex ≥2 or total ≥5  otherwise → summarize
```

**Step details:**

| Step | Input | Output | Reference |
|------|-------|--------|-----------|
| Analyze scope | The tested skill's SKILL.md | Functional domains, path set, decision points, capability boundaries | scope-analysis.md |
| Design scenarios | Scope-analysis output | Equivalence-class combinations, boundary tests, end-to-end cases | scenario-design.md |
| Coverage check | Scenario-design output | Coverage-standard check results item by item | scenario-design.md (per-step coverage standards) |
| Error patterns | All files of the tested skill | Anti-pattern check results item by item | error-patterns.md |
| User confirmation | Summary of all of the above | Test-case list + user approval/revision | — |
| Execute | Scenario cards + context template | Sub-agent rehearsal reports | execution-light/full.md |
| Fatal check | Sub-agent return values | Continue / abort this round | execution-light.md |
| Summarize | All reports + expected effects | Defect list + comparative analysis + scoring | summarization.md, scoring-rubric.md |

**Light mode:** everything in conversation, no files written. Sub-agents are forbidden from writing files.
**Full mode:** write a test plan first → delegate sub-agents to write report files → read files and summarize.

| | Light mode | Full mode |
|---|---|---|
| Applicable when | complex scenarios < 2 and total < 5 | complex scenarios ≥ 2 or total ≥ 5 |
| Test plan | verbal confirmation, no file | test-plan.md written first |
| Sub-agent output | return-value report, no file writes | allowed to write into reports/ directory |
| Data source | sub-agent conversation return values | reading report files |

Temp directory: `$SKILL_TEST_DIR/<round-id>/`; falls back to `<cwd>/.quick-tests/<round-id>/` when unset.

---

## Core constraints

### 🚫 Isolation rule (information boundary)

When delegating to sub-agents, information that must **never** appear in the context:

- Expected effects
- The existence of other test units
- That this is a baseline / control / experiment group
- Any comparative information

The sub-agent receives only: usage-scenario description + entry path + goal + loading rules + rehearsal guide + failure behavior.

### 🔧 Loading rules (tool constraints)

Sub-agents **must** read all files of the tested skill with `read_file`. **Forbidden** to use `skill_view` on the tested skill.

The rehearsal guide is embedded in the context template (empty-start → follow step by step → boundary probing), and does not depend on any external skill.

### 🔄 Capability simulation (behavior rules)

For **external capabilities** referenced by the tested skill, test sub-agents do not actually invoke them — they simulate execution and record assumptions:

| Capability type | Trigger scenario | Simulation |
|-----------------|-----------------|------------|
| Sub-agent delegation | `delegate_task` / `task` | Play the delegated role and continue the rehearsal toward the goal |
| Tool invocation | `bash`, `eval`, `browser`, etc. | Read tool intent and arguments → rehearse plausible results from the scenario |
| Script execution | `scripts/*.py` etc. | Read script source → rehearse the logical output (no actual run) |

Mark uniformly in path tracing: `[能力模拟] [委派/工具/脚本] → 动作描述 → 推演结果`（协议字面量，与 references 模板一致，不翻译）

### ⚠️ Failure behavior (fault tolerance)

- **Sub-agent side**: on systemic obstacles (file missing, broken path, etc.) — do not work around on its own; return a 「推演中止」 report directly
- **Main-agent side (launch failure)**: ≥ 2 sub-agents fail to launch (429, timeout, etc.) → abort this round, report the failure reason and advice to the user
- **Main-agent side (rehearsal aborted)**: ≥ 2 sub-agents return 「推演中止」 for the same class of systemic issue → abort this round, output diagnosis

### 📋 Presentation principles (output control)

- Intermediate steps (scope analysis, scenario-design process, coverage-check details) are not proactively shown to the user
- Only output a concise test-case list at the "user confirmation" node
- Expand only when the user asks to see the process

---

## Test-case design methodology

Six-step method based on the ISTQB framework:

| Step | Reference | Output |
|------|-----------|--------|
| 1. Identify input space | references/scope-analysis.md | Functional domains, path sets, decision points, capability boundaries |
| 2. Equivalence-class partitioning | references/scenario-design.md | Usage-scenario combinations (entry × clarity × context) |
| 3. Boundary testing | references/scenario-design.md | Two-way test of each stated boundary |
| 4. Decision-logic coverage | references/scenario-design.md | Decision-tree branch paths (only when a decision tree exists) |
| 5. End-to-end cases | references/scenario-design.md | Complex scenarios + baseline |
| 6. Error-pattern check | references/error-patterns.md | Anti-patterns checked item by item |

Each step produces both design actions and the corresponding coverage standard. Coverage check is the gate after steps 2–6 — no entry to user confirmation unless all pass.

---

## Reference-file index

| Stage | File | Content |
|-------|------|---------|
| Scope analysis | references/scope-analysis.md | Step 1: extract input space (functional domains/path sets/decision points/boundaries) |
| Scenario design | references/scenario-design.md | Steps 2–6: equivalence classes/boundaries/decisions/cases/error patterns + coverage standards + pattern determination |
| Error patterns | references/error-patterns.md | Step 6: anti-pattern list (accumulates with testing experience) |
| Light execution | references/execution-light.md | Light-mode sub-agent delegation format, capability simulation, abort checks |
| Full execution | references/execution-full.md | Full-mode directory structure, plan gate, report management |
| Summarization | references/summarization.md | Step 0 fatal check → per-scenario comparison → multi-unit comparison → defect dedup → global scoring |
| Scoring rubric | references/scoring-rubric.md | Five-dimension scoring system (optional, executed by main agent after summarization) |

## Template index

| Template | Purpose |
|----------|---------|
| templates/test-plan.md | Full-mode test plan (simple test list + complex scenario list) |
| templates/scenario-card.md | Sub-agent report format (with capability-simulation annotations) |
| templates/summary-report.md | Summary report format |

## Sub-agent resources

| File | Purpose |
|------|---------|
| — | All resources needed by sub-agents are embedded in the context template; no standalone resource files needed. |
