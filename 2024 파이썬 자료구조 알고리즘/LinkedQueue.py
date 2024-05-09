import heapq
import sys
input = sys.stdin.readline

N = int(input())
input()

hq = []
n = list(map(int, input().split()))

# print(n)
for i in range(len(n)):
    if n[i] != 0: # 0이 아니면
        heapq.heappush(hq, -n[i]) #최대 힙으로 만들기
        # print(hq)
    else:
        print(-heapq.heappop(hq) if hq else 0, end = ' ')



# import heapq
# import sys
# input = sys.stdin.readline
#
# N = int(input())
# hq = []
# for _ in range(N):
#     n = list(map(int, input().split())
#
#     for i in range(len(n)):
#         if n[i] != 0: # 0이 아니면
#             heapq.heappush(hq, -n[i]) #최대 힙으로 만들기
#         else:
#             print(-heapq.heappop(hq) if hq else 0)