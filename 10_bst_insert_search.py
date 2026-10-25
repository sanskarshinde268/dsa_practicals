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
    return root  # duplicate keys are ignored

def search(root, key):
    if root is None or root.key == key:
        return root
    if key < root.key:
        return search(root.left, key)
    return search(root.right, key)

root = None
values = list(map(int, input("Enter BST values: ").split()))
for value in values:
    root = insert(root, value)
key = int(input("Enter key to search: "))
print("Key is present." if search(root, key) else "Key is not present.")
