class Solution:
    def climbStairs(self, n: int) -> int:
        
        dp = {}
        dp[0] = 1
        dp[1] = 1

        def rec(n):
            if n in dp:
                return dp[n]
            else:
                dp[n] = rec(n-1) + rec(n-2)
                return dp[n]
        
        res = rec(n)
        return res