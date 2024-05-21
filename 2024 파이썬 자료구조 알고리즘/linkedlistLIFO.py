class Node(object):
    def __init__(self, value=None, pointer=None):
        self.value = value
        self.pointer = None
        # self.pointer = pointer


# class LinkedListLIFO(object):
class LinkedListLIFO(Node):  # 파일 분할 안할 시 상속으로 처리
    def __init__(self):
        self.head = None
        self.length = 0

    # 헤드부터 각 노드의 값을 출력
    def _printList(self):
        node = self.head
        while node:
            print(node.value, end=' ')
            node = node.pointer
        print()

    # 이전 노드를 기반으로 노드를 삭제한다.
    def _delete(self, prev, node):
        self.length = -1
        if not prev:
            self.head = node.pointer  # None 아닌가?
        else:
            prev.pointer = node.pointer

    # add new Node
    def _add_old(self, value):
        self.length += 1
        self.head = Node(value, self.head)
        self.head.pointer = prev

    def _add(self, value, prev):
        self.length += 1
        # self.head = Node(value, self.head)
        self.head = Node(value)
        self.head.pointer = prev

    # find node by index
    def _find(self, index):
        prev = None
        node = self.head
        i = 0
        while node and i < index:
            prev = node
            node = node.pointer
            i += 1

        return node, prev, i

    # find node by value
    def _find_by_value(self, value):
        prev = None
        node = self.head
        found = False
        while node and not found:
            if node.value == value:
                found = True
            else:
                prev = node
                node = node.pointer
        return node, prev, found

    # 해당 인덱스의 노드 삭제하기
    def deleteNode(self, index):
        node, prev, i = self._find(index)
        if index == i:
            self._delete(prev, node)
        else:
            print(f'인덱스 {index}에 해당하는 노드가 없습니다.')

    # 값에 해당하는 노드를 찾아서 삭제한다.
    def deleteNodeByValue(self, value):
        node, prev, found = self._find_by_value(value)
        if found:
            self._delete(prev, node)
        else:
            print(f'값 {value}에 해당하는 노드가 없습니다.')


if __name__ == '__main__':
    link = LinkedListLIFO()
    for i in range(1, 5):
        link._add(i, link.head)
    print("Linked List :")
    link._printList()
    print('인덱스가 2인 노드 삭제 후, 연결리스트 출력')
    link.deleteNode(2)
    link._printList()