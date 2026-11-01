---
name: "multi-ask"
description: |
  Batch adjudication: assemble a batch of already-formed open decisions into
  one questionnaire, ask the user once, and continue from the structured
  answers. 批量向用户征集裁决：把一批待决问题连同论述一次问完，收回结构化答卷。

  Triggers: the agent has accumulated several open decisions and needs the
  user's rulings — 攒起多个待决问题、一次性征求意见、一个个问太碎、多问题往返；
  or the user explicitly asks for batch questioning — 「批量问 / 问卷 / 一次问完 /
  一起问 / 列个问题给我 / 我一起答」。Also "questionnaire for the user to fill in",
  "ask me several things at once", "batch questions".

  This skill asks the user — the adjudicator — for rulings. Not for
  questionnaires that gather knowledge or opinions from third parties on the
  user's behalf (surveys, polls, collecting feedback from other people).
  Not for a single question that belongs in the conversation.
metadata:
  version: "0.1.0"
  last_updated: "2026-11-01"
  author: "Cxalio"
---

# multi-ask

## 这个技能做什么

把一批待决问题组装成**问卷**（markdown 文档：任意论述正文 + 若干问题块），用户在脚本打开的本地交互页上一次性作答，脚本产出一份**答卷**（JSON 纯数据），agent 读答卷继续推进。逐题往返的代价是节奏被打断、每题都缺少完整论述；问卷把论述与问题一次呈上，把反馈一次收回。

裁决指用户就某个待决点给出的选择或判断。问卷只装用户裁决物：偏好、价值取舍、影响用户且不可逆的选择、只有用户知道的事实。agent 自己能裁定的不进问卷，能查证的先查证再决定是否进问卷。

## 全流程

1. **起草问卷**：写一个 markdown 文件。决策所需的背景写在块外正文，每个待决问题写成一个 `qa` 问题块。
2. **校验**：`python scripts/multi_ask.py validate <问卷.md>`。有错误时按每行的修复指引逐条改，直到输出 `OK: <n> 题`。
3. **收卷**：`python scripts/multi_ask.py show <问卷.md>`。该命令在前台阻塞，直到用户提交或按 Ctrl+C；提交后打印答卷文件路径。
4. **读答卷**：读该路径下的 JSON，按 `id` 对照问卷中的问题块，取出 `selected` 与 `text`。
5. **回读**（可选）：`python scripts/multi_ask.py assemble <答卷.json>` 输出问卷全文、问题块位置替换为作答结果，用于把用户裁决连同原论述一起放回上下文。

脚本为单文件，只依赖 Python 3 标准库，无需安装任何包；下文命令中的 `python` 在宿主上不可用时改用 `python3`。

## 问卷格式

问卷是普通 markdown：标题、段落、列表、链接、引用、fenced code block 均可自由使用。块外正文即题面论述；**问题块内只放结构数据，不放题面文本**——题面写在问题块上方。

问题块是语言标记为 `qa` 的 fenced code block：

````markdown
选项命名用哪种？

```qa
id: answer-naming
type: radio
options:
  - seq — 按序号递增命名
  - time — 按提交时间戳命名
```
````

块体内每行一个 `key: value`，只接受三个字段：

| 字段 | 必需 | 取值 |
|---|---|---|
| `id` | 是 | 问题块标识，全卷唯一，不含空格 |
| `type` | 是 | `radio`（单选）、`checkbox`（多选）、`yes-no`（判断） |
| `options` | 否 | 选项列表。`radio`/`checkbox` 缺省即开放题；`yes-no` 缺省用默认标签「是/否」 |

选项行写在 `options:` 之下，格式为 `- <选项id> — <选项文本>`：连字符、空格、选项 id、空格、长破折号 `—`、空格、选项文本。选项 id 在该问题块内唯一、不含空格；选项文本非空，可含中文标点、空格与长句。

id 的两级作用域：问题块 `id` 在整个问卷内唯一；选项 `id` 只在所属问题块内唯一，不同问题块可以复用同一选项 id。命名不设模式约束。id 仅供脚本配对答卷使用，不会显示在交互页或拼装答卷中。

### 题型

| `type` | 提交约束 | 答卷记录 |
|---|---|---|
| `radio` | 至多选 1 项 | 选项 id 数组，0 或 1 个 |
| `checkbox` | 任意多项 | 选项 id 数组 |
| `yes-no` | 恰选 1 项 | `["yes"]` 或 `["no"]` |
| 开放题 | 无选项 | 空数组 |

- `radio` / `checkbox` 不给 `options` 即**开放题**：没有选项，只收自由输入。
- `yes-no` 不给 `options` 时使用默认标签「是/否」；给出 `options` 时必须恰好是 `yes` 与 `no` 各一次，文本可覆盖（如「同意/反对」）。交互页恒为单选，答卷恒记 `yes` / `no`。

