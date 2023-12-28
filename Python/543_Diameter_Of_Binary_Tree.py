# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        def dfs(self, root):
            if not root:
                return 0

            left = dfs(self, root.left)
            right = dfs(self, root.right)
            diameter = left + right

            self.maxDiameter = max(self.maxDiameter, diameter)

            return max(left, right) + 1

        self.maxDiameter = 0
        dfs(self, root)
        return self.maxDiameter

