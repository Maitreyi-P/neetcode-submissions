class Solution:
    def trap(self, height: List[int]) -> int:
        

        total = 0
        l = 0
        r = len(height) - 1
        lmax = height[l]
        rmax = height[r]

        while l < r:
            if lmax <= rmax:
                l += 1
                if lmax - height[l] >= 0:
                    total += lmax - height[l]
                lmax = max(lmax, height[l])
            else:
                r -= 1
                if rmax - height[r] >=0:
                    total += rmax - height[r]
                rmax = max(rmax, height[r])

        return total
                    
