#
#
# n1 = float(input('첫 번째 정수는?'))
# print(n1)
# print(type(n1))
# # n1 = int(input('첫 번째 정수는?'))
# # n2 = int(input('두 번째 정수는?'))
# print(f'  {n1}+{n2} = {n1 + n2}  ')

#
# print('당신이 좋아하는 과일은?')
# a = input()
# print(a, '입니다.')
# print(f'{a}입니다.') #f - string


# print("I eat %d apples." % 3)
# # I eat 3 apples
#
# print("%s" % "Hi")
# print("%10s" % "Hi")
# print("%-10s" % "Hi")


# import pandas as pd
#
# df = pd.read_csv('https://raw.githubusercontent.com/nabilera1/csv_link/main/hilton_meal_menu_09_30_2021.csv',
#                  encoding='utf-8')
# print(df.head(10))

# print('''
# What
# a wonderful
# world.
# ''')
# food = input()
# print('my food : %s' % food)
# print(f'my food : {food}')
# print('my food : {}'.format(food))
# a = [1, 2, 3]
# t1=(1)
# print(t1)
# print(type(t1))
#
# t1=(1,)
# print(t1)
# print(type(t1))
#
# t1=1,
# print(t1)
# print(type(t1))

d = {1: 'a', 2: 'b'}
print(d.get(1))
print(d[1])

dd = {'name':'pey', 'phone':'0119993323', 'birth': '1118'}
print(dd.get('name'))