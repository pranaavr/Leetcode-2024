class Solution:
    def rob(self, nums: List[int]) -> int:

        p1 = p2 = 0
        
        for n in nums:
            p1, p2 = p2, max(n+p1, p2)
        
        return max(p1, p2)


        