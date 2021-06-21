#수의 규칙

n, k=map(int, input().split())
cnt=0
while n>=k://5 7 의 경우 바로 빠져나옴
    while n%k !=0:
        n-=1
        cnt+=1
    n//=k
    cnt+=1
while n>1:
    n-=1
    cnt+=1

print(cnt)




# n,k=map(int, input().split())
# cnt=0
# while n>=k:
#     while n%k!=0:
#         n-=1
#         cnt+=1
#     n//=k
#     cnt+=1
# while n>1:
#     n-=1
#     cnt+=1
# print(cnt)

# n,k=map(int, input().split())
# cnt=0
# while True:
#     target=(n//k)*k
#     cnt+=(n-target)
#     n=target
#
#     if n<k:
#         break;
#     cnt+=1
#     n//=k
#
# cnt+=(n-1)
# print(cnt)
