class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        i = 0
        ct = 0
        mx = 0

        for j in range(len(nums)):
            if nums[j] == 0:
                ct += 1
            
            while ct > k:
                if nums[i] == 0:
                    ct -= 1
                i += 1
            
            mx = max(mx, j-i+1)
        
        return mx