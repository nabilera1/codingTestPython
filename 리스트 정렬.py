import random

li=list()
print(li)
for i in range(1,11,1):
    li.append(random.randint(1,100))
print('-----------------')
print(li)
print(len(li),'개 숫자를 정렬합니다.')
print('-----------------')

li.sort() #리스트를 정렬
print(li)
print('1번째 숫자 %d' %li[0])
print('6번째 숫자 %d' %li[5])


# []
# -----------------
# [76, 60, 49, 16, 26, 44, 4, 29, 86, 81]
# 10 개 숫자를 정렬합니다.
# -----------------
# [4, 16, 26, 29, 44, 49, 60, 76, 81, 86]
# 1번째 숫자 4
# 6번째 숫자 49