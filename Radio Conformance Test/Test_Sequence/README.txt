>>> import serial.tools.list_ports
>>> ports = serial.tools.list_ports.comports()
>>> for port in ports:
    print(f"设备: {port.device}, 描述: {port.description}")


设备: COM3, 描述: Intel(R) Active Management Technology - SOL (COM3)
设备: COM1, 描述: 通信端口 (COM1)
设备: COM56, 描述: Silicon Labs Dual CP2105 USB to UART Bridge: Enhanced COM Port (COM56)
设备: COM57, 描述: Silicon Labs Dual CP2105 USB to UART Bridge: Standard COM Port (COM57)
>>>