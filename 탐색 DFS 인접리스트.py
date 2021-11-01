#dfs 설명 먼저 하기

def dfs(graph, v, visited):
    visited[v]=True
    print(v,end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph,i,visited)

graph=[
    [],
    [2,3,8], #001100001
    [1,7],   #010000010
    [1,4,5], #010011000
    [3,5],   #000101000
    [3,4],   #000110000
    [7],     #000000010
    [2,6,8], #001000101
    [1,7]    #010000010
]

visited=[False]*9
#0번은 사용안함
dfs(graph,1,visited)
