class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        nums = sorted(candidates)
        res = []
        subset = []

        def dfs(i,tot):
            if tot == target:
                res.append(subset.copy())
                return
            if i >= len(nums) or tot > target:
                return

            subset.append(nums[i])
            dfs(i+1, tot+nums[i])

            while i+1 < len(nums) and nums[i]==nums[i+1]:
                i+=1
            subset.remove(nums[i])
            dfs(i+1, tot)


        dfs(0,0)
        return res