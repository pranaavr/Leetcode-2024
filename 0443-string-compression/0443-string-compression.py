class Solution:
    def compress(self, chars: List[str]) -> int:
        i = 0
        w = 0
        n = len(chars)
        while i < n:
            f = i
            while f < len(chars) and chars[f] == chars[i]:
                f += 1
            chars[w] = chars[i]
            w += 1
            if f-i > 1:
                for c in str(f-i):
                    chars[w] = c
                    w += 1
            i = f
        
        return w
        
        