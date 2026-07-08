class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freqmap = {}

        for n in nums:
            if n in freqmap:
                freqmap[n] += 1
            else:
                freqmap[n] = 1

        maxheap = []

        for num,freq in freqmap.items():
            heapq.heappush_max(maxheap, (freq,num))

        res = []

        while k > 0:
            res.append(heapq.heappop_max(maxheap)[1])
            k -= 1

        return res