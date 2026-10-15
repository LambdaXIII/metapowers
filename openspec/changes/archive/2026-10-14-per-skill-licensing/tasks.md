# Tasks

## 1. 吊销全局许可证声明

- [x] 1.1 删除根目录 `LICENSE` 文件
- [x] 1.2 README.md：移除 MIT 徽章，「许可」节改写为「许可证因技能而异，见各技能 SKILL.md 中的 `license` 标注；仓库其他内容（规格、开发文档等）保留所有权利」
- [x] 1.3 README.en.md：同步改写英文版徽章与 License 节，措辞与 1.2 对应

## 2. 各技能 license 字段（dev 侧）

- [x] 2.1 journaling：顶层新增 `license: "CC-BY-NC-SA-4.0"`
- [x] 2.2 rehearsal：顶层 `license` 由 `"MIT"` 改为 `"CC-BY-NC-SA-4.0"`
- [x] 2.3 skill-master：顶层 `license` 由 `"MIT"` 改为 `"CC-BY-NC-SA-4.0"`
- [x] 2.4 agent-prompt-design：顶层新增 `license: "MIT"`
- [x] 2.5 web-deep-research：顶层新增 `license: "MIT"`
- [x] 2.6 web-entity-search：顶层新增 `license: "MIT"`
- [x] 2.7 skill-exposition：确认现值 `"MIT"` 与登记一致，不改动

## 3. 版本递增与 CHANGELOG（dev 侧）

- [x] 3.1 五个受影响技能 metadata.version 各递增 patch 并将 last_updated 置为 "2026-10-14"：journaling 5.1.0→5.1.1、rehearsal 2.2.0→2.2.1、agent-prompt-design 1.0.4→1.0.5、web-deep-research 2.5.1→2.5.2、web-entity-search 1.3.2→1.3.3（skill-exposition 无变更、skill-master 未发布，均不动）
- [x] 3.2 五个 CHANGELOG 各加对应新版本节，含一条 license 字段变更（新增/变更，一句话写清对象与变更），版本节按降序置顶

## 4. 规格折回与验证

- [x] 4.1 `openspec validate --all` 通过
- [x] 4.2 折回主树：licensing 新能力落 `openspec/specs/licensing/`，skill-package MODIFIED 折回 `openspec/specs/skill-package/spec.md`
- [x] 4.3 冒烟核对：逐一检查 7 个 dev 侧 SKILL.md 顶层 license 字段与 licensing 规格登记表一致；根目录无 LICENSE；两份 README 无 MIT 徽章与仓库级许可背书
