class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        mem = {}

        def trav(cur):
            
            if cur == 0:
                return 0 
            if cur in mem:
                return mem[cur]

            best = float('inf')
            for coin in coins:
                if cur-coin >= 0:
                    best = min(best, trav(cur-coin)+1)        
            mem[cur] = best
            return best
        
        res = trav(amount)
        return res if res <= amount else -1