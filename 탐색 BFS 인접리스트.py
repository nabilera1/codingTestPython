from collections import deque # double ended queue
def bfs(start):
    queue=deque([start])
    visited[start]=True
    while queue:
        v=queue.popleft() # 큐 왼쪽 값을 꺼냄
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i]=True

graph=[
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]
visited=[False]*9
# visited=[0]*9
bfs(1)