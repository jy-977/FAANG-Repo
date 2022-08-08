class Solution:
    def hammingWeight(self, n: int) -> int:
        cnt =0
        while n : 
            if(n&-n==1) : cnt+=1
            n = n>>1
        return cnt

        # 50ms ,14mb