class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        nums.sort()

        prev = nums[0]
        longest_len = 1
        curr_len = 1
        for n in nums[1:]:
            if n-prev == 1:
                curr_len += 1
                if curr_len > longest_len:
                    longest_len = curr_len
            elif prev == n:
                pass
            else:
                curr_len = 1
            prev = n

        return longest_len