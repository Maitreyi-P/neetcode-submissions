class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        
        edgemap = defaultdict(list)

        for i in range(len(edges)):
            edgemap[edges[i][0]].append((edges[i][1], succProb[i]))
            edgemap[edges[i][1]].append((edges[i][0], succProb[i]))

        maxheap = []
        heapq.heappush_max(maxheap,(1,start))
        probdict = {start:1}

        while maxheap:
            p1,n1 = heapq.heappop_max(maxheap)


            if p1 < probdict[n1]:
                continue

            if n1 == end:
                return p1

            for n2,p2 in edgemap[n1]:
                new_prob = p1 * p2

                if n2 not in probdict or probdict[n2] < new_prob:
                    probdict[n2] = new_prob
                    heapq.heappush_max(maxheap, (new_prob, n2))


        return 0

