class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        snums = sorted(nums)
        if not nums:
            return 0
        res = 1

        count = 1
        for i in range(len(snums)-1):
            if snums[i+1] == snums[i]:
                continue
            if snums[i+1] == snums[i]+ 1:
                count += 1
                res = max(res, count)
            else:
                count = 1
                
        return res