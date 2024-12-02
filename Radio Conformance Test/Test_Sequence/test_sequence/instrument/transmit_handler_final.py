#!/usr/bin/env python
# -*- coding: utf-8 -*-


from test_sequence.instrument.instrument_control import inst_control
from conf import ARB_PATH,PATH_JSON_TX
import os
import time

import json

class SignalGeneratorCommand():
    """
    思路：该类是射频仪器信号发生器类，负责发射信号和设置参数，
    先校验再发命令
    """
    def __init__(self,config):
        self.instrument=inst_control#此处硬编码，而不是作为参数传递，因为两者有强依赖，所以不使用依赖注入
        self.config=config
        self.config={
            "rf_port":"",

            "source_bbmode": "",
            "source_list": "",
            "eattenuation": "",
            "dgain": "",

            "frequency": "",
            "level": "",

            "arb_file":"",
            "arb_repetition":"",

            "retrigger":"",
            "trig_arb_autostart ":"",
            "trigger_arb_delay":"",
        }
        # validate=Validate()
    """参数校验（目前写在每个方法内部）"""
    def validate(self):
        pass

    """以下是General Setting的设置"""
    # 设置端口
    def set_rf(self,rf_port):
        try:
            port=int(rf_port)
        # if isinstance(rf_port,int):

            if port>=1 and port<=8:
                print(f"设置端口：{port}")
                self.instrument.send(f"CONFigure:SOURce:ROUTe:SCENario:SALone RF18")
                self.instrument.send("CONFigure:SOURce:ROUTe:USAGe:ALL RF18,OFF,OFF,OFF,OFF,OFF,OFF,OFF,OFF")
                self.instrument.send(f"CONFigure:SOURce:ROUTe:USAGe RF{port},ON")

            else:
                print(f"输入的端口：{rf_port} 不在1~8范围内")
                # raise SystemExit()(f"输入的端口：{rf_port}out of range")
                raise SystemExit()
            # except ValueError as e:
            #     raise SystemExit()

        # except ValueError as e:
        #     raise

        except Exception as e:
            # print(f"status":{status},"error_msg":{error_msg})
            # port = int(rf_port)
            # print(port)
            print(f"输入的端口：{rf_port} 不仅仅含有正整数,可能含有其他字符，请修改")
            raise ValueError("An error occurred in set_rf")


    # //设置frequency、
    def set_frequency(self,frequency):
        try:
            freq=float(frequency)
        # if isinstance(frequency,float):
            print(f"设置frequency：{freq}")
            self.instrument.send(f"CONFigure:SOURce:RFSettings:FREQuency {frequency}")
        # except ValueError as e:
        #     print("继续跳出")
        #     raise
        except:
            # print(f"status":{status},"error_msg":{error_msg})
            print(f"输入的频率:{frequency}不是数字")
            raise ValueError("An error occurred in set_frequency")

    # 设置level
    def set_level(self,level):
        try:
            float(level)
            # if isinstance(level,float):
            print(f"设置level：{level}")
            self.instrument.send(f"CONFigure:SOURce:RFSettings:LEVel {level}")
        except:
            print(f"输入的发射功率：{level} 不是数字")
            raise ValueError("An error occurred in set_level")

    # //设置baseband mode 、list模式、external attenuation、dgain
    def set_source_bbmode(self,source_bbmode):
        bbmode=source_bbmode.upper()
        list_source_bbmode=["CW","ARB"]
        if bbmode in list_source_bbmode:
            print(f"设置baseband mode：{bbmode}")
            self.instrument.send(f"CONFigure:SOURce:BBMode {bbmode}")
            if bbmode=="ARB":
                try:
                    arb_files=[f for f in os.listdir(ARB_PATH) if os.path.isfile(os.path.join(ARB_PATH,f)) and f.endswith()==".wv"]
                except:
                    # if not arb_files:
                    print("有效的arb文件为空")
                else:
                    self.set_arb_setting(arb_files)
        else:
            print(f"输入的基带模式：{source_bbmode}不在可选项内")

    # //设置external attenuation
    def set_eattenuation(self,eattenuation):
        try:
            float(eattenuation)
            # if isinstance(eatten,float):
            print(f"设置external attenuation：{eattenuation}")
            self.instrument.send(f"CONFigure:SOURce:RFSettings:EATTenuation {eattenuation}")
        except:
            print(f"输入的外部线衰：{eattenuation} 不是数字")

    # //设置dgain
    def set_dgain(self,dgain):
        try:
            float(dgain)
        # if isinstance(dgain,float):
            print(f"设置dgain：{dgain}")
            self.instrument.send(f"CONFigure:SOURce:RFSettings:DGAin {dgain}")
        # else:
        except:
            print(f"输入的dgain：{dgain} 不是数字")


    # //设置list模式
    def set_source_list(self,source_list):
        list_switch=source_list.upper()
        list_switch_list=["OFF","ON"]
        if list_switch in list_switch_list:
            print(f"设置list模式：{list_switch}")
            self.instrument.send(f"CONFigure:SOURce:LIST {list_switch}")
            if "ON"==list_switch:
                self.set_list_setting()
                print("list模式 ON")
            return list_switch
        else:
            print(f"输入的list模式：{source_list}不在可选项内")

    """以下是BaseBand Configuration的设置"""
    # //Load ARB波形，设置repeiion，查询波形属性
    def set_arb_file(self,file_name):
        print(f"Load ARB波形：{file_name}")
        self.instrument.send(f"CONFigure:SOURce:ARB:FILE '{file_name}'")
        self.instrument.send("CONFigure:SOURce:ARB:FILE?")

        self.instrument.send("CONFigure:SOURce:ARB:FILE:DATE?")
        self.instrument.send("CONFigure:SOURce:ARB:FILE:VERSion?")
        self.instrument.send("CONFigure:SOURce:ARB:FILE:OPTion?")
        # self.set_trig_arb

    def set_arb_repetition(self,arb_repetition):
        print(f"设置arb_repetition：{arb_repetition}")
        self.instrument.send(f"CONFigure:SOURce:ARB:REPetition {arb_repetition}")
        if arb_repetition == "SIGN":
            """设置单次播放的次数"""
            self.instrument.send(f"CONFigure:SOURce:ARB:CYCLes 20")
            pass

    # //设置ARB波形autostart、trigger delay
    def set_trig_arb(self,retrigger,trig_arb_autostart,trigger_arb_delay):
        print(f"设置ARB波形autostart:{trig_arb_autostart}、trigger delay：{trigger_arb_delay}")
        self.instrument.send(f"CONFigure:SOURce:TRIGger:ARB:RETRigger {retrigger}")
        self.instrument.send(f"CONFigure:SOURce:TRIG:ARB:AUTostart {trig_arb_autostart}")
        self.instrument.send(f"CONFigure:SOURce:TRIGger:ARB:DELay {trigger_arb_delay}")

    """以下是List Configuration的设置"""
    def set_list_cw(self):
        # // 设置baseband mode 、list模式、repetition、increment、increment enabling// 共设置5个step

        self.instrument.send(f"CONFigure:SOURce:LIST:REPetition SING")
        self.instrument.send(f"CONFigure:SOURce:LIST:INCRement 'Dwell Time'")
        self.instrument.send(f"CONFigure:SOURce:LIST:INCRement:ENABling 'Immediate'")
        self.instrument.send(f"CONFigure:SOURce:LIST:SSTop 0,4")
        self.instrument.send(f"")

        #// 设置每个channel的重复次数、level、frequency、dgain 、// reenabling、dwell time、modulation状态
        self.instrument.send(f"CONFigure:SOURce:LIST:IREPetition:ALL 1,1,1,1,1")
        self.instrument.send(f"CONFigure:SOURce:LIST:RFLevel:ALL -15.00,-25.00,-35.00,-45.00,-55.00")
        self.instrument.send(f"CONFigure:SOURce:LIST:FREQuency:ALL 2120E+6,2120E+6,2120E+6,2120E+6,2120E+6")
        self.instrument.send(f"CONFigure:SOURce:LIST:DGAin:ALL 0,0,0,0,0")
        self.instrument.send(f"CONFigure:SOURce:LIST:REENabling:ALL ON,OFF,OFF,OFF,OFF")
        self.instrument.send(f"CONFigure:SOURce:LIST:DTIMe:ALL 100E-6,100E-6,100E-6,100E-6,100E-6")
        self.instrument.send(f"CONFigure:SOURce:LIST:MODulation:ALL OFF,OFF,OFF,OFF,OFF")
        self.instrument.send(f"")

        pass

    def set_list_arb(self):
        # // 查询多段波形属性，设置多端跳段模式，查询当前段
        self.instrument.send(f"CONFigure:SOURce:ARB:MSEGment:NUMBer?")
        self.instrument.send(f"CONFigure:SOURce:ARB:MSEGment:DURation?")
        self.instrument.send(f"CONFigure:SOURce:ARB:MSEGment:PAR?")
        self.instrument.send(f"CONFigure:SOURce:TRIGger:ARB:SEGMents:MODE CONT")
        self.instrument.send(f"CONFigure:SOURce:ARB:SEGMents:CURRent?")
        self.instrument.send(f"")
        pass


    def start_transmit(self):

        # 打开Generator并查询Generator当前状态
        print(f"打开Generator")

        self.instrument.send("CONFigure:SOURce:STATe ON")
        print(f"查询Generator当前状态")
        self.instrument.send("CONFigure:SOURce:STATe?")
        # if self.config.get("source_list")=="ON":
        #     self.instrument_control.send("CONFigure:SOURce:STATe?")
        # // 查询可靠性
        print(f"查询可靠性")
        # self.instrument.send("CONFigure:SOURce:LIST:ESINgle")
        self.instrument.send("CONFigure:SOURce:RELiability:ALL?")


    def transmit_close(self):
        print(f"关闭Generator")

        self.instrument.write("CONFigure:SOURce:STATe OFF")



