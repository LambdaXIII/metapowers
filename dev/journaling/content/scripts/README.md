# Frontmatter 脚本工具

读取、验证、合并写入、整体替换 Markdown 文件中的 YAML frontmatter。零第三方依赖——Python 和 JavaScript（Node.js）各一个文件。

## 快速开始

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

两版本（`.py` 和 `.mjs`）行为完全一致，输出格式相同。Python 需要 3.8+，Node.js 需要 18+。

## 命令参考

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

**示例**：
```bash
frontmatter get note.md                        # 全部字段 → JSON 对象
frontmatter get note.md summary                # 单个字段 → JSON scalar
frontmatter get note.md summary,tags           # 多个字段 → JSON 对象
frontmatter get note1.md note2.md title        # 多文件单字段 → {"file1": "...", "file2": "..."}
frontmatter get *.md                           # glob → 多文件全部字段
```

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

**选项**：`--journal-root <path>`（可选）检查 tags 是否在 TAGS.md 中注册。

**示例**：
```bash
frontmatter check note.md      # 单文件
frontmatter check *.md         # 批量
```

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

**示例**：
```bash
# 修改摘要，清空状态
frontmatter update note.md --data '{"summary":"新摘要","status":null}'

# 从 JSON 文件读取
frontmatter update note.md --file data.json

# 批量更新日期
frontmatter update *.md --data '{"last_update":"2026-06-30"}'

# 预览
frontmatter update note.md --data '{"summary":"preview"}' --dry-run
```

### `replace` — 整体替换

```
frontmatter replace <target> --data '<json>' | --file <path>
```

**完全替换** frontmatter 内容——仅接受单文件目标。body 区不修改。

`--data` 内容必须包含四个必填字段：`title`、`summary`、`tags`、`last_update`。

**选项**：`--dry-run` 预览变更，不写入文件。

**示例**：
```bash
# 直接指定数据
frontmatter replace note.md --data '{"title":"T","summary":"S","tags":["t"],"last_update":"2026-06-30"}'

# 从另一个 md 文件复制 frontmatter
frontmatter replace target.md --file source.md

# 从 YAML 模板
frontmatter replace note.md --file template.yaml
```

## 常用场景

### 批量更新 last_update

```bash
frontmatter update experience/*.md --data '{"last_update":"2026-06-30"}'
```

### 检查所有条目格式

```bash
frontmatter check experience/*.md knowledge/*.md active_works/*.md
```

### 预览变更

```bash
frontmatter update note.md --data '{"status":"completed"}' --dry-run
```

### 获取所有条目的标题列表

```bash
frontmatter get experience/*.md title
# → {"exp/note1.md": "Title 1", "exp/note2.md": "Title 2", ...}
```

### 幂等替换（读取 → 处理 → 写回）

```bash
data=$(frontmatter get note.md)
# ... 修改 data ...
frontmatter replace note.md --data "$data"
```

## 错误处理

| 场景 | stderr 输出 | 退出码 |
|------|-----------|--------|
| 文件不存在 | `file not found: <path>` | 1（至少一个文件找不到） |
| glob 无匹配 | `no files matched` | 1 |
| frontmatter 格式错误 | `文件名: 具体错误` | 1 |
| YAML 解析失败 | `parse error: line N: ...` | 1 |
| 写入失败 | 系统错误信息 | 1 |
| 验证通过 | （stdout）`文件名: valid` | 0 |

错误信息写入 stderr，标准输出写入 stdout，便于管道处理。

## 限制

- **YAML 子集**：仅支持字符串、数字、布尔、null、列表、注释。不支持嵌套对象、锚点、别名、多行字符串展开（`|` 和 `>` 保留原始文本）。
- **必填字段**：`replace` 要求 `--data` 包含所有四个必填字段（`title`、`summary`、`tags`、`last_update`），不可部分替换。
- **单文件目标**：`replace` 仅接受一个目标文件。
- **JSON 数据格式**：`--data` 必须使用标准 JSON（双引号，无尾逗号）。复杂数据推荐用 `--file` 传递。
- **get 的目标/字段区分**：`get` 通过启发式规则区分文件路径和字段名——含通配符、路径分隔符、文件扩展名的参数视为目标，其余视为字段名。

## 文件清单

```
scripts/
├── README.md           # 本文件
├── frontmatter.py      # Python 3.8+ 实现
├── frontmatter.mjs     # Node.js 18+ ESM 实现
├── check-links.py      # Python 3.8+ 实现
└── check-links.mjs     # Node.js 18+ ESM 实现
```


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

两版本（`.py` 和 `.mjs`）行为完全一致，输出格式相同。Python 需要 3.8+，Node.js 需要 18+。

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

### 使用场景

**场景 1：维护周期 — Phase 3 断链检查**

维护协议 P3-S2-dim3 要求检查指向已归档内容的死链。全 journal 扫描：

```bash
python check-links.py INDEX.md
```

关注输出中的：
- `summary.broken`：断链总数（预期维护结束时为 0）
- `broken_links`：每条断链的 target、类型、出现位置（source + line + text）
- `orphan_files`：无任何入链的文件——可能是孤立知识，也可能是未被正确索引的有效条目

断链修复时应区分两种情形：
- **已迁移至新位置** → 用 `--file` 查入链来源，逐一修复链接指向
- **已归档但未提取关键点** → 决定是否从 archive 拉回

**场景 2：日常查询 — "谁引用了这个文件"**

查看某个文件的完整引用关系：

```bash
python check-links.py INDEX.md --file active_works/note.md
```

输出中的 `referenced_by` 数组列出所有指向此文件的 journal 内文件。适用于：
- 重构前评估影响范围（修改或移除一个文件前，了解哪些文件引用它）
- 查找遗漏的交叉引用（发现本应引用但实际未引用的其他条目）
- 识别高价值文件（了解哪些文件被广泛引用，适合升级为次级索引）

