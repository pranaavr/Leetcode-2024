class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr = total = nums[0]
        for n in nums[1:]:
            curr = max(curr+n, n)
            total = max(curr, total)
        return total
