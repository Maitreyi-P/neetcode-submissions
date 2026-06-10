class Solution:
    def maxArea(self, heights: List[int]) -> int:
        width = len(heights) - 1
        l = 0
        r = len(heights) -1
        maxarea = 0

        while l < r:
            h = min(heights[l], heights[r])
            area = width * h
            maxarea = max(maxarea,area)
            if heights[l] <= heights[r]:
                l+=1
            elif heights[l] > heights[r]:
                r-=1
            width -=1

        return maxarea
