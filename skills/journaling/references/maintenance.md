# Maintenance

Journal cleanup is not automatic. Trigger when the journal feels off.

## Trigger Signals

- Stale active items: completed but not archived
- Topic fragmentation: same topic across multiple files
- Outdated information: facts or decisions no longer valid
- Mixed content: single file contains both stale and valid information
- Classification drift: directory scheme no longer matches usage
- Informal directories: directories with content that exist outside the standard structure (active/, goal/, experience/, archive/, workspace/). These signal either missing formalization or content that should be redistributed.
- Dashboard staleness: index.md status lines no longer reflect reality
- **Dashboard dilution**: 专项工作 has >1 line per domain, 最近变更 has >7 entries, or 经验摘要 contains axioms already in persona/memory. The dashboard drifts from "signal" to "log" — it reflects reality but fails to highlight what demands attention.
- Tag sprawl: 扫描所有条目的 tags frontmatter 发现未注册或同义标签。自由格式标签会退化为噪声——不可搜索，丧失可发现性价值。
- **Memo accumulation**: `.maintenance-memo.md` has 10+ items. The maintenance debt is accumulating faster than the regular schedule can absorb. Overrides single-signal deferral — alone this is a qualified off-cycle trigger.
- Time-based: if last maintenance was over 14 days ago, perform at least a quick diagnostic scan — but content indicators (dashboard dilution, active/ staleness, topic fragmentation) are the primary triggers. Don't run a full maintenance pass on time alone if no content signals are present.

## Trigger Priority: Compound Signals

A single signal means "note it, don't interrupt current work." When signals compound, urgency escalates:

| Signals | Action |
|---------|--------|
| 1 signal | Note it. Do not interrupt current work. |
| 2 signals | Schedule off-cycle maintenance pass at the next session break (natural pause, topic switch, or end of current user interaction). |
| 3+ signals **or** memo ≥15 | Off-cycle maintenance pass **now** — complete current user interaction, then start maintenance. |

The "Don't Auto-Trigger" stance (single signal) does not override compound urgency. When ≥2 independent signals fire, the journal's integrity risk outweighs the interruption cost.

## Framework: Four-Phase Maintenance

### Phase 1: Diagnose (make reversible preliminary judgments; defer irreversible actions to Phase 2)

All judgments made in Phase 1 can be revised — they are starting points, not commitments. Grouping, staleness tagging, and tag classification are all preliminary. The irreversible operations (moving files, deleting content) happen in Phase 2.

| # | Step | Input | Output |
|---|------|-------|--------|
| 0 | **Read maintenance memo** | `.maintenance-memo.md` at journal root | Prioritized list of pre-reported issues. These become additional diagnosis targets — they don't replace the systematic scan (Steps 1-9) but ensure nothing that was noticed during daily work gets forgotten. After processing memo items, clear them from the file. |
| 1 | **File-level scan** | Full file list + directory tree | Anomaly log (non-markdown files, misplaced entries, informal directories not in the standard structure, etc.) |
| 2 | **Group by topic** | All files | Per-topic thread summary (3–5 lines: background + current state + key files) |
| 3 | **Mark staleness** | Per file | Status tags: `fully stale` / `partially stale` / `still valid` |
| 4 | **Deep-check partially stale** | Files tagged `partially stale` | Extraction checklist: which information units to keep, which are stale |
| 5 | **Review classification** | Topic summaries + current directory structure | Structure change proposal (add/remove dashboards, rename directories, etc.) |
| 6 | **Dashboard signal audit** | index.md (all sections) | Signal health report |
| 7 | **Update Protocol Declaration signal line** | index.md Protocol Declaration | Rewrite the `维护信号` line to reflect the current maintenance snapshot. Examples: `维护信号：经验摘要含 axiom(2) · 最近变更 9/7 · 维护备忘 12/10`. This makes maintenance signals visible at a glance in the next session startup without requiring a full dashboard scan. |
| 8 | **Tag audit** | All entry frontmatter + tag-registry.md | Three lists: (a) tags used but not in registry; (b) synonymous tags (same meaning, different names); (c) one-off tags (used only once, no clear category). Output a remediation plan with per-tag decisions: register, merge, or remove. **Overlap note:** A tag may appear in multiple lists (e.g., one-off + unregistered). Decision priority: if worth keeping → register; if synonym → merge (canonical tag wins); if neither worth keeping nor a synonym → remove, regardless of use count. **Vague-but-common branch:** tags like `misc`, `general`, `notes` are never worth keeping — remove from all entries regardless of frequency. |
| 9 | **Gate audit** | index.md action gate + write gate | For each gate: (a) count rules — action gate max 9, write gate max 5 per sub-table; (b) check each rule's failure incident — is the project still active? Is the failure pattern still recurring? Remove dead rules. (c) Check for overlapping rules → merge. (d) Check for gaps — has a new failure pattern emerged that needs a new rule? Add it. |

