class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        res = max(piles) 

        l = 1
        r = res

        while l <= r:
            m = l + (r-l) //2

            time = 0

            for p in piles:
                time += math.ceil(p/m)

            if time > h:
                l = m + 1

            elif time <= h:
                res = min(res, m)
                r = m - 1

        
        return res
        