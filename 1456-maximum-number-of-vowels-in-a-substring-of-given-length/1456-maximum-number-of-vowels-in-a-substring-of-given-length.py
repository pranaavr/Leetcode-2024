class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vs = { 'a', 'e', 'i', 'o', 'u'}

        cnt = 0
        for c in s[:k]:
            if c in vs:
                cnt += 1
        
        mx = cnt

        for i in range(k, len(s)):
            if s[i] in vs:
                cnt += 1
            if s[i-k] in vs:
                cnt -= 1
            if cnt > mx:
                mx = cnt
        
        return mx