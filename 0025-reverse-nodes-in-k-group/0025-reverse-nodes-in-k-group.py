# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        def reverse(head, k):
            curr = head
            prev = None
            while k > 0:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
                k -= 1
            return prev
        
        dummy = ListNode()
        dummy.next = head
        prev_group = dummy
        while True:
            kth = prev_group
            count = 0
            while kth and count < k:
                kth = kth.next
                count += 1
            if not kth:
                break
            
            next_group = kth.next
            kth.next = None

            new_group_head = reverse(prev_group.next, k)
            old_group_head = prev_group.next
            prev_group.next = new_group_head
            old_group_head.next = next_group

            prev_group = old_group_head
        
        return dummy.next
