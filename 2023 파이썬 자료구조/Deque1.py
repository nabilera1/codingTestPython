from Queue1 import Queue
class Deque(Queue):
    def enqueue_back(self, item):
        self.items.append(item)

    def dequeue_front(self):
        value = self.items.pop(0)
        if value is not None:
            return value
        else:
            print('Deque is empty')

if __name__ == '__main__':
    dq = Deque()
    print(dq.isEmpty())
