class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        dp = {}
        def dfs(i,j):
            if (i,j) in dp:
                return dp[(i, j)]

            if i >= len(nums):
                return 0

            #notincl
            res = dfs(i+1,j)

            #incl
            if j == -1 or nums[i] > nums[j]:
                res = max(res, 1 + dfs(i + 1 ,i))
            
            dp[(i,j)] = res
            return res
          

        return dfs(0,-1)
                
            

            