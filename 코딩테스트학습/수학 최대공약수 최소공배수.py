# 두 수를 입력 받아 최대공약수 구하기
# (최소공배수도 구할 수 있어야 함.)
# [입력]
# 10 12
# [출력]
# 2


from math import gcd
a, b = map(int, input().split())
# 최대공약수, 최소공배수
print(gcd(a, b), a * b // gcd(a, b))