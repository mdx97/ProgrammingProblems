from common import ListNode, build_linked_list

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        return self.toLinkedList(self.toNumber(l1) + self.toNumber(l2))
    
    def toNumber(self, ll):
        exponent = 0
        node = ll
        total = 0
        while node:
            digit = node.val
            total += (digit * 10**exponent)
            exponent += 1
            node = node.next
        return total

    def toLinkedList(self, number):
        if number == 0:
            return ListNode(0)
        head = None
        node = None
        while number > 0:
            digit = number % 10
            new = ListNode(digit)
            if head is None:
                head = new
            else:
                node.next = new
            node = new
            number = number // 10
        return head

sol = Solution()
ll1 = build_linked_list([2, 4, 3])
ll2 = build_linked_list([5, 6, 4])
print(sol.addTwoNumbers(ll1, ll2))