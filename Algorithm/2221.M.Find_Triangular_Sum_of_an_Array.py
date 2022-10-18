class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        #brute force : 7334 18.20% faster / 14.1mb 48.31less  (nlogn)
#         n = len(nums)
#         for i in range(n):
#             for j in range(n-i-1) :
#                 nums[j] = (nums[j]+ nums[j+1])%10
#             if n-i-1!=0 : nums[n-i-1]= 0 
#         return nums[0]



#idea 2) 331ms 90.23% faster / 14mb 77.25% less
# (a+b)%10 == a%10 + b%10 
# o(n)풀이법 진짜 오래걸렸다,,,
# 1
# 1 1
# 1 2 1
# 1 3 3 1
# 1 4 6 4 1 
# 1 N-1/1 (n-1)(n-1)/1*2  (n-1)(n-2)(n-3)/1*2*3 ---> 파스칼의 삼각형 공식


            res, nCr, n = 0, 1, len(nums) - 1
            for r, num in enumerate(nums):
                res = (res + num  * nCr) % 10
                nCr = nCr * (n - r) // (r + 1)
            return res