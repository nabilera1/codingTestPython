# class BHeap:
#     def downheap(self, i):
#         while i <= self.N:
#             l, r = 9999, 9999
#
#             if i * 2 <= self.N:
#                 l = self.a[i * 2]
#
#             if i * 2 + 1 <= self.N:
#                 r = self.a[i * 2 + 1]
#
#             t = min(l, r)
#
#             if t == l:
#                 self.a[i], self.a[i * 2] = self.a[i * 2], self.a[i]
#                 i = i * 2
#             else:
#                 self.a[i], self.a[i * 2 + 1] = self.a[i * 2 + 1], self.a[i]
#                 i = i * 2 + 1
#

class BHeap:
    def __init__(self, a): # 생성자, a는 리스트
        self.a = a    # a[0] 사용 안함
        self.N = len(a) - 1 # 힙의 항목 수

    def create_heap(self): # 초기 힙 만들기, heapq.heapify()
        for i in range(self.N//2, 0, -1):
            self.downheap(i)

    def insert(self, key_value): # 삽입 연산, heapq.heappush()
        self.N += 1
        self.a.append(key_value) # 새로운 키(항목)를 맨 끝에 저장
        self.upheap(self.N) # 위로 올라가며 힙속성 회복시키기 위해

    def delete_min(self): # 최솟값 삭제, heapq.heappop()
        if self.N == 0:  # underflow 경우
            print('힙이 비어 있음')
            return None
        minimum = self.a[1]  # a[1]의 최솟값을 minimum에 저장하여 리턴
        self.a[1], self.a[-1] = self.a[-1], self.a[1]  # 힙의 마지막 항목과 교환
        # self.a[1], self.a[self.N] = self.a[self.N], self.a[1]

        del self.a[-1]  # 힙의 마지막 항목 삭제
        # self.a.pop()

        self.N -= 1
        self.downheap(1) # 힙속성을 회복시키기 위해
        return minimum

    # def downheap(self, i):
    #     while i <= self.N:
    #         l, r = 9999, 9999
    #
    #         if i * 2 <= self.N:
    #             l = self.a[i * 2]
    #
    #         if i * 2 + 1 <= self.N:
    #             r = self.a[i * 2 + 1]
    #
    #         t = min(l, r)
    #
    #         if t == 9999 or self.a[i] <= t:
    #             break
    #
    #         if t == l:
    #             self.a[i], self.a[i * 2] = self.a[i * 2], self.a[i]
    #             i = i * 2
    #         else:
    #             self.a[i], self.a[i * 2 + 1] = self.a[i * 2 + 1], self.a[i]
    #             i = i * 2 + 1

    def downheap(self, i): # 힙 내려가며 힙속성 회복
        while 2*i <= self.N: # i의 왼쪽자식이 힙에 있으면
            k = 2*i  # k는 왼쪽자식의 인덱스
            if k < self.N and self.a[k][0] > self.a[k+1][0]: #왼쪽과 오른쪽자식의 승자를 결정하여 k가 승자의 인덱스가됨
                k += 1
            if self.a[i][0] < self.a[k][0]:
                break  # 현재 노드가 자식 승자보다 작으면, 루프를 중단하고
            self.a[i], self.a[k] = self.a[k], self.a[i] # 현재 노드가 자식 승자보다 크면 현재 노드와 자식 승자와 교환
            i = k   # 자식 승자가 현재 노드가 되어 다시 반복하기 위해

    def upheap(self, j): # 힙 올라가며 힙속성 회복
        while j > 1 and self.a[j//2][0] > self.a[j][0]: # 현재노드가 루트가 아니고 동시에 부모가 크면
            self.a[j], self.a[j//2] = self.a[j//2], self.a[j]  # 부모와 현재 노드 교환
            j = j//2  # 부모가 현재 노드가 되어 다시 반복하기 위해

    def print_heap(self): # 힙 출력
        for i in range(1, self.N+1):
            print(f'{self.a[i]}', end='')
        print('\n힙 크기 = ', self.N)


# from binary_heap import BHeap
if __name__ == '__main__':
    a = [None] * 1

    a.append([50])
    a.append([60])
    a.append([20])
    a.append([30])
    a.append([15])

    b = BHeap(a)
    print('힙 만들기 전:')
    b.print_heap()

    b.create_heap() # 힙 만들기
    print('최소힙:')
    b.print_heap()

    print('최솟값 삭제 후')
    print(b.delete_min())
    b.print_heap()

    b.insert([5])
    print('5 삽입 후')
    b.print_heap()