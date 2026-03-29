class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()

        res = []
        for i in range(len(nums)):
            if nums[i] > 0:
                break

            if i > 0 and nums[i] == nums[i-1]:
                continue
                     
            l = i+1
            r = len(nums)-1
            while l < r:
                cur = [nums[i], nums[l], nums[r]]
                tot = sum(cur)
                if tot > 0:
                    r -= 1
                elif tot < 0:
                    l += 1
                else:
                    res.append(cur)
                    r -= 1
                    l += 1
                    while l < len(nums) and nums[l] == nums[l-1]:
                        l += 1
        
        return res
