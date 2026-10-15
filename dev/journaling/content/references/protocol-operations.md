# Operations Protocol

改变 journal 状态的操作——新建、补充、编辑、收录、移动、归档、删除——共享同一套逻辑：读取并遵守 journal 规则、价值与归属判断、关联一致、INDEX 反映。先给这套共同逻辑，再给各操作的差异指引。用户明确触发的专项整理（维护）走维护协议（[`protocol-maintenance.md`](protocol-maintenance.md)）；条目层面的编辑、移动、删除、合并等日常整理在本篇处理，不触发维护。所有操作以已读 `<journal-root>/INDEX.md` 为前提。

操作的目标是内容就绪（条目有完整 frontmatter，body 可读）且路径轻量。写得不完美没关系——维护协议兜底，关键是不打断主线工作。

---

## 共同逻辑

### 读取并遵守 journal 规则

任何改变 journal 状态的操作前必读 journal 规则文档——技能强制存在，即使为空；内容由 journal 自定（分类板块、标签板块、INDEX 结构板块、笔记元数据字段板块、写作需求板块等）。加载其中定义的规则并按之执行；为空或未定义相应板块时，用种子默认方案（目录/tag/元数据字段，见 ../templates/seed/）。

规则文档不存在属异常（必须存在）——此时从 ../templates/seed/ 复制规则文档种子到 `<journal-root>` 补齐（入口文件名由机制固定；只补缺失文件，不触发初始化协议的其他步骤，避免连带覆盖已有 INDEX）。

本义务在此定义一次，各操作路径与初始化、维护协议引用它，不逐字重复。

### 判断是否值得写

Not everything belongs in the journal. Before committing content, check:

- **Long-lived?** Will this still be useful weeks from now? If not, discard.
- **Version-independent?** Not tied to a software version, config snapshot, or one-time event?
- **Reference value?** If read a week from now, would it still hold meaning?

Content that fails all three (quick-test results, build logs, transient findings) does not belong in the journal.

价值判断对全族操作同一组判据——收录现存文档时同样由此三问裁定，不设独立的收录准入流程。

### 编写 frontmatter 与 body

- 必须有 YAML frontmatter（技能硬性）。
- 字段方案：按 journal 规则元数据板块；未定义时用种子推荐方案（见 ../templates/seed/ 规则文档种子的元数据字段板块）。
- 格式语法：见 `spec-frontmatter.md`（通用格式规范）。
- 目录归属与标签：遵循 journal 规则分类板块/标签板块（未定义时用种子方案）。
- summary 锚定范围（见 `spec-note.md` Summary Anchoring）；正文承载理解。

### 关联一致与可发现链路

- **关联一致**：笔记之间通过引用互相关联，改动文件名或位置会破坏指向旧位置的引用。
- 写完思考：这条内容将来被需要时如何被发现？
  - 属于需要入口的内容（被读取路径依赖）→ 按 journal 规则建立发现入口
  - 属于读时无需感知的内容 → 不建入口

只给判断原则，不预设任何载体。

### 交叉引用（轻量启发）

写 body 时扫描内容相近的既有条目（按 journal 规则定义的组织方式——如同目录、同标签），有明确关系（互补主题、矛盾发现、直接扩展）加 `Related:` 或 `See also:` 行——一次快速扫描，不是深读。

### INDEX 反映

写入后 INDEX 应能反映新内容——价值陈述，非技能硬性义务；INDEX 同步的具体规则由 journal 规则（INDEX 结构板块）定义，规则要求更新时按规则执行。

### 交付前自检（四问提醒）

1. **可执行性** — 未来重读时能直接使用吗？
2. **独立性** — 脱离本 session 对话上下文与其他条目，只读这一份能理解吗？
3. **边界覆盖** — 结论的适用条件与失效场景说明了吗？
4. **可复现性** — 半年后回来重读，能理解当时为什么这样决定吗？

---

## 各操作差异指引

未单列差异的操作（更新 frontmatter、改标题、归档、批量整理等）按共同逻辑执行，其语义依 journal 规则。标题指 frontmatter 的 `title` 字段（见 `spec-frontmatter.md`）；文件名中的主题与标题是否联动依 journal 规则的命名约定——种子命名只约定文件名格式、不含联动，规则未给出联动约定时与用户确认。

### 新建与补充

新建笔记按共同逻辑执行。补充已有条目，判断取决于条目何时写的：

- 同 session（刚写的笔记）：用 Summary Anchoring 的 scope 检查（见 `spec-note.md`）——新内容仍在原 summary 范围内？是 → 扩展原条目（范围扩大则更新 summary）；否 → 新建条目。范围还在形成中，不必过度思考。
- 跨 session（旧笔记）：标准更严——必须是**直接扩展**且不改变原 summary：summary 不变 → 追加到原条目；summary 会变 → 新建条目，并在新条目中回链 `Related: [old entry title](path/to/old-entry.md)`。
- 不要担心两条目间的冗余、重叠或矛盾——维护时解决（见 [`protocol-maintenance.md`](protocol-maintenance.md)）。Split now, merge later.

### 收录（现存文档存入 journal）

拷贝文件到 journal 对应位置，再在其上修改调整（避免手工抄写）；frontmatter、summary、链接、分类等加工与写入流程一致。价值判断与新建同一组判据，不设独立的收录准入流程。

### 合并条目

用户要求把重复条目并成一条时——这是用户引导下的普通操作，不是维护的触发。最小做法：确定保留方（信息更全或更新的一方）；将彼方与保留方缺异的实质内容并入保留方；收敛后的 summary 覆盖合并后的范围（按 Summary Anchoring 更新，见 `spec-note.md`）；冲突的矛盾点在正文中注明取舍理由而不是静默择一；被并条目移入临时保存目录并在原位置留一行指向保留方的关系注记；修复指向被并文件的所有引用，INDEX 登记同步。

### 移动（调整条目位置或文件名）

归属判断依 journal 规则（分类板块）；改动文件名或位置时，先搜索旧引用的全部出现位置，逐一更新并确认无残留。

### 删除（条目退场）

退场语义依 journal 规则的删除约定执行；本技能不设删除协议、不预设删除语义，仅在规则沉默时提供安全缺省：将条目移入临时保存目录（与维护协议的红线口径一致——不真正删除文件），并同步更新 INDEX 中该条目的登记行或链接、修复指向该条目的引用（见「关联一致」；重点是带路径的链接，按名解析的链接确认仍可解析即可）。临时保存目录的名称与位置依 journal 规则；规则未定义类似设施时，与用户确认名称后在 `<journal-root>` 下创建（不存在则创建）。

---

## 如果你能够委派子代理

如果当前会话中主线话题仍在继续，
且你有能力委派子代理完成任务，
那么以下是一种建议的工作方式：

1. 直接将笔记写入一个临时目录
2. 委派子代理读取RULES.md并按照规范整理，如提炼tags、放置笔记、更新INDEX等

这样你就可以很快地继续工作，并且最小化对当前话题的干扰了。
