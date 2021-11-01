# https://docs.google.com/document/d/17ORr3kIlWwGnrEhOkcnIq9EvJVOoUVHinuDrMcxO6yU/edit?usp=sharing
# 문제 설명 있음

n,m=map(int, input().split())
graph=[]
for i in range(n):
    graph.append(list(map(int,input())))

def dfs(x,y):
    if x<=-1 or x>=n or y<=-1 or y>=m:
        return False
    if graph[x][y]==0:
        graph[x][y]=1
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        return True
    return False
cnt=0
for i in range(n):
    for j in range(m):
        if dfs(i,j)==True:
            cnt+=1
print(cnt)
