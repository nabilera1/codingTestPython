import pandas as pd
import numpy as np

# simple array
data = np.array(['g', 'e', 'e', 'k', 's'])
# data = ['g', 'e', 'e', 'k', 's'] # 리스트도 같은 결과 나옴

ser = pd.Series(data)
print(ser)

# https://www.geeksforgeeks.org/python-pandas-series/
