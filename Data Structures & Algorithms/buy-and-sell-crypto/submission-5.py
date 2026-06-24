class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        l=0
        r=1
        maxp = 0

        while r < len(prices):
            if prices[r] < prices[l]:
                l+=1
            else:
                maxp = max(maxp, prices[r]-prices[l])
                r+=1

        return maxp
