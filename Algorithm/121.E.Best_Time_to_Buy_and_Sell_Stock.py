class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #problem analysis
        #1) buy fisrt sell next
        #2) the fastest smallest / 
        
        #two pointers
#         L, R =0, len(prices)-1
        
#         output = prices[R]- prices[L]
#         for i in range(len(prices)) : 
#             print(L, R)
#             if(L>=R): break
#             if(price[R]-prices[L+1]>max ) : 
#                 L+=1
#             elif(prices[R-1]-prices[R]>=0) : 
#                 R-=1
#             output = max(output, prices[R]-prices[L])
#         return 0 if output<=0 else output
        # .. 안됨
        
        #dp.. 도 가능하지, 않을까?  ==> time exceed ==> 2265ms (10.02% faster) / 25.1mb (38.27% mless)
        maxP = 0
        minP = prices[0]
        # f(x+1) = max(f(x-1), arr[x]-min(arr[:x]))
        for i in range(1,len(prices)) : 
            minP = prices[i] if minP>prices[i] else minP #-min(arr[:x])
            maxP = maxP if( maxP > prices[i]-minP) else prices[i]-minP #max(memo[i-1], prices[i]-minP)
        return maxP
        #min max 오래걸림.., memozation 없앰 
        #--> 이거 dp 아님... one pass래
      