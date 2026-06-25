class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        mem = [-1]* (amount+1)

        def dfs(target):
            if target == 0:
                return 0
            if target < 0:
                return math.inf

            if mem[target] != -1:
                return mem[target]

            res = math.inf
            for c in coins:
                res = min(res,dfs(target-c))

            mem[target] = res + 1
            return mem[target]

        val = dfs(amount)
        return val if val != math.inf else -1