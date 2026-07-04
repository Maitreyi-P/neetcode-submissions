class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        res = max(nums)
        currMin = 1
        currMax = 1

        for n in nums:
            if n == 0:
                currMax,currMin = 1,1
                continue
            temp = currMax
            currMax = max(n, currMax * n, currMin * n)
            currMin = min(n, temp * n, currMin * n)
            res = max(res, currMax, currMin)

        return res


