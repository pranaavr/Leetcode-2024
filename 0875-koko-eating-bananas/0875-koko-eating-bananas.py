import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        l = 1
        r = max(piles)

        best = r
        while l <= r:
            k = (l+r)//2    # bananas per hour
            
            # calculate total hours
            tot = 0
            for p in piles:
                tot += math.ceil(p/k)
            
            if tot <= h: # if total hours less than h, eating speed needs to decrease
                best = min(best, k)
                r = k - 1
            else: # if total hours more than h, eating speed needs to increase
                l = k + 1
        
        return best
            
