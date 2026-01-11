class Solution:
    def waysToBuyPensPencils(self, total: int, cost1: int, cost2: int) -> int:
        count = 0

        mx = total//cost1

        for i in range(0, mx+1):
            pens = i * cost1
            diff = total - pens
            c = diff//cost2
            count += c + 1
        
        return count