# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # reversal
        # prev = None
        # curr = head
        # while curr:
        #     forward = curr.next
        #     curr.next = prev
        #     prev = curr
        #     curr = forward
        lst = []
        while head:
            lst.append(head.val)
            head = head.next
        if lst == lst[::-1]:
            return True
        return False
        