class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]

        n = len(nums)
    
        return max(self.helper(nums[0:n-1]), self.helper(nums[1:n]))


    def helper(self, arr):
        if not arr:
            return 0

        if len(arr) == 1:
            return arr[0]

        dp = [-1] * len(arr)

        dp[0] = arr[0]
        dp[1] = max(arr[0], arr[1])

        for i in range(2, len(arr)):
            dp[i] = max(dp[i-2] + arr[i], dp[i-1])

        return dp[-1]

