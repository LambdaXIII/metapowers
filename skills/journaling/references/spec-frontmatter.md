# Frontmatter Specification

> YAML frontmatter 的格式规范和字段说明。每个 journal 条目必须有 frontmatter，这是检索、组织和维护的基础。
>
> 使用场景：
> - 写新条目时参考必有字段和格式
> - 考虑添加自定义字段时查阅指导原则

---

## 1. YAML 语法规则

### 1.1 基本格式

- Frontmatter 必须放在文件最开头，以 `---` 开始，以 `---` 结束，各自单独成行
- 字段名和值之间用冒号加空格分隔：`字段名: 值`
- 字段名统一使用**英文小写 + kebab-case**

### 1.2 数据类型

| 类型 | 规范 | 示例 |
|------|------|------|
| 字符串 | 含空格或特殊字符时用英文双引号包裹 | `title: "My Entry"` |
| 数字 | 整数或小数，不加引号 | `rating: 8` |
| 布尔值 | 仅 `true` / `false`，全小写 | `completed: true` |
| 数组 | 每行一项，以 `- ` 开头 | `tags:\n  - lesson\n  - research` |
| 日期 | `YYYY-MM-DD` | `last_update: 2026-06-26` |

---

## 2. Required Fields

以下字段是所有条目**必须包含**的。即使暂时没有值或尚未填写，也应在 frontmatter 中保留字段名。

### `title`

| 属性 | 值 |
|------|---|
| 类型 | 字符串 |
| 作用 | 笔记的标题，是引用入口和检索线索 |
| 规范 | 简洁、描述性。能让未来的你仅凭标题判断是否打开 |

### `summary`

| 属性 | 值 |
|------|---|
| 类型 | 字符串 |
| 作用 | 一句话摘要。是**锚点**——决定是否打开、判断新内容是否属于本条目 |
| 规范 | 一句话（非段落）。应描述"这件事/经验/决策的核心是什么"，而非"我做了什么"。一个好的 summary 应该让半年后的你不需要打开就知道这条笔记是否和当前问题相关 |

### `tags`

| 属性 | 值 |
|------|---|
| 类型 | 数组[字符串] |
| 作用 | 检索入口。所有 tag 必须来自 `<journal-root>/TAGS.md` |
| 规范 | 遵循 TAGS.md 中的 Rules。如果 TAGS.md 未定义规则，至少选一个 tag。先注册后使用 |

### `last_update`

| 属性 | 值 |
|------|---|
| 类型 | 日期 |
| 作用 | 本条内容**最后一次实质性修改或确认有效**的日期。时效性锚点 |
| 规范 | `YYYY-MM-DD`。不限于文件修改日期——如果你今天重新读了一条旧笔记并确认它仍然有效，更新 `last_update` 到当天。这是该笔记是否仍然值得信任的信号 |

---

## 3. Recommended Optional Fields

以下字段不是必须的，但在特定场景下很有价值。详情请根据条目内容按需添加。

| 字段 | 类型 | 场景 | 说明 |
|------|------|------|------|
| `status` | 字符串 | `active_works/` 中的任务 | 标记条目生命周期状态。推荐值：`active`（进行中）、`completed`（已完成）、`superseded`（已被替代）、`abandoned`（已放弃）。也可由各 journal 在 TAGS.md 中自行定义规则，或不使用此字段 |
| `author` | 字符串 | 多 agent 共享场景 | 标识条目作者。通常从环境变量自动注入，默认 `"main"`。单 agent 场景不需要 |
| `date` | 日期 | 创建日期有独立意义时 | 如果创建日期与 `last_update` 不同并且有保留价值（如决策记录需要知道"这个决定是哪天做的"），用此字段记录初始创建日期 |

---

## 4. Custom Fields

当你需要 frontmatter 没有覆盖的元数据维度时，可以添加自定义字段。

### 4.1 什么时候添加

