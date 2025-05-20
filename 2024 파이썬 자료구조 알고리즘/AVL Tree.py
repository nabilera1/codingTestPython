# AVL 전체코드 참고

class Node:
    def __init__(self, key, value, height, left=None, right=None): # Node 생성자
        self.key    = key
        self.value  = value
        self.height = height
        self.left   = left
        self.right  = right

class AVL:
    def __init__(self): # AVL트리 생성자
        self.root = None

    def height(self, n): # 높이 리턴
        if n == None:
            return 0
        return n.height

    def put(self, key, value): # 삽입 연산
        self.root = self.put_item(self.root, key, value)

    def put_item(self, n, key, value):
        if n == None:
            return Node(key, value, 1) #height 1
        if n.key > key:
            n.left = self.put_item(n.left, key, value)
        elif n.key < key:
            n.right = self.put_item(n.right, key, value)
        else:
            n.value = value  # key가 이미 트리에 있으므로 value 갱신
            return n
        n.height = max(self.height(n.left), self.height(n.right)) + 1
        return self.balance(n) # 노드 n의 균형 점검 및 불균형을 바로 잡음


    def balance(self, n): # AVL 트리에서 불균형 발생시 회전 연산을 통해 트리의 균형을 맞추는 코드
        if self.bf(n) > 1:  #노드 n의 왼쪽 서브트리가 높아서 불균형 발생
            if self.bf(n.left) < 0: # 노드 n의 왼쪽 자식의 오른쪽서브트리가 높은 경우
                n.left = self.rotate_left(n.left) # 아래 라인과 함께 LR-회전
            n = self.rotate_right(n) # LL-회전

        elif self.bf(n) < -1: #노드 n의 오른쪽 서브트리가 높아서 불균형 발생
            if self.bf(n.right) > 0: # 노드 n의 오른쪽자식의 왼쪽 서브트리가 높은 경우
                n.right = self.rotate_right(n.right) # 아래 라인과 함께 RL-회전
            n = self.rotate_left(n) # RR-회전
        return n

    def bf(self, n): # bf 계산
        return self.height(n.left) - self.height(n.right)

    def rotate_right(self, n): # 우로 회전
        x = n.left
        n.left = x.right
        x.right = n
        n.height = max(self.height(n.left), self.height(n.right)) + 1 # 높이 갱신
        x.height = max(self.height(x.left), self.height(x.right)) + 1 # 높이 갱신
        return x  # 회전 후 x가 n의 이전 자리로 이동되었으므로

    def rotate_left(self, n): # 좌로 회전
        x = n.right
        n.right = x.left
        x.left = n
        n.height = max(self.height(n.left), self.height(n.right)) + 1 # 높이 갱신
        x.height = max(self.height(x.left), self.height(x.right)) + 1 # 높이 갱신
        return x  # 회전 후 x가 n의 이전 자리로 이동되었으므로

    def delete(self, key): # 삭제 연산
        self.root = self.delete_node(self.root, key)

    def delete_node(self, n, key):
        if n == None:
            return None
        if n.key > key: # 왼쪽 자식으로 이동
            n.left = self.delete_node(n.left, key)
        elif n.key < key: # 오른쪽 자식으로 이동
            n.right = self.delete_node(n.right, key)
        else:  # 삭제할 노드 발견
            if n.right == None: # case 0, 1
                return n.left
            if n.left == None:  # case 1
                return n.right
            target = n          # case 2
            n = self.minimum(target.right) # 중위 후속자를 찾아서 n이 참조하게 함
            n.right = self.del_min(target.right)
            n.left  = target.left
        n.height = max(self.height(n.left), self.height(n.right)) + 1
        return self.balance(n)

    def delete_min(self):  # 최솟값 삭제
        if self.root == None:
            print('트리가 비어 있음')
        self.root = self.del_min(self.root)

    def del_min(self, n):
        if n.left == None:
            return n.right
        n.left = self.del_min(n.left)
        n.height = max(self.height(n.left), self.height(n.right)) + 1
        return self.balance(n)

    def min(self): # 최솟값 찾기
        if self.root == None:
            return None
        return self.minimum(self.root)

    def minimum(self, n):
        if n.left == None:
            return n
        return self.minimum(n.left)

    def preorder(self, n): # 전위순회
        print(str(n.key),' ', end='')
        if n.left:
            self.preorder(n.left)
        if n.right:
            self.preorder(n.right)

    def inorder(self, n): # 중위순회
        if n.left:
            self.inorder(n.left)
        print(str(n.key), ' ', end='')
        if n.right:
            self.inorder(n.right)

if __name__ == '__main__':
    t = AVL()
    t.put(80, 'A')
    t.put(85, 'B')
    t.put(20, 'C')
    t.put(10, 'D')
    t.put(50, 'E')
    t.put(30, 'F')

    print('전위순회:', end='')
    t.preorder(t.root)
    print('\n중위순회:', end='')
    t.inorder(t.root)
    print('\n80와 50 삭제 후:')
    t.delete(80)
    t.delete(50)
    print('전위순회:', end='')
    t.preorder(t.root)
    print('\n중위순회:', end='')
    t.inorder(t.root)