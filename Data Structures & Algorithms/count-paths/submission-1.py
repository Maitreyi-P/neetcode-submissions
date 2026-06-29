class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        #dp
        
        ROWS = m - 1
        COLS = n - 1

        memo = [[-1]*n for _ in range(m)]

        def dfs(r,c):
            if r < 0 or r > ROWS or c < 0 or c > COLS:
                return 0
            
            if memo[r][c] != -1:
                return memo[r][c]

            if r == ROWS and c == COLS:
                memo[r][c] = 1
                return 1

            memo[r][c] = dfs(r,c+1) + dfs(r+1,c)
            return memo[r][c]

        return dfs(0,0)
            