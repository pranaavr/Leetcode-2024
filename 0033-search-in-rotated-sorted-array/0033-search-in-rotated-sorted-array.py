class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums) - 1

        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid

            if nums[low] <= nums[mid]: # this means the left half is sorted
                if nums[low] <= target < nums[mid]:
                    high = mid - 1     # target has to be in the left half since we know its sorted
                else:
                    low = mid + 1   # target is in the other half
            else: # why would this side be sorted?
                if nums[mid] < target <= nums[high]:
                    low = mid + 1   # target is in right half
                else:
                    high = mid - 1  # target is in left half
        
        return -1

