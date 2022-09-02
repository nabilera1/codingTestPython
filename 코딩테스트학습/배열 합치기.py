# 정렬된 배열 합치기
# 입력
# 5 4
# 2 3 6 7 8
# 1 8 9 11
#
# 출력
# 1 2 3 6 7 8 8 9 11
# n, m = map(int, input().split())
# a=list(map(int,input().split()))
# b=list(map(int,input().split()))
# n=a+b
# # print(n)
# n.sort()
# print(*n) # 온라인 저지에서 불일치로 판별되면 반복문으로 출력할 것

n, m = map(int, input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
n=a+b
# print(n)
n.sort()
for i in range(n):
	print(i, end=' ')