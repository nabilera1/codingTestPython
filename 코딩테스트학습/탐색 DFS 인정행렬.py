#무방향 그래프 만들기
graph=[]
for i in range(4):
    graph.append(list(map(int,input().split())))
print(graph)

### 아래 입력된 인접행렬 값으로 그래프(노드 1,2,3,4)를 그려보시오.
# 0 1 1 1
# 1 0 0 1
# 1 0 0 1
# 1 1 1 0


###.split()
# 00100
# 11000
# 11111
# [[100], [11000], [11111]]