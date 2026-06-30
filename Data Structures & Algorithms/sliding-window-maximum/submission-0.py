class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        heap = []
        heapq.heapify_max(heap)

        res = []
        for i in range(len(nums)):
            heapq.heappush_max(heap,(nums[i],i))
            l = i - k + 1
            while heap[0][1] < l:
                heapq.heappop_max(heap)
            if i >= k - 1:
                res.append(heap[0][0])

        return res


