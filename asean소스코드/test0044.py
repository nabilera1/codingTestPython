# [문제]
# 다음 코드가 어떤 결과를 만드는지 설명하고,
# 같은 결과를 만들어주는 mysum이라는 함수를 만들어 보세요.

# sum = 0
# n = int(input())
# for i in range(1, n + 1, 2):#range(1,6,2) => 1 3 5
#     sum += i #sum=sum+i
# print('총합은 ', sum)

# [문제]
# 위의 코드에서 sum=0 없다면 어떻게 되는지 설명해보시오.

# def mysum():
#     sum = 0
#     n = int(input())
#     for i in range(1, n + 1, 2):#range(1,6,2) => 1 3 5
#         sum += i #sum=sum+i
#     return sum
# print('총합은 ', mysum())

def mysum(n):
    sum = 0
    for i in range(1, n + 1, 2):#range(1,6,2) => 1 3 5
        sum += i #sum=sum+i
    return sum

n = int(input())
print('총합은 ', mysum(n))