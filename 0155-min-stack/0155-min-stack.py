class MinStack:

    def __init__(self):
        self.stack = []
        self.recent = None

    def push(self, val: int) -> None:
        if not self.recent:
            self.recent = val
        else:
            self.recent = min(self.recent, val)
        self.stack.append(Node(val, self.recent))

    def pop(self) -> None:
        self.stack = self.stack[:-1]

    def top(self) -> int:
        return self.stack[-1].getVal()
        
    def getMin(self) -> int:
        return self.stack[-1].getMin()


class Node:
    def __init__(self, val, mini):
        self.val = val
        self.min = mini
    
    def getVal(self):
        return self.val
    
    def getMin(self):
        return self.min

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()