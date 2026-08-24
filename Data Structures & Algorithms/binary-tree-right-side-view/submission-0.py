# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
     def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        queue = deque()
        ans=[]

        if root is None:
            return []

        queue.append(root)

        while queue:
            level = []

            for i in range(len(queue)):
                u = queue.popleft()

                if u.left:
                    queue.append(u.left)

                if u.right:
                    queue.append(u.right)

                level.append(u.val)

            result.append(level)

        

        for i in result:
            ans.append(i[-1])
        
        return ans

