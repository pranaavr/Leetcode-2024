# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return
            
        # find length
        length, iter = 0, head
        while iter:
            iter = iter.next
            length+=1
        
        # set ptr at midway point
        count, iter = 0, head
        while iter:
            if count == (length // 2) - 1:
                prev = iter
                mid = iter.next
                prev.next = None
                break
            iter = iter.next
            count += 1
        
        prev, curr = None, mid
        while curr:
            next_temp = curr.next
            curr.next = prev
            prev = curr
            curr = next_temp
        mid = prev

        first, second = head, mid
        while first:
            temp1, temp2 = first.next, second.next
            first.next = second
            if temp1 is None:
                break
            second.next = temp1
            first, second = temp1, temp2
        

        