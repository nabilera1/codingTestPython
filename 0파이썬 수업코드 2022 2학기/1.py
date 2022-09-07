#
#
# n1 = float(input('첫 번째 정수는?'))
# print(n1)
# print(type(n1))
# # n1 = int(input('첫 번째 정수는?'))
# # n2 = int(input('두 번째 정수는?'))
# print(f'  {n1}+{n2} = {n1 + n2}  ')


print('당신이 좋아하는 과일은?')
a = input()
print(a, '입니다.')
print(f'{a}입니다.') #f - string


# print("I eat %d apples." % 3)
# # I eat 3 apples
#
# print("%s" % "Hi")
# print("%10s" % "Hi")
# print("%-10s" % "Hi")


import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/nabilera1/csv_link/main/hilton_meal_menu_09_30_2021.csv',
                 encoding='utf-8')
print(df.head(10))


