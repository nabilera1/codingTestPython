import math

# 이렇게 풀면 안됨. 중간의 0도 카운트
# print(str(math.factorial(100)).count('0'))

fac=str(math.factorial(100))
print(fac)
n=0
while fac[-(n+1)]=='0':
    n+=1
print(n) # 24개가 나옴.
