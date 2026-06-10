class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if len(nums) == 0:
            return 0
            
        snums = sorted(nums)

        res = 1
        count = 1
        for i in range(len(snums) - 1):
            if snums[i+1] == snums[i]:
                continue
            if snums[i+1] == snums[i] + 1:
                count+= 1
                res = max(count,res)
            else:
                count = 1
                res = max(count,res)
        return res
        