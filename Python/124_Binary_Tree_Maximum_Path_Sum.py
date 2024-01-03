# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxPathSum(self, root):
        max_path = [root.val]
        def dfs(root):
            if not root:
                return 0

            left = max(dfs(root.left), 0)
            right = max(dfs(root.right), 0)

            max_path[0] = max(max_path[0], root.val + left + right)
            return root.val + max(left, right)
        dfs(root)
        return max_path[0]
