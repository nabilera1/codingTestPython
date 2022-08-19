import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
df=pd.read_csv('temp_steam.csv', encoding='cp949') #utf-8
print(df.shape)
print(df.info()) #df.info 괄호가 없는 경우는
print('*'*50)
print(df.columns) #컬럼 이름
print(df.head()) #df.head(10), default 5
print(df.tail())
#NaN 문제

df500=df.head(500)
print(df500)
x=df500[0]
y=df500[1]
plt.plot(x, y)
plt.show()