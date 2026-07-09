class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        ROWS = len(grid)
        COLS = len(grid[0])

        maxarea = 0

        def dfs(r,c):
            if r<0 or r >= ROWS or c < 0 or c >= COLS or grid[r][c] == 0:
                return 0

            grid[r][c] = 0

            currarea = 1

            currarea += dfs(r+1,c)
            currarea += dfs(r-1,c)
            currarea += dfs(r,c+1)
            currarea += dfs(r,c-1)

            return currarea

        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    maxarea = max(maxarea,dfs(r,c))

        return maxarea
