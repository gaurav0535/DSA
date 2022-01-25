# Definition for a  binary tree node
# class TreeNode:
#	def __init__(self, x):
#		self.val = x
#		self.left = None
#		self.right = None

class Solution:
    # @param A : root node of tree
    # @param B : root node of tree
    # @return an integer
    def isSameTree(self, A, B):
        if A == None and B == None:
            return 1

        if A == None and B != None:
            return 0
        if A != None and B == None:
            return 0

        if A.val != B.val:
            return 0
        else:
            val1 = self.isSameTree(A.left, B.left)
            val2 = self.isSameTree(A.right, B.right)
            if val1 == val2:
                return 1
        return 0


