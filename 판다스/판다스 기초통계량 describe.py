import pandas as pd

df = pd.read_csv('temp_steam.csv', encoding='cp949')
# df = pd.read_csv('temp_steam.csv', header=None, encoding='cp949')
#위와 같은 경우 숫자와 글자가 함께 존재해 기초통계량이 다르게 나온다. 오류
print(df.describe())
print(df.dtypes)
print(df.shape)
print(df.info())
