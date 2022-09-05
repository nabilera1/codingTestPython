# [입력된 배열의 요소의 총합을 구하는 프로그램과 sum()함수]
# data = [1, 2, 3, 4, 5]
# sum=0
# for i in data:
#     sum+=i
# print(sum)

#
# data = [11, 2, 3, 4, 5]
# print(sum(data))
#
# x = min(5, 10, 25)
# print(x)
#
# print(min(5, 10, 25))
# print(max(5, 10, 25))
#
# x=-7.25
# print(x)
# print(abs(x))
#
# x=pow(4,3) #4x4x4
# print(x)
#
# import math
# x=math.sqrt(81)
# print(x)
#
# x=math.ceil(1.4)
# print(x)
#
# x=math.floor(1.4)
# print(x)
#
# x=math.pi
# print(x)



# [문제]
# 5개의 숫자를 입력받아서
# 그 중 가장 큰 숫자를 알려주는 프로그램을 만드시오.
# 5
# 33
# 12
# 19
# 7
# MAX= 33
# n=list()
n=[]
for i in range(5):
    num=int(input())
    n.append(num)
# print(n)
print('MAX=',max(n))
