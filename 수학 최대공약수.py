# 두 수를 입력 받아 최대공약수 구하기

# [입력]
# 10 12
# [출력]
# 2

# Using Recursion : 재귀적 용법으로 구해보기
def 최대공약수(a,b): # GCD
    if b==0:
        return a
    else:
        return 최대공약수(b, a%b)

a, b= map(int, input().split()) # 10 12
print(최대공약수(a,b))
