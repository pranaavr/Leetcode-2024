class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        z = nums.count(0)
        i = 0
        while i < len(nums)-z:
            if nums[i] == 0:
                nums.append(nums.pop(i))
            else:
                i += 1
        