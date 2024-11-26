#!/usr/bin/env python
# -*- coding: utf-8 -*-

from test_sequence.instrument.measurement_sle import receive_handler

class get_data():
    def __init__(self,config=None):
        self.receive_handler=receive_handler
        self.result = self.receive_handler.measure_sle(config)
    def get_tx_power(self):
        if self.result:
            tx_power=self.result["power_current"]
            return tx_power
        else:
            print("tx_power error")
            return None

    def get_time(self):
        if self.result:
            test_time=self.result["test_time"]
            return test_time
        else:
            print("test_time error")
            return None

    def get_EVM(self):
        if self.result:
            test_EVM=self.result["test_EVM"]
            return test_EVM
        else:
            print("test_EVM error")
            return None




# tx_power=get_tx_power.measure(config)


if __name__ == '__main__':
    _power = get_data()
    _power.get_tx_power()