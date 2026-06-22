class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = {}
        for i in range(len(nums)):
            if nums[i] in count:
                count[nums[i]]+=1
            else:
                count[nums[i]] = 1
        
        #heap

        heap = []
        for val, c in count.items():
            heap.append((c,val))

        heapq.heapify(heap)

        while len(heap) > k:
            heapq.heappop(heap)

        res = []
        
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res