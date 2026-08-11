class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        #prims

        
        N = len(points)

        adj = {i:[] for i in range(N)} #i : list of [cost, node] for all points
        for i in range(N):
            x1,y1 = points[i]
            for j in range(i+1, N):
                x2,y2 = points[j]
                dist = abs(x1-x2) + abs(y1-y2)
                adj[i].append([dist, j])
                adj[j].append([dist, i])
        
        res = 0
        visit = set()
        minheap = [[0,0]]

        while len(visit) < N:
            cost, node = heapq.heappop(minheap)
            if node in visit:
                continue
            res += cost
            visit.add(node)
            for nC, n in adj[node]:
                if n not in visit:
                    heapq.heappush(minheap, [nC, n])

        return res

