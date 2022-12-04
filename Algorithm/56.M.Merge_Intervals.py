287 ms, faster than 66.02% 
 18.9 MB, less than 27.48% o


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        start, end = intervals[0][0], intervals[0][1]
        res = []
        i=1
        while i < len(intervals):
            if intervals[i][0] <= end : 
                end = max(intervals[i][1],end)
                i+=1
            else : 
                res.append([start,end])
                start,end = intervals[i][0], intervals[i][1]
        res.append([start,end])
        return res