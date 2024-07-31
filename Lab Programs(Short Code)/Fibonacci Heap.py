import math
class FibonacciTree:
    def __init__(self, value):
        self.value, self.child, self.order = value, [], 0
    def add_at_end(self, t):
        self.child.append(t)
        self.order += 1
class FibonacciHeap:
    def __init__(self):
        self.trees, self.least, self.count = [], None, 0
    def insert_node(self, value):
        new_tree = FibonacciTree(value)
        self.trees.append(new_tree)
        self.least = new_tree if not self.least or value < self.least.value else self.least
        self.count += 1
    def get_min(self):
        return self.least.value if self.least else None
    def extract_min(self):
        s = self.least
        if s:
            self.trees += s.child
            self.trees.remove(s)
            self.least = min(self.trees, key=lambda x: x.value) if self.trees else None
            self.consolidate()
            self.count -= 1
            return s.value
    def consolidate(self):
        a = [None] * (int(math.log2(self.count)) + 1)
        while self.trees:
            x = self.trees.pop(0)
            o = x.order
            while a[o]:
                y = a[o]
                x, y = (x, y) if x.value <= y.value else (y, x)
                x.add_at_end(y)
                a[o], o = None, o + 1
            a[o] = x
fib_heap = FibonacciHeap()
num_elements = int(input("Enter the number of elements to insert: "))
values = [int(input(f"Enter value {i + 1}: ")) for i in range(num_elements)]
[fib_heap.insert_node(value) for value in values]
print('Min value of the Fibonacci Heap:', fib_heap.get_min())
print('Min value removed:', fib_heap.extract_min())
