# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        n = -1
        count = head
        while count:
            count = count.next
            n += 1
        
        print(n)

        res = 0
        curr = head
        while curr:
            if curr.val == 1:
                res += 2**n
            curr = curr.next
            n -= 1
        
        return res
        