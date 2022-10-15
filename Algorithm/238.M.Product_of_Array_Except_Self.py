class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #neetcode solution 참고 
        
        #idea 1) 600ms faster than 23.73% 22.4mb less than 24.35%
#         prefix =  [0]* (len(nums))
#         postfix = [0]* (len(nums))
#         output = [0]* (len(nums))
#         for i in range(len(nums)) : 
#             if i==0 : 
#                 prefix[i] = nums[i] 
#                 postfix[len(nums)-1] = nums[len(nums)-1]
#             else : 
#                 prefix[i] = prefix[i-1] * nums[i] 
#                 postfix[len(nums)-i-1] = nums[len(nums)-1-i] *  postfix[len(nums)-i]
        
#         for i in range(len(nums)) : 
#             if i== 0: 
#                 output[i] = postfix[i+1]
#             elif i== len(nums)-1 : 
#                 output[i] = prefix[i-1]
#             else : 
#                 output[i] = prefix[i-1]* postfix[i+1]
#         return output
        # idea2 ) 252ms 88.15% faster / 21.3mb less than 58.59% elss
        output = [0]* (len(nums))
        pre,post = 1, 1
        for i in range(len(nums)) : 
            output[i] = pre
            pre = pre*nums[i]
        for i in range(len(nums)) : 
            output[len(nums)-i-1]*=post
            post = post * nums[len(nums)-i-1]
        return ouptut