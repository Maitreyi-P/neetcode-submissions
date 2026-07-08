class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        res = []

        l = 0
        r = l + k - 1

        window = nums[l:r+1]
        
        biggest = -math.inf
        big_i = -1

        for i in range(len(window)):
            if nums[i] > biggest:
                biggest = nums[i]
                big_i = i

        res.append(biggest)

        while r < len(nums)-1:
            l += 1
            r += 1

            if nums[r] <= biggest and l <= big_i:
                res.append(biggest)
            
            elif nums[r] > biggest:
                biggest = nums[r]
                big_i = r
                res.append(biggest)
            
            else:
                biggest = -math.inf
                for i in range(l,r+1):
                    if nums[i] > biggest:
                        biggest = nums[i]
                        big_i = i
                res.append(biggest)


        return res



