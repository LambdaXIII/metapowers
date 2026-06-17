# metapowers

> Agent 技能开发工坊 — 一套帮助 Agent 设计、测试、研究、蒸馏技能的通用 Skill。
> 基于 [skill-creator](https://github.com/anthropics/skill-creator) 标准，追加了严格的元数据、文档和通用性规范。

---

## 安装

每个 Skill 独立安装，按需取用：

```bash
npx skills add agent-prompt-design    # Agent 系统提示词设计方法论
npx skills add skill-quick-test       # 技能可用性快速测试
npx skills add skill-distillator      # 技能文档蒸馏
npx skills add web-deep-research      # 深度网络研究
npx skills add web-entity-search      # 快速实体搜索
```

或用通配符一次安装全部：

```bash
npx skills add metapowers/*
```

安装后 Agent 即可在对话中自动加载 — 无需手动 import 或配置。

---

## 技能

### agent-prompt-design

Agent 系统提示词设计方法论，覆盖结构设计、内容编写、工具协议、安全加固到运营管理。特色在于将安全视为设计起点而非部署终点，针对推理模型时代（2026）的专项策略，以及十大反模式诊断体系。

[:arrow_upper_right: 完整文档](skills/agent-prompt-design/SKILL.md) &nbsp;·&nbsp; [:page_facing_up: 设计说明](skills/agent-prompt-design/README.md)

---

### skill-quick-test

通过子代理并行推演快速验证技能可用性 — Agent 拿到 SKILL.md 后能否正确理解并走通流程。特点在于 ISTQB 六步测试设计、能力模拟（不实际执行外部调用）、以及严格的隔离铁律（子代理不知道预期效果）。

[:arrow_upper_right: 完整文档](skills/skill-quick-test/SKILL.md) &nbsp;·&nbsp; [:page_facing_up: 设计说明](skills/skill-quick-test/README.md)

---

### skill-distillator

将技能的"执行文档"（SKILL.md + references/）蒸馏为人类可读的"方法论文档"。五阶段转化流水线（理解 → 解构 → 编排 → 表达 → 质检），自动识别技能类型并适配转换策略，输出渐进式披露的多层文档结构。

[:arrow_upper_right: 完整文档](skills/skill-distillator/SKILL.md) &nbsp;·&nbsp; [:page_facing_up: 设计说明](skills/skill-distillator/README.md)

---

### web-deep-research

系统化深度网络研究 — 线索链追踪、按信息性质交叉比对（事实评置信度、知识做组合、意见析争议、数据追方法论），交付结论可由读者独立检验的研究报告。核心约束：收集与评估严格分离，先完整收集再统一判断，避免锚定效应。

[:arrow_upper_right: 完整文档](skills/web-deep-research/SKILL.md) &nbsp;·&nbsp; [:page_facing_up: 设计说明](skills/web-deep-research/README.md)

---

### web-entity-search

快速结构化实体搜索，填补"直接搜索"和"深度研究"之间的空白。消歧 → 分类 → 按维度模板填充 → 置信回检 → 输出，覆盖 7 种实体类型。核心纪律：≥ 2 个来源即停止，不蔓延为研究报告。

[:arrow_upper_right: 完整文档](skills/web-entity-search/SKILL.md) &nbsp;·&nbsp; [:page_facing_up: 设计说明](skills/web-entity-search/README.md)

---

## 设计哲学

### 通用性优先

metapowers 只收**通用** Skill — 换一个完全不同的项目、换一个 Agent 也能用。垂直领域、特定团队工作流、依赖专有工具的技能不适合这里。

### 独立运行，互相推荐

每个 Skill 自成一体：不依赖其他技能、不假设项目结构、不硬编码环境信息。技能之间只在 description 中互相推荐（如 web-entity-search 推荐 web-deep-research 处理更复杂的研究），但不会设计成硬性依赖。

### 三种文件，三种读者

| 文件 | 读者 | 内容 |
|---|---|---|
| `SKILL.md` | Agent | 指令：索引、流程、约束。按需加载 `references/`，复制使用 `templates/` |
| `README.md` | 人 | 设计锚定：为什么这样设计、关键取舍、维护注意事项。只在设计实质变化时才更新 |
| `CHANGELOG.md` | 人 & Agent | 每次迭代的变更记录，Keep a Changelog 格式 |

### 严格元数据

每个 Skill 的 frontmatter 必须包含 `metadata` 字段，记录 `version`、`last_updated`、`author`（均字符串）。这确保技能可追溯、可版本化管理。

---

## 贡献

1. **确认通用性** — 这个 Skill 换一个人、换一个项目还能用吗？
2. **遵循规范** — 按 [`AGENTS.md`](AGENTS.md) 中的额外要求构建 frontmatter、CHANGELOG 和 README
3. **独立提交** — 一次只改一个 Skill，不混合无关修改
4. **展示 diff** — 提交前让维护者看到完整变更
5. **先问再写** — 不确定是否适合收进来？开 Issue 讨论

---

## 许可

[MIT](LICENSE)
