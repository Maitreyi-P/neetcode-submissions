class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return nums[0]
        if not nums:
            return 0

        n = len(nums)

        arr1 = nums[0:-1]
        arr2 = nums[1:]

        return max(self.helper(arr1),self.helper(arr2))


    def helper(self, arr):

        if not arr:
            return 0
        if len(arr) == 1:
            return arr[0]

        dp = [-1]*len(arr)

        dp[0] = arr[0]
        dp[1] = max(arr[0],arr[1])

        for i in range(2,len(arr)):
            dp[i] = max(dp[i-1], arr[i]+dp[i-2])
        
        return dp[-1]
        
        