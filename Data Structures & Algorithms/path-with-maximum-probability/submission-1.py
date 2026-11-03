class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        
        nodemap = defaultdict(list)
        for i in range(len(edges)):
            nodemap[edges[i][0]].append((succProb[i],edges[i][1]))
            nodemap[edges[i][1]].append((succProb[i],edges[i][0]))

        maxheap = [(1,start_node)]

        visit = set()
        maxprob = 0.0

        while maxheap:
            p1, n1 = heapq.heappop_max(maxheap)
            if n1 in visit:
                continue
            visit.add(n1)
            if n1 == end_node:
                return p1

            for p2,n2 in nodemap[n1]:
                if n2 not in visit:
                    heapq.heappush_max(maxheap, (p1*p2,n2))


        return maxprob