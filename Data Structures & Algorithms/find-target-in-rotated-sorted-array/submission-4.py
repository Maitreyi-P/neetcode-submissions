class Solution:
    def bs(self,arr,target):

        if len(arr) == 1:
            if arr[0] == target:
                return 0
        # print(arr)
        l = 0
        r = len(arr) - 1
        while l<=r:
            m = (l + r) // 2
            if arr[m] == target:
                return m
            elif arr[m] > target:
                r = m - 1
            else:
                l= m + 1
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

        arr1 = nums[0:pivot]
        arr2 = nums[pivot:]

        # print(arr1,arr2)
        
        if self.bs(arr1,target) == -1:
            if self.bs(arr2,target) == -1:
                return -1
            else:
                return self.bs(arr2,target) + pivot
        else:
            return self.bs(arr1,target)

