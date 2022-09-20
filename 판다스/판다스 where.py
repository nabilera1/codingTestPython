import pandas as pd
import numpy as np

data = {'time': [1, 2, 3, 4, 5], 'score': [50, 60, 70, 80, 90], 'remarks':[0,0,0,0,0]}
df = pd.DataFrame(data)
print(df)
print(type(df))

# Series객체.where(조건, 거짓일시 나타낼 값)
print(df['time'].where(df['time'] < 3, 10))
print(df['time'].where(df['time'] > 2, 10))
# df = df['time'].where(df['time'] < 3, 60)
# print(type(df))
#
# df = df['time'].where(df['time'] < 3, 60)
# print(df)


print(np.where(df['time'] < 3, 10, df['time']))
# numpy에서는 순서가 다름

print(df)

df['time'] = np.where(df['time'] < 3, 10, df['time'])
# 수정

print(df)

#70점 이상인 학생 합격 불합격 나타내기, O, X로 표기
df['remarks'] = np.where(df['score']>=70, 'O','X')
print(df)
