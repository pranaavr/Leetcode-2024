class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        res = []
        m = max(candies)
        for c in candies:
            if extraCandies + c >= m:
                res.append(True)
            else:
                res.append(False)
        return res