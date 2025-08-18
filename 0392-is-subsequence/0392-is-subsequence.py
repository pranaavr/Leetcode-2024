class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        sl = list(s)
        for c in t:
            if c == sl[0]:
                sl = sl[1:]
                if not sl:
                    return True
        return False