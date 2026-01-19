class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        s = list(s)
        for c in t:
            if s[0] == c:
                s.pop(0)        
            if not s:
                return True
        return False
