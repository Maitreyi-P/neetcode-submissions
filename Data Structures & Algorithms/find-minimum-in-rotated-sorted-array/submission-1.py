class Solution:

    def findMin(self, nums: List[int]) -> int:

        ans = math.inf
        i = 0
        j = len(nums) -1
        m = 0
        while m < j:
            if nums[m+1]>= nums[m]:
                m+=1
            else:
                break
        if m==j:
            return nums[0]

        return nums[m+1]
        


