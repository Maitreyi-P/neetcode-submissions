class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        
        ROWS = len(matrix)
        COLS = len(matrix[0])

        dp = {}

        def dfs(i,j, prev):
            
            if i < 0 or i >= ROWS or j < 0 or j >= COLS:
                return 0

            if matrix[i][j] <= prev:
                return 0

            if (i,j) in dp:
                return dp[(i,j)]
            
            prev = matrix[i][j]
            res = max(dfs(i+1,j,prev),dfs(i-1,j,prev),dfs(i,j+1,prev),dfs(i,j-1,prev))

            dp[(i,j)] = res + 1
            return dp[(i,j)]

        ans = 0

        for i in range(ROWS):
            for j in range(COLS):
                ans = max(ans, dfs(i,j,-1))
        return ans

            