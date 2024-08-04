"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """

        if not head:
            return None

        # first pass - create interwoven
        curr = head
        while curr:
            new_node = Node(curr.val, curr.next)
            curr.next = new_node
            curr = curr.next.next
        
        # second pass - set randoms
        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next

        # extract copies
        original = head
        point = head.next
        copy = point
        while original:
            original.next = original.next.next
            copy.next = copy.next.next if copy.next else None
            original, copy = original.next, copy.next
        return point