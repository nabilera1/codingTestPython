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
val=[0 for i in range(0,20)]
y_val=[i for i in range(0,40)]
x=list(val)
y=list(val)
# print(x)
# print(y)
# input()
i=0
ser = serial.Serial('COM7', 9600)
ser.close() # 아두이노 등에서 열린 시리얼포트 닫기
ser.open()
while True:
    data = ser.readline()
    x.append(i)
    y.append(data)
    plt.scatter(i, float(data))
    plt.plot(x, y)
    #y축에 온도에 맞게 값이 출력되도록 수정
    plt.xlabel('Time')
    plt.ylabel('Temp')
    plt.title('STEAM')
    i+=1
    plt.legend()
    plt.show()
    plt.pause(0.0001)


