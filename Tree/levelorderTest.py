# To import queue datastructure
import collections


# Code to implement a binary tree
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


# Function for level Order Traversal
def levelOrderTraversal(root):
    ans = []

    # Return Null if the tree is empty
    if root is None:
        return ans

    queue = collections.deque()
    queue.append(root)

    while queue:
        currSize = len(queue)
        currList = []
        while currSize > 0:
            currNode = queue.popleft()
            currList.append(currNode.val)
            currSize -= 1

            if currNode.left is not None:
                queue.append(currNode.left)

            if currNode.right is not None:
                queue.append(currNode.right)

        ans.append(currList)

    return ans


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

# Check if the algorithm work
print(levelOrderTraversal(root))

