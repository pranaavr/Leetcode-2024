class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(i, curr):
            if i == len(nums):
                res.append(curr[:])
                return
            # choice 1: don't include nums[i]
            backtrack(i + 1, curr)
            # choice 2: include nums[i]
            curr.append(nums[i])
            backtrack(i + 1, curr)
            curr.pop()

        backtrack(0, [])
        return res