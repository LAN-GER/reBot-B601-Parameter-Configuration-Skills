# motorbridge-cli 参数速查

## scan

```bash
motorbridge-cli scan [options]
```

| 参数 | 说明 | 示例 |
|------|------|------|
| `--vendor` | 电机品牌：`robstride`, `damiao`, `all` | `--vendor robstride` |
| `--start-id` | 起始 ID（十进制或十六进制） | `--start-id 1` 或 `--start-id 0x01` |
| `--end-id` | 结束 ID | `--end-id 7` |
| `--timeout-ms` | 超时毫秒 | `--timeout-ms 300` |
| `--channel` | CAN 通道 | `--channel can0` |
| `--feedback-ids` | Robostride host ID 候选 | `--feedback-ids 0xFD` |

## id-set

```bash
motorbridge-cli id-set [options]
```

| 参数 | 说明 | 示例 |
|------|------|------|
| `--vendor` | 电机品牌 | `--vendor robstride` |
| `--motor-id` | 当前电机 ID | `--motor-id 127` |
| `--new-motor-id` | 目标电机 ID | `--new-motor-id 7` |
| `--feedback-id` | Host/反馈 ID | `--feedback-id 0xFD` |
| `--store` | 是否持久化（1/0） | `--store 1` |
| `--verify` | 是否验证（1/0） | `--verify 1` |
| `--timeout-ms` | 超时毫秒 | `--timeout-ms 500` |

## id-dump

> **注意**：当前仅支持 Damiao 电机。Robostride 请使用 `scan` 代替。

```bash
motorbridge-cli id-dump --vendor damiao --motor-id <ID>
```

## run

发送控制指令（默认命令）。

```bash
# Robostride MIT 模式
motorbridge-cli run --vendor robstride --motor-id 1 --pos 0.0 --vel 0.0 --kp 0.0 --kd 0.0 --tau 0.0

# Robostride POS_VEL 模式
motorbridge-cli run --vendor robstride --motor-id 1 --pos 0.0 --vlim 1.0
```

## 常用组合

### 扫描单颗电机
```bash
motorbridge-cli scan --vendor robstride --start-id 5 --end-id 5 --timeout-ms 500
```

### 修改并验证
```bash
motorbridge-cli id-set --vendor robstride --motor-id 127 --new-motor-id 7 --feedback-id 0xFD --store 1 --verify 1 --timeout-ms 500
motorbridge-cli scan --vendor robstride --start-id 7 --end-id 7 --timeout-ms 500
```
