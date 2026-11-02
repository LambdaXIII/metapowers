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

1. **起草问卷**：写一个 markdown 文件。决策所需的背景与章节写在块外正文，每个待决问题写成一个围栏问题块，题面放在块内首行。
2. **校验**：`python scripts/multi_ask.py validate <问卷.md>`。有错误时按每行的修复指引逐条改，直到输出 `OK: <n> 题`。
3. **收卷**：`python scripts/multi_ask.py show <问卷.md>`。该命令在前台阻塞，直到用户提交或按 Ctrl+C；提交后打印答卷文件路径。
4. **读答卷**：读该路径下的 JSON，按 `block` 对照问卷中的问题块，取出 `selected` 与 `free`。
5. **回读**（可选）：`python scripts/multi_ask.py assemble <答卷.json>` 输出问卷全文、问题块位置替换为作答结果，用于把用户裁决连同原论述一起放回上下文。

脚本为单文件，只依赖 Python 3 标准库，无需安装任何包；下文命令中的 `python` 在宿主上不可用时改用 `python3`。

## 问卷格式

问卷是普通 markdown：标题、段落、列表、链接、引用、表格、fenced code block 均可自由使用。问题块嵌在论述之间；**题面写在块内首行，块外只写背景与论证**，不要在块外重复题面。问题块与题面不承担文档结构，不能充当标题：需要章节时，在正文中用真正的标题（如 `##`）建立章节。

问题块是围栏语言标明题型的 fenced code block：`single-choice`（单选）、`multi-choice`（多选）、`yes-or-no`（判断）。`multiple-choice` 是 `multi-choice` 的兼容别名，写 `multi-choice` 即可。完整示例见 `examples/skill-design-discussion.md`（章节与问题交错、同章节多题、单选/多选/判断/开放题与推荐标记）。

````markdown
按序号命名还是按时间戳命名？

```single-choice
<answer-naming> 答卷文件怎么命名？
- [ ] <seq> 按序号递增命名，目录列表即索引。
- [x] <time> 按提交时间戳命名，天然防并发。
```
````

块内只有两层：

1. **首行**：`<块 id> 题面`。尖括号内是块 id，其后是问题文本。
2. **选项行**：一行一个，写成 `- [ ] <选项 id> 选项文本`。行首方括号内写 `x` 即 `- [x] <选项 id> 选项文本`，标记该选项为推荐。

题面可续写在后续行，直到第一个选项行；选项文本也可以续写在后续行。题面按 markdown 行内语法渲染，连续普通行合并为一段；题面不承担文档结构，块内不要写标题、列表或分隔线——论述放在块外，题面保持一句话到几句话。id 写在尖括号内，非空、不含空格。

零选项的问题块即**开放题**（只有自由输入），只有 `single-choice` 与 `multi-choice` 允许零选项。选择题只写一个选项则校验不通过：把题面改写成完整命题、围栏换成 `yes-or-no`，或与同类问题合并为一道 `multi-choice`。

想推荐某个选项时把 `[ ]` 写成 `[x]`。推荐只是建议标记，**不等于预先选中**：交互页不为它预勾选，用户完全自由作答；推荐信息不写入答卷，也不出现在拼装结果里。同一问题块可标记多个推荐选项，也可以不标记。

id 的两级作用域：块 id 在整个问卷内唯一；选项 id 只在所属问题块内唯一，不同问题块可以复用同一选项 id。命名不设模式约束。id 仅供脚本配对答卷使用，不会显示在交互页、提交完成页或拼装结果中。

### 题型

| 围栏语言 | 提交约束 | 答卷记录 |
|---|---|---|
| `single-choice` | 至多选 1 项 | 选项 id 数组，0 或 1 个 |
| `multi-choice` | 任意多项 | 选项 id 数组 |
| `yes-or-no` | 恰选 1 项 | `["yes"]` 或 `["no"]` |
| 开放题（单/多选零选项） | 无选项 | 空数组 |

`yes-or-no` 不写选项时，交互页给出默认标签「同意 / 驳回」；写了选项时只接受 `<yes>` 与 `<no>` 两个标签，选项文本替换默认标签（如 `- [ ] <yes> 采纳`），顺序随意、也可以只给一个。交互页恒为单选，答卷恒记 `yes` / `no`。

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

校验覆盖面：全卷至少一个白名单问题块；块首行是 `<块 id> 题面`；题面非空；选项行格式合法；选项 id 块内唯一；选项文本非空；`single-choice` / `multi-choice` 不得只有一个选项；`yes-or-no` 的选项标签只能是 `yes` / `no`；块 id 全卷唯一；围栏闭合。id 含空格会落在首行或选项行的格式错误上，改用不含空格的 id 即可。

