class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        def bs(arr,target):
            l = 0
            r = len(arr) - 1

            while l <= r:
                m = l + (r - l) //2
                if arr[m] == target:
                    return m
                elif arr[m] < target:
                    l = m + 1
                else:
                    r = m - 1
            return -1

        l = 0
        r = len(nums) - 1

        while l < r:
            m = l + (r - l)//2
            
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m

        pivot = l 

        smallarr = nums[l:]
        bigarr = nums[0:l]

        if target > smallarr[-1]:
            res = bs(bigarr,target)
            return res
        else:
            res = bs(smallarr,target)
            if res != -1:
                return res + pivot
            return res
                