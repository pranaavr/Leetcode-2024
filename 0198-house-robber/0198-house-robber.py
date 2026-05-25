class Solution:
    def rob(self, nums: List[int]) -> int:
        
        c1, c2 = 0, 0
        for num in nums:
            c1, c2 = c2, max(c1+num, c2)
        
        return max(c2, c1)