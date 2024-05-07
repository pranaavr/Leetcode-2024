# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        hit = []
        curr = head
        while curr:
            if curr.val == 'x':
                return True
            else:
                curr.val = 'x'
            curr = curr.next
        return False
            
