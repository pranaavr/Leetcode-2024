class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        seen = list(set(nums))
        seen.sort()
        nums[:len(seen)] = seen
        return len(seen)