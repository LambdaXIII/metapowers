# Maintenance

## 目标

本协议结束时，所有维护信号归零，规范过时项已更新，过期条目已归档，
仪表盘无债务，维护备忘清零。下一个 session 从干净的仪表盘开始。

Journal cleanup is not automatic. Trigger when the journal feels off.

## Trigger Signals

- Stale active items: completed but not archived
- Topic fragmentation: same topic across multiple files
- Outdated information: facts or decisions no longer valid
- Mixed content: single file contains both stale and valid information
- Classification drift: directory scheme no longer matches usage
- Informal directories: directories with content that exist outside the current classification (those defined in `CLASSIFICATION.md` or, if CLASSIFICATION.md does not exist, the initial 4‑directory seed: inbox/, experience/, knowledge/, active_works/). These signal either missing formalization or content that should be redistributed.
- Dashboard staleness: INDEX.md status lines no longer reflect reality
- **Dashboard dilution**: 专项工作 has >1 line per domain, 最近变更 has >7 entries, or 经验摘要 contains axioms already in persona/memory. The dashboard drifts from "signal" to "log" — it reflects reality but fails to highlight what demands attention.
- Tag sprawl: 扫描所有条目的 tags frontmatter 发现未注册或同义标签。自由格式标签会退化为噪声——不可搜索，丧失可发现性价值。
- **Memo accumulation**: `.maintenance-memo.md` has 10+ items. The maintenance debt is accumulating faster than the regular schedule can absorb. Memo ≥10 alone maps to 2‑signal urgency (schedule off‑cycle at next session break). Memo ≥15 alone maps to 3+ signal urgency (off‑cycle now).
- Time-based: if last maintenance was over 14 days ago, perform at least a quick diagnostic scan — but content indicators (dashboard dilution, active_works/ staleness, topic fragmentation) are the primary triggers. Don't run a full maintenance pass on time alone if no content signals are present.

## Trigger Priority: Compound Signals

A single signal means "note it, don't interrupt current work." When signals compound, urgency escalates:

| Signals | Action |
|---------|--------|
| 1 signal | Note it. Do not interrupt current work. |
| 2 signals | Schedule off-cycle maintenance pass at the next session break (natural pause, topic switch, or end of current user interaction). |
| 3+ signals **or** memo ≥15 | Off-cycle maintenance pass **now** — complete current user interaction, then start maintenance. |

The "Don't Auto-Trigger" stance (single signal) does not override compound urgency. When ≥2 independent signals fire, the journal's integrity risk outweighs the interruption cost.

---

## Framework: Five‑Phase Maintenance

The maintenance framework follows a strict data‑first sequence:

```
Phase 0: Scan          — 收集数据，不做判断
Phase 1: Rule Review   — 基于扫描结果审查规范（分类规则 → tags）
Phase 2: Restructure   — 基于确认后的规范重组条目
Phase 3: Quality Check — 验证重组质量
Phase 4: Finalize      — 记录并关闭维护
```

Phase 0 和 Phase 1 之间有一道关键边界：**P0 只回答"当前是什么状态"**；**P1 才回答"这个状态是否需要改变规范"**。不要跨越边界。

---

### Phase 0: Scan — Build the Journal Snapshot

> 只收集数据，不做判断。所有输出是描述性的——标记问题，但不决定如何处理。
>
> Phase 0 的输出是一份 Journal 全局快照。Phase 1 的所有决策基于这份快照。

> `.maintenance-memo.md` accumulates during daily work. When you notice a problem — stale INDEX.md lines, fragmented topics, missing tags, structural drift — that isn't urgent enough to fix immediately, append a one-line note. The file doesn't exist until you first write to it; absence means zero accumulation.

