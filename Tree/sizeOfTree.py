from SingleNode import Node



# preOrder = N L R
# inOrder = L K R
# postOrder = L R N


def size(root):
    if root is None:
        return 0

    i = size(root.left)
    j = size(root.right)

    sum = i + j + 1

    return sum


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.right.left = Node(6)
root.right.right = Node(7)

root.left.left = Node(4)
root.left.right = Node(5)

print(size(root))

