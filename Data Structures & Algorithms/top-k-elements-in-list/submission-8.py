class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freqmap = {}
        for n in nums:
            if n not in freqmap:
                freqmap[n] = 0
            freqmap[n] += 1

        minheap = []
        for num, freq in freqmap.items():
            heapq.heappush(minheap,[freq,num])

        while len(minheap) > k:
            heapq.heappop(minheap)

        res = []
        for freq,num in minheap:
            res.append(num)

        return res