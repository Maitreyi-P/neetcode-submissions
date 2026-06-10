class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort(key=lambda pair: pair[0]) #sorting by first elem in each interval
        output = [intervals[0]]

        for i in range(len(intervals)):
            s,e = intervals[i]
            last = output[-1][-1]

            if s <= last:
                output[-1][-1] = max(last, e)
            else:
                output.append(intervals[i])
        return output
