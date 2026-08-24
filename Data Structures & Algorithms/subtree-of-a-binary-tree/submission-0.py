class Solution:
    def issametree(self, l1, l2):
        if l1 is None and l2 is None:
            return True

        if l1 is None or l2 is None:
            return False

        if l1.val != l2.val:
            return False

        return self.issametree(l1.left, l2.left) and \
               self.issametree(l1.right, l2.right)

    def isSubtree(self, root, subRoot):
        if root is None:
            return False

        if self.issametree(root, subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)