- **程序化查询**：你需要用结构化查询筛选、聚合、统计时（如按 `milestone:` 分组查看进度）
- **跨条目筛选**：你需要快速找出符合某个条件的条目集合时
- 能用 tag 表达 → 优先用 tag
- 能写在 body 里且自然语言搜索就能找到 → 优先写在 body 里
- 自定义字段是最后选择——它增加了 frontmatter 的维护成本

### 4.2 命名规范

- 与系统字段一致：`lowercase-kebab-case`
- 语义明确：另一个 agent 看到字段名能理解含义
- 避免缩写：`deadline` ✓，`dl` ✗

### 4.3 类型选择

| 场景 | 推荐类型 | 示例 |
|------|---------|------|
| 标记/分类 | tag（数组字符串） | 为什么不用 tag？ |
| 数值 | 数字 | `rating: 8.5` |
| 状态/开关 | 布尔 | `completed: true` |
| 时间点 | 日期 | `deadline: 2026-07-15` |
| 多值分类 | 数组 | `related:\n  - entry-a\n  - entry-b` |

### 4.4 一致性原则

- 同一自定义字段在同类条目中使用**相同的字段名和类型**
- 如果一个字段属于某类条目的标准维度，即使当前值为空也**保留字段名**（留空其值）
- 例如一条 `active_works/` 下的任务如果暂时没有截止日期，可以写 `deadline:`（留空）而不是不写这个字段——这样保持结构一致性

### 4.5 按目录扩展字段

不同目录的内容性质不同，可以按目录引入不同的自定义字段：

| 目录 | 可能需要的字段 |
|------|--------------|
| `experience/` | 通常不需要扩展字段——title + summary + tags + last_update 已足够 |
| `active_works/` | `status:`、`deadline:`、`blocked_by:`（数组）、`depends_on:`（数组） |
| `knowledge/` | `source:`（信息来源 URL）、`author:`（原作者） |

这不是硬性规定——根据实际需求灵活添加。如果你发现某个目录下的条目频繁使用同一组自定义字段，可以考虑在 TAGS.md 或 CLASSIFICATION.md 中记录该约定。

---

## 5. Field Ordering

字段按照以下顺序排列，便于阅读和维护：

```
title
summary
tags
last_update
[status]          ← 可选，如需要
[author]          ← 可选，如需要
[date]            ← 可选，如需要
[custom fields]   ← 按逻辑分组排列
```

---

## 6. Examples

### 基本条目（experience/）

```yaml
---
title: "WSL 下 vite 需 --host 0.0.0.0 才能局域网访问"
summary: "WSL mirror 网络模式下，vite 默认绑定 127.0.0.1，需 --host 0.0.0.0 才能从局域网访问"
tags:
  - lesson
  - environment
last_update: 2026-06-26
---
```

### 活跃任务（active_works/）

```yaml
---
title: "Journaling skill v4.2 — 全量一致性检查"
summary: "tags+分类规则+frontmatter 确定后，对所有文件做一次交叉检查，清理旧引用"
tags:
  - documentation
  - plan
last_update: 2026-06-26
status: active
deadline: 2026-06-28
---
```

### 带创建日期的知识条目（knowledge/）

```yaml
---
title: "个人笔记库分类方法论调研"
summary: "对 PARA、Zettelkasten、Johnny Decimal、MOC/LYT 等系统的实际用户实践做了系统性调研，提取了 6 个通用抽象和 5 个失败模式"
tags:
  - research
  - knowledge
last_update: 2026-06-26
date: 2026-06-25
source: "web-deep-research agent report"
---
```

---

## 7. Common Errors

| 错误 | 正确 |
|------|------|
| `title:My Entry`（冒号后无空格） | `title: My Entry` |
| `tags: lesson, research`（内联数组） | `tags:\n  - lesson\n  - research` |
| `completed: True`（布尔值大写） | `completed: true` |
| `last_update: 2026.06.26`（日期格式错误） | `last_update: 2026-06-26` |
| 缺少 `---` 闭合或用 `~~~` 代替 | 必须用 `---` 包裹 |
| 字段名用中文或混用大小写 | 统一英文小写 kebab-case |
