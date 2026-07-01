class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        l = 1

        r = max(piles) 
        res = r

        while l <= r:
            sp = l + (r - l)//2

            time = 0

            for p in piles:
                time += math.ceil(p/sp)
            
            if time > h:
                l = sp + 1
            else:
                res = min(sp,res)
                r = sp - 1
        
        return res

            