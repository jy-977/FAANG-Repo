class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        #problem analysis
            #accumulated sum
            #range : small

            
#idea 1) DP --------------------------------------------
        #dp : 73ms 40.94% faster / 14.2mb 27.13 % less
        # output=[0 for _ in range(len(nums))]
        # output[0] = nums[0]
        # for i in range(1,len(nums)):
        #     output[i] = output[i-1] + nums[i]   
        # return output
    
    #edgecase 처리 연습
    #길이 
        
#solution 1 ) -----------------------------------------
        #solution : 내장함수 accumulate
        #85ms 16.55% faster , 14.mb 72.59% less
        # from itertools import accumulate
        # return list(accumulate(nums))