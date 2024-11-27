#!/usr/bin/env python
# -*- coding: utf-8 -*-


from test_sequence.modules.config_file_read import operate_file_to_dict
import conf
import time
from test_sequence.dut.dut_control import dut_control

from test_sequence.testcases.data_testcase import for_result
from test_sequence.modules.reports import reports

# print(PATH_9020)

file_handler=operate_file_to_dict()
# 9020参数配置
config_9020=file_handler.file_to_dict(conf.PATH_9020)


#dut参数配置
config_dut=file_handler.file_to_dict(conf.PATH_DUT_TX)
com_config=file_handler.file_to_dict(conf.PATH_DUT_COM)
ip=conf.IP
power_class=conf.power_class



#
dut_contr=dut_control(com_config)
dut_contr.basic_command()
dut_contr.tx_command(config_dut)
time.sleep(1)

result=for_result().get_result(test_case="tx_power",config=config_9020,ip=ip,power_class=power_class)
dut_contr.end_command()
dut_contr.reset_command()
dut_contr.serial_handler.close()
report=reports()
report_txt=report.output_txt(result,"report.txt")
report_html=report.output_html(result,"report.html")
report_csv=report.output_csv(result,"report.csv")

