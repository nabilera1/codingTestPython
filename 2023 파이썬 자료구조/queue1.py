class Queue(object):
    def __init__(self):
        self.items = list()  # []

    def isEmpty(self):
        return not bool(self.items)

    def enqueue(self, value):
        self.items.insert(0, value)

    def dequeue(self):
        value = self.items.pop()
        if value is not None:
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