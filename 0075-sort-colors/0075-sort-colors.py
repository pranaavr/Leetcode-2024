class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        low, mid, high = 0, 0, len(nums)-1      # mid is basically the pointer thats actually iterating and checking everything
        while mid <= high:
            if nums[mid] == 0:          
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:        # don't do anything, check the next position
                mid += 1
            else:                       # nums[mid] == 2, switch the numbers at high and mid position. we know that high is 2 now, so go to next position (back 1)
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1        
