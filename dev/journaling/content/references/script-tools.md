# Script Tools Guide

> scripts/ 目录下零依赖脚本工具的完整指南——命令参考、输出格式、行为说明。双版本（`.py` 与 `.mjs`）行为完全一致，输出格式相同。Python 需要 3.8+，Node.js 需要 18+。
>
> 快速入门与场景路由见 SKILL.md 的 Scripts 节；每个脚本的 `--help` 含精简用法。

---

## 工具清单

```
scripts/
├── frontmatter.py      # Python 3.8+ 实现
├── frontmatter.mjs     # Node.js 18+ ESM 实现
├── check-links.py      # Python 3.8+ 实现
└── check-links.mjs     # Node.js 18+ ESM 实现
```

- `frontmatter` — 读取、验证、合并写入、整体替换 YAML frontmatter
- `check-links` — 提取 journal 全部链接、检查目标、分析入链/出链关系

两版本 API、行为、输出格式完全一致，可互换使用。

---

## frontmatter

读取、验证、合并写入、整体替换 Markdown 文件中的 YAML frontmatter。

### 快速开始

```bash
# 读取所有字段
python frontmatter.py get note.md
node frontmatter.mjs get note.md

# 读取指定字段
python frontmatter.py get note.md title summary,tags

# 验证格式
python frontmatter.py check *.md

# 合并写入（delta 合并：覆盖同名字段，保留其他字段）
python frontmatter.py update note.md --data '{"summary":"新的摘要","status":null}'

# 整体替换（覆盖整个 frontmatter）
python frontmatter.py replace note.md --data '{"title":"T","summary":"S","tags":["a"],"last_update":"2026-06-30"}'
```

### `get` — 读取

```
frontmatter get <target...> [<fields...>]
```

读取一个或多个 Markdown 文件的 frontmatter 字段。

**字段参数**：空格或逗号分隔的字段名。省略则输出全部字段。

**输出格式**（由文件数和字段数决定）：

| 文件数 | 字段数 | 输出格式 |
|--------|--------|---------|
| 1 | 0（全部） | `{"field": value, ...}` |
| 1 | 1 | JSON 原生值（`"string"` / `[...]` / `null`） |
| 1 | ≥2 | `{"field1": value1, ...}`（仅含指定字段） |
| ≥2 | 0（全部） | `[{"file": "...", ...fields}, ...]` |
| ≥2 | 1 | `{"file1": value1, ...}` |
| ≥2 | ≥2 | `[{"file": "...", "field1": ..., ...}, ...]` |

请求不存在的字段返回 JSON `null`。

**选项**：
- `--pretty`（默认）美化 JSON 输出
- `--no-pretty` 关闭缩进

### `check` — 验证

```
frontmatter check <target...>
```

验证 frontmatter 格式合规性。

**检查项**：
- 必填字段存在性：`title`（非空字符串）、`summary`（字符串）、`tags`（YAML list）、`last_update`（YYYY-MM-DD）
- 可选字段类型：`status`（字符串）、`author`（字符串）、`date`（YYYY-MM-DD）
- tags 必须是 YAML list 格式（禁止内联 `[a, b]` 或逗号分隔）
- 布尔值必须全小写（`true`/`false`，`True`/`False` 报错）
- 自定义字段名必须 `lowercase-kebab-case`

**退出码**：0 = 全部通过；1 = 至少一个文件有问题。

**选项**：`--journal-root <path>`（可选，预留——当前版本不执行标签注册校验）。

### `update` — 合并写入

```
frontmatter update <target...> --data '<json>' | --file <path>
```

将字段**合并**到现有 frontmatter 中——覆盖同名字段，保留其他字段不变。body 区不修改。

**合并语义**：
- 字段存在且值非 null → 覆盖
- 字段存在且值为 null → 清空字段值（保留字段名）
- 字段不存在且值非 null → 新增
- 字段不存在且值为 null → 无操作

**必需**：`--data '<json>'` 或 `--file <path>`。

`--file` 自动识别格式：
- `.md` → 提取 frontmatter
- `.json` → JSON 解析
- `.yaml` / `.yml` → YAML 解析

**选项**：`--dry-run` 预览变更，不写入文件。

### `replace` — 整体替换

```
frontmatter replace <target> --data '<json>' | --file <path>
```

**完全替换** frontmatter 内容——仅接受单文件目标。body 区不修改。

`--data` 内容必须包含四个必填字段：`title`、`summary`、`tags`、`last_update`。

**选项**：`--dry-run` 预览变更，不写入文件。

### frontmatter 错误处理

