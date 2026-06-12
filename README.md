# reBot B601 Parameter Configuration Skills

> **Kimi / AI Agent Skills for reBot Arm B601 Series Parameter Configuration**
>
> 适用于 Windows 环境下 reBot Arm B601-RS / B601-DM 机械臂的参数配置与初始化。

---

## 中文

本仓库收集并维护用于 **reBot Arm B601 系列机械臂** 参数配置的 [Kimi Skills](https://github.com/LAN-GER/reBot-B601-Parameter-Configuration-Skills)。

这些 Skill 为 AI Agent 提供结构化的初始化流程，覆盖电机 ID 写入、零点校准、环境配置等关键步骤。

### 支持的机械臂型号

| 型号 | 电机类型 | 状态 |
|------|---------|------|
| B601-RS | Robostride (RS-00 / RS-06) | ✅ 已支持 |
| B601-DM | Damiao (DM4310 / DM4340) | ⏳ 待添加 |

### Skill 列表

| Skill 名称 | 说明 | 路径 |
|-----------|------|------|
| `rebot-b601-rs-init` | B601-RS Windows 初始化全流程 | [`rebot-b601-rs-init/`](rebot-b601-rs-init/) |

### 使用方式

#### 方式一：Kimi Code CLI（推荐）

```bash
# 克隆本仓库
git clone https://github.com/LAN-GER/reBot-B601-Parameter-Configuration-Skills.git

# 启动 Kimi 时指定 skills 目录
kimi --skills-dir ./reBot-B601-Parameter-Configuration-Skills
```

#### 方式二：Kimi Desktop / Daimon

将本仓库目录配置为 Kimi 的 skills 根目录，Agent 会自动识别并加载其中的 Skill。

### 目录结构

```
reBot-B601-Parameter-Configuration-Skills/
├── README.md                              # 本文件
└── rebot-b601-rs-init/                    # B601-RS 初始化 Skill
    ├── SKILL.md                           # 核心流程文档
    └── references/                        # 参考文档
        ├── windows-init-full-log.md       # 完整操作记录
        └── motorbridge-cli-reference.md   # CLI 参数速查
```

### 相关资源

- **控制代码仓库**: [vectorBH6/reBotArm_control_py](https://github.com/vectorBH6/reBotArm_control_py)（`develop-rs` 分支）
- **官方文档**: [Seeed Studio Wiki](https://wiki.seeedstudio.com/cn/rebot_arm_b601_rs_pinocchio_meshcat/)
- **motorbridge SDK**: [motorbridge/motorbridge](https://github.com/motorbridge/motorbridge)

### 贡献

欢迎提交 Issue 或 PR 补充更多 Skill：
- B601-DM 初始化 Skill
- Linux 环境初始化 Skill
- 高级调试与诊断 Skill

---

## English

This repository collects and maintains [Kimi Skills](https://github.com/LAN-GER/reBot-B601-Parameter-Configuration-Skills) for **reBot Arm B601 Series** robotic arm parameter configuration.

These Skills provide AI Agents with structured initialization workflows, covering motor ID assignment, zero-point calibration, environment setup, and more.

### Supported Arm Models

| Model | Motor Type | Status |
|-------|-----------|--------|
| B601-RS | Robostride (RS-00 / RS-06) | ✅ Supported |
| B601-DM | Damiao (DM4310 / DM4340) | ⏳ Pending |

### Skill List

| Skill Name | Description | Path |
|-----------|-------------|------|
| `rebot-b601-rs-init` | B601-RS Windows initialization full workflow | [`rebot-b601-rs-init/`](rebot-b601-rs-init/) |

### Usage

#### Option 1: Kimi Code CLI (Recommended)

```bash
# Clone this repository
git clone https://github.com/LAN-GER/reBot-B601-Parameter-Configuration-Skills.git

# Launch Kimi with skills directory
kimi --skills-dir ./reBot-B601-Parameter-Configuration-Skills
```

#### Option 2: Kimi Desktop / Daimon

Set this repository directory as Kimi's skills root directory. The Agent will automatically discover and load Skills from it.

### Directory Structure

```
reBot-B601-Parameter-Configuration-Skills/
├── README.md                              # This file
└── rebot-b601-rs-init/                    # B601-RS initialization Skill
    ├── SKILL.md                           # Core workflow document
    └── references/                        # Reference documents
        ├── windows-init-full-log.md       # Complete operation log
        └── motorbridge-cli-reference.md   # CLI parameter quick reference
```

### Related Resources

- **Control Code Repo**: [vectorBH6/reBotArm_control_py](https://github.com/vectorBH6/reBotArm_control_py) (`develop-rs` branch)
- **Official Documentation**: [Seeed Studio Wiki](https://wiki.seeedstudio.com/cn/rebot_arm_b601_rs_pinocchio_meshcat/)
- **motorbridge SDK**: [motorbridge/motorbridge](https://github.com/motorbridge/motorbridge)

### Contributing

Issues and PRs welcome for additional Skills:
- B601-DM initialization Skill
- Linux environment initialization Skill
- Advanced debugging & diagnostics Skill

---

## License

MIT License
