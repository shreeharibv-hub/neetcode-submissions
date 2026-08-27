# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        count=0

        def dfs(node,max_count):
            if not node:
                return
            nonlocal count
            max_count=max(max_count,node.val)
            if node.val>=max_count:
                count+=1
            dfs(node.left,max_count)
            dfs(node.right,max_count)
            
        dfs(root,root.val)
        return count

            
        