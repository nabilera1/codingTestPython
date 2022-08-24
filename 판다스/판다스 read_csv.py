import pandas as pd

df = pd.read_csv('temp_steam.csv', encoding='cp949')  # utf-8
print(df.shape)
# print(df.info()) #df.info 괄호가 없는 경우는
print('*' * 50)
print(df.columns)  # 컬럼 이름
# print(df.columns[0],df.columns[1]) #컬럼 이름
print(df.head())  # df.head(10), default 5
print(df.tail())
# NaN 문제