**场景 3：重构前影响分析**

在执行维护 Phase 2 重组前，先用全 journal 报告了解当前链接结构：

```bash
python check-links.py INDEX.md --absolute
```

通过 `most_referenced` 了解哪些文件是"中枢节点"——它们不适合随意移动或重命名。结合 `per_file` 的出入链关系，可以在重组前评估每个操作的影响范围。

**场景 4：Journal 健康检查（非维护场景）**

即使不触发完整维护，也可以定期运行快速诊断：

```bash
python check-links.py INDEX.md 2>&1 | python -c "import json, sys; d=json.load(sys.stdin); s=d['summary']; print(f'Links: {s["total_links"]} total, {s["broken"]} broken, {s["orphan_files"]} orphan')"
```

关注异常信号：broken > 0、orphan_files > 2、某个文件的入链突然激增或消失。

### 最佳实践

1. **从 INDEX.md 入口运行**：始终以 `INDEX.md` 为 `<entry>` 参数。这确保 journal-root 自动发现正确，且操作边界覆盖整个 journal。

2. **维护中先跑全量再修细节**：Phase 3 先用 `check-links INDEX.md` 获取全景，再用 `--file` 逐个修复具体文件。

3. **配合 frontmatter 工具使用**：
   - 断链修复后如果需要更新 frontmatter last_update：`python frontmatter.py update <file> --data '{"last_update":"2026-06-30"}'`
   - 验证修复后的文件格式：`python frontmatter.py check <file>`

4. **输出解析**：
   - 全 journal 模式输出为标准 JSON——可 pipe 给 `python -c` 或 `jq` 做进一步处理
   - `--no-pretty` 模式适合脚本间管道传输（单行 JSON）
   - `diff -w` 可用于跨版本（Python vs JS）输出一致性验证

5. **wikilink vs markdown 链接的路径解析差异**：
   - markdown 链接 `[text](path)`：相对于**源文件所在目录**解析
   - wikilink `[[path]]`：相对于 **journal-root** 解析（遵循 Obsidian 规范）
   - 这意味着 `[[foo.md]]` 在 `subdir/note.md` 中解析到 `<journal-root>/foo.md`，而非 `subdir/foo.md`。编写 wikilink 时请使用 journal-root 全路径。

6. **exit 0 即使有断链**：脚本的 exit 码只反映自身执行是否成功（journal-root 未找到等），不反映是否有断链。断链数是数据内容，通过 JSON 的 `summary.broken` 字段获取。


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
    "self_refs": 1,
    "orphan_files": 2
  },
  "broken_links": [ ... ],
  "orphan_files": [ ... ],
  "most_referenced": [ ... ],
  "per_file": [ ... ]
}
```

- **`summary`**：全局统计——`total_links`（总链接数）、`broken`（断链数）、`valid`（有效链接数）、`external`（外部链接数）、`self_refs`（自引用数）、`orphan_files`（孤立文件数）
- **`broken_links`**：按 target 聚合的断链列表，每条含 `{target, type, occurrences: [{source, line, text}]}`
- **`orphan_files`**：无入链且非 INDEX.md 的文件列表（按路径排序）
- **`most_referenced`**：被引用次数最多的前 10 个文件，格式 `[{file, refs}]`
- **`per_file`**：每个文件的出链和入链详情。出链按 target 聚合，入链按 source 聚合

**单文件聚焦输出**（`--file`）：仅输出一个文件的信息，结构为 `{journal_root, files_scanned, file, self_refs, links, referenced_by}`。

### 支持的链接格式

- **标准 Markdown 链接**：`[text](target)`
- **Obsidian wikilink**：`[[target]]` / `[[target|别名]]`

以下链接**不报告**：
- URL（`https://`、`http://`、`ftp://`、`mailto:` 开头）
- 纯锚点（`#section`，不含文件路径部分）

含 `#` 的混合目标（如 `file.md#section`）仅保留文件路径部分进行检查。

### 常用场景

#### 检查 journal 完整性

```bash
python check-links.py INDEX.md | python -c "import json,sys; d=json.load(sys.stdin); print(f'broken={d[\"summary\"][\"broken\"]} orphan={d[\"summary\"][\"orphan_files\"]}')"
```

#### 查找孤立文件

```bash
python check-links.py INDEX.md | python -c "import json,sys; d=json.load(sys.stdin); [print(f) for f in d['orphan_files']]"
```

#### 查看文件入链（谁引用了我）

```bash
python check-links.py INDEX.md --file experience/note.md | python -c "import json,sys; d=json.load(sys.stdin); [print(r['source']) for r in d['referenced_by']]"
```

#### 维护前全面审计

```bash
python check-links.py INDEX.md --absolute > /tmp/journal-audit.json
# 检查 broken_links、orphan_files、most_referenced
```

### 错误处理

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

### 限制

- **仅检查 .md 文件**：不追踪图片、PDF 等非 Markdown 附件链接
- **不验证 URL**：HTTP/HTTPS 链接直接跳过，不检查可达性
- **不展开符号链接**：路径 resolve 不追踪 symlink
- **代码块内误识别**：代码块中的类链接语法（如 `[array](index)`）可能被当作真实链接提取——维护协议要求"宁可多报不可漏报"

### 文件清单

```
scripts/
├── README.md           # 本文件
├── frontmatter.py      # Python 3.8+ 实现
├── frontmatter.mjs     # Node.js 18+ ESM 实现
├── check-links.py      # Python 3.8+ 实现（新增）
└── check-links.mjs     # Node.js 18+ ESM 实现（新增）
```