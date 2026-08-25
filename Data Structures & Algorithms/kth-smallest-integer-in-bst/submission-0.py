class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = 0

        def inorder(node):
            nonlocal count

            if node is None:
                return None

            left = inorder(node.left)

            count += 1

            if count == k:
                return node.val

            right = inorder(node.right)

            return left if left is not None else right

        return inorder(root)