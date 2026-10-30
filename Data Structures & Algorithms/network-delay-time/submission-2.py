class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        nodemap = defaultdict(list)

        for u,v,t in times:
            nodemap[u].append((v,t))

        minheap = [(0,k)]

        visit = set()
        time = 0

        while minheap:
            t1,n1 = heapq.heappop(minheap)
            if n1 in visit:
                continue
            visit.add(n1)
            time = t1

            for n2,t2 in nodemap[n1]:
                if n2 not in visit:
                    heapq.heappush(minheap, (t1+t2, n2))
                    

        if len(visit) == n:
            return time

        return -1


