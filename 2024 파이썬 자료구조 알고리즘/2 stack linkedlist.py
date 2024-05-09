# LinkedList로 스택 구현


## Linked List : 연결 리스트


### Node: 정점



class Node(object):
    def __init__(self, value=None, pointer=None):
        self.value = value
        self.pointer = pointer


n1 = Node()
print(n1)


class Stack(object):
    def __init__(self):
        self.head = None  # 더미 노드
        self.count = 0

    def isEmpty(self):
        return not bool(self.head)

    def push(self, item):
        self.head = Node(item, self.head)
        self.count += 1

    def pop(self):
        if self.count > 0 and self.head:
            node = self.head
            self.head = node.pointer
            self.count -= 1
            # 빠진 번호 value를 리턴해 보세요
            return node.value
        else:
            print('Stack is Empty')
            z

    def _printList(self):
        node = self.head
        while node:
            print(node.value, end='  ')
            node = node.pointer

        print()

    def peek(self):
        if self.count > 0 and self.head:
            return self.head.value
        else:
            print('Stack is Empty')

    def size(self):
        # returns stack size
        return self.count


s = Stack()
print(f'Stack is Empty : {s.isEmpty()}')  # 스택이 비었는지 확인

# 스택에 학생 0번~9번까지 추가하기


for i in range(10):
    s.push(i)
s._printList()  # 출력

# 스택에서 5명의 학생들을 이동, pop()시키세요.
# 그리고 남은 학생들을 출력해주세요.
for i in range(5):
    s.pop()
s._printList()

# peek
print(s.peek())


## Stack 추가 코드



class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self):
        self.head = Node('head')
        self.size = 0

    def __str__(self):  # __repr__ 과 비슷함
        cur = self.head.next
        out = ''
        while cur:
            out += str(cur.value) + '->'
            cur = cur.next
        return out[:-2]  # 마지막에 화살표 빼기

    def getSize(self):
        return self.size

    def isEmpty(self):
        return self.size == 0

    def peek(self):
        if self.isEmpty():
            raise Exception('스택이 비었습니다.')
        return self.head.next.value

    def push(self, value):
        node = Node(value)

        node.next = self.head.next
        self.head.next = node
        self.size += 1

    def pop(self):
        if self.isEmpty():
            raise Exception('Popping from an empty stack')
        top = self.head.next
        # self.head = self.head.next
        self.head.next = self.head.next.next
        self.size -= 1
        return top.value


s = Stack()
print(f's : {s}')
print(f's : {s.head}')
print(f's : {s.head.value}')

for i in range(10):
    s.push(i)
print(f'Stack : {s}')

for _ in range(5):
    print(f'Pop : {s.pop()}')

print(f'Stack : {s}')


