class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        def canShip(cap):
            count = 1
            tot = 0
            for w in weights:
                if tot + w > cap:
                    count += 1
                    tot = w
                else:
                    tot += w

            if count <= days:
                return True
            return False
        
        mincap = max(weights)
        maxcap = sum(weights)

        l = mincap
        r = maxcap

        res = r

        while l <= r:
            cap = l + (r-l)// 2
            if canShip(cap):
                res = min(res,cap)
                r = cap - 1
            else:
                l = cap + 1
        
        return res
            
        

        