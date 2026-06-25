class Solution:
    def numDecodings(self, s: str) -> int:

        dp = [-1]*len(s)

        def dfs(i):
            if i == len(s):
                return 1
            if s[i] == "0":
                return 0
            if i > len(s):
                return 0

            if dp[i] != -1:
                return dp[i]

            res =  dfs(i+1) 

            if i < len(s) -1:
                if s[i] < "3" and s[i]+s[i+1] <= "26":
                    res+= dfs(i+2)
            
            dp[i] = res
                
            return dp[i]

        return dfs(0)
                
            