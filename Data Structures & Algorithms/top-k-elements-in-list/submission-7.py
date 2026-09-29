class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freqMap = {}

        for i in nums:
            if i in freqMap:
                freqMap[i] += 1
            else:
                freqMap[i] = 1

        minheap = []
        for num,freq in freqMap.items():
            heapq.heappush(minheap, [freq,num])

        while len(minheap) > k:
            heapq.heappop(minheap)

        res = []
        for freq, num in minheap:
            res.append(num)

        return res