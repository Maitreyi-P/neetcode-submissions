class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        res = []
        q = deque()

        l = r = 0

        while r < len(nums):
            while q and nums[q[-1]] < nums[r]: #pop out all smaller nums
                q.pop()

            q.append(r)

            if l > q[0]: #window moved past
                q.popleft()
            
            if (r + 1) >= k:
                res.append(nums[q[0]])
                l+=1

            r+=1

        return res