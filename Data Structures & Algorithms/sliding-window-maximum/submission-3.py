class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        res = []
        l = 0
        r = k - 1

        window = nums[l:r+1]

        max_elem = -math.inf
        max_idx = -1

        for i in range(len(window)):
            if nums[i] > max_elem:
                max_elem = nums[i]
                max_idx = i

        res.append(max_elem)

        while r < len(nums) - 1:
            l += 1
            r += 1
            if nums[r] > max_elem:
                max_elem = nums[r]
                max_idx = r
            if l > max_idx:
                max_elem = -math.inf
                for i in range(l,r+1):
                    if nums[i] > max_elem:
                        max_elem = nums[i]
                        max_idx = i
            res.append(max_elem)

        return res

                
