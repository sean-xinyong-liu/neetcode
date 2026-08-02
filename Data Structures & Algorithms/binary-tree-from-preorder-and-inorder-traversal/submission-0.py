# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_index_map = {val: index for index, val in enumerate(inorder)}
        preorder_index = 0
        def build(left, right):
            nonlocal preorder_index
            if left > right:
                return None
            val = preorder[preorder_index]
            preorder_index += 1
            node = TreeNode(val)
            mid = inorder_index_map[val]
            node.left = build(left, mid - 1)
            node.right = build(mid + 1, right)
            return node
        return build(0, len(preorder) - 1)