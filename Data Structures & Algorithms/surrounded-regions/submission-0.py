class Solution:
    def solve(self, board: List[List[str]]) -> None:
        
        #go through the border cells. if O, do dfs and change to T

        ROWS = len(board)
        COLS = len(board[0])
        directions = [[0,1],[0,-1],[-1,0],[1,0]]

        def dfs(r,c):
            if r<0 or c<0 or r>=ROWS or c>= COLS or board[r][c] == "X" or board[r][c] == "T":
                return
            board[r][c] = "T"
            for dr,dc in directions:
                dfs(r+dr,c+dc)
        
        for c in range(COLS):
            dfs(0,c)
            dfs(ROWS-1,c)

        for r in range(ROWS):
            dfs(r,0)
            dfs(r,COLS-1)

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"
                if board[r][c] == "T":
                    board[r][c] = "O"

        