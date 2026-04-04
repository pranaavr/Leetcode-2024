import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        piles.sort()

        l = 1
        r = piles[-1]

        best = r
        while l <= r:
            k = (l+r)//2    # bananas per hour
            
            # calculate total hours
            tot = 0
            for p in piles:
                tot += math.ceil(p/k)
            
            if tot <= h: # if total hours less than h, eating speed needs to decrease
                best = k
                r = k - 1
            else: # if total hours more than h, eating speed needs to increase
                l = k + 1
        
        return best
            
