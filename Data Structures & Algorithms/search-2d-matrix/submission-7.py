class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rowlist = []
        row = 0
        for i in matrix:
            rowlist.append(i[0])

        for i in range(len(rowlist)):
            if target >= rowlist[i]:
                row = i
        
        l = 0
        r = len(matrix[0]) -1
        # if l == r:
        #     if matrix[0][0] == target:
        #         return True
        #     else:
        #         return False
        while l <= r:
            m = l + (r-l)//2
            print(l,r)
            print(row)
            print(m)
            if matrix[row][m] > target:
                r -= 1
            elif matrix[row][m] < target:
                l += 1
            elif matrix[row][m] == target:
                return True
                
        return False
        
