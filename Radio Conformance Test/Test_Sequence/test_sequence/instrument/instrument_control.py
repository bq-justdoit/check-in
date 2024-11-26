#!/usr/bin/env python
# -*- coding: utf-8 -*-


'''程序

@description
    说明
'''
import pyvisa


class InstrumentControl():
    def __init__(self, ip="192.168.3.244"):
        self.ip = ip
        self.rm = pyvisa.ResourceManager()
        self.state=0
        # self.connect()

    def connect(self):
        # self.resource_name = "TCPIP0::" + self.ip + "::inst0::INSTR"
        self.resource_name = f"TCPIP0::{self.ip}::inst0::INSTR"
        print(self.resource_name)
        try:
            self.instrument = self.rm.open_resource(self.resource_name)
            self.state=1
            return self.state
        except Exception:
            print("出错了，可能是连接设备失败")
            return self.state

    def is_connected(self):
        if self.state:
            print("已连接设备")
            return self.state
        else:
            print("未连接设备")
            return self.state

    def write(self, command):
        ret = self.instrument.write(command)
        print("command: ",command)
        print("ret: ",ret)

    def read(self):
        return self.instrument.read()

    def query(self, command):
        self.write(command)
        ret = self.read()
        print("ret: ",ret)
        return ret

    def send(self, command):
        if "?" in command:
            ret = self.query(command)
        else:
            ret =self.write(command)
            
        return ret

    def close(self):
        self.instrument.close()

inst_control=InstrumentControl()

if __name__ == '__main__':
    inst1 = inst_control
    # inst1.connect()
    inst1.is_connected()
    # inst1.send("*IDN?")
