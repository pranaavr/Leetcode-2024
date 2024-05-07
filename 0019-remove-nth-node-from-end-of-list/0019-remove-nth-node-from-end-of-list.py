# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        lst = []
        while curr:
            lst.append(curr.val)
            curr = curr.next
        del lst[-n]
        head, curr = None, None
        for l in lst:
            if not head:
                head = ListNode(l)
                curr = head
            else:
                curr.next = ListNode(l)
                curr = curr.next
        return head