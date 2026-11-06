# Changelog

## 未定版

- scripts/multi_ask.py：交互页左侧空白区新增标题目录，点击跳转并按滚动位置高亮，窄视口隐藏
- SKILL.md：定位改为「从容、详细的批量问答」，description、是什么、为什么重写；论述与题面的分工写进入口，题量改为由待决点决定
- references/organizing-questions.md：主线改为「论述写足」，新增「每题自成一体」「篇幅」两节，删去以压缩为导向的表述
- references/writing-questions.md：开篇补论述 / 题面 / 选项的分工与自检
- SPEC.md：新增「问答的价值来自论述充分，而不是题量」
- examples/release-plan.md：每题之前补齐实质论述，并声明本卷示范的内容
- SKILL.md：重写为「是什么 / 为什么 / 怎么做」三节，「怎么做」改为按情形指向参考文档的路由并给出阅读顺序；description 补回读触发，正文写明脚本与用户同机的前提
- references/writing-questions.md、organizing-questions.md：补「论述 / 题面 / 选项」的分工与自检，删去「论述越长判断越差」这类与写足论述相抵的表述
- references/questionnaire-format.md：新增问卷格式契约——围栏与题型、id 规则、续行与并入规则、渲染边界、拼错围栏的后果、yes-or-no 标签方向
- references/script-usage.md：新增脚本用法——运行前提、五步流程、三命令、答卷结构、assemble 配对契约、读答卷的处置准则
- references/organizing-questions.md：新增组织方法——分拣哪些题进卷、什么算已定、依赖链拆批、背景粒度、长卷版式
- references/writing-questions.md：新增单题写法——判断题命题、选项集合、单候选、承重假设、选项写法
- examples/release-plan.md：新增示例问卷，替换 skill-design-discussion.md（后者把技能自身已定的设计当作待决问题）；每题前有实质论述，覆盖多级章节、同章多题、mermaid、四种题型与推荐标记
- scripts/multi_ask.py：推荐选项的彩虹改为固定宽度循环花纹（`background-size: 240px` 平铺），此前渐变按元素宽度铺开、文字只取到第一段橙色
- scripts/multi_ask.py：答卷文件命名改为「问卷名 + 提交时间点」，同名时才追加三位序号并按同名文件名累积（`<问卷名>.answers.<YYYYMMDD-HHMMSS>[.NNN].json`）
- scripts/multi_ask.py：围栏未闭合改为校验错误（原为静默截断后文）；非白名单围栏名接近题型名时给出拼写提示
- SPEC.md：正文组织改为入口路由；方法参考只给判断不立细则；新增操作文档写清边界与失败形态
- script-contract.md：同步校验清单（围栏闭合、围栏名提示）、yes-or-no 计数措辞、SKILL.md 要点与 license 登记

## 0.1.0

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
