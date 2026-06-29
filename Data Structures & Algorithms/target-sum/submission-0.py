class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        dp = {}

        def dfs(i, tot):

            if i >= len(nums):
                if tot == target:
                    return 1
                return 0

            if (i,tot) in dp:
                return dp[(i,tot)]

            #add 
            add = dfs(i + 1, tot + nums[i])
            
            #subtract
            sub = dfs(i + 1, tot - nums[i])

            dp[(i,tot)] = add + sub
            return dp[(i,tot)]

        return dfs(0,0)
