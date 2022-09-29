# a = '개울가에 소년이 나타났다. 소녀는 개울가를 건너고자 한다.'
# print(a.count('개울가'))
# # print(a.count(' '))
# # 소년 - > 준규
# # print(a.replace('소년', '준규'))
# # a = a.replace('소년', '준규')
# # print(a)
# # find     index
# print(f"소년은 {a.find('소년')+1}번째 있습니다.")
# print(a.find('철수'))
# print(a.index('철수'))

# a = ','.join('abcd')
# print(a)
# print(type(a))
# # print(type(''))

# Yes / No ?   Yes  yEs yes YES yes1
# a = input('Yes / No ?')
# a = a.upper()  # 대문자  lower() 소문자
# print(a)

#
# a = 'Life is Good'
# print(a.split())
# a = 'Life/is/Good'
# print(a.split('/'))


# a = [1, 2, 3, ['a', 'b', 'c']]
# print(a[-1])
# print(a[3])
# print(a[3][0])
# print(a[-1][0])
# print(a[-1][-3])

# arr = [1, 2, ['a', 'b', ['Life', 'is']]]
# print(a[2][2][0][2])

# list1 = ['c', 't', 'a', 'b']
# print(list1)
# list1.sort()
# print(list1)
# # print(list1.reverse())
# list1.reverse()
# print(list1)
# 숫자 10 이하에서 5보다 작고 짝수인 것을 출력하는 코드를 작성
# i=[]
# print([i for n in range(11) if n < 5 and n % 2 == 0])

# i = 0
# sum = 0
# while i < 1001:
#     i = i + 1
#     if i % 3 == 0:
#         sum += i
#
# # print(sum)
# a = [n for n in range(1001) if n % 3 == 0]
# print(sum(a))

# print(*range(1, 101))
# print(list(range(1, 101)))
# print(*list(range(1, 101)))
# #1에서 100까지 총합이 출력됨.
# print(sum(list(range(1, 101))))

# 구구단 출력

# for i in range(2,10):
#     for j in range(1, 10):
#         print(f'{j} x {i} = {j*i:>2}', end='  ')
#         # print(f'{j} x {i} = {j*i:<2}', end=' ')
#     print()

# t = 1
# print(type(t))  # <class 'int'>
# t = (1)
# print(type(t))
# t = 1,
# print(type(t))  # <class 'tuple'>
# t = (1,)
# print(type(t))

#
# a={}
# print(type(a)) # <class 'dict'>


#
# s2 = set("Hello")
# # print(s2)
#
# l1 = [1, 2, 3, 4, 5, 6, 3, 4]
# l2 = [4, 5, 6, 7, 8, 9, 8]
# s1 = set(l1)
# s2 = set(l2)
# print(s1)
# print(s2)
# # 교집합, intersection, &
# print(f'교집합 : {s1.intersection(s2)}')
# print(f'교집합 : {s1 & s2}')
# # 합집합, union, |
#
# # 차집합, difference, -

# 집합 자료형의 함수
# s1 = {1, 2, 3}
# print(type(s1))
# s1 = s1 | {4}  # + 은 에러
# print(s1)
#
# s1.add(5)
# print(s1)
#
# s1.update([6, 7, 8])
# print(s1)
#
# s1.discard(7)  # remove, discard로 바꿔 실행해보세요.
# print(s1)
# s1.discard(7)
# print(s1)

# # bool a = True # C++ 스타일, 파이썬은 안됨.
# # SyntaxError: invalid syntax. Perhaps you forgot a comma?
# a = True
# print(a)
# print(type(a))
# a = 1
# print(a)
# print(type(a))
# a = [1]
# print(id(a))
# a = [1, 2, 3]
# print(id(a))
# b = a
# print(id(b))
# a, b = 5, 3
# print(a, b)
# a, b = b, a
# print(a, b)

def add_mul(ch, *args):
    print(type(args))
    if ch == 'add':
        result = 0
        for i in args:
            result = result + i
    elif ch == 'mul':
        result = 1
        for i in args:
            result = result * i
    return result


print(add_mul('add', 1, 2, 3))
print(add_mul('add', 1, 2))
n = list(map(int, input().split()))
print(n)
print(add_mul('add', n[0], n[1]))
