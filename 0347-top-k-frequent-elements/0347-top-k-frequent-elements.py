class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        map = {}
        for n in nums:
            if n in map:
                map[n] += 1
            else:
                map[n] = 1

        frequencies = list(map.items())
        frequencies.sort(key=lambda a: a[1], reverse=True)
        return [element for element, count in frequencies[:k]]