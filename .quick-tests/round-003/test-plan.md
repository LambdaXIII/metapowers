# web-search-protocol Quick Test Plan

- **被测技能**: web-search-protocol（环境技能）
- **路径**: `C:\Users\Cxalio\AppData\Local\hermes\skills\research\web-search-protocol\`
- **版本**: 当前安装版本
- **模式**: Full（复杂场景 3 ≥ 2）
- **轮次**: round-003

---

## 范围摘要

- **功能域**: 5 项（搜索发现、三层内容提取、GitHub 专用通道、浏览器工具链、JSON 处理规范）
- **决策点**: 有（多层决策树：有URL? → 提取链选择 → fallback 路径）
- **边界**: curl 限用、Layer 不可跳跃、ddgs 降级、jq 强制

## 场景设计

### S01: 正门 + 精确 + 裸
- **使用场景**: 精确需求，裸上下文，正门进入
- **模拟背景**: 开发者知道 Python，需要了解 asyncio TaskGroup，不知道去哪找文档。第一次接触 web_search 工具。
- **入口路径**: `SKILL.md` — 正门
- **用户想达成**: "我需要了解 Python asyncio 的 TaskGroup 功能。我不知道应该去哪里找。"
- **预期效果**:
  - 预期路径: SKILL.md §1 决策树 → [需要信息] → 无URL → web_search → 选URL → 提取流程判断
  - 预期不会卡住: 决策树第一级分支清晰，应能顺利进入 web_search 步骤

### S02: 侧门 + 抽象 + 半知
- **使用场景**: 抽象需求，半知上下文，侧门进入
- **模拟背景**: Agent 曾用过这个技能，知道有国内网络实测数据，但不记得具体文件名。从 references 目录直接进入。
- **入口路径**: `references/web-backends-china.md` — 侧门
- **用户想达成**: "我记得这个技能有个关于国内网络访问的实测数据，帮我找到并确认哪些后端在国内可用。"
- **预期效果**:
  - 预期路径: 直接读取 web-backends-china.md → 发现 backends 表格 → 如果缺少上下文，需回链到 SKILL.md 获取完整后端列表
  - 预期不会卡住: 文件应独立可读，但可能需要回链

### S03: 回访 + 精确 + 全知
- **使用场景**: 精确需求，全知上下文，回访进入
- **模拟背景**: Agent 之前用过这个技能，知道有 design-journal.md，想回顾设计历史。
- **入口路径**: `references/design-journal.md` — 回访
- **用户想达成**: "打开这个技能的 design journal 看看。"
- **预期效果**:
  - 预期路径: 直接读取 design-journal.md → 应能独立理解内容 → 回链到 SKILL.md 获取上下文
  - 预期不会卡住: 文件应独立可读

## 测试单元

| 单元 | 场景 | 加载技能 | 报告文件 |
|------|------|---------|---------|
| S01-a | S01 | ✅ | reports/S01-a.md |
| S01-b | S01 | ❌ (baseline) | reports/S01-b.md |
| S02-a | S02 | ✅ | reports/S02-a.md |
| S02-b | S02 | ❌ (baseline) | reports/S02-b.md |
| S03-a | S03 | ✅ | reports/S03-a.md |
| S03-b | S03 | ❌ (baseline) | reports/S03-b.md |

## 简单测试（主代理验证）

| ID | 内容 | 方法 |
|----|------|------|
| B01 | curl 边界内：GitHub API rate limit 可用 curl | 检查 SKILL.md §6.3 表意一致 |
| B02 | curl 边界外：通用网页抓取被禁止 | 检查 §6.3 表意一致 |
| E01 | 交叉引用检查 | 验证 SKILL.md → references 链接有效 |

## 覆盖检查

| 维度 | 覆盖项 | ✅ |
|------|--------|---|
| 入口 | 正门 S01 / 侧门 S02 / 回访 S03 | ✅ |
| 明确度 | 精确 S01,S03 / 抽象 S02 | ✅ |
| 上下文 | 裸 S01 / 半知 S02 / 全知 S03 | ✅ |
| 边界 | B01, B02 | ✅ |
| 决策 | S01 覆盖主分支 | ✅ |
| baseline | 每场景 a/b | ✅ |
