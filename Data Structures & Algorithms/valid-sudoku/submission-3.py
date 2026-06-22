class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        rowdict = defaultdict(list)
        coldict = defaultdict(list)
        sqdict = defaultdict(list)

        ROWS = COLS = len(board)

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == ".":
                    continue
                elif board[r][c] in rowdict[r] or board[r][c] in coldict[c] or board[r][c] in sqdict[(r//3,c//3)]:
                    return False
                rowdict[r].append(board[r][c])
                coldict[c].append(board[r][c])
                sqdict[(r//3,c//3)].append(board[r][c])
        
        return True

        