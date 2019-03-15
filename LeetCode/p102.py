from common import TreeNode

class Solution(object):
    def levelOrder(self, root):
        if not root:
            return []
        nodes = [root]
        traversal = []
        while nodes:
            level = [node.val for node in nodes]
            traversal.append(level)
            new = []
            for node in nodes:
                if node.left:
                    new.append(node.left)
                if node.right:
                    new.append(node.right)
            nodes = new
        return traversal

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
sol = Solution()
print(sol.levelOrder(root))