#!/usr/bin/env python
# -*- coding: utf-8 -*-


'''程序

@description
    说明
'''

# TODO 将一个功能类的函数进行解耦
"""
为什么需要解耦？ 这是一个好问题。

合适的代码设计是 高内聚、低耦合的。 简单来说，高内聚= 一个组件相关的东西都在一个目录/类里，低耦合=组件互相的依赖尽量少。
如此设计的优点在于，使代码尽量简洁易读，维护方便，可灵活调用。
"""
"""
实例：
    TransmitHandler 等同于 仪器的 Generator功能。
    
    当前TransmitHandler看上去是具备了CW/ARB两种类型的信号功能，假设需要切换不同的端口、信道、波形等等参数，TransmitHandler类使用起来就可能使人困惑。
    
    我们尝试把 TransmitHandler 类进行解耦，可以参照 Generator功能.
    
    分为 三部分 
        General Settings
        BaseBand Configuration
        List Configuration
        
    
    General Setting 包含
         端口设置
         线损设置
         频率设置
         下行信号设置
         List Mode 模式的开关控制设置
         基带信号(CW/ARB)的选择设置
    
    BaseBand Configuration 包含
        双音信号设置（暂时不管）
        ARB 设置
            波形文件设置
            波形文件播放模式（重复/单次）
            单次播放的次数
            Trigger等
         
    
    List Configuration 包含
        列表模式的设置（暂时不管）


让我们来设置一个 Generator 功能的类，如下：

"""


class TransmitHandlerDemo():
    def __init__(self):
        """
        初始化函数，当类被实例化的时候，__init__函数立即执行并仅执行一次。（单次立即执行）
        """

    """以下是General Setting的设置"""

    def general_set_rf_port(self, port):
        """
        设置射频发射端口
        :return:
        """
        """
        逻辑处理，假设此接口要求传入的是数字
        """
        if not isinstance(port, int):
            raise Exception("传入非数字，抛出异常")

        if port < 1 or port > 9:
            raise Exception("传入的端口非1~8，抛出异常")

        rf_port = f"RF{port}"

        print(f"设置端口 :{rf_port}")

    def general_set_att_loss(self, loss):
        """
        设置射频发射端口 线损
        :return:
        """
        pass

    def general_set_frequency(self, frequency):
        """
        设置射频发射 频率
        :return:
        """
        pass

    def general_set_level(self, level):
        """
        设置射频发射 下行信号
        :return:
        """
        pass

    def general_set_list_mode_state(self, state):
        """
        设置射频发射 List Mode 开关
        :return:
        """
        pass

    def general_set_base_band(self, base_band):
        """
        设置射频发射 基带信号类型
        :return:
        """
        pass

    """以下是BaseBand Configuration的设置"""

    def baseband_set_arb(self, arb_file):
        """
        设置射频发射 波形文件
        :param arb_file:
        :return:
        """
        pass

    def arb_repetition(self, repetition):
        """
        设置射频发射 波形 播放模式
        :param repetition:
        :return:
        """
        pass

        if repetition == "SIGN":
            """设置单次播放的次数"""
            pass


if __name__ == '__main__':
    # 使用
    tx_demo = TransmitHandlerDemo()

    # TODO 使用的时候可以按需使用
    # tx_demo.general_set_rf_port(port=1)
    # tx_demo.general_set_level(level=10)

    # 例如
    """
    测以下配置  RF1 高中低3个信道，10个下行信号level
    """
    port = 1
    freq_list = ["2402", "2440", "2480"]
    level_list = ["-20", "-30", "-40", "-50", "-60", "-20", "-30", "-40", "-50", "-60"]

    # 端口只设置一次
    tx_demo.general_set_rf_port(port=1)
    for freq in freq_list:
        # 频率设置3次
        tx_demo.general_set_frequency(frequency=freq)
        for level in level_list:
            # level设置10次
            tx_demo.general_set_level(level=level)

    """如果不解耦，以上设计在一起，需要每个都要设置10次"""
    pass

from test_sequence.instrument.instrument_control import inst_control


