from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        # best = 0

        # l, r = 0, 0
        # while r <= len(s):
        #     if len(set(s[l:r])) == (r-l):
        #         best = max(best, r-l)
        #         r += 1
        #     else:
        #         l += 1
        
        # return best

        longest = 0

        l, r = 0, 0
        cur = set()
        while r < len(s):
            if s[r] in cur:
                cur.remove(s[l])
                l += 1
            else:
                cur.add(s[r])
                longest = max(longest, r-l+1)
                r += 1
        
        return longest