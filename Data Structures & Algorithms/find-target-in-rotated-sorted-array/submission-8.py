class Solution:
    def search(self, nums: List[int], target: int) -> int:

        def bs(arr,target):
            l=0
            r=len(arr)-1
            while l <= r:
                m = l + (r-l)//2
                if arr[m] > target:
                    r = m-1
                elif arr[m] < target:
                    l = m+1
                elif arr[m] == target:
                    return m
            return -1

                
        l = 0
        r = len(nums) -1
        while l<r:
            m = l + (r-l)//2
            if nums[m] > nums[r]:
                l = m+1
            else:
                r=m
        pivot = l

        arr1 = nums[0:pivot]
        arr2 = nums[pivot:]

        res1 = bs(arr1,target)
        if res1!= -1:
            return res1
        res2 = bs(arr2,target)
        if res2!= -1:
            return res2+pivot
        
        return -1
        
        