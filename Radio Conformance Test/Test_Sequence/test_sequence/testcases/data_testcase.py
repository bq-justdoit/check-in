#!/usr/bin/env python
# -*- coding: utf-8 -*-

# from test_sequence.instrument.measurement_sle import receive_handler
#
# class get_tx_power():
#     def __init__(self):
#         self.receive_handler=receive_handler
#     def measure(self,config):
#         result=self.receive_handler.measure_sle(config)
#         self.tx_power=result["power_current"]
#         self.test_time=result["test_time"]
#         return self.tx_power
#
# get_tx_power=get_tx_power()
#
# class judge_power():
#     def __init__(self,config):
#         self.get_tx_power=get_tx_power
#         self.tx_power=self.get_tx_power.measure(config)
#         self.result={}
#         pass
#     def judge(self,power_class):
#         if power_class==0:
#             if self.tx_power>20:
#                 print("输出功率范围测试pass")
#                 self.result["test_result"] = "pass"
#                 return self.result
#             else:
#                 print("输出功率范围测试fail")
#                 self.result["test_result"] = "fail"
#                 return self.result
#
#         if power_class==1:
#             if self.tx_power<=20 & self.tx_power>10:
#                 print("输出功率范围测试pass")
#                 self.result["test_result"] = "pass"
#                 return self.result
#             else:
#                 print("输出功率范围测试fail")
#                 self.result["test_result"] = "fail"
#                 return self.result
#
#         if power_class == 2:
#             if self.tx_power <= 10 & self.tx_power > 4:
#                 print("输出功率范围测试pass")
#                 self.result["test_result"] = "pass"
#                 return self.result
#             else:
#                 print("输出功率范围测试fail")
#                 self.result["test_result"] = "fail"
#                 return self.result
#
#         if power_class == 3:
#             if self.tx_power <= 4 & self.tx_power > 0:
#                 print("输出功率范围测试pass")
#                 self.result["test_result"] = "pass"
#                 return self.result
#             else:
#                 print("输出功率范围测试fail")
#                 self.result["test_result"] = "fail"
#                 return self.result
#
#         if power_class == 4:
#             if self.tx_power <= 0:
#                 print("输出功率范围测试pass")
#                 self.result["test_result"] = "pass"
#                 return self.result
#             else:
#                 print("输出功率范围测试fail")
#                 self.result["test_result"] = "fail"
#                 return self.result

from test_sequence.testcases.judge_power import jud_power
# from test_sequence.testcases.tx_power import get_tx_power


# judge_power=judge_power(config=None)
class for_result():
    def __init__(self):
        pass
    def get_result(self,test_case="tx_power",config=None,ip="192.168.3.211",power_class=2):
        judge_power=jud_power(config,ip)
        case=test_case
        judge_power.config=config
        judge_power.ip=ip
        test_result=judge_power.judge(power_class)["test_result"]
        test_data=judge_power.tx_power
        test_time=judge_power.test_time

        result={
            "test_case":case,
            "test_result":test_result,
            "test_data":test_data,
            "test_time":test_time,
        }

        return result

if __name__ == '__main__':
    result=for_result().get_result()
    print(result)
