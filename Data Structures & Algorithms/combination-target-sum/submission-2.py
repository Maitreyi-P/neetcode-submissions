class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res = []

        subset = []
        total = 0

        def dfs(i, subset, total):
            if total == target:
                res.append(subset.copy())
                return

            if i >= len(nums) or total > target:
                return

            total += nums[i]
            subset.append(nums[i])
            dfs(i, subset, total)



            total -= nums[i]
            subset.pop()
            dfs(i+1, subset, total)

        dfs(0,subset, total)

        return res
                