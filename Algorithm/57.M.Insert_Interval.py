177 ms
17.2mb

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
            
            #전제
            # sorted
            # merged
            
            # step 1:append before new interval     step2 : insert  step3 : merge & append last
            #------------------------------------- newInterval ----------------------------------
            
            #step 2 : append newInterval into intervals
            res = []
            i=0
            while i < len(intervals) and intervals[i][0] <newInterval[0] : 
                res.append(intervals[i])
                i+=1

            
            #step 2 : insert newInterval
            if not res or res[-1][1]< newInterval[0] : 
                res.append(newInterval)
            else : 
                res[-1][1] = max(newInterval[1],res[-1][1])
            
            #step3 : merge & append last
            while i<len(intervals) : 
                if res[-1][1]>= intervals[i][0] : 
                    res[-1][1] = max(intervals[i][1], res[-1][1])
                else:
                    res.append(intervals[i])
                i+=1
            
            return res