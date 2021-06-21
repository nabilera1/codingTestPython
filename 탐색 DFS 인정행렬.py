graph=[]
for i in range(3):
    graph.append(list(map(int,input().split())))
print(graph)

###
# 00100
# 11000
# 11111
# [[0, 0, 1, 0, 0], [1, 1, 0, 0, 0], [1, 1, 1, 1, 1]]

###.split()
# 00100
# 11000
# 11111
# [[100], [11000], [11111]]