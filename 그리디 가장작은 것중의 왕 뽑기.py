# n,m=map(int, input().split())
# result=0;
# for i in range(n):
#     data=list(map(int,input().split()))
#     minValue=min(data)
#     result=max(result,minValue)
# print(result)

n, m=map(int,input().split())
result=0
for i in range(n):
    arr=list(map(int, input().split()))
    mm=min(arr)
    result=max(result,mm)
print(result)

