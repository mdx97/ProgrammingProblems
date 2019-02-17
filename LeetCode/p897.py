from common import TreeNode

class Solution(object):
    def increasingBST(self, root):
        if not root:
            return None
        all_values = self.traverse(root)
        last_node = None
        first_node = None
        
        for val in all_values:
            node = TreeNode(val)
            if (not first_node):
                first_node = node
            if (last_node):
                last_node.right = node
            last_node = node
        
        return first_node
            
    def traverse(self, node):
        values = []
        if (node.left):
            values.extend(self.traverse(node.left))
            
        values.append(node.val)
        
        if (node.right):
            values.extend(self.traverse(node.right))
            
        return values
