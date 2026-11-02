class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        
        ROWS = len(grid)
        COLS = len(grid[0])

        if grid[0][0] == 1 or grid[ROWS-1][COLS-1] == 1:
            return -1 

        directions = [[-1,0],[1,0],[0,-1],[0,1],[-1,-1],[-1,1],[1,-1],[1,1]]

        q = deque()
        visit = set()
        q.append((0,0))


        path = 1
        while q:
            curr = 0
            for i in range(len(q)):
                r,c = q.popleft()
                if r<0 or r>=ROWS or c<0 or c>=COLS or (r,c) in visit or grid[r][c] == 1:
                    continue
                
                visit.add((r,c))
                if r == ROWS - 1 and c == COLS -1:
                    return path

                for dr,dc in directions:
                    nr,nc = r+dr, c+dc
                    q.append((nr,nc))

            path += 1


        return -1



            