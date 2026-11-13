class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        
        ROWS = len(heights)
        COLS = len(heights[0])

        directions = [(-1,0), (1,0), (0,-1),(0,1)]

        minheap = [[0,0,0]]

        bestdict = {(0,0):0}

        while minheap:
            e,r,c = heapq.heappop(minheap)

            if bestdict[(r,c)] < e:
                continue

            if r == ROWS - 1 and c == COLS - 1:
                return e

            for dr,dc in directions:
                nr = r + dr
                nc = c + dc
                if nr<0 or nr>=ROWS or nc < 0 or nc >= COLS:
                    continue

                ne = max(e , abs(heights[nr][nc] - heights[r][c]))
                
                if (nr,nc) not in bestdict or bestdict[(nr,nc)] > ne:
                    bestdict[(nr,nc)] = ne
                    heapq.heappush(minheap,[ne,nr,nc])


        

        