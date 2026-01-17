class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        hsh = {}
        for a in arr:
            if a not in hsh:
                hsh[a] = 0
            hsh[a] += 1
        vals = list(hsh.values())
        return len(set(vals)) == len(vals)