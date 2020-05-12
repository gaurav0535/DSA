class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.key = data


# preOrder = N L R
# inOrder = L N R
# postOrder = L R N


def depthOfTree(root1, level, maxLength):
    if root1 is None:
        print("MaxLength",maxLength)
        return 0
    if level > maxLength:
        maxLength = level

    depthOfTree(root1.left, level + 1, maxLength)
    depthOfTree(root1.right, level + 1, maxLength)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.right.left = Node(6)
root.right.right = Node(7)
root.right.right.right = Node(9)
root.left.left = Node(4)
root.left.right = Node(5)
depthOfTree(root, 0, 0)
