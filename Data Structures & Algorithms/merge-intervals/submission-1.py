class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort(key=lambda pair: pair[0])
        res = [intervals[0]]

        for i in range(len(intervals)):
            a,b = intervals[i]
            last = res[-1][-1]

            if a <= last:
                res[-1][-1] = max(b,last)
            else:
                res.append(intervals[i])

        return res