class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        l = 0
        r = len(nums)-1

        nums.sort()
        ops = 0
        while l < r:
            if nums[r] + nums[l] == k:
                r -= 1
                l += 1
                ops += 1
            elif nums[r] + nums[l] > k:
                r -= 1
            else:
                l += 1
        return ops
