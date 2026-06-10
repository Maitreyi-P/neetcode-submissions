class Solution:
    def trap(self, height: List[int]) -> int:
        #using two pointers
        
        n = len(height)
        if n == 0:
            return 0
        
        l = 0
        r = n-1
        maxl = height[l]
        maxr = height[r]
        res = 0

        while l<r:
            if maxl <= maxr:
                l+=1
                if maxl - height[l] >= 0:
                    res += maxl - height[l]
                maxl = max(maxl, height[l])
            elif maxr < maxl:
                r -=1
                if maxr - height[r] >= 0:
                    res += maxr - height[r]
                maxr = max(maxr, height[r])
        
        return res