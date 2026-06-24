class Solution:
    def bs(self, arr, target):
        l = 0
        r = len(arr) - 1

        while l<=r:
            m = l + (r-l) // 2
            if arr[m] == target:
                return m
            elif arr[m] < target:
                l = m+1
            else:
                r = m-1
        return -1



    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) -1

        while l < r:
            m = l + (r-l) //2
            if nums[m] > nums[r]:
                l = m+1
            else:
                r=m
        pivot = l

        arr1 = nums[pivot:]
        arr2 = nums[0:pivot]
        print(arr1)
        print(arr2)

        res1 = self.bs(arr1, target)
        if res1!= -1:
            return res1+pivot
        else:
            res2 = self.bs(arr2, target)
            if res2!= -1:
                return res2

        
        return -1
