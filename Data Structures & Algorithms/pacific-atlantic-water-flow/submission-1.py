class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        ROWS = len(heights)
        COLS = len(heights[0])

        pac, atl = set(),set()

        def dfs(r,c, visit, prevheight):
            if r<0 or c<0 or r>=ROWS or c>=COLS or (r,c) in visit or heights[r][c]< prevheight:
                return

            visit.add((r,c))
            prevheight = heights[r][c]
            dfs(r-1,c,visit,prevheight)
            dfs(r+1,c,visit,prevheight)
            dfs(r,c-1,visit,prevheight)
            dfs(r,c+1,visit,prevheight)


        for r in range(ROWS):
            dfs(r,0,pac,heights[r][0])
            dfs(r,COLS-1,atl,heights[r][COLS-1])

        for c in range(COLS):
            dfs(0,c,pac,heights[0][c])
            dfs(ROWS-1,c,atl,heights[ROWS-1][c])

        res = []
        for pair in atl:
            if pair in pac:
                res.append(list(pair))

        return res

        
        