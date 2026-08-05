class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        graph = defaultdict(list)
        for u, v, t in times:
            graph[u].append((v,t))

        heap = [(0,k)]

        visit = set()
        tot = 0

        while heap:
            time, node = heapq.heappop(heap)

            if node in visit:
                continue
            
            visit.add(node)
            tot = max(tot, time)

            for v,t in graph[node]:
                heapq.heappush(heap,(t + time, v))

        if len(visit) != n:
            return -1

        return tot