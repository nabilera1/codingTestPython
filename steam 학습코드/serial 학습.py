from configparser import LegacyInterpolation
from threading import Thread
import serial #파이참에서 pyserial설치
import time
import collections
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import struct
import pandas as pd
import numpy as np

plt.ion()
fig = plt.figure()
i=0
x=list()
y=list()
i=0
ser = serial.Serial('COM7',9600)
ser.close() # 아두이노 등에서 열린 시리얼포트 닫기
ser.open()
while True:
    data = ser.readline()
    #data=(ser.readline()[2:].decode("utf-8")).strip()
    #data=ser.readline().strip()
    #data=ser.readline().strip().decode()
   # print(data.decode())
    x.append(i)
    #y.append(data.decode())
    y.append(data)

    plt.scatter(i, float(data))
    i+=1
    plt.show()
    plt.pause(0.0001)



#Traceback (most recent call last):
# File "C:\Users\user\PycharmProjects\codingTestPython\steam 학습코드\serial 학습.py", line 23, in <module>
#   print(data.decode())
#UnicodeDecodeError: 'utf-8' codec can't decode byte 0xb0 in position 20: invalid start byte
