import serial.tools.list_ports
ports=serial.tools.list_ports.comports()
serialInst=serial.Serial()
portList=[]

for p in ports:
    portList.append(str(p))
    print(str(p))

