class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def isSubtree(self, s, t):
        if s is None:
            return False
        return self.compare(s, t) or self.isSubtree(s.left, t) or self.isSubtree(s.right, t)

    def compare(self, s, t):
        return self.traverse(s) == self.traverse(t)

    def traverse(self, n):
        string = ""
        if n.left:
            string += self.traverse(n.left) + " "
        string += n.val + " "
        if n.right:
            string += self.traverse(n.right) + " "

        return string
        
