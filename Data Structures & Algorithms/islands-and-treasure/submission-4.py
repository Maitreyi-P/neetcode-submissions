class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        

        INF = 2147483647
        ROWS = len(grid)
        COLS = len(grid[0])

        directions = [(-1,0),(1,0), (0,1), (0,-1)]

        q = deque()
        visit = set()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r,c))
                    visit.add((r,c))

        path = 0
        while q:
            for i in range(len(q)):
                r,c = q.popleft()
                grid[r][c] = path
                
                for dr,dc in directions:
                    nr,nc = r+dr, c+dc
                    if nr < 0 or nc < 0 or nr >= ROWS or nc >= COLS or grid[nr][nc] == -1 or (nr,nc) in visit:
                        continue
                    q.append((nr,nc))
                    visit.add((nr,nc))

            path += 1


                          


        
