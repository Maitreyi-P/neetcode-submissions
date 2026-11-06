class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        

        l = 1
        r = max(piles)

        while l < r:
            m = l + (r-l)//2

            time = 0
            for p in piles:
                time += math.ceil(p/m)
            
            if time > h:
                l = m + 1
            else:
                r = m

        return l
