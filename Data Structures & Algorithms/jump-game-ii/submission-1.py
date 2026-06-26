class Solution:
    # def jump(self, nums: List[int]) -> int:

    #     def dfs(i):
    #         if i >= len(nums) - 1:
    #             return 0
    #         if nums[i] == 0:
    #             return math.inf

    #         end = min(i + nums[i], len(nums) - 1)

    #         res = math.inf
    #         for j in range(i + 1, end + 1):
    #             res = min(res, 1 + dfs(j))
            
    #         return res

    #     return dfs(0)

    def jump(self, nums: List[int]) -> int:

        mem = [-1] * len(nums)
        def dfs(i):

                if mem[i] != -1:
                    return mem[i]

                if i >= len(nums) - 1:
                    return 0
                if nums[i] == 0:
                    return math.inf

                end = min(i + nums[i], len(nums) - 1)

                res = math.inf
                for j in range(i + 1, end + 1):
                    res = min(res, 1 + dfs(j))
                    mem[i] = res
                
                return mem[i]

        return dfs(0)
