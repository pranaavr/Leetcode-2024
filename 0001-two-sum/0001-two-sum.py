class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        for i in range(len(nums)):
            val = target - nums[i]
            if val in nums and nums.index(val) != i:
                return [i, nums.index(val)]

        for i,n in enumerate(nums):
            val = target - n
            if val in nums:
                i2 = [i for i, n in enumerate(nums) if n == val]
                return [i, i2]
        
        return []