class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freqMap = {}
        res = []

        for n in nums:
            if n in freqMap:
                freqMap[n] += 1
            else:
                freqMap[n] = 1
        
        min_heap = []
        heapq.heapify(min_heap)

        for n, freq in freqMap.items():
            heapq.heappush(min_heap,(freq,n))

        while len(min_heap) > k:
            heapq.heappop(min_heap)

        for freq, n in min_heap:
            res.append(n)

        return res