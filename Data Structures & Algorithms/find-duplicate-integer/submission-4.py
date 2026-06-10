class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        s = sorted(nums)
        for i in range(len(nums)-1):
            if s[i+1] == s[i]:
                return s[i]
        