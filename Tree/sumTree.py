class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.key = data


# preOrder = N L R
# inOrder = L K R
# postOrder = L R K

def inOrder(root):
    if root is None:
        return

    inOrder(root.left)
    print(root.key)
    inOrder(root.right)


def sumTree(root):
    if root is None:
        return 0

    ls = sumTree(root.left)
    rs = sumTree(root.right)

    sum = ls + rs + root.key

    root.key = sum

    return sum


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.right.left = Node(6)
root.right.right = Node(7)
root.right.right.right = Node(9)
root.left.left = Node(4)
root.left.right = Node(5)

inOrder(root)

print("calling sumTree")
sumTree(root)

print("printing inOrder")
inOrder(root)
