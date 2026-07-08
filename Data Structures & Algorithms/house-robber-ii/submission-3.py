class Solution:
    def rob(self, nums: List[int]) -> int:
        
        
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]

        dp = {}

        def rec(i,flag):
            if (i, flag) in dp:
                return dp[(i,flag)]
            if i >= len(nums) or (flag and i >= len(nums) - 1):
                return 0

            dp[(i,flag)] = max(nums[i] + rec(i+2, flag), rec(i+1, flag))
            return dp[(i,flag)]
        
        return max(rec(0, True), rec(1, False))
            

