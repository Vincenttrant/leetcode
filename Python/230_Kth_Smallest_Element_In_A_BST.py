# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        array = []

        def dfs(root):
            if not root:
                return

            dfs(root.left)
            array.append(root.val)
            dfs(root.right)

        dfs(root)
        return array[k - 1]