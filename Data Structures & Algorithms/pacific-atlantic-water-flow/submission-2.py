class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        

        ROWS = len(heights)
        COLS = len(heights[0])

        pac, atl = set(),set()

        def dfs(r,c,prev,visit):
            if r<0 or r>=ROWS or c<0 or c>=COLS or (r,c) in visit or heights[r][c] < prev:
                return

            visit.add((r,c))
            dfs(r+1,c,heights[r][c],visit)
            dfs(r-1,c,heights[r][c],visit)
            dfs(r,c+1,heights[r][c],visit)
            dfs(r,c-1,heights[r][c],visit)

            return


        for r in range(ROWS):
            dfs(r,0,-1,pac)
            dfs(r,COLS-1, -1, atl)

        for c in range(COLS):
            dfs(0,c,-1,pac)
            dfs(ROWS-1,c,-1,atl)

        res = []
        for point in pac:
            if point in atl:
                r,c = point
                res.append([r,c])

        return res

        