# Writing Protocol

## 定位

本协议定义对 journal 条目进行内容操作——新建笔记、补充已有条目、更新 frontmatter。
核心目标：内容就绪（entry 有完整 frontmatter，body 可读）+ 写入路径轻量。
写得不完美没关系——维护协议兜底。关键是不打断主线工作。

---

## 写入流程（规范性动作，按序执行）

### 1. 判断是否值得写

Not everything belongs in the journal. Before committing content, check:

- **Long-lived?** Will this still be useful weeks from now? If not, discard.
- **Version-independent?** Not tied to a software version, config snapshot, or one-time event?
- **Reference value?** If read a week from now, would it still hold meaning?

Content that fails all three (quick-test results, build logs, transient findings) does not belong in the journal.

### 2. 读取 journal 规则

写入前必读 journal 规则文档——技能强制存在，即使为空；内容由 journal 自定（分类板块、标签板块、INDEX 结构板块、笔记元数据字段板块、写作需求板块等）。加载其中定义的规则并按之执行；为空或未定义相应板块时，用种子默认方案（目录/tag/元数据字段，见 ../templates/seed/）。

规则文档不存在属异常（强制义务：必须存在）——此时从 ../templates/seed/ 复制规则文档种子到 `<journal-root>` 补齐（入口文件名由机制固定；只补缺失文件，不触发初始化协议的其他步骤，避免连带覆盖已有 INDEX）。

### 3. 编写 frontmatter 与 body

- 必须有 YAML frontmatter（技能硬性）。
- 字段方案：按 journal 规则元数据板块；未定义时用种子推荐方案（见 ../templates/seed/ 规则文档种子的元数据字段板块）。
- 格式语法：见 `spec-frontmatter.md`（通用格式规范）。
- 目录归属与标签：遵循 journal 规则分类板块/标签板块（未定义时用种子方案）。
- summary 锚定范围（见 `spec-note.md` Summary Anchoring）；正文承载理解。

### 4. 检查可发现链路

写完思考：这条内容将来被需要时如何被发现？

- 属于需要入口的内容（被读取路径依赖）→ 按 journal 规则建立发现入口
- 属于读时无需感知的内容 → 不建入口

只给判断原则，不预设任何载体。

---

## 额外说明

- **写得不完美没关系**——维护协议兜底。
- **补充已有条目**：判断取决于条目何时写的——
  - 同 session（刚写的笔记）：用 Summary Anchoring 的 scope 检查（见 `spec-note.md`）——新内容仍在原 summary 范围内？是 → 扩展原条目（范围扩大则更新 summary）；否 → 新建条目。范围还在形成中，不必过度思考。
  - 跨 session（旧笔记）：标准更严——必须是**直接扩展**且不改变原 summary：summary 不变 → 追加到原条目；summary 会变 → 新建条目，并在新条目中回链 `Related: [old entry title](path/to/old-entry.md)`。
  - 不要担心两条目间的冗余、重叠或矛盾——维护时解决（见 `protocal-maintenance.md`）。Split now, merge later.
- **交叉引用（轻量启发）**：写 body 时扫描内容相近的既有条目（按 journal 规则定义的组织方式——如同目录、同标签），有明确关系（互补主题、矛盾发现、直接扩展）加 `Related:` 或 `See also:` 行——一次快速扫描，不是深读。
- **INDEX 的重要性**：写入后 INDEX 应能反映新内容——价值陈述，非强制义务；INDEX 同步的具体规则由 journal 规则（INDEX 结构板块）定义。
- **交付前自检（四问提醒）**——可执行性 / 独立性 / 边界覆盖 / 可复现性：
  1. **可执行性** — 一个新人读完后能直接实现/执行吗？
  2. **独立性** — 脱离所有其他文档只读这一份，能理解吗？
  3. **边界覆盖** — 空输入、错输入、不存在的情况都处理了吗？
  4. **可复现性** — 半年后回来重读，能理解当时为什么这样决定吗？
