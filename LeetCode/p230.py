class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def kthSmallest(self, root, k):
        def in_order(node):
            if not node.left and not node.right:
                return [node.val]
            traversal = []
            if node.left:
                traversal.extend(in_order(node.left))
            traversal.append(node.val)
            if node.right:
                traversal.extend(in_order(node.right))
            return traversal

        return in_order(root)[k - 1]

root = TreeNode(1)
root.right = TreeNode(2)
sol = Solution()
print(sol.kthSmallest(root, 2))