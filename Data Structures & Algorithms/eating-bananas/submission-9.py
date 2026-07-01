class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        l = 1

        r = max(piles) 
        res = r

        while l <= r:
            speed = l + (r - l)//2

            time = 0

            for p in piles:
                time += math.ceil(p/speed)
            
            if time <= h:
                res = min(speed,res)
                r = speed - 1
            else:
                l = speed + 1
                
        
        return res

            