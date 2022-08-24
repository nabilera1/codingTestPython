import pandas as pd
df=pd.read_csv('sunshine_cloudy.csv')
print(df.describe())
print(df)
print('피어슨 상관계수 :', df['sunshine'].corr(df['cloudy'], method='pearson'))
