class MedianFinder:

    def __init__(self):
        # root is highest number
        self.lower = []
        # root is lowest number
        self.upper = []

    def addNum(self, num: int) -> None:
        if self.upper and num > self.upper[0]:
            heapq.heappush(self.upper, num)
        else:
            heapq.heappush(self.lower, -num)
        
        # rebalance
        if len(self.lower) - len(self.upper) > 1:
            heapq.heappush(self.upper, -heapq.heappop(self.lower))
        elif len(self.upper) - len(self.lower) > 1:
            heapq.heappush(self.lower, -heapq.heappop(self.upper))

    def findMedian(self) -> float:
        if len(self.lower) > len(self.upper):
            return -self.lower[0]
        elif len(self.upper) > len(self.lower):
            return self.upper[0]
        return (-self.lower[0] + self.upper[0]) / 2.0


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()