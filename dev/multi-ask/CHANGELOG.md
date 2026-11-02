# Changelog

## 未定版

- 初始化技能开发框架（dev/multi-ask/ 目录、CHANGELOG、SPEC）
- SPEC.md：新增技能设计规格
- script-contract.md：新增脚本工件契约（DSL、校验清单、命令行、答卷 JSON、拼装格式）
- scripts/multi_ask.py：新增问卷校验、交互收卷、拼装脚本（validate / show / assemble）
- scripts/multi_ask.py：交互页与拼装答卷不再向用户显示任何 id
- scripts/multi_ask.py：选项行新增 `[x] ` 推荐标记（推荐≠预选，交互页显推荐签但不预勾，推荐不入答卷）
- scripts/multi_ask.py：推荐标识改为选项文字彩虹渐变（移除五角星装饰与随机渲染）；内容宽度 +50%，提交条压至 1/3 高且按钮与内容同宽
- scripts/multi_ask.py：交互页排版收紧（正文 15.5px/1.7、标题与段落间距压缩），问题与选项去掉卡片框、按正文流式排布
- scripts/multi_ask.py：mermaid fenced 块在交互页渲染为图（浏览器端加载渲染器，失败降级为源码文本）；script-contract.md、SKILL.md 同步该渲染约定
- script-contract.md、SKILL.md：明确题面与问题块不承担文档结构，章节须在正文中以真正的标题建立
- scripts/multi_ask.py：卷末总评区改为分隔线 + 单句提示，移除「总评」标签与冗长占位文案
- scripts/multi_ask.py：选项行字号、行高与间距对齐正文列表，只保留可点击与悬停反馈
- scripts/multi_ask.py：问题块（选项与自由输入）左缩进 1.5rem，与正文列表同线
- scripts/multi_ask.py：本地服务改用 ThreadingHTTPServer，避免浏览器空闲连接阻塞页面加载
- examples/skill-design-discussion.md：新增示例问卷（章节与问题交错、同章节多题、单选/多选/判断/开放题与推荐标记）
- scripts/multi_ask.py：交互页视觉重做为暖纸朱砂样式
- SKILL.md：新增技能入口与脚本使用说明
- SKILL.md、script-contract.md：拼装答卷格式同步去除 id 标记，id 可见性约束入契约
