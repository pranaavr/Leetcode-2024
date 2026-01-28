class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        n = len(cost)
        cost.append(0)

        mem = {}
        # n-1 or n-2
        def rec(n):
            if n in mem:
                return mem[n]
            if n == 0:
                return cost[0]
            if n == 1:
                return cost[1]
            if rec(n-1) < rec(n-2):
                mem[n] = cost[n] + rec(n-1)
                return mem[n]
            else:
                mem[n] = cost[n] + rec(n-2)
                return mem[n]            
        
        return rec(n)