class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        memo = [-1]*len(cost)

        def dfs(step):
        
            if step >= len(cost):
                return 0
            if memo[step] != -1:
                return memo[step]

            memo[step] =  min(dfs(step+1),dfs(step+2)) + cost[step]
            return memo[step]

        return min(dfs(0),dfs(1))
