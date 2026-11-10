class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        edgemap = defaultdict(list)
        for u, v, t in times:
            edgemap[u].append((v,t))


        minheap = []
        heapq.heappush(minheap, (0,k))

        dist = {k:0}

        while minheap:
            t1,n1 = heapq.heappop(minheap)

            #stale entry:
            if t1 > dist[n1]:
                continue

            for n2,t2 in edgemap[n1]:
                new_time = t1 + t2
                if n2 not in dist or new_time < dist[n2]:
                    dist[n2] = new_time
                    heapq.heappush(minheap, (new_time,n2))

        if len(dist) == n:
            return max(dist.values())
        return -1

            