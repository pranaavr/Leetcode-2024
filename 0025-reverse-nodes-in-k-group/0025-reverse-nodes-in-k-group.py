# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        group_prev = dummy        
        
        while True:
            kth = group_prev
            for _ in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next
            group_next = kth.next

            prev = group_next
            temp = group_prev.next
            while temp != group_next:
                front = temp.next
                temp.next = prev
                prev = temp
                temp = front
            
            front = group_prev.next
            group_prev.next = kth
            group_prev = front

        return dummy.next
            
            
                