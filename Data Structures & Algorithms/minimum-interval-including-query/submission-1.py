class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        
        res = []
        hmap = {}

        intervals.sort()

        minheap = []

        i = 0

        for q in sorted(queries):
            while i < len(intervals) and intervals[i][0] <= q:
                s,e = intervals[i]
                length = e - s + 1
                heapq.heappush(minheap, (length, e))
                i += 1


            while minheap and minheap[0][1] < q:
                heapq.heappop(minheap)

            if minheap:
                hmap[q] = minheap[0][0]

        for q in queries:
            if q in hmap:
                res.append(hmap[q])
            else:
                res.append(-1)
        return res
