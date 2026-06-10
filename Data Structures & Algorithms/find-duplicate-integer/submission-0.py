class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        hmap = {}

        for i in range(len(nums)):
            if nums[i] in hmap:
                return nums[i]
            else:
                hmap[nums[i]] = 1
        
       
            