| # | Step | Input | Output |
|---|------|-------|--------|
| 0 | **Read maintenance memo** | `.maintenance-memo.md` at journal root | Prioritized list of pre‑reported issues. These become additional scan targets — they don't replace the systematic scan (Steps 1‑8) but ensure nothing that was noticed during daily work gets forgotten. |
| 1 | **File‑level scan** | Full file list + directory tree | Anomaly log: non‑markdown files, misplaced entries, directories not in the current classification, entries with contradictions between their content and their directory. |
| 2 | **Group by topic** | All files | Per‑topic thread summary (3‑5 lines: background + current state + key files). |
| 3 | **Mark staleness** | Per file | State tags: `fully stale`（内容已过时或无当前项目关联） / `partially stale`（部分信息仍有效、部分已过时） / `still valid`（内容当前仍准确）。这些是推荐性标签——agent 根据 journal 自身情况和内容性质自行判定。标签仅描述状态，所标记内容的处置由 Phase 2 决定。 |
| 4 | **Deep‑check partially stale** | Files tagged `partially stale` | Extraction checklist: which information units to keep, which are stale. |
| 5 | **Collect directory usage stats** | Current directory tree + entry counts per directory | Per‑directory report: entry count, last‑modified range, topics present. For directories not in CLASSIFICATION.md, note whether the directory is an informal addition or a naming mismatch. |
| 6 | **Collect dashboard signal data** | INDEX.md (all sections) | Per‑section raw data: number of lines per domain in 专项工作, entry count in 最近变更, number of 经验摘要 entries with their current enforcement/survival/axiom tags (if tagged). |
| 7 | **Collect tag data** | All entry frontmatter + `<journal-root>/TAGS.md` | Three raw lists: (a) tags used but not in TAGS.md; (b) synonymous tags (same meaning, different names); (c) one‑off tags (used only once, no clear category). Do not decide what to do yet — just list them. |
| 8 | **Custom section audit** | INDEX.md | For any non-standard sections the agent has added to INDEX.md (e.g., self-regulation rules): assess whether they are still relevant, up-to-date, and anchored to valid journal entries. |

**Output of Phase 0**: A Journal Global Snapshot document containing:
- Directory usage report (from Step 5)
- Topic summaries (from Step 2)
- Anomaly log (from Step 1)
- Dashboard signal data (from Step 6)
- Tag raw lists (from Step 7)
- Custom section audit (from Step 8)
- Staleness tags + extraction checklists (from Steps 3‑4)

> ⚠️ **Phase 0 不产生决策。** 如果你发现自己在 Phase 0 中说"这个应该放到 X 目录"或"这个 tag 应该合并"，你正在跨入 Phase 1。停下——先把数据收集完。Phase 1 会基于完整数据做判断。

---

> ⚠️ **进入 Phase 1 前**：重读 Phase 0 快照数据（目录统计、staleness 标记、tag 列表），
> 确认数据解读无误后再做分类/tags 决策。如果对某个标记有疑问，重新打开对应文件确认——不要依赖记忆或假设。

> 基于 Phase 0 的快照，逐层审查规范。**依赖顺序**：先确定分类规则，再基于分类规则审查 tags。
>
> 两条规范的依赖链：
>
> ```
> CLASSIFICATION.md（分类规则）
>      ↓ 确定后
> Tags（基于分类规则的上下文）
> ```

#### Step 1: Review Classification Rules

**Input**: Phase 0 Step 5 (directory usage stats) + current `CLASSIFICATION.md` (if exists)

**Questions to answer**:

1. **覆盖性**：当前分类规则是否覆盖了所有现有内容？
   - 有没有内容不属于任何已定义目录？
   - 如果有，是需要调整规则，还是创建新目录？

2. **一致性**：规则是否与实际使用一致？
   - CLASSIFICATION.md 说 `experience/` 只放个人经验，但目录里有 40% 的外部研究——这是规则被忽略了，还是规则本身不适配？
   - 目录名和实际内容的"气味"是否一致？

3. **正交性**：是否有两条规则经常被同时适用？
   - 某条内容可以合理地放在两个目录 -> 是需要合并目录，还是跨域内容应该用链接/MOC 处理？

4. **健康度**：Phase 0 Step 5 报告的健康度数据
   - 空目录（0‑2 条）：是否需要合并？
   - 拥挤目录（>20 条）：是否需要拆分？如果拆，往哪个方向？
   - 不在 CLASSIFICATION.md 的非正式目录：是否应该被正式接纳？

**决策框架**：

