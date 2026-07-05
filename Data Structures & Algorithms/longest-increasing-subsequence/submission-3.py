class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        dp={}
        def rec(i,j):
            if i >= len(nums):
                return 0
            if (i,j) in dp:
                return dp[(i,j)]
            if nums[j] < nums[i] or j == -1:
                dp[(i,j)]=max(rec(i+1,i) + 1, rec(i+1,j))
                return dp[(i,j)]
            else:
                dp[(i,j)]=rec(i+1,j)
                return dp[(i,j)]


        return rec(0,-1)  

