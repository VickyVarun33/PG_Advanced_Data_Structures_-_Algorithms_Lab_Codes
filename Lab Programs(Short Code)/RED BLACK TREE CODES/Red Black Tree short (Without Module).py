class Node:
    def __init__(self, key, parent=None, color='R', left=None, right=None):
        self.key, self.parent, self.color, self.left, self.right = key, parent, color, left, right
class RedBlackTree:
    def __init__(self):
        self.NIL_LEAF = Node(None, color='B')
        self.root = self.NIL_LEAF
    def insert(self, key):
        def insert_recursive(node, key):
            if node == self.NIL_LEAF:
                return Node(key, color='R')
            if key < node.key:
                if node.left is None:
                    node.left = Node(key, color='R', parent=node)
                else:
                    node.left = insert_recursive(node.left, key)
            else:
                if node.right is None:
                    node.right = Node(key, color='R', parent=node)
                else:
                    node.right = insert_recursive(node.right, key)
            return node
        self.root = insert_recursive(self.root, key)
        self.root.color = 'B'
    def in_order_traversal(self, node):
        if node is not None and node != self.NIL_LEAF:
            self.in_order_traversal(node.left)
            print(node.key, end=' ')
            self.in_order_traversal(node.right)        
rb_tree = RedBlackTree()
while True:
    key_str = input("Enter a key (or 'q' to quit): ")
    if key_str.lower() == 'q':
        break
    try:
        key = int(key_str)
        rb_tree.insert(key)
    except ValueError:
        print("Invalid input. Please enter a valid integer key.")
print("In-order traversal of Red-Black Tree:")
rb_tree.in_order_traversal(rb_tree.root)
