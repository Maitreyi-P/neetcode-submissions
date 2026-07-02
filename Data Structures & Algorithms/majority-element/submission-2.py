class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        nums.sort()
        maj = (len(nums)//2) 

        return nums[maj]
        
        