class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
        
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    
    def __repr__(self):
        node = self
        string = ""
        while node:
            string += str(node.val)
            string += " -> "
            node = node.next
        return string[:-4]

def build_linked_list(arr):
    head = ListNode(arr[0])
    node = head
    for i in range(1, len(arr)):
        new = ListNode(arr[i])
        node.next = new
        node = new
    return head
