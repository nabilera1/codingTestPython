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

#구구단 출력

for i in range(1,10):
    for j in range(2, 10):
        print(f'{j} x {i} = {j*i:<3}', end=' ')
        # print(f'{j} x {i} = {j*i:<2}', end=' ')
    print()







