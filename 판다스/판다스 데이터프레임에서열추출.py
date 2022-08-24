import pandas as pd
df=pd.read_csv('temp_steam.csv', encoding='cp949') #utf-8
print(type(df))

# print(df.shape)
# print(df.info())
# print('*'*50)
# print(df.columns) #컬럼 이름
# print(df.head()) #df.head(10), default 5
# print(df.tail())
# print('*'*50)
x=df.loc[0:100,'time']
y=df.loc[0:100,'temp']
print(x.shape)
print(x)
print(y)
# #NaN 문제
