from common import TreeNode

# Depth-First Search.
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        lca = root
        
        def dfs(node):
            nonlocal lca
            me = node.val == p.val or node.val == q.val
            left = dfs(node.left) if node.left else False
            right = dfs(node.right) if node.right else False
            
            if (left and right) or (me and left) or (me and right):
                lca = node

            return me or left or right

        dfs(root)
        return lca