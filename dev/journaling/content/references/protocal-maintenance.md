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
Phase 1: Review → Design → Settle → Plan
                       — 带着三规则审查现状、设计目标组织方式、确认三规则变更、制定重组计划
Phase 2: Execute       — 先改三规则，再重组条目
Phase 3: Quality Check — 双向检验：规则微调 + 条目合规
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
| 0 | **Read maintenance memo** | `.maintenance-memo.md` at journal root | Prioritized list of pre‑reported issues. These become additional scan targets — they don't replace the systematic scan (Steps 1‑9) but ensure nothing that was noticed during daily work gets forgotten. |
| 1 | **File‑level scan** | Full file list + directory tree | Anomaly log: non‑markdown files, misplaced entries, directories not in the current classification, entries with contradictions between their content and their directory. |
| 2 | **Group by topic** | All files | Per‑topic thread summary (3‑5 lines: background + current state + key files). |
| 3 | **Mark staleness** | Per file | State tags: `fully stale`（内容已过时或无当前项目关联） / `partially stale`（部分信息仍有效、部分已过时） / `still valid`（内容当前仍准确）。这些是推荐性标签——agent 根据 journal 自身情况和内容性质自行判定。标签仅描述状态，所标记内容的处置由 Phase 2 决定。 |
| 4 | **Deep‑check partially stale** | Files tagged `partially stale` | Extraction checklist: which information units to keep, which are stale. |
| 5 | **Collect directory usage stats** | Current directory tree + entry counts per directory | Per‑directory report: entry count, last‑modified range, topics present. For directories not in CLASSIFICATION.md, note whether the directory is an informal addition or a naming mismatch. |
| 6 | **Collect dashboard signal data** | INDEX.md (all sections) | Per‑section raw data: number of lines per domain in 专项工作, entry count in 最近变更, number of 经验摘要 entries with their current enforcement/survival/axiom tags (if tagged). |
| 7 | **Collect tag data** | All entry frontmatter + `<journal-root>/TAGS.md` | Three raw lists: (a) tags used but not in TAGS.md; (b) synonymous tags (same meaning, different names); (c) one‑off tags (used only once, no clear category). Do not decide what to do yet — just list them. |
| 8 | **Custom section audit** | INDEX.md | For any non-standard sections the agent has added to INDEX.md (e.g., self-regulation rules): assess whether they are still relevant, up-to-date, and anchored to valid journal entries. |
| 9 | **Collect convention data** | `<journal-root>/CONVENTIONS.md` (if exists) | List of convention entries: pattern name, scope, file path, created date, self-check status. Report whether any convention's scope overlaps with other rules or is stale. |
| 10 | **Scan archive/** | `<journal-root>/archive/` directory listing | Archive snapshot: all entries with file dates, tags (extracted from frontmatter or filename), and original directory source. Note entries archived in the current cycle by comparing file mtime to the last maintenance date. These are **protected**: they must not be hard-deleted in this cycle. |
| 11 | **Check contract staleness** | Contract files found in common carrier locations (agent config dirs: RULES.md, AGENTS.md; project AGENTS.md; global agent config) — located by grepping for `index\.md\|journal-root\|写入操作.*journaling` (case-insensitive). | Contract staleness report: (a) path of each contract file found, (b) per-file line-by-line comparison with latest template across four dimensions — startup wording strength (第一步 + ⚠️), read-INDEX rationale specificity (maintenance signals / active works / experience traps / 信息盲区), write-operation scope completeness (includes 移动/归档/删除), spelling/grammar errors, (c) gap summary listing each dimension's pass/fail. |

**Output of Phase 0**: A Journal Global Snapshot document containing:
- Directory usage report (from Step 5)
- Topic summaries (from Step 2)
- Anomaly log (from Step 1)
- Dashboard signal data (from Step 6)
- Tag raw lists (from Step 7)
- Custom section audit (from Step 8)
- Staleness tags + extraction checklists (from Steps 3‑4)
- Convention status (from Step 9)
- Archive snapshot (from Step 10)
- Contract staleness report (from Step 11)

> ⚠️ **Phase 0 不产生决策。** 如果你发现自己在 Phase 0 中说"这个应该放到 X 目录"或"这个 tag 应该合并"，你正在跨入 Phase 1。停下——先把数据收集完。Phase 1 会基于完整数据做判断。

---

### Phase 1: Review → Design → Settle → Plan

> ⚠️ **进入 Phase 1 前**：重读 Phase 0 快照数据（目录统计、staleness 标记、tag 列表、convention 状态），
> 确认数据解读无误后再做决策。如果对某个标记有疑问，重新打开对应文件确认——不要依赖记忆或假设。

Phase 1 是一个完整的认知链：先理解现状、再设计方案、然后确认规则、最后制定执行计划。**不碰文件。**

三份规则文件平等并列——CLASSIFICATION.md、TAGS.md、CONVENTIONS.md 同为制度文件，不设先后依赖顺序。

#### P1-S1: 带着三规则审查现状

将 CLASSIFICATION.md、TAGS.md、CONVENTIONS.md 作为透镜，解读 Phase 0 快照。

**不决策**——只建立"当前规则视角下的全貌"。

对每份规则：
- **CLASSIFICATION.md**（存在时）：覆盖性（是否覆盖所有内容）、一致性（与实际使用是否一致）、正交性（是否有重叠）、健康度（空目录/拥挤目录）
- **TAGS.md**（存在时）：注册列表的完整度、使用模式、维度结构是否合理
- **CONVENTIONS.md**（存在时）：scope 是否仍然有效、是否有 stale 或冲突的 convention

**输出**：三规则现状笔记——各规则的覆盖情况和潜在问题清单。

> **格式审查**：除内容审查外，对每份存在的规则文件，加载对应的 skill 规范文件（`references/design-classification.md` / `references/design-tags.md` / `references/spec-conventions.md`），对照文件格式要求逐项检查。即使技能规范中格式约束不多，也必须重新阅读确认——避免跨版本格式漂移。发现格式不符 → 标记为 P1-S3 变更清单中的 UPDATE。


> **合约审查**：Phase 0 Step 11 的合约过期报告列出各合约与最新模板的差异。对每个差异按以下标准判断：
> +- 启动措辞强度不足（缺少「第一步」+ ⚠️ + 价值说明）→ 标记 P1-S3 变更清单 UPDATE
> +- 读 INDEX 理由不具体（仍用「获取全局背景知识」等泛泛表述）→ 标记 P1-S3 UPDATE
> +- 写操作范围不完整（举例缺移动/归档/删除）→ 标记 P1-S3 UPDATE
> +- 拼写或语法错误 → 标记 P1-S3 FIX
> +- 合约完全匹配最新模板 → 无操作，报告「合约已是最新」

> **Archive 审查**：Phase 0 Step 10 的 archive 快照列出所有已归档条目。对每个条目判断：
> - **恢复**（内容仍有活跃参考价值）→ 标记移回对应目录，注意同步更新其原始目录中的交叉引用
> - **保留**（仍在冷却期或仍有历史参考价值）→ 不动
> - **可硬删除**（非本轮 P2-S3 新移入、确认无用、无交叉引用）→ 标记
>
> **冷却保护**：标记为“可硬删除”的条目必须已存在于 archive/ 中超过当前维护周期（对照 Phase 0 Step 10 记录的“本轮新 archive 条目”列表，禁止将本轮新移入的条目标记为可硬删除）。


#### P1-S2: 设计目标组织方式

从"想要什么结构"出发。同时评估三个维度，不做先后假设：

- **目录结构**：当前分类规则是否支撑理想结构？需要新增/合并/拆分目录？
- **Pattern 选择**：是否需要一个特定项目/领域的次级 INDEX（Dashboard）？当前的 INDEX.md 组织是否满足信号需求？如果 INDEX.md 感觉不够用（信号不清晰、专项工作堆积、变更列表过长），审视当前结构——哪些板块的噪声值超过信号值。
- **标签体系**：当前的标签结构和注册列表是否覆盖了所有内容类别？维度分组是否仍然合适？
- **Convention 需求**：是否需要创建/更新/销毁某条 convention？

引用参考：分类审查四维框架见 `references/design-classification.md`。Dashboard 模式参考 `references/patterns/dashboard.md`。标签设计方法论见 `references/design-tags.md`。Convention 规范见 `references/spec-conventions.md`。

**输出**：理想组织方式设计方案。

#### P1-S3: 确认三规则变更

将设计方案落实到三规则的具体修改内容。

对每份规则，确定需要做什么（CREATE / UPDATE / DELETE）：
- **CLASSIFICATION.md**：规则变更内容
- **TAGS.md**：新 tag 注册 / 合并 / 移除；维度调整
- **CONVENTIONS.md**：新增 / 更新 / 销毁 convention 条目

Tag 决策中使用 Tag Worthiness Criteria：
| 判定 | 行动 |
|------|------|
| 值得保留 | 注册到 TAGS.md |
| 是已注册 tag 的同义词 | 合并——将所有出现替换为正式 tag |
| 不值得保留 | 从所有条目的 frontmatter 中移除 |
| 模糊但常用 | 保留但注册 |

**输出**：三规则变更清单（每项指定 CREATE / UPDATE / DELETE）。不碰文件。

#### P1-S4: 制定重组计划

将变更清单映射为完整的条目重组操作序列。

指定：
1. 规则文件修改顺序（P2-S1 顺序）
2. 条目重组顺序（按目录、按标签、按 convention）
3. 特殊处理（需要提取的内容、需要特别关注的文件）

**输出**：Phase 2 执行计划。

**End of Phase 1 — three sets of rules are now confirmed:**

| 规范 | 状态 |
|------|------|
| Classification rules (CLASSIFICATION.md) | ✅ 确认不变 / ✅ 已修订 |
| Tag registry (TAGS.md) | ✅ 确认 / ✅ 已维护 |
| Conventions (CONVENTIONS.md) | ✅ 确认不变 / ✅ 已修订 / ✅ 不涉及 |

如果三项都没有任何变更，**仍然可以进入 Phase 2**——Phase 2 不只是执行变更，它也处理条目级别的重组（按现有规则搬文件、归档、清理）。

---

### Phase 2: Execute — Apply the Confirmed Rules

> 先改三规则文件，再重组条目。规则就位后，所有操作基于新规则。

> 本阶段所有操作均为加法——新位置先就位，原位置后清理。
> 任何步骤中断只需继续执行，不会丢失数据。确认新文件正确后再清理旧位置。

| # | Step | Description |
|---|------|-------------|
| 1 | **Update rule files first** | 按 P1-S3 的变更清单修改/创建/销毁三规则文件。CLASSIFICATION.md、TAGS.md、CONVENTIONS.md 全部先就位。 |
| 2 | **Extract surviving content** | Using the extraction checklist from Phase 0 Step 4, pull valid information units from files to be archived and write them into the reorganized structure (new files or enrich existing ones). Source files remain in place during extraction — they are still readable. |
> **Archive protection rule**: Entries moved to archive/ in this step are NOT eligible for hard deletion in the current maintenance cycle. They must survive at least until the next full maintenance cycle before hard deletion is considered (Phase 1 archive review will mark candidates, Phase 2 Step 9 will execute).

| 3 | **Archive** | All `fully stale` + `partially stale` files → move to `archive/` (create this directory if it does not yet exist). Partially stale files go whole — their original stays intact as history. By this point, surviving content has already been extracted. |
| 4 | **Reorganize structure** | Apply the classification structure from the confirmed CLASSIFICATION.md. Move entries between directories, rename directories if needed. Update INDEX.md links to their new paths BEFORE physically moving the files — the target paths are already determined by the Phase 1 reorganization plan. |
| 5 | **Tag remediation** | Execute the tag decisions from Phase 1 P1-S3: (a) register new tags in TAGS.md; (b) merge synonyms — replace all occurrences with the canonical tag; (c) remove discarded tags from entry frontmatter. **After removal:** verify affected entries still have ≥1 tag, or follow the rules in TAGS.md. Report counts: registered X, merged Y, removed Z. |
| 6 | **Trim 最近变更** | Cut to last 7 entries. The purpose is recency signal — "what happened in the last few sessions?" — not a chronological log. Older entries are findable via file system. |
| 7 | **Collapse 专项工作** | Reduce to one line per domain. Encode current work scene in each line (not just "active"/"completed"). Completed milestones from domains with no active work → remove after 2‑session cooling period. Scene encoding format: `Domain — 📝 当前工作场景：简短描述 [→](link)`. 一行一域 + 场景编码——让下次 session 一眼看清各域状态. |
| 8 | **Split 经验摘要** | Tag each 经验摘要 entry as `enforcement` (reinforces a specific agent operating rule), `survival` (environment/tool trap not covered by persona/memory), or `axiom` (behavioral principle already in persona/memory). Remove axiom entries (de‑duplication: they are injected every turn already). Keep enforcement and survival entries. |
| 9 | **Execute archive cleanup** | Hard-delete only entries marked for hard deletion in Phase 1. Before deletion: (a) verify each matches the Phase 1 mark list exactly — no entry that was not explicitly marked, (b) confirm none were archived in the current cycle — cross-check against Phase 0 Step 10’s protected list. After deletion: report count of deleted entries and retained entries. |


> **"Extract first, archive later" logic**: Source files stay in place while extraction runs — no interruption‑safety checklist needed. After extraction is confirmed (new files written and verified), the archival move is safe. The original files enter `archive/` intact, preserving complete history alongside the extracted content.

> **Dashboard updates happen in Phase 2, not Phase 4.** File moves (Step 4) immediately invalidate all dashboard links pointing to moved files. Update INDEX.md links BEFORE moving files — otherwise the dashboard enters a broken‑link state between Phase 2 and Phase 4.

---

### Phase 3: Quality Check — Bidirectional Verification

双向检验：规则与条目互相校正。

**Step 1: Review process → micro‑adjust rules**

回顾 Phase 2 执行过程——是规则不合理导致执行困难，还是执行偏差？

- 目录归属是否有模糊边界 → CLASSIFICATION.md 是否需要微调？
- 标签分配是否不自然 → TAGS.md 维度是否需要调整？
- convention scope 是否覆盖不全或有冲突 → CONVENTIONS.md 是否需要修正？

如需调整，直接修改对应规则文件。规则文件始终反映"我实际希望条目遵循的规则"。

**Step 2: Verify entries against finalized rules**

以最终确认的三规则为基准验证：

| # | Dimension | Description |
|---|-----------|-------------|
| 1 | **Logical conflicts** | Contradictions between note contents. |
| 2 | **Content overlap** | Topic overlap or near‑duplication across notes. |
| 3 | **Broken links** | References pointing to archived content. Distinguish two cases: migrated to new location → fix the link; archived without extracting key points → decide whether to pull them back. Check any custom section tables first — they are often the most link‑dense parts of INDEX.md. |
| 4 | **Tag compliance** | After remediation, scan all entries: every tag must appear in `<journal-root>/TAGS.md`. Verify each entry follows the rules defined in TAGS.md. Flag any violators. |
| 5 | **Convention compliance** | Check that convention entries referenced in configs/dashboards are up-to-date with their CONVENTIONS.md definitions. No scope drift. |

---

### Phase 4: Finalize

| 1 | **重写 INDEX.md** | 加载 `references/spec-index.md`，按当前技能规范完全重写 INDEX.md。保留 Phase 2 已更新的内容（已修剪的最近变更、已折叠的专项工作、已去重的经验摘要、已修复的链接），但格式和结构严格遵循 spec。不增量修补——重写确保跨版本一致性。 |
| 2 | **Update Protocol Declaration signal line** | Rewrite the `维护信号` line in INDEX.md Protocol Declaration to reflect the current maintenance snapshot. Examples: `维护信号：经验摘要含 axiom(2) · 最近变更 9/7 · 维护备忘 12/10 · active_works/ 积灰`. Includes convention status if relevant. This makes maintenance signals visible at a glance in the next session startup without requiring a full dashboard scan. |
| 3 | **Record restructuring** | Append a restructuring record to `INDEX.md` 最近变更. Include: what phases ran, what rules changed (if any), count of files moved/tags fixed/types corrected, and any convention changes. |
| 4 | **Clear maintenance memo** | If `.maintenance-memo.md` exists and was read in Phase 0, clear its contents (or delete the file). All accumulated issues have been addressed through the full maintenance cycle — an empty or absent memo resets the accumulation counter for the next daily‑use cycle. |

---

## Pitfalls

- **Phase 0‑to‑Phase 1 boundary crossing**: The most common maintenance error is skipping straight from scanning to deciding — "I see a problem, let me fix it now." This skips the rule review step and leads to inconsistent decisions. Always complete Phase 0 fully (produce the snapshot document) before entering Phase 1.

- **Rule review without data**: Never start Phase 1 without a Phase 0 snapshot. The snapshot is the foundation — without it, Phase 1 decisions are based on memory and impression, not evidence.

- **Editing rules and entries at the same time**: Phase 2 is designed as "rules first, entries second." If you modify a rule file mid‑entry‑restructuring, you may need to backtrack. Complete P2-S1 fully before entering P2-S2.

- **Only one‑directional quality check**: Phase 3 is bidirectional. After adjusting entries, always return to the rules to confirm they still reflect reality. A rule that no entry follows is worse than no rule.

- **Custom section tables are link‑dense**: any custom tables added to INDEX.md (self-regulation rules, etc.) are the highest‑risk area for broken links after restructuring. Each table row may reference 2‑3 journal files. Check these first in Phase 3 Step 2.

- **Large‑file extraction fog**: Files >500 lines (e.g., 896‑line architecture dumps) make the "what to extract" decision hard. If no clear unique insight survives beyond what's already in other files, the correct decision is to not extract — the archive preserves the original for future reference.

- **Phantom dashboard signals**: `INDEX.md` 专项工作 lines with no journal file behind them (e.g., `竞品追踪 — 运行中` with no link, no entry anywhere). These survive unnoticed because they don't appear in file scans or link checks — they're text, not broken links. During Phase 0 Step 1, cross‑reference every untagged dashboard line against the file tree. A line without a `[→](...)` link that returns zero 搜索 hits is a phantom. Remove it in Phase 2.

- **Dashboard‑link staleness**: Phase 2 file moves immediately break dashboard links. Update INDEX.md links BEFORE moving files — not in Phase 4. The dashboard is the sole entry point for the next session; broken links mean the agent starts with invalid references.

- **Classification over‑revision**: A classification scheme that changes every maintenance pass is worse than a flawed but stable one. Phase 1 has a built‑in bias toward "confirm unchanged" — only revise when there is clear evidence of mismatch. If you are unsure, defer to the next maintenance cycle. The criteria are designed to be conservative.

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

Experience entries that are validated, generalized, reusable, and non‑project‑specific can become skills during maintenance. Manual, not automatic.
