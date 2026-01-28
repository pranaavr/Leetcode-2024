class Solution:
    def tribonacci(self, n: int) -> int:
        mem = {}

        def trib(n):
            if n in mem:
                return mem[n]
            if n == 0:
                return 0
            if n == 1 or n == 2:
                return 1
            res = trib(n-1) + trib(n-2) + trib(n-3)
            mem[n] = res
            return res
        
        seq = trib(n)
        return seq
        
