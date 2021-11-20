# 바운드 볼
#
# 번호가 적힌 N개의 공을 바구니에 넣고 K개 만큼 빼기를 반복할 것이다.
# 이 때 마지막에 바구니에 남은 공의 번호를 출력하시오.
# 단 바구니의 깊이는 10000미만이다.
#
# 첫 줄에는 총 횟수 n을 입력받는다
# 총 횟수 n만큼 다음 1번, 2번 명령 2줄이 반복된다.
# 1번 바구니에 넣을 N개의 공 번호를 입력받는다.
# 2번 바구니에서 뺄 공의 숫자를 입력받는다.
#
# 입력
# 2
# 1 2 3
# 2
# 2 3 4 5
# 1
# [출력]
# 1 2 3 4
total=int(input())
basket=[]
for i in range(total):
    t=list(map(int, input().split()))
    n=int(input())
    for i in range(n):
        t.pop()
    for i in t:
        basket.append(i)
for i in basket:
    print(i, end=' ')