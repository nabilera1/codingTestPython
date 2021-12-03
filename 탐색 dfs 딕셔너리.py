def dfs(graph, start, visited):
    visited[start] = True
    print(start, end=' ')
    for i in graph[start]:
        if not visited[i]:
            dfs(graph, i, visited)

#딕셔너리와 리스트 사용
graph = {1: [2, 5],
         2: [1, 3, 4],
         3: [2],
         4: [2],
         5: [1, 6, 7],
         6: [5],
         7: [5]
         }

visited = [False] * 8
print(graph)
print(visited)
print(dfs(graph, 1, visited))
# {1: [2, 5], 2: [1, 3, 4], 3: [2], 4: [2], 5: [1, 6, 7], 6: [5], 7: [5]}
# [False, False, False, False, False, False, False, False]
# 1 2 3 4 5 6 7 None