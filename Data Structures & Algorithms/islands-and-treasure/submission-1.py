class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        #BFS is always the best for shortest path in unweighted grid

        INF = 2147483647

        directions = [[-1,0],[1,0],[0,-1],[0,1]]

        ROWS = len(grid)
        COLS = len(grid[0])


        def bfs(r,c):
            q = deque([[r,c]])
            visited = [[False] * COLS for _ in range(ROWS)]
            visited[r][c] = True

            steps = 0
            while q:
                for _ in range(len(q)):
                    row,col = q.popleft()
                    if grid[row][col] == 0:
                        return steps

                    for dr,dc in directions:
                        nr,nc = row+dr, col+dc
                        if nr >= 0 and nc>=0 and nr<ROWS and nc<COLS and not visited[nr][nc] and grid[nr][nc]!= -1:
                            visited[nr][nc] = True
                            q.append([nr,nc])
                steps+=1

            return INF

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == INF:
                    grid[r][c] = bfs(r,c)
             