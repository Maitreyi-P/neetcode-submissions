class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
       

        def lower_bound(target):
            l = 0
            r = len(nums)
            while l < r:
                m = l + (r-l)//2

                if nums[m] < target:
                    l = m+1
                else:
                    r = m

            return l

        left = lower_bound(target)

        if left == len(nums) or nums[left] != target:
            return [-1,-1]
        
        right = lower_bound(target+1)

        return [left,right-1]
