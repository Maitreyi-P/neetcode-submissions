class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        ROWS = len(grid)
        COLS = len(grid[0])


        q = deque()
        visit = set()
        time = 0
        fresh = 0

        def add(r,c):
            nonlocal fresh
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or (r,c) in visit or grid[r][c] == 0:
                return
            if grid[r][c] == 1:
                grid[r][c] = 2
                fresh -= 1
                q.append((r,c))

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    q.append((r,c))


        while q and fresh > 0:
            for i in range(len(q)):
                r,c = q.popleft()
                visit.add((r,c))

                add(r + 1, c)
                add(r - 1, c)
                add(r, c + 1)
                add(r, c - 1)
                
            time += 1

        
        return time if fresh == 0 else -1
            
                

                