class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        

        res = []

        for q in queries:
            smallest = math.inf
            for s,e in intervals:
                if s <= q <= e:
                    smallest = min(smallest, e - s + 1)

            if smallest == math.inf:
                res.append(-1)
            else:
                res.append(smallest)

        return res