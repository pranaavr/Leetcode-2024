# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        curr = ListNode()

        def helper(nod, list1, list2):
            if not list2:
                nod.next = list1
                return
            if not list1:
                nod.next = list2
                return
            if list1.val <= list2.val:
                nod.next = list1
                helper(nod.next, list1.next, list2)
            else:
                nod.next = list2
                helper(nod.next, list1, list2.next)
        
        helper(curr, list1, list2)
        return curr.next