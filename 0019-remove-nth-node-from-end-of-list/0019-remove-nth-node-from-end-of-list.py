# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        sentinel = ListNode()
        sentinel.next = head
        slow = sentinel
        fast = sentinel
        
        for _ in range(n + 1):
            if fast:
                fast = fast.next
            else:
                return head
        
        while fast:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next

        return sentinel.next