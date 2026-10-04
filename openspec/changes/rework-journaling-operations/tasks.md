# Tasks

## 1. 非只读操作参考

- [x] 1.1 新建 `dev/journaling/content/references/protocal-operations.md`：概述（操作族定义——改变 journal 状态的操作：编写、收录、移动、删除等）、共享原则、族义务（读取并遵守 journal 规则，单处定义，含规则文档缺失时从种子补齐的语义）、各操作最小指引（编写 → 指向写入协议；收录 → 拷贝到对应位置再修改调整、避免手工抄写；移动 → 归属判断指向 journal 规则，改动文件名或位置时先搜索旧引用的全部出现位置；删除 → 退场语义指向 journal 规则的删除约定）、与维护协议的层级声明（维护执行期间维护协议的操作规范优先）
- [x] 1.2 内容定界自检：参考不展开操作步骤、不代述 journal 规则的具体语义、不重复写入协议流程，保持「最小指引 + 上游指向」

## 2. 收录并入写入

- [x] 2.1 删除 `dev/journaling/content/references/protocal-import.md`
- [x] 2.2 `protocal-write.md` 增补收录表述：现存文档收录 = 拷贝文件到 journal 对应位置再在其上修改调整（避免手工抄写），frontmatter、summary、链接、分类等加工与写入流程一致；「判断是否值得写」处补一句承接收录价值判断；第 2 步「读取 journal 规则」改为引用非只读操作参考的族义务
- [x] 2.3 grep 全库（`dev/journaling/content/`）清理 protocal-import 互引用（SKILL.md 的 Linked Files 与场景表、维护协议相关参考列表、design-discovery-contract、protocal-init、spec-note 等处），核对无残留

## 3. 维护触发专项化

- [x] 3.1 `protocal-maintenance.md` 开头触发表述改写：维护只由用户明确触发，是一个专项动作、建议在专门会话中执行；agent 不自行执行，必要时提醒用户触发（提醒内容以维护备忘为承接）；补充泛化阅读认可声明——非维护场景可读取本协议论述作为启发性参考，这不触发流程义务
- [x] 3.2 `SKILL.md` Operating Principles 自治原则收窄：自治域覆盖写入与用户引导下的操作，专项维护排除在外；目录重组、标签合并等示例表述与触发裁定对齐；删除处理条目对齐非只读操作参考的路由表述

## 4. SKILL.md 结构更新

- [x] 4.1 加载指引（协议表）重排：Init / Write / 非只读操作参考（一行，指名操作族并指引到共同论述）/ Maintenance，删除 Import 行
- [x] 4.2 Linked Files 更新：删除 protocal-import 条目，新增 protocal-operations 条目
- [x] 4.3 description 校对：触发动词面不变（创建、写入、编辑、移动、归档、删除等），确认与收录并入、操作参考建立后无冲突；frontmatter `last_updated` 更新，`version` 待功能完成后统一定

## 5. 标题命题建议

- [x] 5.1 `spec-note.md` 新增标题建议段（引导性）：标题组织为命题形式——交付这条笔记的判断，而不只是指示话题；附对比例（「苹果的颜色」指示话题 vs「苹果是红的」交付判断）；注明笔记本身不含命题时不适用

## 6. 发现合约融合

- [x] 6.1 `design-discovery-contract.md` Step 3 更新：模板更新——保留「会话开始时读取 INDEX」强制底线与跨宿主通用要素（journal-root 声明、定位立场、价值裁量、加载触发、操作边界、与其他记忆机制的分工），快照类机制表述以宿主适配说明取代硬编码；新增设计讲解——要素框架（立场、路由、规程不进注入）与写作原则（立场先于动作、机制适配），鼓励 agent 按宿主实际机制发挥
- [x] 6.2 权限原则落文：agent 对宿主提示词只能提案、提醒、编写草稿，写入或更改由用户执行或经用户批准
- [x] 6.3 `protocal-init.md` Phase 3：回退方案的模板文本与新模板同步；「合约已存在的情况」的评估判据从四维度比对升级为按要素框架的覆盖检查
- [x] 6.4 `design-discovery-contract.md`「已有合约的检测」节的四维度表同步升级为要素覆盖检查

## 7. 一致性收尾

- [x] 7.1 残留核查：protocal-import 引用清零；「收录 / importing」表述与新结构一致；技能内容内互引用无断链
- [x] 7.2 `dev/journaling/CHANGELOG.md` 置顶新增「未定版」节，按一句话体例逐条记录本次逻辑变更
- [x] 7.3 `openspec validate --all` 结构校验通过