| 场景 | stderr 输出 | 退出码 |
|------|-----------|--------|
| 文件不存在 | `file not found: <path>` | 1（至少一个文件找不到） |
| glob 无匹配 | `no files matched` | 1 |
| frontmatter 格式错误 | `文件名: 具体错误` | 1 |
| YAML 解析失败 | `parse error: line N: ...` | 1 |
| 写入失败 | 系统错误信息 | 1 |
| 验证通过 | （stdout）`文件名: valid` | 0 |

错误信息写入 stderr，标准输出写入 stdout，便于管道处理。

### frontmatter 限制

- **YAML 子集**：仅支持字符串、数字、布尔、null、列表、注释。不支持嵌套对象、锚点、别名、多行字符串展开（`|` 和 `>` 保留原始文本）。
- **必填字段**：`replace` 要求 `--data` 包含所有四个必填字段，不可部分替换。
- **单文件目标**：`replace` 仅接受一个目标文件。
- **JSON 数据格式**：`--data` 必须使用标准 JSON（双引号，无尾逗号）。复杂数据推荐用 `--file` 传递。
- **get 的目标/字段区分**：`get` 通过启发式规则区分文件路径和字段名——含通配符、路径分隔符、文件扩展名的参数视为目标，其余视为字段名。

---

## check-links

提取 journal 中全部 markdown 链接、检查目标文件是否存在、分析入链/出链关系。零第三方依赖，纯只读——不修改任何文件。

### 快速开始

```bash
# 全 journal 链接检查
python check-links.py INDEX.md
node check-links.mjs INDEX.md

# 聚焦单文件的出链和入链
python check-links.py INDEX.md --file active_works/note.md

# 从任意目录运行
python check-links.py --journal-root .
```

### 命令参考

```
check-links [options] <entry>
```

**参数**：

| 参数 | 说明 |
|------|------|
| `<entry>` | Journal 入口路径（INDEX.md、任意 journal 文件或目录）。用于自动发现 journal root（向上查找 INDEX.md）。 |

**选项**：

| 选项 | 说明 |
|------|------|
| `--journal-root <path>` | 手动指定 journal 根目录。当 `<entry>` 省略时必需。 |
| `--file <path>` | 聚焦到单个文件（路径相对于 journal-root）。省略则输出全 journal 报告。 |
| `--absolute` | `resolved` 字段以绝对路径输出。 |
| `--relative-to <path>` | `resolved` 字段相对于指定路径输出。与 `--absolute` 同时给定时以最后一个为准。 |
| `--no-pretty` | 禁用 JSON 缩进（默认带缩进输出）。 |
| `--help` | 显示帮助信息，退出码 0。 |

默认情况下 `resolved` 字段相对于链接源文件所在目录输出。

### 链接解析语义

遵循 `spec-note.md` 的 Link Convention（唯一权威来源）。摘要：

- **EXTERNAL**：URL、本地绝对路径（如 `C:/…`）——仅分类标记，不验证可达性
- **WRONG**：mdlink 无扩展名——非法
- `[[foo]]`（wikilink 无扩展名）→ 库内按名搜索；多匹配 → ambiguous
- `[[foo.md]]` / `[foo.md]`（带扩展名、无路径）→ 相对当前文件目录；失败时 fallback：wikilink → 无扩展名按名搜索；mdlink → journal-root 精确路径
- 带 `./`/`../` 前缀 → 相对当前文件目录
- 带路径无前缀 → 相对 journal-root

每个链接输出 `status` 字段：`internal` / `external` / `wrong` / `ambiguous`。断链判定只针对 `internal` 链接（`exists: false`）。

### 输出格式

**全 journal 报告**（JSON）：

```json
{
  "journal_root": "/path/to/journal",
  "files_scanned": 42,
  "summary": {
    "total_links": 156,
    "broken": 3,
    "valid": 150,
    "external": 3,
    "wrong": 1,
    "ambiguous": 0,
    "self_refs": 1,
    "orphan_files": 2
  },
  "broken_links": [ ... ],
  "orphan_files": [ ... ],
  "most_referenced": [ ... ],
  "per_file": [ ... ]
}
```

- **`summary`**：全局统计——`total_links`（总链接数）、`broken`（内部断链数）、`valid`（有效内部链接数）、`external`（外部链接数）、`wrong`（非法 mdlink 数）、`ambiguous`（歧义链接数）、`self_refs`（自引用数）、`orphan_files`（孤立文件数）
- **`broken_links`**：按 target 聚合的断链列表，每条含 `{target, type, occurrences: [{source, line, text}]}`
- **`orphan_files`**：无入链且非 INDEX.md 的文件列表（按路径排序）
- **`most_referenced`**：被引用次数最多的前 10 个文件，格式 `[{file, refs}]`
- **`per_file`**：每个文件的出链和入链详情。出链按 target 聚合（每条含 `status`、`resolved`、`exists`、`inside_journal`），入链按 source 聚合