class TransmitHandler():
    def __init__(self):
        self.instrument_control = inst_control
        self.instrument_control.connect()

    def transmit_close(self):
        self.instrument_control.write("CONFigure:SOURce:STATe OFF")

    def transmit_cw_signals(self, rf_port, frequency, power):
        if not self.instrument_control.state:
            print("未连接设备!无法发射")
            return 0
        else:
            self.frequency = frequency
            self.power = power
            self.rf_port = rf_port
            self.instrument_control.connect()

            # 设置端口
            # 设置端口
            self.instrument_control.write("CONFigure:SOURce:ROUTe:SCENario:SALone RF18")
            self.instrument_control.write("CONFigure:SOURce:ROUTe:USAGe:ALL RF18,OFF,OFF,OFF,OFF,OFF,OFF,OFF,OFF")
            self.instrument_control.write(f"CONFigure:SOURce:ROUTe:USAGe {self.rf_port},ON")

            # 设置baseband mode 、list模式、external attenuation、dgai
            self.instrument_control.write(command="CONFigure:SOURce:BBMode CW")
            self.instrument_control.write(command="CONFigure:SOURce:LIST OFF")
            self.instrument_control.write(command="CONFigure:SOURce:RFSettings:EATTenuation 0")
            self.instrument_control.write(command="CONFigure:SOURce:RFSettings:DGAin 0")

            # 设置frequency、level
            self.instrument_control.write(f"CONFigure:SOURce:RFSettings:FREQuency {self.frequency}")
            self.instrument_control.write(f"CONFigure:SOURce:RFSettings:LEVel {self.power}")

            # 打开Generator并查询Generator当前状态
            self.instrument_control.write("CONFigure:SOURce:STATe ON")
            self.instrument_control.query("CONFigure:SOURce:STATe?")

            print(f"CW信号已发射：频率 = {self.frequency} Hz, 功率 = {self.power} dBm")

        # 控制仪表发射LTE波形函数
        def transmit_arb_signals(self, rf_port, frequency, power):

            # 设置端口
            self.instrument_control.send("CONFigure:SOURce:ROUTe:SCENario:SALone RF18")
            self.instrument_control.send("CONFigure:SOURce:ROUTe:SCENario:SALone RF18")
            self.instrument_control.send("CONFigure:SOURce:ROUTe:SCENario:SALone RF18")

            # 设置baseband mode 、list模式、external attenuation、dgain
            self.instrument_control.send("CONFigure:SOURce:ROUTe:SCENario:SALone RF18")
            self.instrument_control.send("CONFigure:SOURce:ROUTe:SCENario:SALone RF18")
            self.instrument_control.send("CONFigure:SOURce:ROUTe:SCENario:SALone RF18")
            self.instrument_control.send("CONFigure:SOURce:ROUTe:SCENario:SALone RF18")

            self.instrument_control.send("CONFigure:SOURce:ROUTe:SCENario:SALone RF18")
            self.instrument_control.send("CONFigure:SOURce:ROUTe:SCENario:SALone RF18")

            self.instrument_control.send("CONFigure:SOURce:ROUTe:SCENario:SALone RF18")
            self.instrument_control.send("CONFigure:SOURce:ROUTe:SCENario:SALone RF18")
            self.instrument_control.send("CONFigure:SOURce:ROUTe:SCENario:SALone RF18")
            self.instrument_control.send("CONFigure:SOURce:ROUTe:SCENario:SALone RF18")
            self.instrument_control.send("CONFigure:SOURce:ROUTe:SCENario:SALone RF18")
            self.instrument_control.send("CONFigure:SOURce:ROUTe:SCENario:SALone RF18")

            self.instrument_control.send("CONFigure:SOURce:ROUTe:SCENario:SALone RF18")
            self.instrument_control.send("CONFigure:SOURce:ROUTe:SCENario:SALone RF18")
            self.instrument_control.send("CONFigure:SOURce:ROUTe:SCENario:SALone RF18")

            self.instrument_control.send("CONFigure:SOURce:ROUTe:SCENario:SALone RF18")
            self.instrument_control.send("CONFigure:SOURce:ROUTe:SCENario:SALone RF18")

            self.instrument_control.send("CONFigure:SOURce:ROUTe:SCENario:SALone RF18")


if __name__ == '__main__':
    pass
    # cw_signals = TransmitHandler()
    # cw_signals.transmit_cw_signals("RF6", "1.2E+9", "-30")
