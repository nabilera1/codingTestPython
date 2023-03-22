class Node(object):
    def __init__(self, value = None, pointer = None ):
        self.value = value
        self.pointer = pointer


class LinkedQueue(object):
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def isEmpty(self):
        return not bool(self.head)

    def dequeue(self):
        if self.head:
            value = self.head.value
            self.head = self.head.pointer
            self.count -= 1
            return value
        else:
            print('Queue is empty')  # 교재, 파이썬에서는 문제 없이 동작
            # return 'Queue is empty' #

    def enqueue(self, value):
        node = Node(value)
        if not self.head:
            self.head = node
            self.tail = node
        else:
            if self.tail:  # 없어도 될 듯.
                self.tail.pointer = node
            self.tail = node
        self.count += 1

    def size(self):
        return self.count

    def peek(self):
        return self.head.value

    def __repr__(self):
        if self.head:
            return repr(self.head.value)

    def print(self):
        node = self.head
        while node:
            print(node.value, end=' ')
            node = node.pointer
        print()

if __name__ == '__main__' :
    q = LinkedQueue()
    q.dequeue()
    q.enqueue(5)
    print(q.dequeue())