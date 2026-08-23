# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def is_equal(self,l1,l2):
        if l1==l2:
            return True
        else:
            return False
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True
        if p is None or q is None:
            return False
        if not self.is_equal(p.val,q.val):
            return False

        else:
            l=self.isSameTree(p.left,q.left)
            r=self.isSameTree(p.right,q.right)

            return l and r

        
        