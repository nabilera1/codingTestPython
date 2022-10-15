
import pandas as pd

# dataset
df = pd.DataFrame([[1, 2, 3], [4, 5, 6],
                   [7, 8, 9], [10, 11, 12]],
                  columns=['a', 'b', 'c'])

# dataFrame
print(df)

# finding mean by rows
# df.mean(axis='rows')
df.mean(axis=0)
