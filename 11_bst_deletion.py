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

def min_node(node):
    while node.left:
        node = node.left
    return node

def delete(root, key):
    if root is None:
        return None
    if key < root.key:
        root.left = delete(root.left, key)
    elif key > root.key:
        root.right = delete(root.right, key)
    else:
        if root.left is None:
            return root.right
        if root.right is None:
            return root.left
        successor = min_node(root.right)
        root.key = successor.key
        root.right = delete(root.right, successor.key)
    return root

def inorder(root):
    if root:
        inorder(root.left); print(root.key, end=" ")
        inorder(root.right)

root = None
for x in map(int, input("Enter BST values: ").split()):
    root = insert(root, x)
key = int(input("Enter key to delete: "))
root = delete(root, key)
print("Inorder after deletion:")
inorder(root)
print()
