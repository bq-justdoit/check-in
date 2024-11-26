#!/usr/bin/env python
# -*- coding: utf-8 -*-

import serial
import serial.tools.list_ports

class serial_handler():
    def __init__(self):
        pass

    def search(self):
        ports = serial.tools.list_ports.comports()
        for port in ports:
            print(f"设备: {port.device}, 描述: {port.description}")
    def open(self,com_config):
        port=com_config["port"]
        baudrate=com_config["baudrate"]
        bytesize=com_config["bytesize"]
        patiry=com_config["patiry"]
        stopbits=com_config["stopbits"]
        timeout=com_config["timeout"]

        self.ser=serial.Serial(
            port=port,# 替换为实际的串口号 (Linux 可用 '/dev/ttyUSB0')
            baudrate=baudrate,# 波特率
            bytesize=bytesize,# 数据位 (默认 8 位)
            patiry=patiry,# 校验位 (无校验)
            stopbits=stopbits,# 停止位 (1 位)
            timeout=timeout,#超过时间（秒）
            # baudrate=baudrate, # 波特率
            # bytesize=serial.EIGHTBITS,# 数据位 (默认 8 位)
            # patiry=serial.PARITY_NONE,# 校验位 (无校验)
            # stopbits=serial.STOPBITS_ONE,# 停止位 (1 位)
            # timeout=1 #超过时间（秒）
        )

    def is_open(self):
        if self.ser.is_open:
            print(f"串口{self.ser.port}已打开")
        else:
            print(f"无法打开串口{self.ser.port}")

    def write(self,command):
        command=command
        self.ser.write(command.encode())

    def receiver(self):
        response = self.ser.read(100)  # 读取 100 字节数据，调整为需要的长度
        print(f"模组响应: {response.decode()}")  # 解码为字符串

    def close(self):
        self.ser.close()


serial_handler=serial_handler()