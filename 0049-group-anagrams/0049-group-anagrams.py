class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        map = {}
        for st in strs:
            s = ''.join(sorted(st))
            if s in map.keys():
                map[s].append(st)
            else:
                map[s] = [st]
        return map.values()