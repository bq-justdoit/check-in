#!/usr/bin/env python
# -*- coding: utf-8 -*-


'''程序

@description
    说明
'''
import pyvisa


class InstrumentControl():
    def __init__(self):
        self.rm = pyvisa.ResourceManager()
        self.state=0
        # self.connect()

    def connect(self,ip):
        # self.resource_name = "TCPIP0::" + self.ip + "::inst0::INSTR"
        self.ip=ip
        self.resource_name = f"TCPIP0::{ip}::inst0::INSTR"
        print("="*40)
        print("\n")
        print(self.resource_name)
        try:
            self.instrument = self.rm.open_resource(self.resource_name)
            self.state=1
            return self.state
        except Exception:
            print("出错了，连接设备失败")
            return self.state

    def is_connected(self):
        if self.state:
            print("已连接设备")
            return self.state
        else:
            print("未连接设备")
            return self.state

    def write(self, command):
        if self.state:
            ret = self.instrument.write(command)
            print("command: ",command)
            print("ret: ",ret)
        else:
            print("未连接设备,无法发送命令")
            return None

    def read(self):
        if self.state:
            return self.instrument.read()
        else:
            print("未连接设备，无法读取")
            return None

    def query(self, command):
        if self.state:
            self.write(command)
            ret = self.read()
            print("ret: ",ret)
            return ret
        else:
            print("未连接设备，无法读取")
            return None

    def send(self, command):
        if self.state:
            if "?" in command:
                ret = self.query(command)
            else:
                ret =self.write(command)

            return ret
        else:
            print("未连接设备，无法读取")
            return None

    def close(self):
        if self.state:
            self.instrument.close()
            print("设备已关闭")
            self.state = 0
        else:
            print("未连接设备，无法关闭")
            return None

inst_control=InstrumentControl()

if __name__ == '__main__':
    inst1 = inst_control
    inst1.connect()
    inst1.is_connected()
    inst1.write("*IDN?")
    inst1.send("*IDN?")
