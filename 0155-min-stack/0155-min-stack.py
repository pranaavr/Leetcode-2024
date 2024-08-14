class MinStack(object):

    def __init__(self):
        self.stack = []
        self.min = []
        

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.stack.append(val)
        if self.min:
            if val <= self.min[-1]:
                self.min.append(val)
        else:
            self.min.append(val)
        

    def pop(self):
        """
        :rtype: None
        """
        pop = self.stack.pop()
        if pop == self.min[-1]:
            self.min.pop()
        return pop
        

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.min[-1]
        
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()