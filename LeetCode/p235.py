from common import TreeNode

# Binary Search.
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        def binary_search(node):
            if p.val < node.val and q.val < node.val:
                return binary_search(node.left)
            elif p.val > node.val and q.val > node.val:
                return binary_search(node.right)
            return node
        
        return binary_search(root)
