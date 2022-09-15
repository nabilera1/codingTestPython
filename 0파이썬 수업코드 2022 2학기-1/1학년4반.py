# y = 3.42134234
# print('{0:0.4f}'.format(y))
# print('{0:10.4f}'.format(y))
# print('{0:<10.4f}'.format(y))
# print('{0:>10.4f}'.format(y))
#
# 딕셔너리는 키와 밸류
# d = {'apple':'사과', 'age':30}
# print(f"apple은 {d['apple']}입니다. 나이는 {d['age']}입니다.")

# a, b = map(int, input().split())
# print("{0:10}".format(a))
# print("x", end="")
# print("{0:9}".format(b))
# print("-" * 10)
# print("{0:10}".format(a * b))

# a = '개울가에 소년이 나타났다. 소녀는 개울가를 건너고자 한다.'
# print(a.count('개울가'))
# print(a.count(' '))

# a = ' '
# print(type(a))

# Yes / No : yEs
# a = input()
# a = a.upper()  # 모두 대문자로 바꾸기
# print(a)

# upper  /  lower

# a = '개울가에 소년이 나타났다. 소녀는 개울가를 건너고자 한다.'
# # print(a.count('개울가'))
# a = a.replace('개울가', 'PC방')
# print(a)
# a = a.replace(' ', '')
# print(a)
#
# a = 'Life is Good'
# print(a.split())
# a = 'Life/is/Good'
# print(a.split('/'))

a = [1, 2, 3]
b = [5, 6, 7]
print(len(a))
# print(a * b)
# TypeError: can't multiply sequence by non-int of type 'list'


# money = 2000
# card = True   # true TRUE
# if money >= 3000 or card:
#     print('택시')
# else:
#     print('조깅')


# print('a' in 'python')
# print('t' in 'python')
i = 1
while i < 6:
    print('*' * i)
    i += 1
