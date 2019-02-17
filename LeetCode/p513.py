class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def findBottomLeftValue(self, root):
        row = [root]
        last_row = []
        
        while len(row) > 0:
            new_row = []
            for node in row:
                if (node.left):
                    new_row.append(node.left)
                if (node.right):
                    new_row.append(node.right)
            last_row = row
            row = new_row
            
        return last_row[0].val