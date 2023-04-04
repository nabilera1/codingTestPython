class Node:
    def __init__(self, data=None):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def add_node(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node
            new_node.prev = cur

    def traverse_left_to_right(self):
        cur = self.head
        while cur:
            print(cur.data, end = ' ')
            cur = cur.next
        print()
    def traverse_right_to_left(self):
        cur = None
        if self.head is not None:
            cur = self.head
            while cur.next is not None:
                cur = cur.next
        while cur is not None:
            print(cur.data, end = ' ')
            cur = cur.prev
        print()

