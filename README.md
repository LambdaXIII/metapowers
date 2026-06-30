[English](README.en.md) | 中文

# metapowers

[![License](https://img.shields.io/badge/license-MIT-blue)](LICENSE)

> Agent 技能开发工坊 —— 一套通用 Skill，以及产出这些 Skill 的工程规范。

---

## 目录

- [背景](#背景)
- [功能特性](#功能特性)
- [安装](#安装)
- [技能目录](#技能目录)
- [项目结构](#项目结构)
- [设计哲学](#设计哲学)
- [贡献](#贡献)
- [许可](#许可)

---

## 背景

AI Agent 通过「技能」（Skill）获取领域专长——一份 SKILL.md 文件 + 几个参考文档，就能让 Agent 掌握系统提示词设计、深度研究、知识蒸馏等能力。

但技能的质量参差不齐。有的技能写满设计者的内心独白而非可执行指令，有的技能改了几行错别字就升一个大版本，有的技能的设计意图散落在每次对话中无从追溯。

metapowers 解决这些问题——它提供一套经过验证的**通用技能**，以及一份让所有技能保持高质量的**工程规范**（[AGENTS.md](AGENTS.md)）。

---

## 功能特性

- **6 个生产级技能** —— 覆盖提示词设计、深度研究、知识蒸馏、技能测试、实体搜索、长期记忆
- **开发与发布分离** —— `dev/` 是工地，`skills/` 是展厅；设计文档不随技能分发
- **设计锚定制度** —— 每个技能一份 SKILL-DESIGN.md，记录设计意图和关键取舍，防止架构漂移
- **严格的文档纪律** —— 技能内容零歧义、自包含、不依赖会话上下文
- **版本号有标准** —— Patch/Minor/Major 三级判定，功能完成后再统一确定

---

## 安装

安装全套 metapowers 技能：

```bash
npx skills add LambdaXIII/metapowers
npx skills add LambdaXIII/metapowers -g # 推荐全局安装
```

也可按需安装单个技能：

```bash
npx skills add LambdaXIII/metapowers --skill agent-prompt-design
npx skills add LambdaXIII/metapowers --skill skill-quick-test
npx skills add LambdaXIII/metapowers --skill skill-distillator
npx skills add LambdaXIII/metapowers --skill web-deep-research
npx skills add LambdaXIII/metapowers --skill web-entity-search
npx skills add LambdaXIII/metapowers --skill journaling
```
---

## 技能目录

### agent-prompt-design

Agent 系统提示词设计方法论。覆盖结构设计、内容编写、工具协议、安全加固到运营管理。特色：安全视为设计起点；推理模型时代（2026）专项策略；十大反模式诊断体系。

### skill-quick-test

通过子代理并行推演快速验证技能可用性。ISTQB 六步测试设计 + 能力模拟 + 隔离铁律。

### skill-distillator

将技能的执行文档蒸馏为人类可读的方法论文档。五阶段转化流水线，自动识别技能类型并适配转换策略。

### web-deep-research

系统化深度网络研究。线索链追踪 + 按信息性质交叉比对（事实评置信度、知识做组合、意见析争议、数据追方法论）。

### web-entity-search

快速结构化实体搜索，填补直接搜索和深度研究之间的空白。覆盖 7 种实体类型，≥ 2 个来源即停止。

### journaling

Agent 长期记忆的笔记本系统。结构化笔记 + 维护协议 + 渐进式披露。Journal 服务于 Agent 自身。

---

## 项目结构

```
metapowers/
├── dev/                    # 开发空间
│   └── <skill-name>/
│       ├── content/        # 技能内容（= 发布包）
│       ├── SKILL-DESIGN.md # 设计锚定文档
│       ├── CHANGELOG.md    # 变更记录
│       ├── test-space/     # 测试用例
│       └── research/       # 参考资料
├── skills/                 # 发布目录
│   └── <skill-name>/       # 从 dev/<name>/content/ 复制
└── AGENTS.md               # 工程规范
```

---

## 设计哲学

**通用性优先** —— 只收换一个人、换一个项目也能用的通用技能。

**独立运行，互相推荐** —— 每个技能自成一体，技能之间只在 description 中互相推荐，不设计成硬性依赖。

**开发与发布分离** —— `dev/` 保存设计文档和变更记录，`skills/` 只发布干净的技能包。

**文档先于代码** —— 先写 SKILL-DESIGN.md 锚定设计方向，再写 content/ 内容。

---

## 贡献

1. **确认通用性** —— 这个技能换一个人、换一个项目还能用吗？
2. **遵循规范** —— 按 [AGENTS.md](AGENTS.md) 构建目录结构、frontmatter、SKILL-DESIGN 和 CHANGELOG
3. **独立提交** —— 一个功能分支对应一个逻辑变更
4. **展示 diff** —— 提交前让维护者看到完整变更
5. **先讨论再写** —— 不确定是否适合？开 Issue 讨论

---

## 许可

[MIT](LICENSE)

