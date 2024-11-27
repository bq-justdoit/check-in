#!/usr/bin/env python
# -*- coding: utf-8 -*-

# import os

# print(os.getcwd())  # 获取当前工作目录
# from setup import PATH_9020,PATH_DUT_TX,PATH_DUT_RX

class operate_list():
    def __init__(self,txt_list):
        self.txt_list=txt_list
        self.dict_config={
        }
    def list_to_dict(self):
        for i in range(len(self.txt_list)):
            temp_list=[]
            if ":" in self.txt_list[i]:
                temp_list.append(self.txt_list[i].split(":")[0])
                temp_list.append(self.txt_list[i].split(":")[1])
            if "\t" in self.txt_list[i]:
                temp_list.append(self.txt_list[i].split("\t")[0])
                temp_list.append(self.txt_list[i].split("\t")[1])
            self.dict_config[temp_list[0]]=temp_list[1]

        return self.dict_config


class operate_file():
    def __init__(self,file):
        self.file=file
    def open(self):
        self.file=open(self.file,'r')
    def file_to_list(self):
        txt_list=self.file.readlines()
        for i in range(len(txt_list)):
            txt_list[i]=txt_list[i].replace("\n","")
        return txt_list

        # txt_list = self.file.readlines()
        # for list in txt_list:
        #     list=txt_list.replace("\n","")
        # return txt_list


class operate_file_to_dict():
    def file_to_dict(self,file):
        self.file_to_list= operate_file(file)
        self.file_to_list.open()
        txt = self.file_to_list.file_to_list()
        # print(txt)
        self.list_to_dict = operate_list(txt)
        # print(self.list_to_dict.list_to_dict())
        dict_config=self.list_to_dict.list_to_dict()
        return dict_config

if __name__ == '__main__':

    # file="9020_measure_param.txt"
    # file_to_list=file_to_list(file)
    # file_to_list.open()
    # txt=file_to_list.file_to_list()
    # # print(txt)
    # list_to_dict=list_to_dict(txt)
    # print(list_to_dict.list_to_dict())
    print("\n")

    # measure_9020 ="9020_measure_param2.txt"
    # measure_9020 =PATH_9020
    # config_dict=operate_file_to_dict()
    # print(config_dict.file_to_dict(measure_9020))
    # print("\n")
    #
    # # dut_tx = "dut_tx_params.txt"
    # dut_tx = PATH_DUT_TX
    # config_dict=operate_file_to_dict()
    # print(config_dict.file_to_dict(dut_tx))
    # print("\n")
    #
    # # dut_rx = "dut_rx_params.txt"
    # dut_rx = PATH_DUT_RX
    # config_dict = operate_file_to_dict()
    # print(config_dict.file_to_dict(dut_rx))
    # print("\n")
    pass

