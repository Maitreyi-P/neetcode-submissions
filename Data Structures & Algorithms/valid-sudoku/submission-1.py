from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        rowdict = defaultdict(list)
        coldict = defaultdict(list)
        sqdict = defaultdict(list)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if board[r][c] in rowdict[r] or board[r][c] in coldict[c] or board[r][c] in sqdict[(r//3,c//3)]:
                    return False
                else:
                    rowdict[r].append(board[r][c])
                    coldict[c].append(board[r][c])
                    sqdict[(r//3,c//3)].append(board[r][c])

        return True
        