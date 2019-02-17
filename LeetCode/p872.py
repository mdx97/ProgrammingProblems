class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def leafSimilar(self, root1, root2):
        root1_seq = self.getLeafSequence(root1)
        root2_seq = self.getLeafSequence(root2)
        
        if (len(root1_seq) != len(root2_seq)):
            return False
        
        same = True
        
        for i in range(len(root1_seq)):
            if (root1_seq[i] != root2_seq[i]):
                same = False
        
        return same

    def getLeafSequence(self, node):
        if (not node.left and not node.right):
            l = []
            l.append(node.val)
            return l
        
        seq_left = []
        seq_right = []
        
        if (node.left):
            seq_left = self.getLeafSequence(node.left)
        if (node.right):
            seq_right = self.getLeafSequence(node.right)
        
        sequence = []
        
        for num in seq_left:
            sequence.append(num)
        for num in seq_right:
            sequence.append(num)
        
        return sequence