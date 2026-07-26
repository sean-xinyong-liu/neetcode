# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def goodNodes(node, max_val):
            if not node:
                return 0
            if node.val >= max_val:
                return 1 + goodNodes(node.left, node.val) + goodNodes(node.right, node.val)
            else:
                return goodNodes(node.left, max_val) + goodNodes(node.right, max_val)
        return goodNodes(root, float("-inf"))