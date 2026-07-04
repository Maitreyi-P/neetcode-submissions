class Solution:
    def climbStairs(self, n: int) -> int:
        
        dp = {}
        def rec(i):
            if i in dp:
                return dp[i]
            if i == 0 or i == 1:
                return 1
            else:
               dp[i] = rec(i-1) + rec(i-2)
               return dp[i]


        return rec(n)
                
            