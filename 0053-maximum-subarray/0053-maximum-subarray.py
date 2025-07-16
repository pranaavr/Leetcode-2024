class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        currsum = maxsum = nums[0]
        for n in nums[1:]:
            currsum = max(n, currsum + n)
            if currsum > maxsum:
                maxsum = currsum
            elif currsum < 0:
                currsum = 0
        return maxsum