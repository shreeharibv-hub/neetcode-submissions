# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0;
        left_depth=self.maxDepth(root.left)
        right_depth=self.maxDepth(root.right)

        if left_depth<right_depth:
            return right_depth+1
        else:
            return left_depth+1
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_dia=0

        if root is None:
            return 0
        left=self.maxDepth(root.left)
        right=self.maxDepth(root.right)

        max_dia=max(max_dia,left+right)
        max_dia = max(max_dia, self.diameterOfBinaryTree(root.left))
        max_dia = max(max_dia, self.diameterOfBinaryTree(root.right))

        return max_dia