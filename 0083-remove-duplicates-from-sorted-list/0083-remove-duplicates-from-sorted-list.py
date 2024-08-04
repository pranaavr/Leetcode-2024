# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        first = head
        while first:
            second = first.next
            while second and first.val == second.val:
                second = second.next
            first.next = second
            first = second
        return head