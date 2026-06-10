class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        for i in range(len(nums)):
           replace_index =  abs(nums[i]) - 1 
           if nums[replace_index] < 0:
                return abs(nums[i])
           else:
                nums[replace_index] *= -1

        
        