| 情况 | 行动 |
|------|------|
| 4 个问题都回答"正常"或"在预期内" | 确认当前规则继续有效。不修改 CLASSIFICATION.md。 |
| 任何一个问题回答"有问题" | 加载 `references/design-classification.md`，走 Step 1‑5 流程，基于 Phase 0 的数据设计修订方案。 |
| CLASSIFICATION.md 不存在 | 加载 `references/design-classification.md`，走 Step 1‑5 流程，基于 Phase 0 的数据设计一份分类方案并写入。 |
| 沿袭默认种子结构（初始化时的 4 目录）但从未写 CLASSIFICATION.md | 评估默认结构是否仍然适配。如果适配，正式写入 CLASSIFICATION.md 确认；如果不适配，走设计流程修订。 |

**Output**: 
- **确认不变** → `CLASSIFICATION.md` 保持原样
- **需要修订** → 更新 `CLASSIFICATION.md`（新的目录定义、边界规则、跨域处理策略）
- **新建** → 写入 `CLASSIFICATION.md`

> ⚠️ **分类规则修订是重大操作。** 一个经过深思熟虑的分类方案不应该在每次维护时都改。只有在覆盖性、一致性、正交性或健康度出现明确信号时才触发修订。如果你在犹豫"要不要改"，默认不改——等到下次维护时如果信号仍然存在，再改。

>
> **Dashboard 组织审查**：如果 INDEX.md 当前的组织方式感觉不够用
> （信号不清晰、专项工作堆积、变更列表过长），审视当前 INDEX.md 的结构——
> 哪些信号在下一页才出现、哪些信息需要滚动才能看到、
> 哪些板块的噪声值超过了信号值。INDEX.md 的组织是自由演化的，没有固定模板。
> 关于为特定项目创建独立的次级 INDEX（Dashboard），参见 `references/dashboard.md`。
>
---

#### Step 2: Review Tags + Registry

**Input**: Phase 0 Step 7 (tag raw lists) + confirmed CLASSIFICATION.md from Step 1

**Three‑phase decision process**:

**Phase 2a: Handle unregistered tags**

对 Phase 0 Step 7 列出的未注册 tag，使用 Tag Worthiness Criteria 决定：

| 判定 | 行动 |
|------|------|
| 值得保留 | 注册到 `<journal-root>/TAGS.md` |
| 是已注册 tag 的同义词 | 合并——将所有出现替换为正式 tag，不在 registry 中创建新条目 |
| 不值得保留 | 从所有条目的 frontmatter 中移除 |
| 模糊但常用 | 保留但注册——有些模糊但高频的 tag 是有效的跨切面工具 |

**Overlap note**: 一个 tag 可能出现在多个列表中（如：未注册 + 单次 + 同义词）。决策优先级：值得保留 → 注册；同义词 → 合并；不值得保留且非同义词 → 移除，无论使用次数。

**Vague‑but‑common branch**: tags like `misc`, `general`, `notes` are never worth keeping — remove from all entries regardless of frequency.

**Phase 2b: Handle synonymous tags**

对于 Phase 0 发现的同义 tag 组，确定 canonical tag（正式名称）。合并指令（tag A → tag B）交给 Phase 2 执行。

**Phase 2c: Registry health check**

| 检查项 | 标准 |
|--------|------|
| TAGS.md 中的 tag 是否还有活跃条目使用？ | 零使用 → 从 TAGS.md 移除（但不必从已归档条目中删除，因为他们不会再被搜索） |
| 是否有新的内容类别需要新的 tag？ | 基于 Phase 0 的 topic 分组判断——如果一个 cluster 有 3+ 条目且没有合适的已有 tag，创建新 tag |
| TAGS.md 结构是否仍然合理？ | 如果已使用维度分类（activity/domain/meta/project 等），当前的维度是否仍然覆盖使用模式？如果出现大量维度外的 tag，考虑是否需要新增维度 |

**Output**:
- 注册/合并/移除/保留的 tag 清单
- Registry 更新内容
- Phase 2 的 tag remediation 指令

---

**End of Phase 1 — two specifications are now confirmed:**

| 规范 | 状态 |
|------|------|
| Classification rules (CLASSIFICATION.md) | ✅ 确认不变 / ✅ 已修订 |
| Tag registry (TAGS.md) | ✅ 确认 / ✅ 已维护 |

如果两条都没有任何变更，**仍然可以进入 Phase 2**——Phase 2 不只是执行变更，它也处理条目级别的重组（按旧规则搬文件、归档、清理）。

---

### Phase 2: Restructure — Apply the Confirmed Rules

