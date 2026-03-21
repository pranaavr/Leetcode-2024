from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cts = defaultdict(int)
        for n in nums:
            cts[n] += 1
        
        res = []
        buckets = [[] for _ in range(len(nums)+1)]

        # create buckets
        for key, val in cts.items():
            buckets[val].append(key)
        
        for i in range(len(buckets) - 1, 0, -1):
            for n in buckets[i]:
                res.append(n)
                if len(res) == k:
                    return res