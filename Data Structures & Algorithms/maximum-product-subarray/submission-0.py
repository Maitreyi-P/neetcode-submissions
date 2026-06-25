class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        #Kadane's algo

        res = max(nums)

        currMax, currMin = 1,1

        for n in nums:
            if n == 0:
                currMax, currMin = 1,1 #reset
                continue
            temp = currMax
            currMax = max(n, currMax * n, currMin * n)
            currMin = min(n, temp * n, currMin * n)

            res = max(res, currMax)
        return res