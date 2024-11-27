#!/usr/bin/env python
# -*- coding: utf-8 -*-

from test_sequence.testcases.get_power import get_data

class jud_power():
    def __init__(self,config=None,ip="192.168.3.211"):
        self.config=config
        self.ip=ip
        self.get_data=get_data(self.config,self.ip)
        if self.get_data.get_tx_power():
            self.tx_power=float(self.get_data.get_tx_power())
        else:
            self.tx_power=None
        self.test_time=self.get_data.get_time()
        self.result={}

    def judge(self,power_class=2):
        self.power_class=power_class
        if not self.tx_power:
            print("judge前面有某个步骤出错了")
        else:
            print("="*20+"\n")
            print("正在judge")
            print(self.tx_power)
            # self.result["test_result"] = "waiting"
            # return self.result["test_result"]
            if self.power_class==0:
                if self.tx_power>20.0:
                    print("输出功率范围测试pass")
                    self.result["test_result"] = "pass"
                    return self.result
                else:
                    print("输出功率范围测试fail")
                    self.result["test_result"] = "fail"
                    return self.result

            if self.power_class==1:
                if self.tx_power<=20.0 and self.tx_power>10.0:
                    print("输出功率范围测试pass")
                    self.result["test_result"] = "pass"
                    return self.result
                else:
                    print("输出功率范围测试fail")
                    self.result["test_result"] = "fail"
                    return self.result

            if self.power_class == 2:
                if self.tx_power <= 10 and self.tx_power > 4:
                    print("输出功率范围测试pass")
                    self.result["test_result"] = "pass"
                    return self.result
                else:
                    print("输出功率范围测试fail")
                    self.result["test_result"] = "fail"
                    return self.result

            if self.power_class == 3:
                if self.tx_power <= 4 and self.tx_power > 0:
                    print("输出功率范围测试pass")
                    self.result["test_result"] = "pass"
                    return self.result
                else:
                    print("输出功率范围测试fail")
                    self.result["test_result"] = "fail"
                    return self.result

            if self.power_class == 4:
                if self.tx_power <= 0:
                    print("输出功率范围测试pass")
                    self.result["test_result"] = "pass"
                    return self.result
                else:
                    print("输出功率范围测试fail")
                    self.result["test_result"] = "fail"
                    return self.result


if __name__ == '__main__':
    judge_power1=jud_power
    judge_power1.judge()
