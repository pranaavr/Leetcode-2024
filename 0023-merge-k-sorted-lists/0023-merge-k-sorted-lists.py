# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        curr = dummy = ListNode()
        
        while curr:
            vals = []
            min_val, min_index = float('inf'), -1
            for i in range(len(lists)):
                if lists[i] and lists[i].val < min_val:
                    min_val = lists[i].val
                    min_index = i
            if min_index == -1:
                break

            curr.next = lists[min_index]
            lists[min_index] = lists[min_index].next
            curr = curr.next
            
        return dummy.next
