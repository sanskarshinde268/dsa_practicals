class Node:
    def __init__(self, key):
        self.key = key
        self.left = self.right = None

def insert(root, key):
    if root is None:
        return Node(key)
    if key < root.key:
        root.left = insert(root.left, key)
    elif key > root.key:  # duplicate values are ignored
        root.right = insert(root.right, key)
    return root

def inorder(root):
    if root:
        inorder(root.left); print(root.key, end=" ")
        inorder(root.right)

def preorder(root):
    if root:
        print(root.key, end=" ")
        preorder(root.left); preorder(root.right)

def postorder(root):
    if root:
        postorder(root.left); postorder(root.right)
        print(root.key, end=" ")

values = list(map(int, input("Enter integers separated by spaces: ").split()))
root = None
for value in values:
    root = insert(root, value)
print("Inorder:"); inorder(root)
print("\nPreorder:"); preorder(root)
print("\nPostorder:"); postorder(root)
print()
