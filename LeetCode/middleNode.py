import math

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def middleNode(self, head):
    length = 0
    node = head

    while (node.next != None):
        length += 1
        node = node.next
    
    mid = math.ceil(length / 2)
    node = head

    for x in range(0, int(mid) - 1):
        node = node.next
    
    return node