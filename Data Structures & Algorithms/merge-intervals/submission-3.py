class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort(key=lambda pair:pair[0])

        res = []
        res.append(intervals[0])

        for i in range(1, len(intervals)):
            res_start, res_end = res.pop()
            curr_start,curr_end = intervals[i][0], intervals[i][1]

            if curr_start <= res_end:
                new_start = min(curr_start, res_start)
                new_end = max(curr_end, res_end)
                res.append([new_start,new_end])
            
            else:
                res.append([res_start,res_end])
                res.append([curr_start,curr_end])

        return res
