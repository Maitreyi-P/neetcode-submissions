from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        rowdict = defaultdict(list)
        coldict = defaultdict(list)
        sqdict = defaultdict(list)

        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    if board[i][j] in rowdict[i] or board[i][j] in coldict[j]:
                        return False
                    rowdict[i].append(board[i][j]) 
                    coldict[j].append(board[i][j]) 

        for square in range(9):
            for i in range(3):
                for j in range(3):
                    row = (square//3) * 3 + i
                    col = (square%3) * 3 + j
                    if board[row][col] != ".":
                        if board[row][col] not in sqdict[square]:
                            sqdict[square].append(board[row][col])
                        else:
                            return False

        
        return True
        