> 基于 Phase 1 确认的规范执行重组。如果规范未变更，则按原有规则执行条目级别的重组（归档、移动、拆分）。

> 本阶段所有操作均为加法——新位置先就位，原位置后清理。
> 任何步骤中断只需继续执行，不会丢失数据。确认新文件正确后再清理旧位置。

| # | Step | Description |
|---|------|-------------|
| 1 | **Extract surviving content** | Using the extraction checklist from Phase 0 Step 4, pull valid information units from files to be archived and write them into the reorganized structure (new files or enrich existing ones). Source files remain in place during extraction — they are still readable. |
| 2 | **Archive** | All `fully stale` + `partially stale` files → move to `archive/` (create this directory if it does not yet exist). Partially stale files go whole — their original stays intact as history. By this point, surviving content has already been extracted. |
| 3 | **Reorganize structure** | Apply the classification structure from the confirmed CLASSIFICATION.md. Move entries between directories, rename directories if needed. Update INDEX.md links to their new paths BEFORE physically moving the files — the target paths are already determined by the Phase 1 reorganization plan. |
| 4 | **Tag remediation** | Execute the tag decisions from Phase 1 Step 2: (a) register new tags in `<journal-root>/TAGS.md`; (b) merge synonyms — replace all occurrences with the canonical tag; (c) remove discarded tags from entry frontmatter. **After removal:** verify affected entries still have ≥1 tag, or follow the rules in TAGS.md. Report counts: registered X, merged Y, removed Z. |
| 5 | **Trim 最近变更** | Cut to last 7 entries. The purpose is recency signal — "what happened in the last few sessions?" — not a chronological log. Older entries are findable via file system. |
| 6 | **Collapse 专项工作** | Reduce to one line per domain. Encode current work scene in each line (not just "active"/"completed"). Completed milestones from domains with no active work → remove after 2‑session cooling period. Scene encoding format: `Domain — 📝 当前工作场景：简短描述 [→](link)`. 一行一域 + 场景编码——让下次 session 一眼看清各域状态。 |
| 7 | **Split 经验摘要** | Tag each 经验摘要 entry as `enforcement` (reinforces a specific agent operating rule), `survival` (environment/tool trap not covered by persona/memory), or `axiom` (behavioral principle already in persona/memory). Remove axiom entries (de‑duplication: they are injected every turn already). Keep enforcement and survival entries. |
| 8 | **Write / update CLASSIFICATION.md** | If Phase 1 modified the classification rules, ensure CLASSIFICATION.md is up to date and placed at journal root. If CLASSIFICATION.md was newly created, confirm it is complete (definitions, boundaries, cross‑domain rules). |

> **"Extract first, archive later" logic**: Source files stay in place while extraction runs — no interruption‑safety checklist needed. After extraction is confirmed (new files written and verified), the archival move is safe. The original files enter `archive/` intact, preserving complete history alongside the extracted content.

> **Dashboard updates happen in Phase 2, not Phase 4.** File moves (Step 3) immediately invalidate all dashboard links pointing to moved files. Update INDEX.md links BEFORE moving files — otherwise the dashboard enters a broken‑link state between Phase 2 and Phase 4.

---

### Phase 3: Quality Check

| # | Dimension | Description |
|---|-----------|-------------|
| 1 | **Logical conflicts** | Contradictions between note contents. |
| 2 | **Content overlap** | Topic overlap or near‑duplication across notes. |
| 3 | **Broken links** | References pointing to archived content. Distinguish two cases: migrated to new location → fix the link; archived without extracting key points → decide whether to pull them back. Check any custom section tables first — they are often the most link‑dense parts of INDEX.md. |
| 4 | **Tag compliance** | After remediation, scan all entries: every tag must appear in `<journal-root>/TAGS.md`. Verify each entry follows the rules defined in TAGS.md. Flag any violators. |

---

### Phase 4: Finalize

