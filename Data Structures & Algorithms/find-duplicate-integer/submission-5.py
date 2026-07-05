class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        n = len(nums) - 1

        nums2 = [0 for i in range(n)]

        for i in range(len(nums)):
            nums2[nums[i] - 1] += 1
        
        for j in range(len(nums2)):
            if nums2[j] > 1:
                return j + 1