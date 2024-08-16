class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        map = {}
        for i in range(len(numbers)):
            # if (target-value) is a key in map
            if target-numbers[i] in map:
                return [map[target-numbers[i]]+1, i+1]
            else:
                map[numbers[i]] = i
