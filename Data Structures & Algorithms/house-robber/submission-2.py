class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]
            
        dp = [-1] * len(nums)

        dp[0] = nums[0]
        dp[1] = nums[1]
        
        # max1 = dp[0]
        # max2 = dp[1]

        for i in range(2,len(dp)):
            maxval = max(dp[0:i-1])
            dp[i] = maxval + nums[i]

        print(dp)
        return max(dp)
            