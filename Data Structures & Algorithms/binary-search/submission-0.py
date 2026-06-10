class Solution:
    def bs(self, l: int, r: int, nums: List[int], target: int):
        if l >r :
            return -1
        
        mid = l + (r-l)//2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            return self.bs(l, r-1, nums, target)
        elif nums[mid] < target:
             return self.bs(l+1, r, nums, target)


    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) -1
        return self.bs(l, r, nums, target)