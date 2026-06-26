class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        #kadane's
        
        res = max(nums)

        currSum = 0

        for n in nums:
            currSum = max(n, currSum + n)
            res = max(res,currSum)

        return res


