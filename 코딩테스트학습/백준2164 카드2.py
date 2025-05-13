# from collections import deque
#
# n = int(input())
# deck = deque()
#
# for i in range(n):
#     deck.append(i + 1)
#
# while len(deck) > 1:
#     deck.popleft()
#     deck.rotate(-1)
# print(deck.pop())



from collections import deque

n = int(input())
deck = deque(range(1, n + 1))

while len(deck) > 1:
    deck.popleft()
    deck.rotate(-1)  # 왼쪽으로 한 칸 회전

print(deck.pop())

