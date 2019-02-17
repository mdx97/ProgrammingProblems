class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children

class Solution(object):
    def maxDepth(self, root):
        if not root:
            return 0
        if len(root.children) == 0:
            return 1
        depths = []
        for i in range(len(root.children)):
            depths.append(self.maxDepth(root.children[i]))
            
        return 1 + max(depths)