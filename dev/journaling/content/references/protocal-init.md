> 本协议定义从头创建 journal 的流程规范。它只定义判断逻辑和流程规则。
> 各文件的初始内容模板见 `templates/seed/` 目录，执行者可按需取用。

---

## 初始化目标

Journal 初始化完成后应处于两个状态：

- **就绪态**：CLASSIFICATION.md、TAGS.md、INDEX.md 已就位。内容是种子级别的——最小可用骨架。以后的内容由写入协议驱动，自然生长。不预填、不预设。
- **可发现态**：后续每次 session 启动时，agent 的上下文中**直接可见**一条指令：必须读取 INDEX.md。不需要搜索、不需要回忆、不需要猜测。

  这是三个阶段共同保证的效果：

  ```
  发现合约（Phase 3 设计）
    → 每次 session 启动时自动注入上下文
      → 指令：读取 <journal-root>/INDEX.md  （Phase 1 确定的位置）
        → INDEX.md 协议声明行告知              （Phase 2 创建/修复的）
          - Read without skill
          - CLASSIFICATION.md（分类规则）
          - TAGS.md（标签系统）
  ```

初始化后的生长由真实使用驱动：
- 第一个 project tag、第一条经验、第一条知识——从工作中自然产出
- 目录在写入时按需创建（由 CLASSIFICATION.md 或后续分类审计催生）
- INDEX.md 的经验摘要和专项工作随实际经验积累自然填充

---

## Phase 1: 确定位置

> journal-root 是所有操作的锚点。位置不确定则后续步骤无依托，文件可能错位。

**判断上下文**：
- 上下文中已明确 journal-root → 采信，直接进入 Phase 2
- 上下文中未明确 journal-root → 询问用户，推荐 `~/.journal`，确认后采信
- 用户执行前已直接指定路径 → 视同已确认，直接使用

Phase 1 完成条件：journal-root 已确定且唯一。无需验证步——确认即完成。

---

## Phase 2: 初始化笔记库内容

逐项检查 CLASSIFICATION.md、TAGS.md、INDEX.md 三个骨架文件。三个文件缺一不可——它们共同定义 journal 的规则骨架。

四个种子目录（inbox/ experience/ knowledge/ active_works/）**不主动创建**。它们由写入操作按需催生——写入时检查目标目录是否存在，不存在则 mkdir。

### 通用检查流程

对每个文件，执行以下步骤：

1. **读取 spec**——加载对应的 reference 文件，了解该文件应该包含什么内容、起什么作用
   - INDEX.md → `references/spec-index.md`
   - CLASSIFICATION.md → `references/design-classification.md`
   - TAGS.md → `references/design-tags.md`
2. **检查 journal-root 下同名文件是否存在**
3. **判断类型**——用 spec 中的 Type Identification 锚点判断已有文件是不是我们需要的文件：

```
已存在同名文件？
├─ 是我们要的（Type Identification 匹配）
│   ├─ 格式符合 spec → 不动
│   └─ 格式不符合 spec → 保留内容，按 spec 重写格式
│
├─ 不是我们要的（只是恰好同名）
│   └─ 重命名为 <原名>.bak → 移到 inbox/ →
│       视同不存在 → 按 spec 创建初始版本
│
└─ 不存在
    └─ 按 spec 创建初始版本（初始内容从 templates/seed/ 取同名文件）
```

> 注意：复制种子文件后，替换 INDEX.md 中的占位符（`YYYY-MM-DD` → 当前日期，`<初始化原因>` → 简短说明）。其余种子文件不包含占位符。

> 核心原则：不判断类型直接覆盖会丢失用户已有内容。先识别、再决策。

### 各文件的 Type Identification 锚点

| 文件 | 锚点——用于判断"这是不是我们要的文件" |
|------|--------------------------------------|
| INDEX.md | 文件顶部包含 `> ⚠️ 本 journal 由 journaling 技能管理` |
| CLASSIFICATION.md | `# Classification` 标题 + `| 目录 | 放什么 | 不放什么 | 一句话判断 |` 快速参考表格 |
| TAGS.md | `# Tags` 标题 + `## Tags` 节 + `| Tag | Meaning |` 表格 |

> 锚点用于**类型识别**，不是格式检测的全部。识别之后，如果格式不符合 spec，应保留内容、重写格式——而不是覆盖。

### 三个文件的 spec 对应关系

| 文件 | Spec（读此文件了解其规范） | Seed（取此文件作为初始内容） |
|------|--------------------------|---------------------------|
| INDEX.md | `references/spec-index.md` | `templates/seed/INDEX.md` |
| CLASSIFICATION.md | `references/design-classification.md` | `templates/seed/CLASSIFICATION.md` |
| TAGS.md | `references/design-tags.md` | `templates/seed/TAGS.md` |

### 验证

逐项确认：
- [ ] `<journal-root>/INDEX.md` 存在且包含协议声明行
- [ ] `<journal-root>/CLASSIFICATION.md` 存在且包含 # Classification 标题和快速参考表格
- [ ] `<journal-root>/TAGS.md` 存在且包含 # Tags 标题、Rules 节和 Tags 表格

---

## Phase 3: 设计发现合约

> ⚠️ **禁止自行执行**——此阶段仅说明、建议、讨论。不做任何写入操作。不改任何配置。

### 为什么需要发现合约

你当前这个 session 知道 journal-root 在哪里。但 agent 是无状态的——下个 session 启动时，今天知道的一切都消失了。如果 journal-root 不在启动时自动可见，那么 Phase 2 创建的所有文件等于不存在。

文件就位但 agent 找不到 = 没有 journal。

### 有效发现合约的条件

一个有效的发现合约必须同时满足：

1. **每次启动自动注入**——agent 不需要搜索、回忆或猜测
2. **包含 journal-root 具体值**——不能是变量或待替换占位符
3. **强制要求无条件加载 INDEX.md**——不能是可选的"建议阅读"

### 方案讨论

可能的载体（取决于你所在的环境）：
- 运行时全局提示词（如 AGENTS.md、CLAUDE.md、.cursorrules）
- 启动配置脚本
- 环境变量

你需要：
1. 识别当前运行时中满足"每次启动自动注入 + 你权限写入 + 跨 session 持久"的载体
2. 向用户说明你的发现和推荐方案
3. 由用户决定是否建立、如何建立

**禁止自行写入。** 用户在了解全部信息后做出决定，由用户或后续 session 执行。

### 回退方案

如果当前环境确实没有任何可用的注入机制：
- 回退到约定路径 `~/.journal/`
- 告知用户：每次启动需手动指定 journal-root，或配置启动脚本。可靠性低于合约模式。

