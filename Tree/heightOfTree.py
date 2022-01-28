# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None
import sys

sys.setrecursionlimit(15000)


class Solution:
    # @param A : root node of tree
    # @return an integer
    def solve(self, A):
        if A is None:
            return -1

        else:
            lDepth = self.solve(A.left)
            rDepth = self.solve(A.right)

        if (lDepth > rDepth):
            return lDepth + 1
        else:
            return rDepth + 1

