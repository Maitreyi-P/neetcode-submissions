class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        nums = set(nums)
        maxl = 0
        count = 0
        for i in nums:
            if i-1 not in nums:
                count = 1
                while i + count in nums:
                    count += 1
            maxl = max(maxl, count)

        return maxl
                