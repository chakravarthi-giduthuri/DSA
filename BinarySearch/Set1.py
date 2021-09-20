class Node:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None


def search(root, key):
    if root is None or root.val == key:
        return root

    if root.val < key:
        return search(root.right, key)
    return search(root.left, key)


root = Node(3)
root.left = Node(2)
root.right = Node(5)
print(root.val)
