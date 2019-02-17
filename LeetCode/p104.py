class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def maxDepth(self, root):
        if not root:
            return 0
        return self.depth(root)
    
    def depth(self, node):
        if (not node.left and not node.right):
            return 1
        left = 0
        right = 0
        if node.left:
            left = self.depth(node.left)
        if node.right:
            right = self.depth(node.right)
        
        return 1 + max(left, right)