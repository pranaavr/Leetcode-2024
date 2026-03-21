from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hsh = defaultdict(list)
        for s in strs:
            hsh[tuple(sorted(s))].append(s)
        return list(hsh.values())