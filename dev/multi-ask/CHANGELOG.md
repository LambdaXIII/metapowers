# Changelog

## 0.1.0

- SKILL.md：技能入口，只写是什么 / 为什么 / 怎么做——界定只装用户裁决物的边界，写明论述承担裁决所需的全部背景、问题块只问要裁决什么，题量由待决点决定，怎么做按情形路由到参考文档
- references/questionnaire-format.md：问卷格式契约——三种围栏与各自的题型语义、块与选项 id 规则、续行与并入、渲染边界，以及每条规则的失败形态
- references/script-usage.md：脚本用法——运行前提、三命令、阻塞等待与中断后果、页面快照、校验能查与不能查的、答卷结构与命名、拼装按路径配对、读答卷的处置
- references/organizing-questions.md：问题组织——先分拣哪些题进卷、什么算已定、每题之前论述写到什么程度、每题自成一体、依赖链拆批、篇幅取用
- references/writing-questions.md：单题写法——论述 / 题面 / 选项各管什么与作答自检、判断题须是命题、选项集合的闭包、单候选的两种收场、承重假设、选项写取舍
- examples/release-plan.md：示例问卷，每题之前带实质论述，示范多级章节、同章多题、mermaid 图、四种题型与推荐标记
- scripts/multi_ask.py：三命令 `validate` / `show` / `assemble`；校验覆盖围栏白名单与闭合、块与选项 id、题面与选项文本、单选项、yes-or-no 标签，错误一次列完并附修复指引，围栏名接近题型名时给拼写提示
- scripts/multi_ask.py：交互页按 markdown 渲染正文，问题块渲染为题面 + 控件 + 每题自由输入，推荐选项以固定宽度彩虹花纹标记（不预选、不入答卷），不显示任何 id；mermaid 块在浏览器端渲染为图，失败降级为源码
- scripts/multi_ask.py：左侧空白区按标题生成目录，点击跳转、滚动高亮当前一节，视口不足以容纳时隐藏
- scripts/multi_ask.py：答卷写为 `<问卷名>.answers.<YYYYMMDD-HHMMSS>[.NNN].json`（仅同秒重名时补三位序号），条目为 `block` / `selected` / `free`，`questionnaire` 记录问卷绝对路径，拼装按该路径查找并保留块内题面
- scripts/multi_ask.py：本地服务起在 `127.0.0.1` 随机端口，线程化处理连接；提交后页面原地切为已提交并禁用控件，不跳转、不自动关闭
- SPEC.md：技能设计规格——以单文件脚本为核心资产，问答的价值来自论述充分而非题量，入口只写是什么与参考路由，方法参考只给判断，操作文档写清边界与失败形态
- script-contract.md：脚本工件契约——DSL、校验清单、命令行、交互页与答卷 JSON、拼装格式、许可证登记
