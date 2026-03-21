from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cts = defaultdict(int)
        for n in nums:
            cts[n] += 1
        l = list(cts.items())
        l.sort(key = lambda x:x[1])
        return [x[0] for x in l[-k:]]
        