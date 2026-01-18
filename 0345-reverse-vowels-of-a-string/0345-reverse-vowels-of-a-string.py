class Solution:
    def reverseVowels(self, s: str) -> str:
        j = []
        v = []
        for i in range(len(s)):
            if s[i].lower() in {'a', 'e', 'i', 'o', 'u'}:
                v.append(s[i])
                j.append(i)
        
        chars = list(s)
        for c in v:
            chars[j.pop()] = c
        
        return "".join(chars)
        
        