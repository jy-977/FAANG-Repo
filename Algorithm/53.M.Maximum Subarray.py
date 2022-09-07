class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        #idea 1 Two pointers
#         안풀렸음
# =====================================================================
        #solution : dp - kadane 부분합 
    
        #solution : kadane 부분합
        #이런 최대 연속 부분합 문제 되게 많음.
        #array의 숫자가 모두 양수인 경우 two pointer로 풀수 있지만
        #이렇게 음수가 끼인 경우 새로운 dp.. 의 개념을 이용한 문제를 품
        #되게 typical 한 문제기 때문에 알아두는게 좋다
        
        #975ms  68.42% faster /28mb  22.80less             
        # F(k) = max(F(k-1)+arr[k], arr[k])    
        # subM = fullM = nums[0]
        # for i in range(1,len(nums)):
        #     subM = max(subM+nums[i], nums[i])
        #     fullM = max(fullM, subM)
        # return fullM

    
#       dp2
#         memo = [0 for _ in range(len(nums))]
#         memo[0] = nums[0]
#         for i in range(len(nums)) : 
#             memo[i] = max(memo[0])
            
#         여기서 f(X) = x까지 원소의 최대 부분합.. 이 아니네..?
# #         점화식 생각해낼때 함정이 
        
#         n = [0 for i in range(len(nums))]
#         n[0] = nums[0]
#         for i in range(1, len(nums)):
#             n[i] = max(n[i-1] + nums[i], nums[i])
#         print(n)
#         return max(n)
    
#========================================================================    
        #solution : divide and conquer
        
    
    
    # n = randint(1,pow(10,5))
        # arr = []
        # for i in range(n) :
        #     arr.append(randint(-pow(10,4), pow(10,4)))
        # print(arr)