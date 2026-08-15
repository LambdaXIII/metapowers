# Issue tracker: GitHub

本仓库的 issue 存于 GitHub Issues（`LambdaXIII/metapowers`），用 `gh` CLI 操作。

## 用途（双通道）

**① 内部：使用/审查技能时发现的问题，当场提交——问题描述与定位一步完成，替代另行记观察笔记。**

技能源码在本仓库（`dev/<skill>/`）。发现问题时当下的上下文最完整，直接提 issue 把描述和定位写全；维护时直接处理，不再提炼观察记录、重新解读。

**② 外部：技能用户的反馈也走本渠道。** 外部反馈未必符合内部格式，由维护者经 triage 整理（见 `triage-labels.md`），信息不足时标 `needs-info` 并评论追问。

## 提交约定（内部提交时）

- **标题**：`<技能名>: <问题一句话>`（如 `rehearsal: 触发条件节对「通读」的边界描述有歧义`）
- **正文**：
  - 问题描述（现象/歧义/改进点）
  - 定位：`dev/<skill>/content/<路径>` 具体文件与节
  - 复现上下文（可选）：触发场景、当时的操作
  - 期望行为
- **标签**：内部提交默认 `needs-triage`（见 `triage-labels.md`）；外部反馈由维护者 triage 时打

## 处理约定

- 维护时 `gh issue list` 拉取 open issues，逐条 triage、处理
- 修复后决策落 `dev/<skill>/SKILL-DESIGN.md` / `CHANGELOG.md`（AGENTS.md §2.2/§2.5/§2.4），再关闭 issue
- issue 是问题追踪，不是设计决策载体——决策正文仍以 SKILL-DESIGN/CHANGELOG 为准

## 操作（gh CLI）

- **建**：`gh issue create --title "..." --body "..."`（多行正文用 heredoc）
- **列**：`gh issue list --state open`（可按标签过滤：`--label needs-triage`）
- **读**：`gh issue view <number> --comments`
- **评论**：`gh issue comment <number> --body "..."`
- **打/去标签**：`gh issue edit <number> --add-label "..."` / `--remove-label "..."`
- **关闭**：`gh issue close <number> --comment "..."`

仓库由 `git remote -v` 推断，`gh` 在 clone 内自动使用当前仓库。

## PRs as a triage surface

**PRs as a request surface: no.**（若将来把外部 PR 当 feature request，改为 `yes`；`/triage` 读取此标记。）

## 与 .scratch 的边界

`.scratch/` 仍是临时草稿区（gitignored）——实施期 SPEC/笔记放那里；**问题追踪一律走 issue，不落 .scratch、不另记观察笔记**。
