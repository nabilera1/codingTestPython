# 세그먼트 트리 문제 - 구간 합 구하기

"""

문제 설명
N개의 수가 주어지고, 다음과 같은 쿼리들을 반복적으로 수행해야 한다:

1. 어떤 수 하나를 다른 값으로 바꾸기
2. 두 수의 인덱스를 입력받아, 그 사이 구간의 합을 출력

세그먼트 트리를 사용하여 각 연산을 O(log N)에 처리하라.
입력 형식
첫째 줄에 정수 N(1 ≤ N ≤ 1,000,000), M, K(1 ≤ M, K ≤ 10,000)가 주어진다.
둘째 줄부터 N개의 줄에 수 a₁, a₂, ..., aₙ이 주어진다. (-2^63 ≤ aᵢ ≤ 2^63-1)
그 다음 M+K개의 줄에는 쿼리가 주어진다.
- 쿼리 1: '1 index value' → a[index]를 value로 바꾼다.
- 쿼리 2: '2 start end' → a[start] ~ a[end]의 구간 합을 출력한다.
출력 형식
각 2번 쿼리에 대해 구간 합을 한 줄씩 출력한다.
입력 예시
5 2 2
1
2
3
4
5
1 3 6
2 2 5
1 5 2
2 3 5
출력 예시
17
12

"""

import sys
input = sys.stdin.readline

def build_tree(arr):
    n = len(arr)
    size = 1
    while size < n:
        size *= 2
    tree = [0] * (2 * size)
    # 리프 노드 채우기
    for i in range(n):
        tree[size + i] = arr[i]
    # 내부 노드 채우기
    for i in range(size - 1, 0, -1):
        tree[i] = tree[2 * i] + tree[2 * i + 1]
    print(f'\ntree : {tree}')
    return tree, size

def update(tree, size, index, value):
    index += size - 1
    tree[index] = value
    while index > 1:
        index //= 2
        tree[index] = tree[2 * index] + tree[2 * index + 1]
    print(f'tree : {tree}')

def query(tree, size, left, right):
    left += size - 1
    right += size - 1
    result = 0
    while left <= right:
        if left % 2 == 1:
            result += tree[left]
            left += 1
        if right % 2 == 0:
            result += tree[right]
            right -= 1
        left //= 2
        right //= 2
    return result

# 입력 처리
n, m, k = map(int, input().split())
arr = [int(input()) for _ in range(n)]
tree, size = build_tree(arr)

for _ in range(m + k):
    a, b, c = map(int, input().split())
    if a == 1:
        update(tree, size, b, c)
    else:
        print(query(tree, size, b, c))

