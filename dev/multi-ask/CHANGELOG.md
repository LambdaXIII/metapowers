# Changelog

## 未定版

- 初始化技能开发框架（dev/multi-ask/ 目录、CHANGELOG、SPEC）
- SPEC.md：新增技能设计规格
- script-contract.md：新增脚本工件契约（DSL、校验清单、命令行、答卷 JSON、拼装格式）
- SKILL.md：新增技能入口、脚本用法与出题纪律
- scripts/multi_ask.py：新增问卷校验、交互收卷、拼装脚本（validate / show / assemble）
- scripts/multi_ask.py：问卷 DSL 采用 Markdown 列表式——`single-choice` / `multi-choice` / `yes-or-no` 围栏，块首行 `<id> 题面`，选项 `- [ ] <选项id> 文本`，`- [x]` 仅标记推荐
- scripts/multi_ask.py：校验覆盖围栏白名单、块与选项 id、题面、选项行与文本、单选项、yes-or-no 标签，错误一次列完并附修复指引
- scripts/multi_ask.py：答卷条目字段为 `block` / `selected` / `free`，不回显题干；`questionnaire` 记录问卷绝对路径，拼装按路径查找；拼装保留块内题面
- scripts/multi_ask.py：交互页不显示任何 id；每题恒定自由输入，卷末总评以分隔线 + 单句提示呈现
- scripts/multi_ask.py：推荐选项以彩虹文字标记（不预选、不入答卷）；选项行字号、行高与间距对齐正文列表并同线缩进
- scripts/multi_ask.py：交互页暖纸朱砂视觉，问题与选项去卡片框、按正文流式排布
- scripts/multi_ask.py：mermaid fenced 块渲染为图（浏览器端加载渲染器，失败降级为源码文本）
- scripts/multi_ask.py：本地服务线程化，浏览器空闲连接不再阻塞页面加载
- examples/skill-design-discussion.md：新增示例问卷（章节与问题交错、同章节多题、单选/多选/判断/开放题与推荐标记）
