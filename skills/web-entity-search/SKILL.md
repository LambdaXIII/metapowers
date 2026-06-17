---
name: web-entity-search
description: >-
  Answer "what is X?" questions by searching the web for named entities.
  Use when the user asks about a specific person, organization, creative
  work, product, event, or concept — this provides a quick structured
  overview: more thorough than a bare search, far lighter than a research
  report.
version: "1.3.0"
last_updated: "2026-06-18"
author: "Ĉalio"
---

# Web Entity Search

回答"XXX 是什么"——通过网络搜索，给出一段有结构的、经过置信度检查的回答。
不是研究报告，不需要链式追踪。只是一个比直接搜索多了框架和纪律的薄层。

**核心流程：** 消歧 → 分类 → 按模板逐维填充 → 置信回检 → 按模板输出。

> **委派建议：** 本技能为简单结构化搜索，强烈建议委派子代理加载此技能独立执行——避免占用主代理上下文，也让搜索过程不被中断。话题通常自包含，极少依赖对话历史。
> 委派时只传任务描述，**不要**读取本技能文件后转述给子代理——让子代理自行加载技能并按 Skill 内的流程执行。

具体使用哪个搜索工具、如何提取网页内容，不在本技能范围内——本技能只负责"搜什么、搜多少、何时停、怎么呈现"。

## Content Index

| 实体类型 | 判断线索 | 参考文件（怎么搜） | 模板文件（怎么呈现） |
|---------|---------|-------------------|---------------------|
| 人物 | 搜索结果中有生卒日期、职业/身份 | `references/person.md` | `templates/person.md` |
| 公司/机构 | 搜索结果中有成立时间、行业归属、产品 | `references/company.md` | `templates/company.md` |
| 作品 | 搜索结果中有创作者、发行日期、类型标签 | `references/creative-work.md` | `templates/creative-work.md` |
| 产品/技术 | 搜索结果中有开发者、功能描述、版本 | `references/product-tech.md` | `templates/product-tech.md` |
| 事件 | 搜索结果中有发生时间地点、参与方 | `references/event.md` | `templates/event.md` |
| 概念/术语 | 搜索结果中有定义、领域归属、理论来源 | `references/concept-term.md` | `templates/concept-term.md` |
| 兜底 | 以上线索均不匹配，或实体横跨多类型 | `references/general.md` | `templates/general.md` |

- **references/** — 搜索指引、维度表（含必填/选填/关键标记）、避坑规则。Step 2 分类后加载，指导 Step 3 逐维填充
- **templates/** — 纯输出结构，带占位符。Step 5 加载，对着填空
- `references/workflow.md` — **完整 5 步流程**（消歧→分类→填充→回检→输出）。必读

## Instructions

1. 阅读 `references/workflow.md`，按 Step 1 → Step 5 执行
2. Step 2 分类后，对照 Content Index 加载对应的参考文件和模板文件

## Capability Boundaries

- **提供**：对单一命名实体的快速结构化搜索、关键维度覆盖、简易置信度检查
- **不提供**：链式线索追踪、多实体对比、争议深度分析——这些属于深度研究的范畴，超出本技能的边界
- **如果实体涉及高度争议的话题**：标注"存在争议"即可，不对争议各方做深入评估
