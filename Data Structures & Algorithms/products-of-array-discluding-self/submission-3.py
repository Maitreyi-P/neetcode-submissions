class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        pref = [0] * len(nums)
        post = [0] * len(nums)

        pref[0] = 1
        post[-1] = 1

        res = []

        for i in range(1,len(nums)):
            pref[i] = pref[i-1] * nums[i-1]

        for j in range(len(nums)-2, -1, -1):
            post[j] = post[j+1] * nums[j+1]

        for k in range(len(nums)):
            res.append(pref[k] * post[k])

        return res