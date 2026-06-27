class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        dp = {}
        def dfs(i,target):
            if (i,target) in dp:
                return dp[(i,target)]

            if i>= len(nums):
                return target == 0
            
            if target < 0:
                return False
            
            dp[(i,target)] = dfs(i+1, target-nums[i]) or dfs(i+1, target)
            return dp[(i,target)]



        
        tot = sum(nums)
        if tot % 2 != 0:
            return False
        
        return dfs(0,tot//2)
