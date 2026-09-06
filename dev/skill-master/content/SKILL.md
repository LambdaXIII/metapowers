---
name: skill-master
description: |
  Skill master (技能设计 / 技能排查 / 技能修改 / 技能审查): design,
  troubleshoot, modify, and review agent skills — the working lifecycle of
  skill development.

  Triggers: 「设计技能 / 做个技能 / 新建技能 / 改进技能 / 修一个技能 /
  技能行为不对劲 / 审查这个技能」; or when an agent needs to turn methodology
  knowledge into a runnable skill, find out why one misbehaves, or judge the
  quality of one.

  Does NOT trigger: expounding an existing skill for humans to read
  (exposition), or runtime behavior testing of a finished skill (quick-test).
metadata:
  version: "0.1.0"
  last_updated: "2026-09-05"
  author: "LambdaXIII"
  license: "MIT"
---

# Skill Master

> 技能开发生命周期的元技能：设计、修改、审查三种工作共用一本入口。
> 加载即得两样东西：前提《什么是一个好的技能》，以及当前工作该读哪本
> 论述的路由。行为与预期不符的排查不是独立工作——它是审查工作的
> 症状排查形态。

## 前提《什么是一个好的技能》

技能是实践的沉淀：先有被走通、被检验的做法，技能把它整理成文档，搬运给
任何零上下文的 agent。技能自身不执行任何操作，运行它的是加载它的 agent
——正文的每一句都要服务「读者拿它去用」这件事。

好技能的内容用四把尺子量：**有用**（每句都服务于读者要做的事）、**全面**
（读者需要的判据与机制不缺席）、**准确**（断言配机制或判据，不悬空）、
**清晰**（一次读懂，不必回头猜）。四标准是对每一段正文的编写要求；目录、
路由、分层这些框架只服务检索与维护——让 agent「做好」的是内容本身，
框架只是让内容找得到、读得进。

好技能有四个可检查的特征，成文后逐条对：

- **定位三问钉死**：提供什么、指导什么、不管什么，三问都答得清——答不
  出「不管什么」的边界必然过宽，锚不住边界就收敛不了内容；
- **一次读懂**：零上下文读者读一遍就能上手，不需要回到原对话里补上下文；
- **无 no-op 句**：逐句问「删了它行为会变吗」，删了不变的是废话；
- **触发面准**：该命中时命中，不与相邻技能互相遮蔽（触发判定见「触发
  条件」；设计方法见 references/general/disclosure.md）。

各工作论述展开的判据这里不重复；本节是它们共享的底座。

## 使用方式

本技能按「当前是什么工作」路由，不按用户怎么措辞路由：

1. 判断现在做的是三类工作（设计 / 修改 / 审查）中的哪一类——拿不准先
   对照「触发条件」；
2. 读路由表中对应的一本工作论述——每本独立自洽，只读所需那一本，不必
   串读；
3. 写或改任何技能内容之前，先读 references/documents/writing-craft.md
   （句子级与结构级编写手艺，三类工作共用）；
4. 涉及打包规范、披露设计时，按路由表读 references/general/ 的两册。

行为与预期不符的处理不另开一路：先走审查工作的症状排查形态，定位到具体
文字，修复再转修改工作——行为不对是写得不对的表现，根因在文档里。

## 路由表

| 读什么 | 是什么 | 何时读 |
|---|---|---|
| [skill-design.md](references/skill-design.md) | 设计工作论述：锚定 → 组织 → 编写 → 验证 | 从零设计新技能，或判断一套做法值不值得做成技能 |
| [skill-modify.md](references/skill-modify.md) | 修改工作论述：先理解现状，再涟漪式改内容 | 对已有技能做变更：修内容、增删、重构、修剪 |
| [skill-review.md](references/skill-review.md) | 审查工作论述：全量评判与症状排查两种输入形态 | 评判已有技能的质量；技能行为与预期不符时排查根因 |
| [writing-craft.md](references/documents/writing-craft.md) | 编写手艺（共享）：句子级与结构级要点 | 写、改、判定任何技能文字之前 |
| [standards.md](references/general/standards.md) | 开放标准规范册：目录、frontmatter、渐进披露、校验 | 开始组织一个技能的文件结构、核对合规时 |
| [disclosure.md](references/general/disclosure.md) | 披露设计论述：description、命名、触发面 | 写 description、定技能名、打磨触发面时 |

## 触发条件

**触发**（任一即触发，括号内是路由去向）：

- 从零设计一个新技能，或把一套做法/知识做成技能（→ 设计工作）
- 修改、改进、重构、修剪一个已有技能（→ 修改工作）
- 技能行为与预期不符——不触发、跑偏、产出不对——要查清原因（→ 审查
  工作的症状排查形态：静态排查问题出在技能文档的哪处，不加载运行技能）
- 评判一个已有技能的质量（→ 审查工作）
- agent 完成工作后自问「这一步该怎么设计 / 这个技能为什么不对劲 /
  这套内容写得怎么样」时，本技能同样适用

**不触发**：

- 把技能内容转写成给人类阅读的说明文——阐述类职责；
- 运行时验证一个技能能否跑通——测试类职责。本技能的审查是静态的文档
  质量审查，不加载运行技能。

## 目录树

```
skill-master/
├── SKILL.md                          # 入口：前提《什么是一个好的技能》+ 路由
└── references/
    ├── skill-design.md               # 设计工作论述
    ├── skill-modify.md               # 修改工作论述
    ├── skill-review.md               # 审查工作论述（含症状排查）
    ├── documents/                    # 文本类编写方法
    │   ├── essay-writing.md          # 论述型文档编写
    │   ├── workflow-writing.md       # 工作流型文档编写
    │   ├── template-writing.md       # 模板编写
    │   └── writing-craft.md          # 编写手艺（共享层）
    ├── scripts/                      # 脚本类
    │   ├── script-design.md          # 脚本设计论述
    │   └── scripting-craft.md        # 脚本手艺
    └── general/                      # 跨类通用
        ├── standards.md              # 开放标准规范册
        └── disclosure.md             # 披露设计论述
```
