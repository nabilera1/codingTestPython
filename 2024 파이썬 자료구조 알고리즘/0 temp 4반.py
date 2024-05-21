class Node(object):
  def __init__(self, value = None, pointer = None):
    self.value = value
    self.pointer = pointer

class LinkedListFIFO(Node):
  def __init__(self):  # head와 tail 코드 사용
    self.head = None
    self.length = 0
    self.tail = None

  def _printList(self):
    node = self.head
    while node:
      print(node.value, end=' ')
      node = node.pointer
    print()

  # 첫 번째 위치에 노드 추가
  def _addFirst(self, value):
    self.length = 1
    node = Node(value)
    self.head = node
    self.tail = node



  # 새 노드를 추가한다. 테일이 있다면, 테일의 다음 노드는
  # 새 노드를 가리키고, 테일은 새 노드를 가리킨다.

  def _add(self, value):
    self.length += 1
    node = Node(value)
    # if self.tail:
    #   self.tail.pointer = node
    self.tail.pointer = node
    self.tail = node

  def addNodeNew(self, value): # 새로 만들어본 코드 ----------------
    self.length += 1
    node = Node(value)
    if not self.head:
      self.head = node
      self.tail = node
    else:
      self.tail.pointer = node
      self.tail = node

  # 새 노드 추가
  def addNode(self, value):
    # if not self.head:
    #   self._addFirst(value)
    # else:
    #   self._add(value)
    self.length += 1
    node = Node(value)
    if not self.head:
      self.head = node
      self.tail = node
    else:
      self.tail.pointer = node
      self.tail = node

  # find node by index, 이전 코드와 동일
  def _find(self, index):
    prev = None
    node = self.head
    i = 0
    while node and i<index:
      prev = node
      node = node.pointer
      i += 1

    return node, prev, i

  # find node by value, 이전 코드와 동일
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


  def _deleteFirst(self):
    self.length = 0
    self.head = None
    self.tail = None
    print("연결리스트가 비었습니다.")


  # 인덱스에 해당하는 노드 삭제
  def deleteNode(self, index):
    if not self.head or not self.head.pointer:
      self._deleteFirst()
    else:
      node, prev, i = self._find(index)
      if i == index and node:
        self.length -= 1
        if i==0 or not prev:
          self.head = node.pointer
          self.tail = node.pointer
        else:
          prev.pointer = node.pointer
      else:
        print('인덱스 {}에 해당되는 노드가 없습니다.'.format(index))

  # 인덱스에 해당하는 노드 삭제, None
  def deleteNode1(self, index):
    if not self.head or not self.head.pointer:
      self._deleteFirst()
    else:
      node, prev, i = self._find(index)
      if i == index and node:
        self.length -= 1
        if i==0 or not prev:
          self.head = None
          self.tail = None
        else:
          prev.pointer = node.pointer
      else:
        print('인덱스 {}에 해당되는 노드가 없습니다.'.format(index))

  # 실습 과제, 통합 deleteNodeNew()를 만들고 다양한 실행결과를 통해
  # 오류가 없는 코드를 제출하시오.
  def deleteNodeNew(self, index):
    pass

  # 값에 해당하는 노드 삭제
  def deleteNodeByValue(self, value):
    if not self.head or not self.head.pointer:
      self._deleteFirst()
    else:
      node, prev, i = self._find_by_value(value)
      if node and node.value == value:
        self.length -= 1
        if i==0 or not prev:
          self.head = node.pointer
          self.tail = node.pointer
        else:
          prev.pointer = node.pointer
      else:
        print('값 {}에 해당되는 노드가 없습니다.'.format(value))
if __name__ == '__main__':
  link = LinkedListFIFO()
  for i in range(1, 5):
    link.addNode(i)
  print('연결리스트 출력')
  link._printList() # 1 2 3 4

  print('인덱스 2인 노드 삭제 후, 연결리스트 출력:')
  link.deleteNode(2)
  link._printList() # 1 2 4
  print('값이 15인 노드 추가 후, 연결리스트 출력')
  link.addNode(15)
  link._printList()  # 1 2 4 15

  for i in range(link.length - 1, -1, -1):
    link.deleteNode(i)
  link._printList()