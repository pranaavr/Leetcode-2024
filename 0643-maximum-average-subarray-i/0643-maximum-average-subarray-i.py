class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        total = sum(nums[:k])
        best = total/k
        for i in range(k, len(nums)):
            total = total - nums[i-k] + nums[i]
            if total/k > best:
                best = total/k
        return best