### `show`

```
python scripts/multi_ask.py show <问卷.md>
```

1. 先校验；不通过即终止，退出码 1。
2. 在 `127.0.0.1` 的随机端口起本地服务并打开浏览器展示交互页；浏览器打开失败时服务继续运行，并打印 URL 供手动打开。
3. 阻塞等待提交。用户提交后写答卷文件（位置与命名见下节），显示提交成功页，打印答卷文件路径，退出码 0。
4. 等待期间被 Ctrl+C 中断：不写答卷文件，退出码 130；需要重新运行 `show`。

交互页把每个问题块渲染为「题面 + 选项控件 + 自由输入框」：`single-choice` 与 `yes-or-no` 用单选按钮，`multi-choice` 用复选框，开放题只有自由输入框，推荐选项以彩色文字标出但不预选。

问卷正文按 markdown 渲染：标题、段落、无序/有序列表、粗体、斜体、行内代码、链接、引用、分隔线、fenced code block 正常排版。`mermaid` fenced 块渲染为图（浏览器需能访问 CDN 加载渲染器），离线或加载失败时降级为源码文本；表格降级为预格式化文本，不阻塞作答——不要用表格承载唯一必须逐项对照的信息。

### `assemble`

```
python scripts/multi_ask.py assemble <答卷.json>
```

按答卷的 `questionnaire` 记录的问卷路径找到问卷（找不到时退回答卷同目录的同名文件），把每个问题块替换为作答结果，整份文档输出到 stdout，退出码 0。答卷或问卷缺失、JSON 非法、答卷引用的问题块 id 或选项 id 在问卷中不存在时，按 `validate` 的同一错误行格式报错并给出修复指引，退出码 1。

## 答卷

答卷文件命名为 `<问卷名去扩展名>.answers.<NNN>.json`，与问卷同目录；`NNN` 为三位序号，从 `001` 起，取同目录同族现有最大序号 +1。同一份问卷可回收多份答卷，文件只增不改。

```json
{
  "questionnaire": "/home/user/notes/release-plan.md",
  "answers": [
    { "block": "naming", "selected": ["seq"], "free": "并发提交多再换时间戳。" },
    { "block": "scope", "selected": ["core", "docs"], "free": "" }
  ],
  "global_comment": "结构清楚。"
}
```

- `questionnaire`：问卷路径。`show` 记录问卷的绝对路径；`assemble` 按该路径找问卷，找不到时退回答卷同目录的同名文件。
- `answers`：每个问题块一条，顺序与问卷一致。`block` 为问题块 id；`selected` 为选项 id 数组；`free` 为自由输入，可为空串。答卷不回显题干，也不含选项文本——定位题目看问卷。
- `global_comment`：总评文本，可为空串。

## 拼装答卷

问卷正文原样保留，每个问题块替换为「题面 + 引用块作答」（不显示块 id）：

```markdown
按序号命名还是按时间戳命名？

> 选：按序号递增命名
> 补充：并发提交多再换时间戳。
```

- 有选择：`选：<选项文本>`，多选以 `；` 连接；`yes-or-no` 显示该题实际标签，未覆盖时即「同意」或「驳回」。
- 有选择且有自由输入：另起一行 `补充：<文本>`。
- 无选择、只写了自由输入：`> 答：<文本>`。
- 整题未答，或答卷缺该块记录：`> 未答`。
- 有总评：文末追加 `---` 分隔线与 `**总评**` 段落。

## 出题纪律

- **依赖链问题不进同一批。** 某个问题的答案会改变后续问题的题目本身时，后续问题等前一题收回答卷后再出。
- **上下文压缩到决策相关。** 每题只保留作出该裁决所需的论述；需要大段原文才能读懂的题，先把原文消化成结论与依据再写题。
- **承重假设显式化。** 问卷依赖的、用户尚未表态的前提写进块外论述或题面，让用户能推翻前提，而不只能在给出的选项里挑。
- **讨论文本问卷化。** 已确认的结论写进论述或不再重问；仍存分歧的待决点逐题立起，一项一题。
- **判断题的题面须为完整命题。** `yes-or-no` 的题面必须是一句可判定真假的陈述，不能是名词短语、半句话或两个待选方向。
- **单选项问题不单独成题。** 只有一个候选答案的问题改写成 `yes-or-no` 判断题，或补齐备选做成 `multi-choice` 多选题。
