class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        n = len(nums)

        res = [False] * (n+1)

        for num in nums:
            if 0 < num < n + 1:
                res[num] = True

        for i in range(1,len(res)):
            if res[i] != True:
                return i

        return n + 1