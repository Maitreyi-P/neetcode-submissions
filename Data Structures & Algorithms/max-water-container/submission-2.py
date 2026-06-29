class Solution:
    def maxArea(self, heights: List[int]) -> int:

        l = 0
        r = len(heights) - 1

        maxwater = 0
        
        while l < r:
            h = min(heights[l],heights[r])
            w = r - l
            maxwater = max(maxwater, h * w)
            if heights[l] > heights[r]:
                r-=1
            else:
                l+=1
        
        return maxwater