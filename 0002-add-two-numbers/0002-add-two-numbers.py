# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()

        carry = False
        cur = dummy
        while l1 or l2:
            
            if not l1:
                num = l2.val
                l2 = l2.next
            elif not l2:
                num = l1.val
                l1 = l1.next
            else:
                num = l1.val + l2.val
                l1, l2 = l1.next, l2.next
            
            if carry:
                num += 1
                carry = False
            if num > 9:
                num -= 10
                carry = True
            cur.next = ListNode(num)
            cur = cur.next
        
        if carry:
            cur.next = ListNode(1)
        
        return dummy.next