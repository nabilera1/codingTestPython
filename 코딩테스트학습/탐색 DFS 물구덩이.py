# https://docs.google.com/document/d/17ORr3kIlWwGnrEhOkcnIq9EvJVOoUVHinuDrMcxO6yU/edit?usp=sharing
# 문제 설명 있음
# 응용 문제
# 물 구덩이 수 구하기, 얼음 얼려 먹기

# 4 5
# 00110
# 00011
# 11111
# 00000
# 출력
# 3
# 첫 번째 줄에 땅 크기 N, M  1<=N,M<=1000
# 두 번째 줄에 N+1번째 줄까지 땅에 대한 표시이다
# 0은 물 구덩이, 1은 밟아도 무너지지 않는 땅이다.
# 전체 땅 속에서 물 구덩이 개수를 출력한다.


# 5 5
# 00110   ===> [0, 0, 1, 1, 0]
# 00010
# 11111
# 00001
# 11100
# 3

n, m = map(int, input().split())
graph = []  # 빈 리스트 선언
for i in range(n):
    graph.append(list(map(int, input())))


def puddle(x, y): # 물웅덩이 갯수 체크
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    if graph[x][y] == 0:  # 물웅덩이이면...
        graph[x][y] = 1
        puddle(x - 1, y)   # puddle(-1, 0)
        puddle(x, y - 1)   # puddle(0, -1)
        puddle(x + 1, y)   # puddle(1, 0)
        puddle(x, y + 1)   # puddle(0, 1)
        return True
    else:
        return False


cnt = 0 #물웅덩이 개수
for i in range(n):
    for j in range(m):
        if puddle(i, j) == True:
            cnt += 1
print(cnt)

