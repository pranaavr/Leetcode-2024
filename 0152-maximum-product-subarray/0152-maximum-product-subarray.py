class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        res = minP = maxP = nums[0]

        for num in nums[1:]:
            cands = [maxP*num, minP*num, num]

            maxP = max(cands)
            minP = min(cands)

            res = max(res, maxP)
        
        return res
            