class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        closest = []

        for i in range(len(points)):
            a,b = points[i]
            dist = (a**2) + (b**2)

            heapq.heappush(closest,(dist, points[i]))

        
        res = []

        while k > 0:
            d, p = heapq.heappop(closest)
            res.append(p)
            k -= 1

        return res

        