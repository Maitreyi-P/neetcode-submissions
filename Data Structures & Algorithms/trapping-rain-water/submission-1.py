class Solution:
    def trap(self, height: List[int]) -> int:
        #uses left and right maxarrays
        n = len(height)
        if n == 0:
            return 0

        maxleft = [0]*n
        maxright = [0]*n
        finarr = [0]*n

        maxleft[0] = 0
        for i in range(1,n):
            maxleft[i] = max(maxleft[i-1],height[i-1])
            
        maxright[n-1] = 0
        for i in range(n-2, -1, -1):
            maxright[i] = max(maxright[i+1], height[i+1])

        for i in range(n):
            if min(maxleft[i],maxright[i]) - height[i] <= 0:
                finarr[i] = 0
            else:
                finarr[i] = min(maxleft[i],maxright[i]) - height[i]

        return sum(finarr)