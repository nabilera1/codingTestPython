
#숫자를 입력받아 총합을 구하는 프로그램을 만드시오.
#1 2 3 4
#10
# num=[0]*11
# print(num)
# for n in range(1,11):
#     num[n]=n
# print(num)
# print(sum(num))


# n=list(map(int, input().split()))
# print(sum(n))

# 만약 아래로 입력을 받는다면
# 1
# 2
# 3
# 4
n=[]
for _ in range(5):
    n.append(int(input()))
print(sum(n))