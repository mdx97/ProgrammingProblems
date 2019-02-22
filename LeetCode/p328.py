from common import ListNode, build_linked_list

# Solution: Build LL of odd nodes and even nodes then splice together.
class Solution(object):
    def oddEvenList(self, head):
        if not head:
            return None
        if not head.next:
            return head
        odd_head = ListNode(head.val)
        odd = odd_head 
        even_head = ListNode(head.next.val) 
        even = even_head 
        node = head.next.next
        parity = 0
        while node:
            new = ListNode(node.val)
            if parity == 0:
                odd.next = new
                odd = new
            else:
                even.next = new
                even = new
            node = node.next
            parity = abs(parity - 1)
        odd.next = even_head
        return odd_head

head = build_linked_list([1, 2, 3, 4, 5])
sol = Solution()
new = sol.oddEvenList(head)
print(new)
