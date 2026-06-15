class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        ROWS = len(grid)
        COLS = len(grid[0])

        visit = set()
        q = deque()
        time = 0
        fresh = 0

        def add(r,c):
            nonlocal fresh
            if r<0 or r>=ROWS or c<0 or c>=COLS or grid[r][c] == 0 or (r,c) in visit:
                return 
            visit.add((r,c))
            grid[r][c] = 2
            fresh-=1
            q.append((r,c))

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r,c))
                    visit.add((r,c))
                elif grid[r][c] == 1:
                    fresh+=1

        while q and fresh >0:
            for i in range(len(q)):
                r,c = q.popleft()

                add(r-1,c)
                add(r+1,c)
                add(r,c-1)
                add(r,c+1)

            time += 1

        if fresh > 0:
            return -1
        return time

        



      
                