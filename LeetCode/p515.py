from common import TreeNode

class Solution(object):
    def largestValues(self, root):
        if not root:
            return []
        
        row = [root]
        maxs = []
        
        while len(row) > 0:
            node_vals = []
            for node in row:
                node_vals.append(node.val)
            
            maxs.append(max(node_vals))
            
            new_row = []
            for node in row:
                if (node.left):
                    new_row.append(node.left)
                if (node.right):
                    new_row.append(node.right)
            
            row = new_row
            
        return maxs
