class Solution:
    def maxArea(self, heights: List[int]) -> int:

        maxvol = 0
        i = 0
        j = len(heights) - 1

        while i<j:
            h = min(heights[i], heights[j])
            w = j-i
            vol = h*w
            maxvol = max(maxvol,vol)
            if heights[i] <= heights[j]:
                i+=1
            elif heights[i] > heights[j]:
                j-=1
        return maxvol