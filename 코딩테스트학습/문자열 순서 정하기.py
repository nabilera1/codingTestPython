
def digit(str):
    newStr=''
    for s in str:
        if s.isdigit():
            newStr+=s
    return int(newStr)

print(digit('a123')+5)

# a=['a23','b1','a3']
# a.sort()
# print(a)
# a1=int(digit('a23'))
# a2=int(digit('a3'))
# print(a1>a2)
# arr=list(input().split())
# arr.sort()
# # print(arr)
# for i in range(1,len(arr)+1):
#     while arr.index(i):
#         print(arr[])




# 차례대로 입력되는 경우 (기초문제)
# input : a1 a2 a3 b1 b2 b3
# output : a1 b1 a2 b2 a3 b3

# arr=list(input().split())
# li=[]
# n=arr.index('b1')
# for i in range(n):
#     li.append(arr[i])
#     li.append(arr[i+n])
# print(*li)
