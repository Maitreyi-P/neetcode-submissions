class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        intervals.sort()

        a,b = intervals[0][0],intervals[0][1]
        count = 0

        for i in range(1,len(intervals)):
            if intervals[i][0] < b:
                b = min(b, intervals[i][1])
                count += 1
            else:
                a = intervals[i][0]
                b = intervals[i][1]

        return count