class Solution:
    def trap(self, height: List[int]) -> int:
        

        l = 0
        r = len(height) - 1
        water = 0

        maxleft = height[l]
        maxright = height[r]

        while l < r:
            if maxleft <= maxright:
                l += 1
                maxleft = max(height[l], maxleft)

                water += maxleft - height[l]

            else:
                r -= 1
                maxright = max(height[r], maxright)

                water += maxright - height[r]

        return water