class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        counts = {}

        for i in range(len(nums)-k+1):
            sub = set(nums[i:i+k])
            for s in sub:
                if s in counts:
                    counts[s] += 1
                else:
                    counts[s] = 1
        
        ret = -1
        for num, count in counts.items():
            if count == 1:
                ret = max(ret, num)

        return ret