# Writing Protocol

## 定位

本协议定义对 journal 条目进行内容操作——新建笔记、补充已有条目、更新 frontmatter、收录现存文档。
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

收录现存文档时，价值判断按同一组判据处理——待收录内容与既有条目高度重叠或无长期价值，由此三问裁定，不设独立的收录准入流程。

### 2. 读取 journal 规则

读取并遵守 journal 规则是非只读操作的族义务——义务内容（规则文档必读、板块加载、种子默认、缺失补齐）单处定义于 [`protocal-operations.md`](protocal-operations.md)。

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

- **收录现存文档**：拷贝文件到 journal 对应位置，再在其上修改调整（避免手工抄写）；frontmatter、summary、链接、分类等加工与写入流程一致。
- **合并条目**（用户要求把重复条目并成一条）：这是用户引导下的普通操作，不是维护协议的触发。最小做法——确定保留方（信息更全或更新的一方）；将彼方与保留方缺异的实质内容并入保留方；收敛后的 summary 覆盖合并后的范围（按 Summary Anchoring 更新，见 `spec-note.md`）；冲突的矛盾点在正文中注明取舍理由而不是静默择一；被并条目移入临时保存目录并在原位置留一行指向保留方的关系注记；修复指向被并文件的所有引用，INDEX 登记同步。
- **写得不完美没关系**——维护协议兜底。
- **补充已有条目**：判断取决于条目何时写的——
  - 同 session（刚写的笔记）：用 Summary Anchoring 的 scope 检查（见 `spec-note.md`）——新内容仍在原 summary 范围内？是 → 扩展原条目（范围扩大则更新 summary）；否 → 新建条目。范围还在形成中，不必过度思考。
  - 跨 session（旧笔记）：标准更严——必须是**直接扩展**且不改变原 summary：summary 不变 → 追加到原条目；summary 会变 → 新建条目，并在新条目中回链 `Related: [old entry title](path/to/old-entry.md)`。
  - 不要担心两条目间的冗余、重叠或矛盾——维护时解决（见 `protocal-maintenance.md`）。Split now, merge later.
- **交叉引用（轻量启发）**：写 body 时扫描内容相近的既有条目（按 journal 规则定义的组织方式——如同目录、同标签），有明确关系（互补主题、矛盾发现、直接扩展）加 `Related:` 或 `See also:` 行——一次快速扫描，不是深读。
- **INDEX 的重要性**：写入后 INDEX 应能反映新内容——价值陈述，非强制义务；INDEX 同步的具体规则由 journal 规则（INDEX 结构板块）定义。
- **交付前自检（四问提醒）**：
  1. **可执行性** — 未来重读时能直接使用吗？
  2. **独立性** — 脱离本 session 对话上下文与其他条目，只读这一份能理解吗？
  3. **边界覆盖** — 结论的适用条件与失效场景说明了吗？
  4. **可复现性** — 半年后回来重读，能理解当时为什么这样决定吗？

## 如果你能够委派子代理

如果当前会话中主线话题仍在继续，
且你有能力委派子代理完成任务，
那么以下是一种建议的工作方式：

1. 直接将笔记写入一个临时目录
2. 委派子代理读取RULES.md并按照规范整理，如提炼tags、放置笔记、更新INDEX等

这样你就可以很快地继续工作，并且最小化对当前话题的干扰了。
