class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        
        left = 0
        right = len(matrix[0])
        top = 0
        bottom = len(matrix)


        for i in range(bottom):
            for j in range(right):
                if matrix[i][j] == 0:

                    for k in range(bottom):
                        if matrix[k][j] == 0:
                            continue
                        matrix[k][j] = -math.inf

                    for k in range(right):
                        if matrix[i][k] == 0:
                            continue
                        matrix[i][k] = -math.inf

        
        for i in range(bottom):
            for j in range(right):
                if matrix[i][j] == -math.inf:
                    matrix[i][j] = 0


        