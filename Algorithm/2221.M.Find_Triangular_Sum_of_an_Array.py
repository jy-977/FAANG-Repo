class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        #brute force : 7334 18.20% faster / 14.1mb 48.31less  (nlogn)
#         n = len(nums)
#         for i in range(n):
#             for j in range(n-i-1) :
#                 nums[j] = (nums[j]+ nums[j+1])%10
#             if n-i-1!=0 : nums[n-i-1]= 0 
#         return nums[0]

        
                
                