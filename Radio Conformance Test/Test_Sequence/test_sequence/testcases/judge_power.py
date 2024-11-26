#!/usr/bin/env python
# -*- coding: utf-8 -*-

from test_sequence.testcases.tx_power import get_data

class judge_power():
    def __init__(self,config=None):
        self.get_data=get_data(config)
        self.tx_power=self.get_data.get_tx_power()
        self.test_time=self.get_data.get_time()
        self.result={}

    def judge(self,power_class=3):
        self.power_class=power_class
        if not self.tx_power:
            print("judge前面有某个步骤出错了")
            return None
        else:
            if self.power_class==0:
                if self.tx_power>20:
                    print("输出功率范围测试pass")
                    self.result["test_result"] = "pass"
                    return self.result
                else:
                    print("输出功率范围测试fail")
                    self.result["test_result"] = "fail"
                    return self.result

            if self.power_class==1:
                if self.tx_power<=20 & self.tx_power>10:
                    print("输出功率范围测试pass")
                    self.result["test_result"] = "pass"
                    return self.result
                else:
                    print("输出功率范围测试fail")
                    self.result["test_result"] = "fail"
                    return self.result

            if self.power_class == 2:
                if self.tx_power <= 10 & self.tx_power > 4:
                    print("输出功率范围测试pass")
                    self.result["test_result"] = "pass"
                    return self.result
                else:
                    print("输出功率范围测试fail")
                    self.result["test_result"] = "fail"
                    return self.result

            if self.power_class == 3:
                if self.tx_power <= 4 & self.tx_power > 0:
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
judge_power=judge_power()

if __name__ == '__main__':
    judge_power1=judge_power
    judge_power1.judge()
