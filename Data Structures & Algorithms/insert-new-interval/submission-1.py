class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        res = []

        for i in range(len(intervals)):
            new_s,new_e = newInterval
            s,e = intervals[i]
            if new_e < s:
                res.append(newInterval)
                return res + intervals[i:]

            elif new_s > e:
                res.append(intervals[i])

            else:
                newInterval = ([min(new_s,s), max(new_e,e)])

        res.append(newInterval)
        return res
                
                