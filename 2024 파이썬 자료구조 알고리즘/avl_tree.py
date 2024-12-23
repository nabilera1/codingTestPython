import tkinter as tk
from tkinter import simpledialog

class Node:
    def __init__(self, key, height=1, left=None, right=None):
        self.key = key
        self.height = height
        self.left = left
        self.right = right

class AVL:
    def __init__(self):
        self.root = None

    def height(self, n):
        if n is None:
            return 0
        return n.height

    def put(self, key):
        self.root = self.put_item(self.root, key)

    def put_item(self, n, key):
        if n is None:
            return Node(key)
        if key < n.key:
            n.left = self.put_item(n.left, key)
        elif key > n.key:
            n.right = self.put_item(n.right, key)
        else:
            return n
        n.height = max(self.height(n.left), self.height(n.right)) + 1
        return self.balance(n)

    def balance(self, n):
        bf = self.bf(n)
        if bf > 1:  # Left heavy
            if self.bf(n.left) < 0:  # LR Case
                n.left = self.rotate_left(n.left)
            return self.rotate_right(n)
        elif bf < -1:  # Right heavy
            if self.bf(n.right) > 0:  # RL Case
                n.right = self.rotate_right(n.right)
            return self.rotate_left(n)
        return n

    def bf(self, n):
        return self.height(n.left) - self.height(n.right)

    def rotate_right(self, n):
        x = n.left
        n.left = x.right
        x.right = n
        n.height = max(self.height(n.left), self.height(n.right)) + 1
        x.height = max(self.height(x.left), self.height(x.right)) + 1
        return x

    def rotate_left(self, n):
        x = n.right
        n.right = x.left
        x.left = n
        n.height = max(self.height(n.left), self.height(n.right)) + 1
        x.height = max(self.height(x.left), self.height(x.right)) + 1
        return x

    def draw_tree(self, canvas, node, x, y, level_gap):
        if node is not None:
            if node.left:
                canvas.create_line(x, y, x - level_gap, y + 50, fill="black")
                self.draw_tree(canvas, node.left, x - level_gap, y + 50, level_gap // 2)
            if node.right:
                canvas.create_line(x, y, x + level_gap, y + 50, fill="black")
                self.draw_tree(canvas, node.right, x + level_gap, y + 50, level_gap // 2)
            self.draw_node(canvas, node.key, x, y)

    def draw_node(self, canvas, key, x, y):
        canvas.create_oval(x - 15, y - 15, x + 15, y + 15, fill="lightblue")
        canvas.create_text(x, y, text=str(key), font=("Arial", 10))

    def clear_canvas(self, canvas):
        canvas.delete("all")

class AVLVisualizer:
    def __init__(self):
        self.avl = AVL()
        self.keys = []
        self.index = 0

        self.root = tk.Tk()
        self.root.title("AVL Tree Visualization")
        self.canvas = tk.Canvas(self.root, width=800, height=600, bg="white")
        self.canvas.pack()

        self.label = tk.Label(self.root, text="Enter numbers to visualize AVL Tree", font=("Arial", 12))
        self.label.pack()

        self.input_button = tk.Button(self.root, text="Input Number", command=self.input_number)
        self.input_button.pack(side=tk.LEFT)

        self.next_button = tk.Button(self.root, text="Next Step", command=self.next_step, state=tk.DISABLED)
        self.next_button.pack(side=tk.LEFT)

        self.reset_button = tk.Button(self.root, text="Reset", command=self.reset)
        self.reset_button.pack(side=tk.LEFT)

    def input_number(self):
        num = simpledialog.askinteger("Input", "Enter a number:", parent=self.root)
        if num is not None:
            self.keys.append(num)
            self.label.config(text=f"Insert Order: {', '.join(map(str, self.keys))}")
            self.next_button.config(state=tk.NORMAL)

    def next_step(self):
        if self.index < len(self.keys):
            key = self.keys[self.index]
            self.avl.put(key)
            self.avl.clear_canvas(self.canvas)
            self.avl.draw_tree(self.canvas, self.avl.root, 400, 50, 200)
            self.index += 1
        if self.index >= len(self.keys):
            self.next_button.config(state=tk.DISABLED)

    def reset(self):
        self.avl = AVL()
        self.keys = []
        self.index = 0
        self.avl.clear_canvas(self.canvas)
        self.label.config(text="Enter numbers to visualize AVL Tree")
        self.next_button.config(state=tk.DISABLED)

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    visualizer = AVLVisualizer()
    visualizer.run()
