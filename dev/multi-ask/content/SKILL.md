---
name: "multi-ask"
description: |
  Unhurried batch questioning: take the decisions that are waiting on the
  user, write each one up with the context it needs, put them into one
  questionnaire, and continue from the structured answers. 从容地问答：把一批待决
  问题连同足够完整的论述一次呈上，让用户按自己的节奏读完、答完，收回结构化答卷。

  Triggers: several decisions are waiting on the user and a conversation-by-
  conversation back-and-forth keeps losing the context — 攒起多个待决点、一次讲清楚
  再问、来回追问太碎、每个问题都要重讲一遍背景；or the user asks for it in
  those words — 「列个问卷 / 一起问 / 我一起答 / 写清楚再问 / 一次问完」；or
  answers are waiting to be read back — 收到答卷、把裁决连同论述放回上下文、拼装
  回读。Also "questionnaire for the user to fill in", "write it up and ask me".

  This skill asks the user — the adjudicator — for rulings. Not for
  questionnaires that gather knowledge or opinions from third parties on the
  user's behalf (surveys, polls, collecting feedback from other people).
  Not for a single question that belongs in the conversation.
license: "MIT"
metadata:
  version: "0.1.0"
  last_updated: "2026-11-07"
  author: "Cxalio"
---

# multi-ask

## 是什么

把一批待决问题写成**问卷**（markdown 文档：论述正文 + 若干问题块），用户在脚本打开的本地交互页上读、答，脚本产出一份**答卷**（JSON 纯数据），agent 读答卷继续推进。脚本、问卷、答卷与用户的浏览器在同一台机器上：交互页只在本机可访问。

问卷里的两份内容各管一件事：**论述**把作出裁决所需的背景写全——约束是什么、每条路的代价落在哪儿、为什么这件事得由用户定；**问题块**只问那一句要裁决什么。论述写足是这个技能的价值所在：用户读完一题就能答、也能反驳，不必回头追问背景。

裁决指用户就某个待决点给出的选择或判断。问卷只装用户裁决物：偏好、价值取舍、影响用户且不可逆的选择、只有用户知道的事实。agent 自己能裁定的不进问卷，能查证的先查证再决定是否进问卷；替用户去问第三方的调查不属于这个技能。

题量由待决点决定：两题可以成卷，十题也可以；只有一道题时直接在对话里问，别为它起问卷。

## 为什么

在对话里逐题追问，每答一句都要重新拼一次背景：用户得先想起上下文，才能判断你在问什么；你拿到一句回答，又得接着补下一句的上下文。问卷把完整论述与问题一起呈上，用户按自己的节奏读完再答，答完一次交回。省下的不是用户的思考，是反复对齐上下文的往返。

## 怎么做

按当前情形读参考文档；第一次用，顺着「分拣 → 格式 → 打磨 → 运行」读完：

- **先分拣：哪些问题该进卷** → [references/organizing-questions.md](references/organizing-questions.md)：什么算已定、每题写多少论述、依赖链怎么拆批、题与题怎么摆。
- **起草问卷、查格式** → [references/questionnaire-format.md](references/questionnaire-format.md)：围栏语法、题型、id 规则、渲染边界；照它写即可通过 `validate`。
- **打磨单道题** → [references/writing-questions.md](references/writing-questions.md)：论述与题面各管什么、判断题、选项集合、承重假设、选项写法。
- **运行脚本、收回与回读答卷** → [references/script-usage.md](references/script-usage.md)：运行前提、五步流程、三命令、答卷结构、未答与总评的读法。
- **要照着成品写** → [examples/release-plan.md](examples/release-plan.md)：一份格式齐全的问卷，示范版式，不必照搬。
