# 母带车间（Mastering Workshop）

## 概述
母带车间根据混音分轨文件（MTR）进行最终母带处理，输出母带文件（MST）。

## 输入
- 混音分轨文件（来自混音车间 — `mixing.md`）
- 母带参考标准
- 交付规格要求

## 处理流程
1. 导入MTR分轨文件
2. 均衡处理：频率调整
3. 动态处理：压缩和限制
4. 立体声增强
5. 输出最终母带

## 输出

### 母带文件（MST / Master Stereo Track）
**文件命名：** `[PID]_MST_[VER].[ext]`
**格式：** 24bit/48kHz WAV，参考通用参考文档的格式规范

示例输出文件：
- `PRJ001_MST_v01.wav`
- `PRJ001_MST_v02.wav`

### 输出存放位置
`./outputs/mastering/[PID]_MST_[VER].wav`

## 参考
- 通用参考文档 — 整体参考

## 下游车间
- 交付车间：使用MST文件进行最终交付
