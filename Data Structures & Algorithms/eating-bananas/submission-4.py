class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        l = 1
        r = max(piles)  #range of eating speeds

        res = r #max initially

        while l <= r:
            mid = r + (l-r)//2

            hours = 0

            for p in piles:
                hours += math.ceil(p/mid) #time taken to eat at this speed

            if hours <= h:
                res = min(res, mid) #check speed here fool not time
                r= mid-1

            else:
                l=mid+1

        return res