from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        queue = deque()

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

        return result