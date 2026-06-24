class Solution:
    def climbStairs(self, n: int) -> int:
        
        memo = [-1]* (n+1)
        memo[n] = 1

        def rec(step):
            if step > n:
                return 0
            if memo[step] != -1:
                return memo[step]
            
            memo[step] = rec(step+1)+ rec(step+2)
            return memo[step]

        return rec(0)

