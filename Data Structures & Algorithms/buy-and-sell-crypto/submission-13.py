class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        maxp = 0
        buy = 0
        sell = 1

        while sell < len(prices):
            if prices[buy] > prices[sell]:
                buy += 1
            else:
                maxp = max(maxp, prices[sell] - prices[buy])
                sell += 1


        return maxp
