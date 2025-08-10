class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_con = 0
        curr_con = 0
        for n in nums:
            if n == 1:
                curr_con += 1
            else:
                max_con = max(max_con, curr_con)
                curr_con = 0
        return max(max_con, curr_con)