Apply the **mistake test** to every line in index.md: "If this line were absent from my next session startup, would I make a mistake?" Lines that fail this test are noise, not signal. "This is important" ≠ "I would make a mistake without it." The test is intentionally harsh — the dashboard is a supplement to memory and gates, not a duplicate of them.

**Per-section audit procedure:**

- **经验摘要**: Tag each entry as `enforcement` (reinforces a specific gate rule — e.g., "文档先行不是好习惯，是唯一质控手段" justifies the doc-review gate rule), `survival` (environment/tool trap not covered by persona/memory — e.g., "WSL mirror 模式下 vite 需 --host 0.0.0.0"), or `axiom` (behavioral principle already in persona/memory — e.g., "讨论→共识→计划→行动"). Enforcement → keep (makes gates feel earned). Survival → keep (no other mechanism catches these). Axiom → remove (de-duplication: it's injected every turn already).

- **专项工作**: Count lines per domain. >1 line per domain → project log, not dashboard. Collapse to one line per domain. The remaining line must encode the current **work scene** — not just "active" or "completed", but what kind of work is happening: `项目 A — 📝 文档修缮：边界条件对齐` tells the agent "the doc-review gate rule will likely trigger." Scene encoding bridges the gap between dashboard (what's happening) and gate (what to read before acting). Completed milestones stay on the dashboard for 2 sessions after completion (cooling period), then sink to experience/ — this prevents the signal from disappearing before it's been consumed.

- **最近变更**: Count entries. >7 → trim to last 7. The purpose is recency signal — "what happened in the last few sessions?" — not a chronological archive of all activity.

- **行动闸门**: Check each rule's linked failure incident — is the project still active? Archived project with no active work scene → remove rule. Rules without active projects are dead weight. Count rules — if ≥10, merge overlapping rules or move non-project-specific rules to memory's hard-constraint section.

- **写入闸门**: Check each self-question — is the failure mode it encodes still relevant? Has a new pollution pattern emerged? Remove stale questions, add new ones for new failure modes. The write gate is a living document — it should reflect current failure patterns, not historical ones.

- **Cross-reference**: Every dashboard line with a `[→](...)` link must resolve to an existing file. Every line without a link must correspond to a real journal entry (搜索验证). Lines failing both checks are phantoms — remove them.

**Key constraint**: Step 3 tags describe *state*, not decisions. `partially stale` is a state label — what to do with it is decided in Phase 2.

**informal-directory pitfall** — Directories not in the standard set (active/, goal/, experience/, archive/, workspace/) are easy to overlook during Step 1 because they contain valid markdown files and don't trigger "misplaced entry" flags. To catch them: after listing all files, extract unique parent directories and diff against the known set. Each informal directory must be either formalized (create README.md, integrate into index.md) or have its contents redistributed into standard directories before removal.

**goal/ classification pitfall** — `goal/` entries are especially prone to drift:
- A goal recorded 7+ days ago with no follow-up is likely stale, not "in progress"
- A design document whose content was migrated to formal project docs is a holding pen — archive it
- A bug-fix list for an old architecture is not a goal
- Ask: "If I deleted this, would any active work lose its north star?" No → not a goal

### Phase 2: Restructure (execute structural changes)

| # | Step | Rationale |
|---|------|-----------|
| 1 | **Extract surviving content first** | Using the extraction checklist from Phase 1 Step 4, pull valid information units from files to be archived and write them into the reorganized structure (new files or enrich existing ones). Source files remain in place during extraction — they are still readable. |
| 2 | **Archive** | All `fully stale` + `partially stale` files → move to `archive/`. Partially stale files go whole — their original stays intact as history. By this point, surviving content has already been extracted. |
| 3 | **Reorganize structure** | Apply the structure change proposal from Phase 1 Step 5. The target structure is now in place. |
| 4 | **Trim 最近变更** | Cut to last 7 entries. The purpose is recency signal — "what happened in the last few sessions?" — not a chronological log. Older entries are findable via file system. |
| 5 | **Tag remediation** | Execute the remediation plan from Phase 1 Step 7. For each tag: (a) register it in tag-registry.md if genuinely needed; (b) merge synonyms — replace all occurrences with the canonical tag, don't register a duplicate; (c) remove one-off tags from entry frontmatter. **After removal:** verify affected entries still have ≥1 tag. Report counts: registered X, merged Y, removed Z. |
| 6 | **Collapse 专项工作** | Reduce to one line per domain. Encode current work scene in each line (not just "active"/"completed"). Completed milestones from domains with no active work → remove after 2-session cooling period. Scene encoding format: `Domain — 📝 当前工作场景：简短描述 [→](link)`. |
| 7 | **Split 经验摘要** | Remove `axiom` entries already covered by persona/memory (de-duplication). Keep `enforcement` entries that reinforce gate rules, `survival` entries for environment/tool traps, and `methodology` entries for reusable cross-domain insights. |

**"Extract first, archive later" logic**: Source files stay in place while extraction runs — no interruption-safety checklist needed. After extraction is confirmed (new files written and verified), the archival move is safe. The original files enter `archive/` intact, preserving complete history alongside the extracted content.

### Phase 3: Quality Check (fix issues introduced by restructuring)

| # | Dimension | Description |
|---|-----------|-------------|
| 1 | **Logical conflicts** | Contradictions between note contents |
| 2 | **Content overlap** | Topic overlap or near-duplication across notes |
| 3 | **Broken links** | References pointing to archived content. Distinguish two cases: migrated to new location → fix the link; archived without extracting key points → decide whether to pull them back |
| 4 | **Tag compliance** | After remediation, scan all entries: every tag must appear in tag-registry.md. Flag any remaining violators. Check that each entry has at least one activity tag or meta tag (project tags are optional, domain tags are optional). Entries with only meta tags and no activity tag are misclassified. |

### Phase 4: Finalize (verify and record the pass)

| # | Step | Description |
|---|------|-------------|
| 1 | **Verify entry points** | Re-check `index.md` — all links resolve, focused work section is clean, recent changes are trimmed. Confirm no broken references were introduced. |
| 2 | **Record restructuring** | Append a restructuring record to `index.md` recent changes. |

> **Dashboard updates happen in Phase 2, not Phase 4.** File moves (Phase 2 Step 3) immediately invalidate all dashboard links pointing to moved files. Update index.md links BEFORE moving files — otherwise the dashboard enters a broken-link state between Phase 2 and Phase 4.

## Skill Graduation

Experience entries that are validated, generalized, reusable, and non-project-specific can become skills during maintenance. Manual, not automatic.

## Tag Worthiness Criteria

When deciding whether an unregistered tag is "worth keeping" during Phase 1 Step 7, apply four dimensions:

| Dimension | Question | Signals "keep" | Signals "remove" |
|-----------|----------|----------------|------------------|
| **Distinction** | How much does this tag narrow a search? | Clearly separates a distinct class of entries (e.g., `competitive-tracking` filters to 2 files out of 50) | Too broad to be useful (e.g., `design`) or already covered by existing tag combinations |
| **Reuse expectation** | Will future entries use this tag? | The activity/project it describes is ongoing and will produce more entries | One-off event or defunct project with no future output |
| **Substitutability** | Can a registered tag combination cover the same need? | No existing tag captures this dimension (e.g., a subsystem tag distinct from a broader project tag) | A pair of existing tags provides the same filtering power (e.g., `[project-tag, debugging]` instead of `bug`) |
| **Context loss** | If removed, does the entry retain enough multidimensional classification? | Removal leaves the entry with only 1-2 very broad tags, losing searchability | After removal, the entry still has 2+ tags across different categories |

A tag doesn't need to score high on all four — even one strong signal can justify keeping it. Conversely, a tag that scores low on all four should be removed regardless of how many entries use it.


## Pitfalls

- **Gate rules are link-dense**: `index.md` 行动闸门 table is the highest-risk area for broken links after restructuring. Each table row references 2–3 journal files. Check this section first in Phase 3.
- **Large-file extraction fog**: Files >500 lines (e.g., 896-line architecture dumps) make the "what to extract" decision hard. If no clear unique insight survives beyond what's already in other files, the correct decision is to not extract — the archive preserves the original for future reference.
- **Phantom dashboard signals**: `index.md` 专项工作 lines with no journal file behind them (e.g., "竞品追踪 — 运行中" with no link, no entry anywhere). These survive unnoticed because they don't appear in file scans or link checks — they're text, not broken links. During Phase 1 Step 1, cross-reference every untagged dashboard line against the file tree. A line without a `[→](...)` link that returns zero 搜索 hits is a phantom. Remove it.
- **Dashboard-link staleness**: Phase 2 file moves immediately break dashboard links. Update index.md links BEFORE moving files — not in Phase 4. The dashboard is the sole entry point for the next session; broken links mean the agent starts with invalid references.

## Cleanup Pattern: Temporary Execution Artifacts

**Scenario**: Directories like `project-implementation/` contain kanban tracking, check reports, and progress logs — temporary products of an implementation pass. The implementation is now complete.

**Handling**:
1. Extract reusable lessons → `experience/` (e.g., kanban workflow insights, tooling pitfalls)
2. Archive the rest intact → `archive/<topic>/implementation/` (file inventory, known issues, phase status)
3. The implementation directory itself is removed once all content is relocated

---

## Cleanup Pattern: Cascade Rename

**Scenario**: A concept, project, entry title, or tool name in the journal has changed. The old name appears in multiple files — updating only the main entry is not enough.

**Required checkpoints** — search the journal for the OLD name in all of:

| Location | What to update |
|----------|---------------|
| Main entry file | Frontmatter `title` and `summary`; body references |
| `index.md` 专项工作 | The project status line |
| `index.md` 最近变更 | The changelog summary line |
| `active/README.md` | The active item description |
| Other journal entries | Cross-references to the renamed item |
| The file itself | If the old name is in the filename, rename is higher-touch |

**Procedure**:
1. Search the journal directory for the old name
2. Enumerate all matches before touching any file
3. Update from most-referenced to least (main entry → index.md → active/README → other entries)
4. Re-read index.md and active/README.md to confirm the old name is gone

**Common traps**:
- Code blocks: edit tool's fuzzy matching may catch adjacent lines. Mitigate by reading affected regions after the edit.
- Deferred updates: "I'll rename the file later when structure stabilizes" — this leaves a dead link. Either rename now or don't promise. No mid-ground.
- Partial updates: It's easy to update the first two mentions and miss the third. The enumeration step prevents this — work from a complete list, not memory.
