#수의 규칙
# 이 문서 공유주소
# https://docs.google.com/document/d/17ORr3kIlWwGnrEhOkcnIq9EvJVOoUVHinuDrMcxO6yU/edit?usp=sharing
# 수의 규칙 1이 될 때까지 다음 규칙을 적용한다.
#
# 두 정 수 N과 K를 입력받는다.
# 어떤 수 N이 1이 될 때까지
# N이 K보다 큰 경우
# 1-1, 1-2 두 과정 중 하나를 선택하여 반복한다.

# 1-1. N 에서 1을 뺀다(정수 N을 K로 정확히 나눌 수 없을 때)
# 1-2. N을 K로 나누어지면 N은 K로 나눈 몫이 저장된다.
# 2. N>=K 인 경우동안 1,2 중 하나를 반복한다.
#
#
# 반복할 때마다 1씩 카운트 된다.
# N이 K보다 작은 경우 1-1을 반복한다.
# N이 1이 되면 1회 카운트하고 종료된다.
#
# 위의 과정을 반복한 횟수를 출력하라.
# [입력]
# 17 4
#
# [출력]
# 4

# 17 4 는 16 4가 된다.
# 16 4는 4 4가 된다.
# 4 4는 1 4가 된다.
# 1 4에서 종료
n, k=map(int, input().split())
cnt=0
while n>=k: # 5 7 의 경우 바로 빠져나옴
    while n%k !=0:
        n-=1
        cnt+=1
        continue
    n//=k
    cnt+=1
while n>=1:
    n=n-1
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
