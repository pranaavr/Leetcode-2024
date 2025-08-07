# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = slow = head
        cycle = False
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                cycle = True
                break
        if cycle:
            seen = set()
            while slow:
                if slow in seen:
                    break
                seen.add(slow)
                slow = slow.next
            fast = head
            while fast:
                if fast in seen:
                    return fast
                fast = fast.next
        return None