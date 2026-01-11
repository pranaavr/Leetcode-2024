class RecentCounter:

    def __init__(self):
        self.pings = []
        

    def ping(self, t: int) -> int:
        self.pings.append(t)
        mini = t-3000
        i = 0
        while True:
            curr = self.pings[i]
            if curr < mini:
                i += 1
            else:
                self.pings = self.pings[i:]
                break
        return len(self.pings)
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)