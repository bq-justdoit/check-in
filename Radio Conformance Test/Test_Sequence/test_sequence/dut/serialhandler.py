#!/usr/bin/env python
# -*- coding: utf-8 -*-

import serial
import serial.tools.list_ports

class serial_handler():
    def __init__(self):
        self.state=0

    def search(self):
        ports = serial.tools.list_ports.comports()
        for port in ports:
            print(f"设备: {port.device}, 描述: {port.description}")
    def open(self,com_config):
        # port=com_config["port","com57"]
        # baudrate=com_config["baudrate",]
        # bytesize=com_config["bytesize"]
        # parity=com_config["parity"]
        # stopbits=com_config["stopbits"]
        # timeout=com_config["timeout"]
        # port=com_config.get("port","COM57")
        # baudrate=com_config.get("baudrate","115200")
        # bytesize=com_config.get("bytesize","EIGHTBITS")
        # parity=com_config.get("parity","PARITY_NONE")
        # stopbits=com_config.get("stopbits","STOPBITS_ONE")
        # timeout=com_config.get("timeout",1)

        port=com_config.get("port","COM57")
        # baudrate=com_config.get("baudrate","115200")
        # bytesize=com_config.get("bytesize",serial.EIGHTBITS)
        # parity=com_config.get("parity",serial.PARITY_NONE)
        # stopbits=com_config.get("stopbits",serial.STOPBITS_ONE)
        # timeout=com_config.get("timeout",1)

        try:
            self.ser=serial.Serial(
                port=port,# 替换为实际的串口号 (Linux 可用 '/dev/ttyUSB0')
                baudrate=115200,# 波特率
                # bytesize=bytesize,# 数据位 (默认 8 位)
                # patiry=patiry,# 校验位 (无校验)
                # stopbits=stopbits,# 停止位 (1 位)
                # timeout=timeout,#超过时间（秒）
                # baudrate=baudrate, # 波特率
                bytesize=serial.EIGHTBITS,# 数据位 (默认 8 位)
                parity=serial.PARITY_NONE,# 校验位 (无校验)
                stopbits=serial.STOPBITS_ONE,# 停止位 (1 位)
                timeout=1 #超过时间（秒）
            )
            self.state=1
            print("已连接串口")
        except Exception:
            print("未连接串口")


    def is_open(self):
        if self.state:
            if self.ser.is_open:
                print("="*20+"\n")
                print(f"串口{self.ser.port}已打开")
                return self.state
            else:
                print(f"无法打开串口{self.ser.port}")
                return None
        else:
            print("未连接串口")
            return self.state

    def write(self,command):
        if self.state:
            command=command
            self.ser.write(command.encode())
            print(f"发送成功command：{command}")
        else:
            print("未连接串口,无法发送命令")
            return None

    def receiver(self):
        if self.state:
            # response = self.ser.read(100)  # 读取 100 字节数据，调整为需要的长度
            # response_dut=response.decode()
            # print(f"模组响应: {response_dut}")  # 解码为字符串
            response2_dut=""
            try:

                while True:
                    if self.ser.in_waiting:  # 检查是否有数据可读
                        data = self.ser.read(self.ser.in_waiting)  # 读取全部可用数据
                        response2_dut=response2_dut+data.decode()+"\r"
                        print(f"接收到的数据: {data.decode('utf-8')}")
                    else:
                        break
                # return response_dut
            except KeyboardInterrupt:
                print("监听结束")
            return response2_dut

        else:
            print("未连接串口,无法读取数据")
            return None

    def close(self):
        if self.state:
            self.ser.close()
            print("="*20+"\n")
            print("串口已关闭")
            self.state=0
        else:
            print("未连接串口,无法关闭串口")
            return None


serial_handler=serial_handler()