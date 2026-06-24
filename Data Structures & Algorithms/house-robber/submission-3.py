class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return nums[0]

        dp = [-1] * len(nums)

        dp[0] = nums[0]
        dp[1] = max(nums[0],nums[1]) #why? because you're deciding to rob either 0 or 1, you want the max of these

        for i in range(2,len(nums)):
            dp[i] = max(dp[i-1], nums[i]+dp[i-2])


        return dp[-1]

        
        

                
