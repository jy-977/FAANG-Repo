class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        output = 0 
        
#       70ms 32.16% / 13.7mb 95.50% faster
        s = set(nums)
        if(0 in s): 
            s.remove(0)
        accx = 0
        while s : 
            x = min(s)-accx 
            accx+=x
            s.remove(accx)
            output+=1
            
        return output