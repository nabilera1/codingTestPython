class Node(object):
    def __init__(self, value = None, pointer = None):
        self.value = value
        self.pointer = pointer

class LinkedListFIFO:
    def __init__(self):
        self.head = None
        self.length = 0
        self.tail = None

    def _printlist(self):
        node = self.head
        while node:
            print(node.value, end=' ')
            node = node.pointer
        print()

    def _addfirst(self, value):
        self.length+=1
        node = Node(value)
        self.head = node
        self.tail = node

    def _deletefirst(self):
        self.length = 0
        self.head = None
        self.tail = None
        print("연결 리스트가 비었습니다.")

    def _add(self,value):
        self.length+=1
        node = Node(value)
        if self.tail:
            self.tail.pointer = node
        self.tail = node

    def addNode(self, value):
        if not self.head:
            self._addfirst(value)
        else:
            self._add(value)

    def _find(self, index):
        prev = None
        node = self.head
        i = 0
        while node and i < index:
            prev = node
            node = node.pointer
            i+=1
        return node, prev, i

    def _find_by_value(self, value):
        prev = Node
        node = self.head
        found = False
        while node and not found:
            if node.value == value:
                found = True
            else:
                prev = node
                node = node.pointer
        return node, prev, found

    def deleteNode(self, index):
        # 노드의 개수가 0 또는 1인 경우를 분리
        if not self.head or not self.head.pointer:
            # 노드의 개수가 1인 경우
            if self.head:
                # index가 0인 경우만 삭제
                if index == 0:
                    self._deletefirst()
                else:
                    print(f'인덱스 {index}에 해당하는 노드가 없습니다.')
            else:
                self._deletefirst()
        else:
            node, prev, i = self._find(index)
            if i == index and node:
                self.length-=1
                if i==0 or not prev:
                    # 이 경우 애초에 찾은 index가 0인, head를 찾은 것.
                    self.head = node.pointer
                    # Head를 찾았는데 Tail을 변경해야 하는 경우는 없음.
                elif node.pointer == None:
                    self.tail = prev
                    self.tail.pointer = None
                else:
                    prev.pointer = node.pointer
            else:
                print(f'인덱스 {index}에 해당하는 노드가 없습니다.')

    def deleteNodeByValue(self, value):
        # 노드의 개수가 0 또는 1인 경우를 분리
        if not self.head or not self.head.pointer:
            # 노드의 개수가 1인 경우
            if self.head:
                # self.head.value == value인 경우만 delete
                if self.head.value == value:
                    self._deleteFirst()
                else:
                    print(f'값 {value}에 해당하는 노드가 없습니다.')
            else:
                self._deleteFirst()
        else:
            node, prev, i = self._find_by_value(value)
            if node and node.value == value:
                self.length-=1
                # i는 True / False로 나타나는 것이므로 Head 판단에 사용되지 않음
                if not prev:
                    self.head = node.pointer
                elif node.pointer == None:
                    self.tail = prev
                    self.tail.pointer = None
                else:
                    prev.pointer = next.pointer
            else:
                print(f'값 {value}에 해당하는 노드가 없습니다.')

if __name__ == '__main__':
    ll = LinkedListFIFO()
    for i in range(1,5):
        ll.addNode(i)
    print("연결 리스트 출력:")
    ll._printlist()
    print("인덱스가 2인 노드 삭제 후, 연결 리스트 출력:")
    ll.deleteNode(2)
    ll._printlist()
    print("값이 15인 노드 추가 후, 연결 리스트 출력:")
    ll.addNode(15)
    ll._printlist()
    print("모든 노드 삭제 후, 연결 리스트 출력:")
    for i in range(ll.length-1, -1, -1):
        ll.deleteNode(i)
    ll._printlist()