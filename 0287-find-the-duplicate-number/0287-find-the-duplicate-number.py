class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_number = len(nums)-1

        for i in range(1, max_number+1):
            if nums.count(i) >= 2:
                return i
        
