# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # def reverse(head):
        #     curr = head
        #     prev = None
        #     while curr:
        #         nxt = curr.next
        #         curr.next = prev
        #         prev = curr
        #         curr = nxt
        #     return prev

        # l1 = reverse(l1)
        # l2 = reverse(l2)

        dummy = ListNode()
        curr = dummy
        carry = 0
        
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            sm = val1 + val2 + carry
            carry = sm // 10
            sm = sm % 10

            curr.next = ListNode(sm)
            curr = curr.next
            if l1: l1 = l1.next
            if l2: l2 = l2.next
        
        if carry:
            curr.next = ListNode(carry)
        
        return dummy.next
        
            