class ListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.head = ListNode(None, None)
        self.tail = ListNode(None, None)
        self.head.next, self.tail.prev = self.tail, self.head
        self.capacity = capacity
        self.map = {}

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.map:
            return -1
        
        node = self.map[key]
        node.prev.next = node.next
        node.next.prev = node.prev

        self.tail.prev.next = node
        node.prev = self.tail.prev
        self.tail.prev = node
        node.next = self.tail

        return node.value


    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        node = ListNode(key, value)
        node.prev = self.tail.prev
        self.tail.prev.next = node
        node.next = self.tail
        self.tail.prev = node
        self.map[key] = node
    
        if len(self.map.keys()) > self.capacity:
            del_node = self.head.next
            self.head.next = del_node.next
            self.head.next.prev = self.head
            del self.map[del_node.key]

            


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)