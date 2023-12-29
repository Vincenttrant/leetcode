# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, root, subRoot):
        def sameTree(root, subRoot):
            if not root and not subRoot:
                return True

            if root and subRoot and root.val == subRoot.val:
                return sameTree(root.left, subRoot.left) and sameTree(root.right, subRoot.right)

            return False

        if not root:
            return False

        if sameTree(root, subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)