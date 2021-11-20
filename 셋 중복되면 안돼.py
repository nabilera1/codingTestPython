# 숫자를 입력받아 정렬하여 출력한다.
# 이 때 중복된 숫자는 하나만 나오도록 하시오.
# [입력]
# 4 5 1 2 3 4 3
# [출력]
# 1 2 3 4 5
n=list(map(int,input().split()))
n=list(set(n))
n.sort()
for i in n:
    print(i, end=' ')

