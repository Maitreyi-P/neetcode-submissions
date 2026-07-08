class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        ROWS = len(matrix)
        COLS = len(matrix[0])

        rowlist = []
        row = 0

        for r in matrix:
            rowlist.append(r[0])

        for i in range(len(rowlist)):
            if target >= rowlist[i]:
                row = i

        searcharray = matrix[row]

        l = 0
        r = len(searcharray) - 1

        while l <= r:
            m = l + (r - l) //2

            if searcharray[m] == target:
                return True
            elif searcharray[m] < target:
                l = m + 1
            else:
                r = m - 1

    
        return False
            
        
        

        