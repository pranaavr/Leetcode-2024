class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        c1, c2 = 0, 0
        cand1, cand2 = None, None

        for num in nums:
            if num == cand1:
                c1 += 1
            elif num == cand2:
                c2 += 1
            elif c1 == 0:
                cand1, c1 = num, 1
            elif c2 == 0:
                cand2, c2 = num, 1
            else:
                c1 -= 1
                c2 -= 1
        

        ret = set()
        for cand in (cand1, cand2):
            if nums.count(cand) > len(nums)//3:
                ret.add(cand)
        return list(ret)