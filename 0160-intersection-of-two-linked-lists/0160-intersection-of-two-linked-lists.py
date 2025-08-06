# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        seenA = set()
        
        while headA:
            seenA.add(headA)
            headA = headA.next

        while headB:
            if headB in seenA:
                return headB
            headB = headB.next
        
        return None