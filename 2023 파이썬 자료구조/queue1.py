class Queue(object):
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return not bool(self.items)

    def enqueue(self, value):
        # q에 새로운 값이 오면 위로 한칸씩 올리는 코드임.
        # 그래서 pop하면 맨 먼저 들어간 값이 나옴.
        self.items.insert(0, value)
        # stack :  self.items.append(value)

    def dequeue(self):
        value = self.items.pop()  # front?
        if value is not None:  # null이 아닌 None 임.
            return value
        else:
            print('Queue is empty')

    def size(self):
        return len(self.items)

    def peek(self):
        if self.items:
            return self.items[-1]
        else:
            print('Queue is empty')

    def __repr__(self):
        return repr(self.items)
