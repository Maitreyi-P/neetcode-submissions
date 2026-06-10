class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        # BFS - sam but use queue

        
        directions=[[1, 0], [-1, 0], [0, 1], [0, -1]]
        ROWS = len(grid)
        COLS = len(grid[0])
        islands = 0

        def bfs(r,c):
            q = []
            grid[r][c] = "0"
            q.append((r, c))
            while q:
                row,col = q.pop()
                for dr, dc in directions:
                    nr, nc = row+dr, col+dc
                    if (nr<0 or nc<0 or nr>=ROWS or nc>= COLS or grid[nr][nc] == "0"):
                        continue
                    q.append((nr,nc))
                    grid[nr][nc] = "0"

        for r in range(ROWS):
            for c in range(COLS):
                 if grid[r][c] == "1":
                        islands+=1
                        bfs(r,c)
        
        return islands
                    

