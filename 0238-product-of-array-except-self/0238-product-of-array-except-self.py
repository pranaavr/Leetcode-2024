class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = 1
        suf = 1
        res = [0]*len(nums)
        for i in range(len(nums)):
            res[i] = pre
            pre *= nums[i]
        for j in range(len(nums)-1, -1, -1):
            res[j] *= suf
            suf *= nums[j]
        return res