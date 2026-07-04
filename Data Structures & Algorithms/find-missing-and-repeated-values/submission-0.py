class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        

        
        ROWS = COLS = len(grid)

        nums = [1 for i in range(ROWS ** 2)]
        print(nums)

        for r in range(ROWS):
            for c in range(COLS):
                idx = grid[r][c]
                nums[idx - 1] -= 1
        print(nums)

        for i in range(len(nums)):
            if nums[i] < 0:
                a = i+1
            if nums[i] == 1:
                b = i+1

        return [a,b]
                