| # | Step | Description |
|---|------|-------------|
| 1 | **Verify entry points** | Re‑check `INDEX.md` — all links resolve, 专项 work section is clean, 最近变更 is trimmed, 经验摘要 is de‑duplicated. Confirm no broken references were introduced. |
| 2 | **Update Protocol Declaration signal line** | Rewrite the `维护信号` line in INDEX.md Protocol Declaration to reflect the current maintenance snapshot. Examples: `维护信号：经验摘要含 axiom(2) · 最近变更 9/7 · 维护备忘 12/10`. This makes maintenance signals visible at a glance in the next session startup without requiring a full dashboard scan. |
| 3 | **Record restructuring** | Append a restructuring record to `INDEX.md` 最近变更. Include: what phases ran, what rules changed (if any), count of files moved/tags fixed/types corrected. |
| 4 | **Clear maintenance memo** | If `.maintenance-memo.md` exists and was read in Phase 0, clear its contents (or delete the file). All accumulated issues have been addressed through the full maintenance cycle — an empty or absent memo resets the accumulation counter for the next daily‑use cycle. |

---

## Pitfalls

- **Phase 0‑to‑Phase 1 boundary crossing**: The most common maintenance error is skipping straight from scanning to deciding — "I see a problem, let me fix it now." This skips the rule review step and leads to inconsistent decisions. Always complete Phase 0 fully (produce the snapshot document) before entering Phase 1.

- **Rule review without data**: Never start Phase 1 without a Phase 0 snapshot. The snapshot is the foundation — without it, Phase 1 decisions are based on memory and impression, not evidence.

- **Simultaneous rule + tag decisions**: Phase 1 Steps 1‑3 are sequential for a reason. Changing classification first, then adjusting types, then reviewing tags prevents rework (a tag decision made under old classification rules may become invalid after the rules change).

- **Custom section tables are link‑dense**: any custom tables added to INDEX.md (self-regulation rules, etc.) are the highest‑risk area for broken links after restructuring. Each table row may reference 2‑3 journal files. Check these first in Phase 3 Step 3.

- **Large‑file extraction fog**: Files >500 lines (e.g., 896‑line architecture dumps) make the "what to extract" decision hard. If no clear unique insight survives beyond what's already in other files, the correct decision is to not extract — the archive preserves the original for future reference.

- **Phantom dashboard signals**: `INDEX.md` 专项工作 lines with no journal file behind them (e.g., `竞品追踪 — 运行中` with no link, no entry anywhere). These survive unnoticed because they don't appear in file scans or link checks — they're text, not broken links. During Phase 0 Step 1, cross‑reference every untagged dashboard line against the file tree. A line without a `[→](...)` link that returns zero 搜索 hits is a phantom. Remove it in Phase 2.

- **Dashboard‑link staleness**: Phase 2 file moves immediately break dashboard links. Update INDEX.md links BEFORE moving files — not in Phase 4. The dashboard is the sole entry point for the next session; broken links mean the agent starts with invalid references.

- **Classification over‑revision**: A classification scheme that changes every maintenance pass is worse than a flawed but stable one. Phase 1 Step 1 has a built‑in bias toward "confirm unchanged" — only revise when there is clear evidence of mismatch. If you are unsure, defer to the next maintenance cycle. The criteria are designed to be conservative.

---

## Cleanup Pattern: Temporary Execution Artifacts

**Scenario**: Directories like `project‑implementation/` contain kanban tracking, check reports, and progress logs — temporary products of an implementation pass. The implementation is now complete.

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
| `INDEX.md` 专项工作 | The project status line |
| `INDEX.md` 最近变更 | The changelog summary line |
| Workspace dashboards or topic `README.md` files | The item description |
| Other journal entries | Cross‑references to the renamed item |
| The file itself | If the old name is in the filename, rename is higher‑touch |

**Procedure**:
1. Search the journal directory for the old name
2. Enumerate all matches before touching any file
3. Update from most‑referenced to least (main entry → INDEX.md → workspace READMEs → other entries)
4. Re‑read INDEX.md and affected workspace files to confirm the old name is gone

**Common traps**:
- Code blocks: edit tool's fuzzy matching may catch adjacent lines. Mitigate by reading affected regions after the edit.
- Deferred updates: "I'll rename the file later when structure stabilizes" — this leaves a dead link. Either rename now or don't promise. No mid‑ground.
- Partial updates: It's easy to update the first two mentions and miss the third. The enumeration step prevents this — work from a complete list, not memory.

---

## Skill Graduation

Experience entries that are validated, generalized, reusable, and non‑project‑specific can become skills during maintenance. Manual, not automatic.
