#!/usr/bin/env python
# -*- coding: utf-8 -*-

from test_sequence.dut.serialhandler import serial_handler
class dut_control():
    def __init__(self,com_config):
        self.serial_handler=serial_handler
        self.serial_handler.open(com_config)

    def basic_command(self):
        if self.serial_handler.is_open():
            self.serial_handler.write(command="a testsuite_sw_at")
            self.serial_handler.write(command="AT+SLEENABLE")
            self.serial_handler.write(command="AT+SLEFACCALLBACK")
            # if "OK" in self.serial_handler.receiver():
            #     print("SLE 使能OK")
            #     self.serial_handler.write(command="AT+SLEFACCALLBACK")
            #     if "OK" in self.serial_handler.receiver():
            #         print("SLE 注册回调 OK")
            #     else:
            #         print("SLE 注册回调 ERROR")
            # else:
            #     print("SLE 使能失败")
        else:
            print("串口连接错误，无法发basic_command")


    def tx_command(self,config):
        if self.serial_handler.is_open():
            freq=config["freq"]
            pwr=config["pwr"]
            payload_len=config["payload_len"]
            phy=config["phy"]
            payload_type=config["payload_type"]
            format1=config["format1"]
            TX_rate=config["TX_rate"]
            pilot=config["pilot"]
            polar=config["polar"]
            interval=config["interval"]

            # self.serial_handler.close()
            command=f"AT+SLETX={freq},{pwr},{payload_len},{payload_type},{phy},{format1},{TX_rate},{pilot},{polar},{interval}"
            self.serial_handler.write(command)
            # self.serial_handler.close()
            self.serial_handler.receiver()
            print(f"常发指令：{command}发送成功")
        else:
            print("串口连接错误，无法发tx_command")



    def rx_command(self,config):
        freq=config["freq"]
        phy=config["phy"]
        format=config["format"]
        pilot=config["pilot"]
        interval=config["interval"]

        command=f"AT+SLERX={freq},{phy},{format},{pilot},{interval}"
        self.serial_handler.write(command)
        self.serial_handler.receiver()
        print(f"常收指令：{command}发送成功")

    def end_command(self):
        if self.serial_handler.is_open():
            self.serial_handler.write(command="AT+SLETRXEND")
            # response = self.serial_handler.receiver()
            # if "OK" in response:
            #     print("SLE 常收常发停止指令发送成功")
            #     print(f"num_packet={response.num_packet},rssi={response.rssi}")
            # else:
            #     print("SLE 常收常发停止指令ERROR")
            # return response

        else:
            print("串口连接错误，无法发end_command")


    def reset_command(self):
        if self.serial_handler.is_open():
            self.serial_handler.write(command="AT+SLERST")
            print("SLE 软件复位指令发送成功")
            # response = self.serial_handler.receiver()
            # if "OK" in response:
            #     print("SLE 软件复位指令发送成功")
            # else:
            #     print("SLE 软件复位指令ERROR")
        else:
            print("串口连接错误，无法发reset_command")


# dut_control=dut_control()

