class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        dp = {}
        
        def dfs(i,a):
            if a == 0:
                return 1
            if i >= len(coins):
                return 0
            if a < 0:
                return 0
            
            if (i,a) in dp:
                return dp[(i,a)]

            #use 
            use = dfs(i, a - coins[i])
            
            #skip
            skip = dfs(i + 1, a)

            dp[(i,a)] = use + skip
            return dp[(i,a)]

        return dfs(0,amount)