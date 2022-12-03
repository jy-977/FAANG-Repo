#210 ms, faster than 13.65% of Python3 
#17.6 MB, less than 32.12% 
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        starts = sorted([i[0] for i in intervals])
        ends = sorted([i[1] for i in intervals])
        s,e = 0,0
        out , count = 0,0
        while s<len(intervals) : 
            if starts[s] <ends[e] : 
                count +=1
                s+=1
            else : 
                count -=1
                e+=1
            
            out = max(count, out)    
        return out
        
        