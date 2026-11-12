class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        ROWS = len(grid)
        COLS = len(grid[0])
        islands = 0

        def bfs(r,c):
            q = deque()
            q.append((r,c))

            while q:
                row, col = q.popleft()
                if row<0 or row>=ROWS or col < 0 or col >= COLS or grid[row][col] == "0":
                    continue
                grid[row][col] = "0"
                q.append((row+1,col))
                q.append((row-1,col))
                q.append((row, col+1))
                q.append((row, col-1))

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    islands += 1
                    bfs(r,c)

        return islands

                
                    
                