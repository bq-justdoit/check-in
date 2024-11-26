#!/usr/bin/env python
# -*- coding: utf-8 -*-


import serial

import time

# 配置串口参数

ser = serial.Serial(

    port='COM3',  # 替换为实际的串口名称 (例如 Linux 上为 '/dev/ttyS0')

    baudrate=9600,  # 波特率

    bytesize=serial.EIGHTBITS,  # 数据位

    parity=serial.PARITY_NONE,  # 校验位

    stopbits=serial.STOPBITS_ONE,  # 停止位

    timeout=1  # 读取超时时间 (秒)

)

# 检查串口是否打开

if ser.is_open:

    print(f"{ser.port} 已打开")

else:

    print(f"无法打开 {ser.port}")

# 写入数据

data_to_send = "Hello Serial"

ser.write(data_to_send.encode())  # 写入需要先编码为字节

# 读取数据

time.sleep(0.1)  # 等待数据准备好

if ser.in_waiting > 0:  # 检查是否有可读数据

    received_data = ser.read(ser.in_waiting).decode()  # 读取并解码

    print(f"接收到的数据: {received_data}")

# 关闭串口

ser.close()

import serial.tools.list_ports

ports = serial.tools.list_ports.comports()

for port in ports:
    print(f"设备: {port.device}, 描述: {port.description}")


import serial

# 配置串口参数
ser = serial.Serial(
    port='COM3',        # 替换为实际的串口名 (Linux 可用 '/dev/ttyUSB0')
    baudrate=115200,    # 波特率，需根据模组要求设置
    bytesize=serial.EIGHTBITS,  # 数据位
    parity=serial.PARITY_NONE,  # 校验位
    stopbits=serial.STOPBITS_ONE,  # 停止位
    timeout=1           # 读取超时时间
)

# 检查串口是否打开
if ser.is_open:
    print(f"{ser.port} 已成功打开")

# 向模组发送指令
command = "AT\r\n"  # 例如发送 AT 指令 (根据模组协议调整)
ser.write(command.encode())  # 编码为字节流

# 接收模组的响应
response = ser.read(100)  # 读取 100 字节数据，调整为需要的长度
print(f"模组响应: {response.decode()}")  # 解码为字符串

# 关闭串口
ser.close()

result = {
            "power_current".lower(): "",
            "power_average": "",
            "power_maximum": "",
            "power_minimum": "",
            "modulation_current": "",
            "modulation_average": "",
            "modulation_maximum": "",
            "modulation_minimum": "",
            "ibemask_current": "",
            "ibemask_average": "",
            "ibemask_maximum": "",
            "ibemask_minimum": "",
        }

"power_current".upper()
"power_current".lower()

with open('example.txt', 'r') as file:
    for line in file:
        print(line.strip())  # 去除换行符

with open('example.txt', 'r') as file:
    content = file.read()  # 读取所有内容为字符串


with open('example.txt', 'w') as file:
    file.write('This is a new file.')


with open('example.txt', 'a') as file:
    file.write('\nAppended content.')

with open('example.txt', 'r') as file:
    lines = file.readlines()  # 每一行作为列表的一个元素
    print(lines)


def output_HTML(self, result):
    test_case = result["test_case"]
    test_data = result["test_data"]
    test_time = result["test_time"]
    test_result = result["test_result"]

    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>{test_case}</title>
    </head>
    <body>
        <tr>
            <td>test_case: {test_case}<br></td>
            <td>test_data: {test_data}<br></td>
            <td>test_time: {test_time}<br></td>
            <td>test_result: {test_result}<br></td>
        </tr>
    </body>
    </html>
    """
    with open(dir + 'report.html', 'w') as report:
        report.write(html_content)

    return report
