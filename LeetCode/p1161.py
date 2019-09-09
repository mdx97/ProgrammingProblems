from common import TreeNode

class Solution(object):
    def maxLevelSum(self, root):
        level = 1
        level_nodes = [root]
        
        maximum = 0
        maximum_level = 0
        
        while level_nodes:
            next_level = []
            total = 0
            
            for node in level_nodes:
                total += node.val
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            
            if total > maximum:
                maximum = total
                maximum_level = level
            
            level_nodes = next_level
            level += 1
        
        return maximum_level
