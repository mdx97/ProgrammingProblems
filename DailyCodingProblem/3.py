"""
Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s), which deserializes the string back into the tree.
"""

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def assign_child(self, node, side):
        if side == 'l':
            self.left = node
        elif side == 'r':
            self.right = node

def serialize(root):
    def preorder(node):
        string = node.val + " "
        if node.left:
            string += "l " + preorder(node.left)
        if node.right:
            string += "r " + preorder(node.right)
        string += "u "
        return string
    return preorder(root)[:-1]

def deserialize(s):
    tokens = s.split()
    root = Node(tokens[0])
    tokens = tokens[1:]
    stack = [root]
    i = 0
    while i < len(tokens):
        operator = tokens[i]
        if operator == 'u':
            stack.pop()
        else:
            new = Node(tokens[i + 1])
            parent = stack[-1]
            parent.assign_child(new, operator)
            stack.append(new)
            i += 1
        i += 1
    return root
        
node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'