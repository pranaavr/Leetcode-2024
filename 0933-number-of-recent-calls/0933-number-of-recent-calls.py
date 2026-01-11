class RecentCounter:

    def __init__(self):
        self.pings = []
        

    def ping(self, t: int) -> int:
        self.pings.append(t)
        mini = t-3000
        for i in range(len(self.pings)):
            if self.pings[i] < mini:
                self.pings.pop(i)
            else:
                break
        return len(self.pings)
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)