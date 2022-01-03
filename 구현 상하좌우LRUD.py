# N*N 크기의 정사각형 지도
# 시작은 (1,1)  맨 마지막 위치는 (N,N)
# 1<=N<=100 , 1<=이동횟수<=100
# 범위를 벗어난 이동 명령은 무시한다.
#
# R : 오른쪽 한 칸 이동
# L : 왼쪽 한 칸 이동
# U : 위 한 칸 이동
# D : 아래 한 칸 이동
#
# 입력 (맵 크기 N, 이동 명령 개수 C)
# 5 6
# R R R U D D
# 출력
# 3 4
#
n, c = map(int, input().split())
#c는 파이선에서 무시
x, y = 1, 1
moveCmd = input().split()
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
moveTypes = ['L', 'R', 'U', 'D']

for m in moveCmd:
    for i in range(len(moveTypes)):
        if m == moveTypes[i]:
            newX = x + dx[i]
            newY = y + dy[i]

    if newX < 1 or newY < 1 or newX > n or newY > n:
        continue
    x, y = newX, newY
print(x, y)

# 5
# R R U D D D
# 4 3
