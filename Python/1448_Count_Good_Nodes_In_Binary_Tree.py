# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def goodNodes(self, root):

        def dfs(root, curMax):
            if not root:
                return 0

            count = 0
            if root.val >= curMax:
                count = 1

            curMax = max(curMax, root.val)

            return count + dfs(root.left, curMax) + dfs(root.right, curMax)

        return dfs(root, root.val)
