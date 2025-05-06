class Node:
    def __init__(self, key, value, left=None, right=None): # 노드 생성자
        self.key   = key
        self.value = value
        self.left  = left
        self.right = right

class BST:
    def __init__(self): # 트리 생성자
        self.root = None

    def get(self, key): # 탐색 연산
        return self.get_item(self.root, key)

    def get_item(self, n, k): # n은 self.root
        if n == None:
            return None # key를 발견 못함
        if n.key > k: # 왼쪽 서브트리 탐색
            return self.get_item(n.left, k)
        elif n.key < k: # 오른쪽 서브트리 탐색
            return self.get_item(n.right, k)
        else:
            return n.value # key를 가진 노드 발견

    def put(self, key, value): # 삽입 연산, t.put(500, 'apple')
        self.root = self.put_item(self.root, key, value)

    def put_item(self, n, key, value): # n은 self.root
        if n == None:
            return Node(key, value)
        if n.key > key: # 왼쪽 서브트리에 삽입
            n.left = self.put_item(n.left, key, value)
        elif n.key < key: # 오른쪽 서브트리에 삽입
            n.right = self.put_item(n.right, key, value)
        else: # 노드 n의 value 갱신
            n.vlaue = value
        return n

    def min(self): # 최솟값 가진 노드 찾기
        if self.root == None:
            return None
        return self.minimum(self.root)

    def minimum(self, n):
        if n.left == None: # if not n.left: #not대신 !도 가능한가?
            return n # 최솟값이 된다.
        return self.minimum(n.left)


    def delete_min(self): # 최솟값 삭제, del_min() 호출
        if self.root == None:
            print('트리가 비어 있음')
        else: # 교과서에는 없음. else가 반드시 있어야 함. 위에 self.root가 None인데 아래 코드 만나면 안되기 때문
          self.root = self.del_min(self.root)

    def del_min(self, n):
        if n.left == None:
            return n.right  # n의 오른쪽자식 리턴
        n.left = self.del_min(n.left) # n의 왼쪽자식으로 재귀호출
        return n # 재연결

    def delete(self, k): # 임의의 키를 삭제 메서드, k 삭제 연산, del_node() 호출, t.delete(200)
        self.root = self.del_node(self.root, k)

    def del_node(self, n, k): # k를 찾아 삭제, n은 루트부터 탐색, minimum(), del_min() 호출
        if n == None:
            return None
        if n.key > k: # 왼쪽자식으로 이동
            n.left = self.del_node(n.left, k)
        elif n.key < k: # 오른쪽자식으로 이동
            n.right = self.del_node(n.right, k)
        else: # 삭제할 노드 발견
            if n.left == None:  # case 1
                return n.right
            if n.right == None: # case 0, 1  이 코드와 아래 코드 순서가 바뀌어도 동일한 결과를 보장하는가?
                return n.left
            # if n.left == None:  # case 1
            #     return n.right
            # 아래는 case 2, 왼쪽 오른쪽 자식 둘 다 있는 경우, 아래 4줄 해당
            target = n
            n = self.minimum(target.right) # 중위 후속자를 찾아서 n이 참조하게 함, 새로운 n은 삭제할 n이 아닌 리턴할 n이다. 위의 n과 현재 n은 다름
            n.right = self.del_min(target.right) # 제일 작은 키 노드가 삭제된 최상위 노드 레퍼런스 리턴하여 연결
            n.left  = target.left # 변경 사항 없이 바로 연결
        return n # 최종 리턴 n은 target 자리에 들어가는 n, 이 n이 리턴되며 호출된 곳으로 타고 올라가며 BST가 다시 구성됨. 재연결
           # target = n
           # n = self.minimum(n.right) # 동일한 결과
           # n.right = self.del_min(target.right)
           # n.left = target.left

    def preorder(self, n): # 전위순회, t.preorder(t.root)
        if n != None:
            print(str(n.key),' ', end='')
            if n.left:
                self.preorder(n.left)
            if n.right:
                self.preorder(n.right)

    def inorder(self, n): # 중위순회
        if n != None:
            if n.left:
                self.inorder(n.left)
            print(str(n.key),' ', end='')
            if n.right:
                self.inorder(n.right)

    def postorder(self, n): # 후위순회
        if n != None:
            if n.left:
                self.postorder(n.left)
            if n.right:
                self.postorder(n.right)
            print(str(n.key),' ', end='')

    def levelorder(self, root): # 레벨순회
        q = []
        q.append(root)
        while len(q) != 0:
            t = q.pop(0)
            print(str(t.key), ' ', end='')
            if t.left != None:
                q.append(t.left)
            if t.right != None:
                q.append(t.right)


t = BST()
t.put(10, "a")
t.put(5, "b")
t.put(15, "c")
t.put(2, "d")
t.put(7, "e")
t.put(12, "f")
t.put(1, "g")
t.put(9, "h")
t.put(11, "i")
t.put(14, "j")

t.preorder(t.root)

print()
t.inorder(t.root)

print()
t.postorder(t.root)

print()
print(t.get(9))
print(t.get(11))
t.get(12)
