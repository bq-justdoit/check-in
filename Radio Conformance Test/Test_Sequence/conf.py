#!/usr/bin/env python
# -*- coding: utf-8 -*-


import os
path_reports="\\docs\\reports\\"
BASE_PATH=os.path.abspath(os.path.dirname(__file__))
REPORTS_PATH=os.path.dirname(__file__)+path_reports
# print(REPORTS_PATH)# 获取脚本所在目录

path_conf="\\docs\\conf\\"
CONF_PATH=os.path.dirname(__file__)+path_conf

measure_9020 ="9020_measure_param2.txt"#填写9020测试参数文件
dut_tx = "dut_tx_params.txt"#填写dut tx测试参数文件
dut_rx = "dut_rx_params.txt"#填写dut rx测试参数文件
dut_com="dut_com.txt"#填写串口连接参数文件
IP="192.168.3.244"#填写9020仪器ip
power_class=2


PATH_9020=CONF_PATH+measure_9020
PATH_DUT_TX=CONF_PATH+dut_tx
PATH_DUT_RX=CONF_PATH+dut_rx
PATH_DUT_COM=CONF_PATH+dut_com
# print(PATH_9020)
# print(PATH_DUT_TX)