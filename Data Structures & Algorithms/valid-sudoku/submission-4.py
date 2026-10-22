class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        rowmap = defaultdict(set)
        colmap = defaultdict(set)
        squaremap = defaultdict(set)

        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == ".":
                    continue
                elif board[r][c] in rowmap[r] or board[r][c] in colmap[c] or board[r][c] in squaremap[(r//3,c//3)]:
                    return False
                else:
                    rowmap[r].add(board[r][c])
                    colmap[c].add(board[r][c])
                    squaremap[(r//3,c//3)].add(board[r][c])

        return True
                
