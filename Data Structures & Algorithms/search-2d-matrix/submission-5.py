class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix) - 1
        n = len(matrix[0]) -1

        i=0
        j = n
        while i<=m and j>-1:
            if target > matrix[i][j]:
                i+=1
            elif target < matrix[i][j]:
                j-=1
            elif target == matrix[i][j]:
                return True
        return False
