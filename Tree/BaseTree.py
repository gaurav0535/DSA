class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.key = data


def inOrder(root):
    if root is None:
        return

    inOrder(root.left)
    print(root.key)
    inOrder(root.right)


def preOrder(root):
    if root is None:
        return
    print(root.key)
    preOrder(root.left)
    preOrder(root.right)

def postOrder(root):
    if root is None:
        return

    postOrder(root.left)
    postOrder(root.right)
    print(root.key)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.right.left = Node(6)
root.right.right = Node(7)

root.left.left = Node(4)
root.left.right = Node(5)

print("In Order")
inOrder(root)

print("Pre Order")
preOrder(root)

print("Post Order")
postOrder(root)