class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        #logic - break into sequences. if number has no left, new seq

        numSet = set(nums)
        longest = 0

        for n in nums:
            if (n-1) not in numSet:  #if no prev neighbor, new seq
                length = 0 #new seq
                while(n + length) in nums: #while the next conseq number is there
                    length += 1
                longest = max(longest, length)

        return longest

        
        