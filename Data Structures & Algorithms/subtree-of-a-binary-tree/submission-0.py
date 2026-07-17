# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSame(p, q):
            if not p or not q:
                return p is q
            return (
                p.val == q.val
                and isSame(p.left, q.left)
                and isSame(p.right, q.right)
            )
        def search(node):
            if not node:
                return False
            return (
                isSame(node, subRoot)
                or search(node.left)
                or search(node.right)
            )
        return search(root)