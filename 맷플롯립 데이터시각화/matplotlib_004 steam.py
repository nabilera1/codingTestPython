import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy import signal

# df=pd.read_csv('temp_steam.csv', encoding='cp949') #utf-8
df=pd.read_csv('../csv/temp_steam.csv', encoding='cp949') #utf-8
print(type(df))

print(df.shape)
print(df.info())
print('*'*50)
print(df.columns) #컬럼 이름
print(df.head()) #df.head(10), default 5
print(df.tail())
print('*'*50)
x=df.loc[0:300,'time']
y=df.loc[0:300,'temp']
df_new=df.loc[0:300,'time':'temp']
print(x.shape)
print(x)
print(y)
# plt.plot(x,y, linestyle='-', marker='o', color='red', label='Temperature')
plt.plot(x,y, color='red', label='Temperature')
plt.title("My Data")
plt.xlabel("Time")
plt.ylabel("Temperature")
plt.xlim(0,150)
plt.ylim(30,80)
plt.legend(shadow=True, borderpad=1)
avg=np.mean(y)
print(f'평균 : {avg}')
avg=df_new['temp'].mean()
max1=max(df_new['temp'])
min1=min(df_new['temp'])

# smooth = signal.savgol_filter(y, 55, 4)
# # print('smooth=',smooth, 'type=',type(smooth))
# #print('np.gradient=',np.gradient(smooth), 'size=',np.gradient(smooth).size)
# dxdy = signal.savgol_filter(np.gradient(smooth), 55, 4)
# dx2dy2 = signal.savgol_filter(np.gradient(dxdy), 55, 4)
#
# #plt.plot(smooth, 'k')
# # plt.plot(np.where(dx2dy2 == dx2dy2.min()), smooth[np.where(dx2dy2 == dx2dy2.min())], 'ro')
# 변곡점=np.where(dx2dy2 == dx2dy2.min())[0][0]
# print('변곡점=',변곡점, y[변곡점])


print(f'평균 : {avg}')
print(f'최댓값 : {max1}')
print(f'최솟값 : {min1}')
plt.text(40, 70, r'$\mu$ :' + f'{avg}')
plt.text(40, 65, r'Max :' + f'{max1}')
plt.text(40, 60, r'Min :' + f'{min1}')
# plt.text(40, 55, f'(x={변곡점}, y= {y[변곡점]})')
plt.show()
