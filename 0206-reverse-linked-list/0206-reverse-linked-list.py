# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        full = []
        while head:
            full.append(head.val)
            head = head.next
        full = full[::-1]    
        head, curr = None, None
        for i in full:
            if not head:
                head = ListNode(i)
                curr = head
            else:
                curr.next = ListNode(i)
                curr = curr.next
        return head