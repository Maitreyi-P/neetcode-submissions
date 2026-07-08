class Solution:
    def rob(self, nums: List[int]) -> int:
        

        dp = {}
        def rec(i):
            if i in dp:
                return dp[i]
            if i >= len(nums):
                return 0

            res1 = nums[i] + rec(i+2) #rob
            res2 = rec(i+1) #don't


            dp[i] = max(res1, res2)
            return dp[i]

        return rec(0)
