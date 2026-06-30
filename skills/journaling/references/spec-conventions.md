# Conventions Specification

> 描述 CONVENTIONS.md 的设计原则和操作建议。CONVENTIONS.md 是 journal root 下的可选文件，
> 记录 journal 中已实例化的设计模式（如 dashboard）及其自维护规则。
> 读取笔记时不加载 CONVENTIONS.md。写入和导入时与个性化规则文件一起前置加载，维护时审查每条 convention。

---

## 核心原则

### 1. 不重复

convention 不应包含 journaling 技能已有的规范。若技能规范已经定义了某行为的默认规则，convention 不应重复它——只记录与默认行为不同或额外的事情。

### 2. 允许偏离，需说明理由

convention 可以与 journaling 技能定义的默认行为不同。惯例（convention）存在即意味着"这里需要特殊处理"。
偏离时需在条目中明确说明：
- 偏离了什么默认行为
- 为什么需要偏离
- 预期收益

目的是确保维护时能判断这个偏离是否仍然值得——不是禁止偏离，是要求偏离有理有据。

### 3. 参考 spec-note 风格

CONVENTIONS.md 中每条条目的写法参考 `references/spec-note.md`：
- summary 定义 scope boundary——明确本条 convention 作用于什么项目/领域
- body 写 reasoning 而非 checklist——记录"为什么这样设计"的决策链
- `last_update` 跟踪时效——每次审查后更新

---

## 文件格式

CONVENTIONS.md 是 Markdown 文件，内容自由组织。推荐包含以下字段：

| 字段 | 说明 |
|------|------|
| **Pattern** | 所采用的设计模式名称（如 `dashboard`） |
| **Scope** | 作用于哪个项目/领域 |
| **File** | 实例文件位置（如 `active_works/Scriptum/dashboard.md`） |
| **Write Awareness** | 写入此 scope 时需要的额外操作 |
| **Self-Check** | 维护审查时的自检判据 |
| **Created** | 创建日期 |

## 与各协议的关系

| 协议 | 如何涉及 |
|------|---------|
| protocal-write.md | 与个性化规则文件一起前置加载。命中 scope → 执行 convention 定义的额外操作 |
| protocal-import.md | 与个性化规则文件一起前置加载。命中 scope → 执行 convention 定义的额外操作 |
| protocal-maintenance.md | P1-S1/P1-S3 审查所有 convention 条目。P2-S1 执行创建/更新/销毁 |
| 启动 / INDEX.md | 不加载——读取笔记时不感知 |
