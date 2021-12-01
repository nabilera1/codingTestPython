# 두 수를 입력받아 사칙연산하는 프로그램을 만들어 보세요.
#
# 차례대로 덧셈, 뺄셈,곱셈, 나눗셈(반올림하여 표시)
#
# [입력]
# 11 5
#
# [출력]
# 16
# 6
# 55
# 2
n,m=map(int,input().split())
print(n+m)
print(n-m)
print(n*m)
print(int(n/m+0.5))
