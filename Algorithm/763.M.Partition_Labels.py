class Solution:
    def partitionLabels(self, s: str) -> List[int]:
#         75ms 52.98 faster / 13.8mb lessthan 68.48% 
        length = len(s)
        left,right = 0,0
        part = {}
        output  = [] 
        for i,c in enumerate(s) :
            part[c] =i
        
        for i in range(len(s)) :
            
            if part[s[i]] >right :
                right = part[s[i]]
                
            if i==right : 
                output.append(right-left+1)
                left = right+1
        return output
        