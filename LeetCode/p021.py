from common import ListNode

# Basic Solution: Build a new list.
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        p2 = l2
        head = None
        curr = None

        while p1 and p2:
            node = ListNode(0)

            if p1.val <= p2.val:
                node.val = p1.val
                p1 = p1.next
            else:
                node.val = p2.val
                p2 = p2.next

            if curr:
                curr.next = node
            else:
                head = node

            curr = node

        for pointer in [p1, p2]:
            while pointer:
                node = ListNode(pointer.val)
                if curr:
                    curr.next = node
                else:
                    head = node
                curr = node
                pointer = pointer.next


        return head

# Node Reuse Solution.
# What a behemoth but is actually pretty fast and memory efficient.
class Solution2(object):
    def mergeTwoLists(self, l1, l2):
        if l1 is None and l2 is None:
            return None
        elif l1 is None:
            return l2
        elif l2 is None:
            return l1
        
        head = None
        
        if l1.val <= l2.val:
            head = l1
            l1 = l1.next
        else:
            head = l2
            l2 = l2.next
        
        last = head

        while l1 and l2:
            if l1.val <= l2.val:
                last.next = l1
                last = l1
                l1 = l1.next
            else:
                last.next = l2
                last = l2
                l2 = l2.next
        
        if l1:
            last.next = l1
        
        if l2:
            last.next = l2

        return head
            