class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        dp = {}
        def rec(amount):
            if amount in dp:
                return dp[amount]
            if amount == 0:
                return 0

            if amount < 0:
                return math.inf

            res = math.inf

            for c in coins:
                res = min(res, rec(amount - c)) 

            dp[amount] = res + 1
            return dp[amount]

        ans = rec(amount)
        if ans == math.inf:
            return -1
        return ans
