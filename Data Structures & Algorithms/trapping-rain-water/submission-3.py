class Solution:
    def trap(self, height: List[int]) -> int:
        #twopointer

        #formula: min(maxl,maxr) - heights[i]
        #but for this, use only maxl OR maxr. shift whatever is smaller and update max

        
        if not height:
            return 0

        l = 0
        r = len(height) -1

        maxl,maxr = height[l], height[r]
        res = 0

        while l<r:
            if maxl <= maxr:
                l += 1
                maxl = max(maxl, height[l])
                res+= maxl - height[l] 

            else:
                r-=1
                maxr = max(maxr, height[r])
                res+= maxr - height[r]

        return res