class SiganalGenerator():
    def __init__(self):
        self.instrument = inst_control
        self.instrument.connect()

    def transmit_signal(self):
        pass
    pass

if __name__ == '__main__':
    # config = {
    #     "frequency":[1,2,3],
    #     "level":[1,2,-2],
    #     "rf_port":1,
    #     "":"",
    # }
    # signal_generator=Signal_Generator(config)
    # frequency_list=config.get("frequency")
    # level_list=config.get("level")
    # rf_port=config.get("rf_port")
    # signal_generator.set_rf(rf_port)
    # for freq in frequency_list:
    #     signal_generator.set_frequency(freq)
    #     for level in level_list:
    #         signal_generator.set_level(level)
    #
    # signal_generator.start_transmit()
    #
    # signal_generator.transmit_close()
    # with open(PATH_JSON_TX,'r') as f:
    #     config=json.load(f)
    # print(config)
    ip="192.168.3.244"
    config = {
        "frequency":[1.000000E+009,2.000000E+009,3.000000E+009],
        "level":[-20,0,-10],
        "rf_port":"10",
        "source_bbmode":"CW",
        "source_list": "OFF",
        "eattenuation":0,
        "dgain":0,
    }
    def transmit_cw(config):
        signal_generator=SignalGeneratorCommand(config)
        frequency_list=config.get("frequency")
        level_list=config.get("level")
        rf_port=config.get("rf_port")
        source_bbmode=config.get("source_bbmode")
        eattenuation=config.get("eattenuation")
        dgain=config.get("dgain")
        source_list=config.get("source_list")

        signal_generator.instrument.connect(ip)
        signal_generator.set_rf(rf_port)
        for freq in frequency_list:
            signal_generator.set_frequency(freq)
            # print("\n")
            for level in level_list:
                signal_generator.set_level(level)
                # print("\n")
                # for bbmode in source_bbmode:
                #     signal_generator.set_source_bbmode(bbmode)
                # print("\n")
                signal_generator.set_source_bbmode(source_bbmode)
                signal_generator.set_eattenuation(eattenuation)
                signal_generator.set_dgain(dgain)
                signal_generator.set_source_list(source_list)

                signal_generator.start_transmit()
                time.sleep(5)


            print("="*40)
            print("="*40)

        signal_generator.transmit_close()


    transmit_cw1=transmit_cw(config)