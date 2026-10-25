class Node:
    def __init__(self, key):
        self.key = key
        self.left = self.right = None

def insert(root, key):
    if root is None:
        return Node(key)
    if key < root.key:
        root.left = insert(root.left, key)
    elif key > root.key:
        root.right = insert(root.right, key)
    return root

def height(root):
    if root is None:
        return 0
    return 1 + max(height(root.left), height(root.right))

def leaves(root):
    if root is None:
        return []
    if root.left is None and root.right is None:
        return [root.key]
    return leaves(root.left) + leaves(root.right)

root = None
for x in map(int, input("Enter BST values: ").split()):
    root = insert(root, x)
print("Depth/height (number of levels):", height(root))
print("Leaf nodes:", *leaves(root))
