
import pandas as pd

# # dataset
# df = pd.DataFrame([[1, 2, 3], [4, 5, 6],
#                    [7, 8, 9], [10, 11, 12]],
#                   columns=['a', 'b', 'c'])
#
# # dataFrame
# print(df)
#
# # finding mean by rows
# # df.mean(axis='rows')
# df.mean(axis=0)

# https://www.geeksforgeeks.org/how-to-use-axis0-and-axis1-in-pandas/


# import pandas as pd
#
# # importing our dataset
# df = pd.read_csv('hiring.csv')
#
# # dropping the column named 'experience'
# df = df.drop(['experience'], axis=1)
#
# # 'viewing the dataframe
# df.head()