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

# a = [1, 2, 3]
# b = [5, 6, 7]
# print(len(a))
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
# i = 1
# while i < 6:
#     print('*' * i)
#     i += 1
#
# a = range(10)
# print(a)
# a = range(1, 10)
# print(a)
# # 리스트에 1~10까지의 내용을 담아서 출력하시오.
# # [1,2,3,4,....,10]
# a = list(range(1,11))
# print(a)
# print(*a)
#
# print(*(range(1, 101)))
# print(sum(range(1, 101)))
# print(f'{"구구단":-^20}')
# li = list(range(1, 101))
# # 각 요소에서 3의 배수를 뽑고 그것의 세제곱의 총합을 구하여 출력하시오.
# print(sum([n ** 3 for n in li if n % 3==0]))
# # 8497467
#
# print(type(1))
# print(type((1)))
# print(type((1,)))
a = {1: 'a'}
key, val = input().split()
a[key] = val
print(a)
