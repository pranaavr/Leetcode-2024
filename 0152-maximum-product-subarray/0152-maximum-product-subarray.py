class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        min_prod = max_prod = prod = nums[0]
        for n in nums[1:]:
            if n < 0:
                min_prod, max_prod = max_prod, min_prod
            max_prod = max(n, max_prod*n)
            min_prod = min(n, min_prod*n)

            prod = max(prod, max_prod)
        
        return prod