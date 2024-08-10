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