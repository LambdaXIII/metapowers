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
  last_updated: "2026-09-06"
  author: "LambdaXIII"
  license: "MIT"
---

# Skill Master

## 使用方式

- 判断当前属于哪类工作：设计 / 修改 / 审查。技能行为与预期不符的排查不是
  独立工作，是审查的症状排查形态，定位后的修复归修改。
- 按路由表读对应论述。各册独立自洽，只读所需那一本。
- 写、改、判定任何技能文字之前，先读
  [writing-craft.md](references/documents/writing-craft.md)——句子级与结构
  级编写手艺，三类工作共用。
- 打包规范与披露设计按路由表读 references/general/ 两册。

## 路由表

| 读什么 | 是什么 | 何时读 |
|---|---|---|
| [skill-design.md](references/skill-design.md) | 设计工作论述：锚定 → 组织 → 编写 → 验证 | 从零设计新技能，或判断一套做法值不值得做成技能 |
| [skill-modify.md](references/skill-modify.md) | 修改工作论述：先理解现状，再涟漪式改内容 | 对已有技能做变更：修内容、增删、重构、修剪 |
| [skill-review.md](references/skill-review.md) | 审查工作论述：全量评判与症状排查两种输入形态 | 评判已有技能的质量；行为与预期不符时排查根因 |
| [writing-craft.md](references/documents/writing-craft.md) | 编写手艺（共享）：句子级与结构级要点 | 写、改、判定任何技能文字之前 |
| [standards.md](references/general/standards.md) | 打包规范册：目录、frontmatter、渐进披露、校验 | 开始组织文件结构、核对合规时 |
| [disclosure.md](references/general/disclosure.md) | 披露设计论述：description、命名、触发面 | 写 description、定技能名、打磨触发面时 |

## 触发条件

**触发**（任一即触发，括号内是路由去向）：

- 从零设计一个新技能，或把一套做法/知识做成技能（→ 设计工作）
- 修改、改进、重构、修剪一个已有技能（→ 修改工作）
- 技能行为与预期不符——不触发、跑偏、产出不对——要查清原因（→ 审查
  工作的症状排查形态）
- 评判一个已有技能的质量（→ 审查工作）
- agent 完成工作后自问「这一步该怎么设计 / 这个技能为什么不对劲 /
  这套内容写得怎么样」时，同样适用

**不触发**：

- 把技能内容转写成给人类阅读的说明文——阐述类职责
- 运行时验证一个技能能否跑通——测试类职责；本技能的审查是静态的文档
  质量审查，不加载运行技能

## 目录树

```
skill-master/
├── SKILL.md                          # 入口：工作路由
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
    │   ├── script-design.md          # 脚本取舍与设计
    │   └── scripting-craft.md        # 脚本编写手艺
    └── general/                      # 跨类通用
        ├── standards.md              # 打包规范册
        └── disclosure.md             # 披露设计论述
```
