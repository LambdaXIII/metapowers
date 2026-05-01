# cx-llm-prompt 技能文件清单

## 核心文件

| 文件 | 用途 |
|------|------|
| `SKILL.md` | 主技能文件，包含六步流程完整定义 |
| `DESIGN.md` | 设计规划文档，记录设计决策和原理 |
| `CHANGELOG.md` | 版本历史 |

## 参考资源

### frameworks/ - 框架定义
| 文件 | 内容 |
|------|------|
| `intro.md` | 四大框架选择指南 |
| `behavior-def.md` | 行为定义型框架详情 |
| `role-driven.md` | 角色驱动型框架详情 |
| `task-pipeline.md` | 任务流水线型框架详情 |
| `hybrid.md` | 混合架构型框架详情 |

### method-design/ - 方法设计
| 文件 | 内容 |
|------|------|
| `principles.md` | 方法设计原则（不预设解） |
| `examples.md` | 各领域方法设计示例 |

### techniques/ - 技巧指南
| 文件 | 内容 |
|------|------|
| `meta-cleaning.md` | 元信息清理指南 |
| `one-sentence.md` | 一句话定位公式 |

### diagnosis/ - 诊断方法
| 文件 | 内容 |
|------|------|
| `checklist.md` | 七维检查清单 |
| `deduction.md` | 推演验证方法 |

### examples/ - 测试案例
| 文件 | 内容 |
|------|------|
| `test-cases.md` | 6个测试案例 |

## 目录结构

```
cx-llm-prompt/
├── SKILL.md                      # 主文件（11KB）
├── DESIGN.md                     # 设计规划
├── CHANGELOG.md                  # 版本历史
├── README.md                     # 文件清单和说明
├── examples/                     # 测试案例
│   └── test-cases.md             # 6个测试案例
└── references/
    ├── frameworks/
    │   ├── intro.md              # 框架选择
    │   ├── behavior-def.md       # 行为定义型
    │   ├── role-driven.md        # 角色驱动型
    │   ├── task-pipeline.md      # 任务流水线型
    │   └── hybrid.md             # 混合架构型
    ├── method-design/
    │   ├── principles.md         # 方法设计原则
    │   └── examples.md           # 领域示例
    ├── techniques/
    │   ├── meta-cleaning.md      # 元信息清理
    │   └── one-sentence.md       # 一句话定位
    └── diagnosis/
        ├── checklist.md          # 七维检查
        └── deduction.md          # 推演验证
```

## 核心创新

1. **六步优先级流程**：0→1→2→3→4→5，终点决定输出
2. **不预设解原则**：步骤2根据领域设计方法，不套用模板
3. **自然判断**：步骤0根据上下文灵活判断意图
4. **综合诊断**：步骤4整合静态（七维）+ 动态（推演）
5. **方法设计原则**：必须回答"如何做"和"如何做好"

## 与现有技能对比

| 维度 | cx-prompt-engineering | cx-llm-prompt |
|------|----------------------|---------------|
| 组织方式 | 能力类型 | 流程步骤 |
| 用户交互 | 询问选择 | 自动决策 |
| "如何做" | 技巧模板 | 领域方法设计 |
| 框架选择 | 提供选项 | 直接推荐 |

## 使用方式

技能被加载后，自动：
1. 识别用户场景（创建/诊断/优化/咨询）
2. 从合适步骤切入
3. 按优先级执行流程
4. 交付结果

用户只需描述需求，无需了解技能内部结构。

## 状态

- **版本**：1.0.0
- **创建日期**：2026-04-01
- **状态**：已完成，待测试验证
