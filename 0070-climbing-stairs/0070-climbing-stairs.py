class Solution:
    def climbStairs(self, n: int) -> int:
        
        if n <= 2:
            return n

        dp = [0]*(n+1)
        for i in range(len(dp)):
            if i <= 2:
                dp[i] = i
            else:
                dp[i] = dp[i-1]+dp[i-2]
        
        return dp[n]