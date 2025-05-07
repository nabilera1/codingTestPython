# Re-import dependencies after code reset
# from __future__ import annotations
from typing import Optional, Any


class Node:
    def __init__(
        self,
        key: int,
        value: Any,
        # left: Optional[Node] = None,
        # right: Optional[Node] = None,
        left = None, right = None,
    ) -> None:
        self.key: int = key
        self.value: Any = value
        self.left: Optional[Node] = left
        self.right: Optional[Node] = right


class BST:
    def __init__(self) -> None:
        self.root: Optional[Node] = None

    def get(self, key: int) -> Optional[Any]:
        return self.get_item(self.root, key)

    def get_item(self, n: Optional[Node], k: int) -> Optional[Any]:
        if n is None:
            return None
        if n.key > k:
            return self.get_item(n.left, k)
        elif n.key < k:
            return self.get_item(n.right, k)
        else:
            return n.value

    def put(self, key: int, value: Any) -> None:
        self.root = self.put_item(self.root, key, value)

    def put_item(self, n: Optional[Node], key: int, value: Any) -> Node:
        if n is None:
            return Node(key, value)
        if n.key > key:
            n.left = self.put_item(n.left, key, value)
        elif n.key < key:
            n.right = self.put_item(n.right, key, value)
        else:
            n.value = value
        return n

    def min(self) -> Optional[Node]:
        if self.root is None:
            return None
        return self.minimum(self.root)

    def minimum(self, n: Node) -> Node:
        if n.left is None:
            return n
        return self.minimum(n.left)

    def delete_min(self) -> None:
        if self.root is None:
            print("트리가 비어 있음")
        else:
            self.root = self.del_min(self.root)

    def del_min(self, n: Node) -> Optional[Node]:
        if n.left is None:
            return n.right
        n.left = self.del_min(n.left)
        return n

    def delete(self, k: int) -> None:
        self.root = self.del_node(self.root, k)

    def del_node(self, n: Optional[Node], k: int) -> Optional[Node]:
        if n is None:
            return None
        if n.key > k:
            n.left = self.del_node(n.left, k)
        elif n.key < k:
            n.right = self.del_node(n.right, k)
        else:
            if n.right is None:
                return n.left
            if n.left is None:
                return n.right
            target = n
            n = self.minimum(target.right)
            n.right = self.del_min(target.right)
            n.left = target.left
        return n

    def preorder(self, n: Optional[Node]) -> None:
        if n:
            print(str(n.key), " ", end="")
            self.preorder(n.left)
            self.preorder(n.right)

    def inorder(self, n: Optional[Node]) -> None:
        if n:
            self.inorder(n.left)
            print(str(n.key), " ", end="")
            self.inorder(n.right)

    def postorder(self, n: Optional[Node]) -> None:
        if n:
            self.postorder(n.left)
            self.postorder(n.right)
            print(str(n.key), " ", end="")

    def levelorder(self, root: Optional[Node]) -> None:
        if root is None:
            return
        q: list[Node] = [root]
        while q:
            t = q.pop(0)
            print(str(t.key), " ", end="")
            if t.left:
                q.append(t.left)
            if t.right:
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
print(t.get(10))
print(t.get(11))
print(t.get(12))

print()