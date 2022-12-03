# 105ms 76.38% 
# 17.3mb 80.61 less

class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort()
        for i in range(1,len(intervals)) : 
            if intervals[i][0]<intervals[i-1][1] : 
                return False
            
        return True


#sorting 먼저 
# interval [i-1]    -------------------*
#interval [i]                   *-----------------
#intervals[i][0]  < interval[i-1][1]  