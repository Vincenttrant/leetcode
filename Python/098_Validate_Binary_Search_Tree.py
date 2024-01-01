# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        array = []

        def dfs(root):
            if not root:
                return

            dfs(root.left)
            array.append(root.val)
            dfs(root.right)

        dfs(root)

        for i in range(len(array) - 1):
            if array[i] >= array[i + 1]:
                return False
        return True