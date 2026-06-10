import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        d = defaultdict(list)

        for i in range(len(points)):
            x,y = points[i]
            dist = math.sqrt((x**2)+(y**2))

            d[dist].append(points[i])

        sd = dict(sorted(d.items()))

        res = []
        for key,val in sd.items():
            for v in val:
                if k > 0:
                    res.append(v)
                    k-=1

        return res