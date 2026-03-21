from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cts = defaultdict(int)
        for n in nums:
            cts[n] += 1
        
        ret = []
        l = [[] for _ in range(len(nums)+1)]

        # create buckets
        for key, val in cts.items():
            l[val].append(key)
        
        while len(ret) < k:
            cur = l.pop()
            if len(cur) > 0:
                ret.extend(cur[:k-len(ret)+1])
        return ret