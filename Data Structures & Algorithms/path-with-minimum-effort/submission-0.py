class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        
        ROWS = len(heights)
        COLS = len(heights[0])
        directions = [(-1,0), (1,0), (0,-1),(0,1)]

        minheap = [[0,0,0]]
        visit = set()


        while minheap:
            effort, r,c = heapq.heappop(minheap)
            if (r,c) in visit:
                continue
            visit.add((r,c))

            if (r,c) == (ROWS-1, COLS-1):
                return effort

            for dr,dc in directions:
                nr,nc = r+dr, c+dc
                if nr<0 or nc<0 or nr>=ROWS or nc>=COLS or (nr,nc) in visit:
                    continue
                neweffort = max(effort, abs(heights[nr][nc] - heights[r][c]))
                heapq.heappush(minheap,[neweffort,nr,nc])

        return 0

                