**单文件聚焦输出**（`--file`）：仅输出一个文件的信息，结构为 `{journal_root, files_scanned, file, self_refs, links, referenced_by}`。

### 使用场景

**场景 1：维护周期 — 断链检查**

维护收尾要求断链清零。全 journal 扫描：

```bash
python check-links.py INDEX.md
```

关注输出中的：
- `summary.broken`：内部断链总数（预期维护结束时为 0）
- `summary.wrong`：无扩展名 mdlink——按 Link Convention 属非法，应改为 wikilink 或补扩展名
- `summary.ambiguous`：无扩展名 wikilink 重名——应改为带路径的明确形式
- `broken_links`：每条断链的 target、类型、出现位置（source + line + text）
- `orphan_files`：无任何入链的文件——可能是孤立知识，也可能是未被正确索引的有效条目

断链修复时应区分两种情形：
- **已迁移至新位置** → 用 `--file` 查入链来源，逐一修复链接指向
- **已归档但未提取关键点** → 决定是否从 archive 拉回

**场景 2：日常查询 — "谁引用了这个文件"**

```bash
python check-links.py INDEX.md --file active_works/note.md
```

输出中的 `referenced_by` 数组列出所有指向此文件的 journal 内文件。适用于：
- 重构前评估影响范围（修改或移除一个文件前，了解哪些文件引用它）
- 查找遗漏的交叉引用
- 识别高价值文件（被广泛引用的文件适合升级为次级索引）

**场景 3：重构前影响分析**

```bash
python check-links.py INDEX.md --absolute
```

通过 `most_referenced` 了解哪些文件是"中枢节点"——它们不适合随意移动或重命名。结合 `per_file` 的出入链关系，可以在重组前评估每个操作的影响范围。

**场景 4：Journal 健康检查（非维护场景）**

```bash
python check-links.py INDEX.md 2>&1 | python -c "import json, sys; d=json.load(sys.stdin); s=d['summary']; print(f'Links: {s[\"total_links\"]} total, {s[\"broken\"]} broken, {s[\"orphan_files\"]} orphan')"
```

关注异常信号：broken > 0、orphan_files > 2、某个文件的入链突然激增或消失。

### 支持的链接格式

- **标准 Markdown 链接**：`[text](target)`
- **Obsidian wikilink**：`[[target]]` / `[[target|别名]]`

以下链接**不报告**：
- URL（`https://`、`http://`、`ftp://`、`mailto:` 开头）——不验证可达性
- 纯锚点（`#section`，不含文件路径部分）

含 `#` 的混合目标（如 `file.md#section`）仅保留文件路径部分进行检查。

### 符号链接行为

- **不展开符号链接**：路径 resolve 不追踪 symlink——符号链接文件不进入文件清单、不参与链接检查；目录符号链接不递归；存在性检查跟随符号链接（指向存在的目标即视为有效）
- journal-root 本身为符号链接时，输出中的路径保持用户输入视角，不替换为磁盘真实路径

### check-links 错误处理

| 场景 | stderr 输出 | 退出码 |
|------|-----------|--------|
| entry 不存在 | `<entry>: file not found` | 1 |
| INDEX.md 未找到 | `INDEX.md not found in ancestors of <entry>` | 1 |
| 无 entry 且无 --journal-root | `entry or --journal-root required` | 1 |
| --file 路径在 journal-root 外 | `<file>: outside journal-root` | 1 |
| --file 路径未找到 | `<file>: not found under journal-root` | 1 |
| 无 .md 文件 | `no markdown files found under <path>` | 1 |
| 检查完成（即使有断链） | JSON 输出到 stdout | 0 |

> **断链是数据内容，不是脚本执行错误。** 有断链时退出码仍为 0——断链数量和详情在 JSON 输出的 `summary.broken` 和 `broken_links` 中。

### check-links 限制

- **仅检查 .md 文件**：不追踪图片、PDF 等非 Markdown 附件链接
- **不验证 URL**：HTTP/HTTPS 链接直接跳过，不检查可达性
- **代码块内误识别**：代码块中的类链接语法（如 `[array](index)`）可能被当作真实链接提取——维护协议要求"宁可多报不可漏报"
