def bfs(graph, start):
    visited = []
    queue = []
    queue.append(start)
    while queue:
        node = queue.pop(0) # FIFO
        if node not in visited:
            visited.append(node)
            queue.extend(graph[node])
            print('v:',visited, '        q:',queue)
    return visited


graph = {1: [2, 5],
         2: [1, 3, 4],
         3: [2],
         4: [2],
         5: [1, 6, 7],
         6: [5],
         7: [5]
         }
# [1, 2, 5, 3, 4, 6, 7]
print(bfs(graph, 1))
