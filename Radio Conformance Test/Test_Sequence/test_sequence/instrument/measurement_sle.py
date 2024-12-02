#!/usr/bin/env python
# -*- coding: utf-8 -*-


'''程序

@description
    说明
'''
import time

from test_sequence.instrument.instrument_control import inst_control


class ReceiveHandler():
    def __init__(self):
        self.instrument_control = inst_control


    # def measure_sle(self, config=None):
    def measure_sle(self, config=None,ip="192.168.3.211"):
        self.instrument_control.ip=ip
        self.instrument_control.connect(ip)
        if not self.instrument_control.state:
            print("未连接设备!无法测量")
            return 0
        else:
            rf = config["rf"]
            eattenuation = config["eattenuation"]
            frequency = config["frequency"]
            enpower = config["enpower"]
            umargin = config["umargin"]
            wftype = config["wftype"]
            sync = config["sync"]
            pdensity = config["pdensity"]
            phy = config["phy"]
            pattern = config["pattern"]
            plength = config["plength"]
            citype = config["citype"]
            mcs = config["mcs"]
            tout = config["tout"]
            repetition = config["repetition"]
            scondition = config["scondition"]
            moexception = config["moexception"]
            scount_modulation = config["scount_modulation"]
            scount_power = config["scount_power"]
            scount_ibemask = config["scount_ibemask"]
            result_modulation = config["result_modulation"]
            result_power = config["result_power"]
            result_ibemask = config["result_ibemask"]
            # result = config["result"]
            trigger_source = config["trigger_source"]
            trigger_threshold = config["trigger_threshold"]
            trigger_tout = config["trigger_tout"]

            # 设置端口模式、端口、external attenuation、freq、reference level、mixlevoffset、freqoffset、mixlevOffset
            self.instrument_control.send(f"CONFigure:SENSe:SPARklink:ROUTe:CSET GLOBal")
            self.instrument_control.send(f"CONFigure:SENSe:SPARklink:ROUTe:GLOBal {rf}")
            self.instrument_control.send(f"CONFigure:SENSe:SPARklink:RFSettings:EATTenuation {eattenuation}")
            self.instrument_control.send(f"CONFigure:SENSe:SPARklink:RFSettings:FREQuency {frequency}MHz")
            self.instrument_control.send(f"CONFigure:SENSe:SPARklink:RFSettings:ENPower {enpower}")
            self.instrument_control.send(f"CONFigure:SENSe:SPARklink:RFSettings:UMARgin {umargin}")
            self.instrument_control.send("CONFigure:SENSe:SPARklink:RFSettings:MLOFfset 0")

            # 设置sparklinktype
            self.instrument_control.send(f"CONFigure:SENSe:SPARklink:ISIGnal:STYPe SLE")
            # //设置measured burst、WirelessFrame type、同步信号、信号密度、bytes、control information type、BandWidth、data pattern
            self.instrument_control.send(f"CONFigure:SENSe:SPARklink:ISIGnal:LENergy:DMODe AUTO")
            self.instrument_control.send(f"CONFigure:SENSe:SPARklink:ISIGnal:LENergy:WFTYpe {wftype}")
            self.instrument_control.send(f"CONFigure:SENSe:SPARklink:ISIGnal:LENergy:SYNC {sync}")
            self.instrument_control.send(f"CONFigure:SENSe:SPARklink:ISIGnal:LENergy:PDENsity {pdensity}")
            self.instrument_control.send(f"CONFigure:SENSe:SPARklink:ISIGnal:LENergy:PHY {phy}")
            self.instrument_control.send(f"CONFigure:SENSe:SPARklink:ISIGnal:LENergy:PATTern {pattern}")
            self.instrument_control.send(f"CONFigure:SENSe:SPARklink:ISIGnal:LENergy:PLENgth {plength}")
            self.instrument_control.send(f"CONFigure:SENSe:SPARklink:ISIGnal:LENergy:CITYpe {citype}")
            # //此命令用于SLE设置PSK mcs

            # self.instrument_control.send(f"CONFigure:SENSe:SPARklink:ISIGnal:LENergy:MCS {mcs}")
            # //设置measurement timeout、repetition mode 、stop condition、error handling
            self.instrument_control.send(f"CONFigure:SENSe:SPARklink:MEValuation:TOUT {tout}")
            self.instrument_control.send(f"CONFigure:SENSe:SPARklink:MEValuation:REPetition {repetition}")
            self.instrument_control.send(f"CONFigure:SENSe:SPARklink:MEValuation:SCONdition {scondition}")
            self.instrument_control.send(f"CONFigure:SENSe:SPARklink:MEValuation:MOEXception {moexception}")
            # //调制类设置statistic count
            self.instrument_control.send(
                f"CONFigure:SENSe:SPARklink:MEValuation:LENergy:SCOunt:MODulation {scount_modulation}")
            # //功率类设置statistic count
            self.instrument_control.send(f"CONFigure:SENSe:SPARklink:MEValuation:LENergy:SCOunt:POWer {scount_power}")
            # //频谱类设置statistic count
            self.instrument_control.send(f"CONFigure:SENSe:SPARklink:MEValuation:LENergy:SCOunt:IBEMask {scount_ibemask}")
            # //使能测试项
            self.instrument_control.send(
                f"CONFigure:SENSe:SPARklink:MEValuation:LENergy:RESult:MODulation {result_modulation}")
            self.instrument_control.send(f"CONFigure:SENSe:SPARklink:MEValuation:LENergy:RESult:POWer {result_power}")
            self.instrument_control.send(f"CONFigure:SENSe:SPARklink:MEValuation:LENergy:RESult:IBEMask {result_ibemask}")
            self.instrument_control.send(f"CONFigure:SENSe:SPARklink:MEValuation:LENergy:RESult {result_modulation},{result_power},{result_ibemask}")
            # //设置trigger source、trigger level、trigger timeout
            self.instrument_control.send(f"CONFigure:SENSe:SPARklink:MEValuation:TRIGger:SOURce '{trigger_source}'")
            self.instrument_control.send(f"CONFigure:SENSe:SPARklink:MEValuation:TRIGger:THReshold {trigger_threshold}")
            self.instrument_control.send(f"CONFigure:SENSe:SPARklink:MEValuation:TRIGger:TOUT {trigger_tout}")
            self.instrument_control.send("CONFigure:SENSe:SPARklink:MEValuation:TRIGger:MGAP 1.000000E-004")
            # //开启测量
            self.instrument_control.send(f"INITiate:SENSe:SPARklink:MEValuation")
            time_start = time.time()

            # 等待测量完成
            self.instrument_control.send("*OPC?")

            for i in range(10):

                # 查询测量状态
                # state = self.instrument_control.send("FETCh:SENSe:POWer:STATe?")
                state = self.instrument_control.send(f"FETCh:SENSe:SPARklink:MEValuation:STATe?")
                if "RDY" in state:
                    break
                # else:
                #     time.sleep(0.02)

            time_stop = time.time()
            test_time = time_stop - time_start

            # # //查询 main measurement state
            # self.instrument_control.send(f"FETCh:SENSe:SPARklink:MEValuation:STATe?")

            result = {
                "test_time": test_time,

            }

            # result = {
            #     "power_current": "",
            #     "power_average": "",
            #     "power_maximum": "",
            #     "power_minimum": "",
            #     "modulation_current": "",
            #     "modulation_average": "",
            #     "modulation_maximum": "",
            #     "modulation_minimum": "",
            #     "ibemask_current": "",
            #     "ibemask_average": "",
            #     "ibemask_maximum": "",
            #     "ibemask_minimum": "",
            #     "test_time": test_time,
            #
            # }

            # //查询power results
            result["power_current"] = self.instrument_control.send(
                f"FETCh:SENSe:SPARklink:MEValuation:LENergy:POWer:CURRent?")
            result["power_average"] = self.instrument_control.send(
                f"FETCh:SENSe:SPARklink:MEValuation:LENergy:POWer:AVERage?")
            result["power_maximum"] = self.instrument_control.send(
                f"FETCh:SENSe:SPARklink:MEValuation:LENergy:POWer:MAXimum?")
            result["power_minimum"] = self.instrument_control.send(
                f"FETCh:SENSe:SPARklink:MEValuation:LENergy:POWer:MINimum?")
            # //查询modulation results
            result["modulation_current"] = self.instrument_control.send(
                f"FETCh:SENSe:SPARklink:MEValuation:LENergy:MODulation:CURRent?")
            result["modulation_average"] = self.instrument_control.send(
                f"FETCh:SENSe:SPARklink:MEValuation:LENergy:MODulation:AVERage?")
            result["modulation_maximum"] = self.instrument_control.send(
                f"FETCh:SENSe:SPARklink:MEValuation:LENergy:MODulation:MAXimum?")
            result["modulation_minimum"] = self.instrument_control.send(
                f"FETCh:SENSe:SPARklink:MEValuation:LENergy:MODulation:MINimum?")
            # //查询IBEMask results
            result["ibemask_current"] = self.instrument_control.send(
                f"FETCh:SENSe:SPARklink:MEValuation:LENergy:IBEMask:CURRent?")
            result["ibemask_average"] = self.instrument_control.send(
                f"FETCh:SENSe:SPARklink:MEValuation:LENergy:IBEMask:AVERage?")
            result["ibemask_maximum"] = self.instrument_control.send(
                f"FETCh:SENSe:SPARklink:MEValuation:LENergy:IBEMask:MAXimum?")
            result["ibemask_minimum"] = self.instrument_control.send(
                f"FETCh:SENSe:SPARklink:MEValuation:LENergy:IBEMask:MINimum?")
            # //结束测试
            self.instrument_control.send(f"ABORt:SENSe:SPARklink:MEValuation")

            return result

    def close_instrument(self):
        self.instrument_control.close()
receive_handler = ReceiveHandler()# receive_handler为该py文件的接口

if __name__ == '__main__':
    _handler = receive_handler
    _handler.measure_sle()
