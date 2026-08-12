# Triage Labels

技能以五个 triage 角色表达，本文件将这些角色映射到本仓库 GitHub tracker 实际使用的标签串。

| 技能角色 | 本仓库标签 | 含义 |
| --- | --- | --- |
| `needs-triage` | `needs-triage` | 待维护者评估（新提交默认，含外部反馈入口） |
| `needs-info` | `needs-info` | 等待提交者补充信息（外部反馈信息不足时） |
| `ready-for-agent` | `ready-for-agent` | 已完整描述，可委托 agent 处理 |
| `ready-for-human` | `ready-for-human` | 需人工决策/实现 |
| `wontfix` | `wontfix` | 不做处理 |

本仓库用法：issue 双通道（内部当场提交 + 外部用户反馈）。新 issue 默认 `needs-triage`；维护者评估后转 `ready-for-human`（需用户拍板）或 `ready-for-agent`（可委托）；信息不足标 `needs-info`；不处理标 `wontfix`。
