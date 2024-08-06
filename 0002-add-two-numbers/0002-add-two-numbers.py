# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        s1 = []
        curr = l1
        while curr:
            s1.append(str(curr.val))
            curr = curr.next
        s2 = []
        curr = l2
        while curr:
            s2.append(str(curr.val))
            curr = curr.next
        num1 = int(''.join(s1[::-1]))
        num2 = int(''.join(s2[::-1]))
        sm = str(num1+num2)
        sm = sm[::-1]

        dummy = ListNode(0)
        curr = dummy
        for i in sm:
            curr.next = ListNode(int(i))
            curr = curr.next

        return dummy.next