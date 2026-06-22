class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        pref = [0] * len(nums)
        suff = [0] * len(nums)
        res = [0] * len(nums)

        pref[0] = 1
        suff[len(nums)-1] = 1

        for i in range(1,len(nums)):
            pref[i] = nums[i-1] * pref[i-1]
        for j in range(len(nums)-2,-1,-1):
            suff[j] = nums[j+1] * suff[j+1]
        
        for k in range(len(nums)):
            res[k] = pref[k] * suff[k]

        return res
