from common import TreeNode

class Solution(object):
    def pruneTree(self, root):
        self.pruneTreeRC(root)
        return root
    
    def pruneTreeRC(self, root):
        if root is None:
            return False
        left_has_1 = self.pruneTreeRC(root.left)
        right_has_1 = self.pruneTreeRC(root.right)
        if not left_has_1:
            root.left = None
        if not right_has_1:
            root.right = None
        return root.val == 1 or left_has_1 or right_has_1

sol = Solution()
root = TreeNode(1)
root.left = TreeNode(0)
root.right = TreeNode(1)
root.right.right = TreeNode(0)
root.right.left = TreeNode(1)
sol.pruneTree(root)