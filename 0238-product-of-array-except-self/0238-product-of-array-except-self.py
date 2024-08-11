class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        def find_product(list):
            product = 1
            for l in list:
                product *= l
            return product

        answer = []
        for n in range(len(nums)):
            n2 = nums[:n]+nums[n+1:]
            answer.append(find_product(n2))
        
        return answer