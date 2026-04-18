# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev_group = dummy

        while True:
            # check
            kth = prev_group
            c = k
            while kth and c > 0:
                kth = kth.next
                c -= 1
            if not kth:
                break
            
            # reverse
            prev, cur = kth.next, prev_group.next
            for _ in range(k):
                tmp = cur.next
                cur.next = prev
                prev = cur
                cur = tmp
            
            # reattach
            tmp = prev_group.next
            prev_group.next = kth
            prev_group = tmp

        
        return dummy.next