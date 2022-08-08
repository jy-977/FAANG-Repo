class Solution:
    def reverseBits(self, n: int) -> int:
        
# idea 1) bit masking 54ms ,    13.9mb
        output = 0
        for _ in range(32) :  
            output = (output<<1)+n%2
            n = n>>1
        return output
    
    
    
# idea 2) solution check
        output =0
        for _ in range(32) : 
            output  = output<<1 + (n&1)
            n=n>>1
        return output
#  content 마지막 bit구하는법!!
# n&1 ==> 뭐야 개쉽자나,,,