### 自由输入与总评

每题恒定附带一个自由输入框，整卷末尾恒定附带一个总评框。这两者由交互页提供，问卷里不声明、不占块结构。用户可以不选任何选项只写自由输入，也可以整题跳过（答卷该条为空数组与空串）。

## 命令

### `validate`

```
python scripts/multi_ask.py validate <问卷.md>
```

只校验，不打开交互页。

- 通过：stdout 输出 `OK: <n> 题`，退出码 0。
- 不通过：不开交互页，一次列完全部错误，退出码 1。每条形如 `<问卷文件>:<行号>: <问题描述> → <修复指引>`，修复指引说明怎么改。

校验覆盖面：字段仅 `id`/`type`/`options`；`id` 存在、非空、不含空格、全卷唯一；`type` 属于三种题型；选项行格式；选项 id 非空、不含空格、块内唯一；选项文本非空；`yes-no` 的 `options` 恰为 `yes` 与 `no` 各一次。

### `show`

```
python scripts/multi_ask.py show <问卷.md>
```

1. 先校验；不通过即终止，退出码 1。
2. 在 `127.0.0.1` 的随机端口起本地服务并打开浏览器展示交互页；浏览器打开失败时服务继续运行，并打印 URL 供手动打开。
3. 阻塞等待提交。用户提交后写答卷文件（位置与命名见下节），显示提交成功页，打印答卷文件路径，退出码 0。
4. 等待期间被 Ctrl+C 中断：不写答卷文件，退出码 130；需要重新运行 `show`。

交互页将问卷正文按 markdown 渲染：标题、段落、无序/有序列表、粗体、斜体、行内代码、链接、引用、分隔线、fenced code block 正常排版。表格与 mermaid 等其余结构降级为预格式化文本，不阻塞作答——不要用表格承载唯一必须逐项对照的信息。

### `assemble`

```
python scripts/multi_ask.py assemble <答卷.json>
```

按答卷的 `questionnaire` 字段在答卷同目录找到问卷，把每个问题块替换为作答结果，整份文档输出到 stdout，退出码 0。答卷或问卷缺失、答卷引用的问题块 id 或选项 id 在问卷中不存在时，按 `validate` 的同一错误行格式报错并给出修复指引，退出码 1。

## 答卷

答卷文件命名为 `<问卷名去扩展名>.answers.<NNN>.json`，与问卷同目录；`NNN` 为三位序号，从 `001` 起，取同目录同族现有最大序号 +1。同一份问卷可回收多份答卷，文件只增不改。

```json
{
  "questionnaire": "release-plan.md",
  "answers": [
    { "id": "naming", "selected": ["seq"], "text": "并发提交多再换时间戳。" },
    { "id": "scope", "selected": ["core", "docs"], "text": "" }
  ],
  "global_comment": "结构清楚。"
}
```

- `questionnaire`：问卷文件名，不含目录。
- `answers`：每个问题块一条，顺序与问卷一致。`id` 为问题块 id；`selected` 为选项 id 数组；`text` 为自由输入，可为空串。答卷不回显题干，也不含选项文本——定位题目看问卷。
- `global_comment`：总评文本，可为空串。

## 拼装答卷

问卷正文原样保留，每个问题块替换为一个引用块（不显示问题块 id）：

```markdown
> 选：按序号递增命名
> 补充：并发提交多再换时间戳。
```

- 有选择：`选：<选项文本>`，多选以 `；` 连接；`yes-no` 记「是」或「否」，该题覆盖了选项文本时记所覆盖的文本。
- 有自由输入：另起一行 `补充：<文本>`。
- 整题未答：`> 未答`。
- 开放题有输入：`> 答：<文本>`。
- 有总评：文末追加 `---` 分隔线与 `**总评**` 段落。

## 出题纪律

- **依赖链问题不进同一批。** 某个问题的答案会改变后续问题的题目本身时，后续问题等前一题收回答卷后再出。
- **上下文压缩到决策相关。** 每题只保留作出该裁决所需的论述；需要大段原文才能读懂的题，先把原文消化成结论与依据再写题。
- **承重假设显式化。** 问卷依赖的、用户尚未表态的前提写进题面论述，让用户能推翻前提，而不只能在给出的选项里挑。
- **讨论文本问卷化。** 已确认的结论写进论述或不再重问；仍存分歧的待决点逐题立起，一项一题。
- **判断题的题面须为完整命题。** `yes-no` 题的论述必须是一句可判定真假的陈述，不能是名词短语、半句话或两个待选方向。
- **单选项问题不单独成题。** 只有一个候选答案的问题改写成判断题，或补齐备选做成多选题。
