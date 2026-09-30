class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        maxprofit = 0
        buy = 0
        sell = 1

        while sell < len(prices):
            if prices[sell] < prices[buy]:
                buy += 1
            else:
                maxprofit = max(maxprofit, prices[sell]-prices[buy])
                sell +=1

        return maxprofit
        

