class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        best = 0

        l, r = 0, 0
        while r <= len(s):
            if len(set(s[l:r])) == (r-l):
                best = max(best, r-l)
                r += 1
            else:
                l += 1
        
        return best
