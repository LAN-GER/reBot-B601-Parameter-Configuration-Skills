---
name: rebot-b601-rs-init
description: >
  Windows 环境下 reBot Arm B601-RS 机械臂初始化全流程 Skill。
  覆盖：PCAN-USB 驱动安装、motorbridge 工具安装、7 颗 Robostride 电机 ID 写入（1~7）、
  Motorbridge Studio 零点校准、Gateway 启停管理。
  触发场景：用户在 Windows 系统上配置 B601-RS 机械臂、
  写入电机 ID、校准零点、初始化新机械臂、设置 Robostride 电机参数。
  关键词：B601-RS、reBot Arm、机械臂初始化、电机 ID、零点校准、
  motorbridge、Robostride、Windows、PCAN-USB、PEAK-System。
---

# reBot B601-RS 初始化 Skill（Windows）

> 本 Skill 适用于 **Windows 系统** 下的 **reBot Arm B601-RS** 机械臂初始化。
> 电机类型：Robostride（RS-00 / RS-06）
> 通信方式：PCAN-USB 转接板（CAN @ 1 Mbps）

## 环境前提

- Windows 10/11
- Python 3.10+（已安装，路径通常为 `C:\Users\<用户名>\AppData\Local\Programs\Python\Python312\`）
- PCAN-USB 转接板已插入
- 机械臂 48V 电源

## 核心流程概览

| 步骤 | 内容 | 关键命令/操作 |
|------|------|--------------|
| 0 | 安装 PCAN-USB 驱动 | 运行 `scripts/download_pcan_driver.py` |
| 1 | 安装 motorbridge | `python -m pip install motorbridge` |
| 2 | 写入电机 ID（1~7）| `motorbridge-cli scan` + `motorbridge-cli id-set` |
| 3 | 校准零点 | 启动 Gateway + Motorbridge Studio 网页 |
| 4 | 关闭 Gateway | `kill <pid>` 或任务管理器 |

**重要原则**：写入 ID 时，每次只连接 **1 颗电机** 到 CAN 总线。

## 详细操作

### Step 0 — 安装 PCAN-USB 驱动

PCAN-USB 转接板需要 PEAK-System 官方驱动才能在 Windows 上正常工作。

#### 自动下载（推荐）

```bash
# 运行 Skill 自带的下载脚本
python scripts/download_pcan_driver.py
```

脚本行为：
1. 尝试从 PEAK-System 官网自动下载驱动安装包
2. 如果自动下载失败，自动打开浏览器跳转到下载页面
3. 提示用户手动下载并安装

#### 手动下载

如果自动下载失败，请访问：
```
https://www.peak-system.com/products/hardware/external-pc-interfaces/pcan-usb/
```

找到 **"Device driver setup 5.x for Windows"**，点击 **Download** 按钮下载。

#### 安装驱动

1. 运行下载的 `.exe` 安装包
2. 按向导完成安装（默认选项即可）
3. 将 PCAN-USB 转接板插入电脑 USB 口
4. 打开 **设备管理器**，确认出现 **"PCAN-USB"** 设备且无黄色感叹号

### Step 1 — 安装 motorbridge

```bash
# 使用已安装的 Python 执行
C:\Users\<用户名>\AppData\Local\Programs\Python\Python312\python.exe -m pip install motorbridge
```

安装后 CLI 工具位置：
```
C:\Users\<用户名>\AppData\Local\Programs\Python\Python312\Scripts\motorbridge-cli.exe
C:\Users\<用户名>\AppData\Local\Programs\Python\Python312\Scripts\motorbridge-gateway.exe
```

验证安装：
```bash
motorbridge-cli.exe --help
```

### Step 2 — 写入电机 ID（逐颗操作）

**每次只连接 1 颗电机**，重复以下流程 7 次：

#### 2.1 扫描当前电机 ID

```bash
# 扫描 ID 1~7（已设置范围）
motorbridge-cli scan --vendor robstride --start-id 1 --end-id 7 --timeout-ms 300

# 扫描 ID 120~127（出厂默认范围）
motorbridge-cli scan --vendor robstride --start-id 120 --end-id 127 --timeout-ms 300
```

#### 2.2 修改电机 ID（如需要）

```bash
motorbridge-cli id-set --vendor robstride \
  --motor-id <旧ID> --new-motor-id <目标ID> \
  --feedback-id 0xFD --store 1 --verify 1 --timeout-ms 500
```

**目标 ID 映射**：
| 关节 | 目标 ID |
|------|---------|
| J1 (底座) | 1 |
| J2 (大臂) | 2 |
| J3 (小臂) | 3 |
| J4 (手腕旋转) | 4 |
| J5 (手腕俯仰) | 5 |
| J6 (手腕偏航) | 6 |
| J7 (夹爪) | 7 |

#### 2.3 验证修改

```bash
motorbridge-cli scan --vendor robstride --start-id <目标ID> --end-id <目标ID> --timeout-ms 500
```

#### 2.4 断开当前电机，连接下一颗

重复直到 7 颗全部完成。

#### 2.5 最终验证（7 颗同时连接）

```bash
motorbridge-cli scan --vendor robstride --start-id 1 --end-id 7 --timeout-ms 500
```

预期结果：`7 motor(s) found`，ID 1~7 全部命中。

### Step 3 — 校准零点

#### 3.1 启动 Gateway

```bash
motorbridge-gateway --bind 127.0.0.1:9002
```

#### 3.2 打开 Motorbridge Studio

浏览器访问：`http://127.0.0.1:9002`

#### 3.3 配置参数

| 参数 | 值 |
|------|-----|
| Vendor | robstride |
| Channel | can0 |
| Model | rs-00 |
| Motor ID | 逐个选择 1~7 |
| Feedback ID | 0xFD |

#### 3.4 逐个设置零点

1. 选择 Motor ID = 1
2. 手动将 J1 关节摆到**零点位置**
3. 点击 **"Set Zero"**
4. 依次对 ID 2~7 重复

**标准零点姿态**：
- J1: 朝前（0°）
- J2: 竖直向上（0°）
- J3: 与 J2 对齐（0°）
- J4~J6: 0°
- J7: 按需

### Step 4 — 关闭 Gateway

```bash
# 查找进程
ps | grep motorbridge-gateway

# 终止
kill <pid>
```

或在 Windows 任务管理器中结束 `motorbridge-gateway.exe`。

## 故障排查

| 现象 | 原因 | 解决 |
|------|------|------|
| scan 无结果 | 电机未上电 | 确认 48V 电源开启 |
| scan 无结果 | CAN 线松动/接反 | 检查 CAN_H、CAN_L |
| scan 无结果 | PCAN-USB 驱动未安装 | 运行驱动下载脚本或手动安装 |
| id-set 超时 | 通信不稳定 | 重试 scan 验证，通常已修改成功 |
| 多颗电机同时扫描冲突 | 总线上有多颗电机 | 每次只接 1 颗 |

## 参考文档

- 完整对话记录与命令示例：见 `references/windows-init-full-log.md`
- motorbridge CLI 详细参数：见 `references/motorbridge-cli-reference.md`

## 相关仓库

- 控制代码：`https://github.com/vectorBH6/reBotArm_control_py`（develop-rs 分支）
- 本 Skill 仓库：`https://github.com/LAN-GER/reBot-B601-Parameter-Configuration-Skills`
