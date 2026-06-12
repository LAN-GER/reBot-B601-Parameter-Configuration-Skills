# B601-RS Windows 初始化完整记录

> 本文档记录了 B601-RS 机械臂在 Windows 环境下的完整初始化操作流程。

---

## 一、环境准备

### 1.1 安装 motorbridge

```bash
C:\Users\<用户名>\AppData\Local\Programs\Python\Python312\python.exe -m pip install motorbridge
```

输出：
```
Successfully installed motorbridge-0.4.5
Scripts: motorbridge-cli.exe, motorbridge-gateway.exe
```

### 1.2 验证 CLI

```bash
"C:\Users\<用户名>\AppData\Local\Programs\Python\Python312\Scripts\motorbridge-cli.exe" --help
```

---

## 二、写入电机 ID（逐颗操作）

### 核心原则
- **每次只连接 1 颗电机**
- 7 颗电机目标 ID：1, 2, 3, 4, 5, 6, 7

### 扫描命令模板

```bash
# 扫描已设置范围
motorbridge-cli scan --vendor robstride --start-id 1 --end-id 7 --timeout-ms 300

# 扫描出厂默认范围
motorbridge-cli scan --vendor robstride --start-id 120 --end-id 127 --timeout-ms 300
```

### 修改 ID 命令模板

```bash
motorbridge-cli id-set --vendor robstride \
  --motor-id <旧ID> --new-motor-id <目标ID> \
  --feedback-id 0xFD --store 1 --verify 1 --timeout-ms 500
```

**注意**：`id-set` 可能返回 `store_parameters failed: response ack timeout`，但通常修改已成功。务必用 `scan` 验证。

### 验证命令模板

```bash
motorbridge-cli scan --vendor robstride --start-id <目标ID> --end-id <目标ID> --timeout-ms 500
```

### 最终验证（7 颗同时连接）

```bash
motorbridge-cli scan --vendor robstride --start-id 1 --end-id 7 --timeout-ms 500
```

预期输出：
```
[hit] probe=0x01 ... device_id=1 ...
[hit] probe=0x02 ... device_id=2 ...
[hit] probe=0x03 ... device_id=3 ...
[hit] probe=0x04 ... device_id=4 ...
[hit] probe=0x05 ... device_id=5 ...
[hit] probe=0x06 ... device_id=6 ...
[hit] probe=0x07 ... device_id=7 ...
scan done: 7 motor(s) found
```

---

## 三、校准零点

### 3.1 启动 Gateway

```bash
motorbridge-gateway --bind 127.0.0.1:9002
```

### 3.2 打开 Motorbridge Studio

浏览器访问：`http://127.0.0.1:9002`

### 3.3 配置参数

| 参数 | 值 |
|------|-----|
| Vendor | robstride |
| Channel | can0 |
| Model | rs-00 |
| Motor ID | 逐个选择 1~7 |
| Feedback ID | 0xFD |

### 3.4 设置零点步骤

1. 选择 Motor ID
2. 手动将对应关节摆到零点位置
3. 点击 **"Set Zero"**
4. 重复 7 次

**标准零点姿态**：
- J1 (底座): 朝前 0°
- J2 (大臂): 竖直向上 0°
- J3 (小臂): 与 J2 对齐 0°
- J4 (手腕旋转): 0°
- J5 (手腕俯仰): 0°
- J6 (手腕偏航): 0°
- J7 (夹爪): 按需

---

## 四、关闭 Gateway

```bash
ps | grep motorbridge-gateway
kill <pid>
```

---

## 五、故障排查

| 现象 | 原因 | 解决 |
|------|------|------|
| scan 无结果 | 电机未上电 | 确认 48V 电源 |
| scan 无结果 | CAN 线问题 | 检查 CAN_H、CAN_L |
| id-set 超时 | 通信不稳定 | scan 验证，通常已改好 |
| 多颗电机冲突 | 总线上有多颗 | 每次只接 1 颗 |
