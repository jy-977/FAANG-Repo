class Solution:
    def findMin(self, nums: List[int]) -> int:
#         problem analysis
# 1) sorted array
# 2) searching
# 3) O(logN)
# 4) small range of len(nums)

# return : min element in List

        




# # IDEA 1 : BINARY SEARCH(81ms 17.56% faster / 14.1mb 95.82% less)
# #  find index of smallest element on rotated list 
        # n = len(nums)
        # left, right = 0, n-1
        # if(nums[left]<=nums[right])  : #not rotated 
        #     return nums[left]
        # else :     #rotated
        #     while (left<right) : 
        #         mid= int((left+right)/2)
        #         if(nums[left] == nums[mid]) : 
        #             return nums[right]
        #         elif(nums[left] <nums[mid] ) :    
        #             left = mid  
        #         else : right = mid
                    
                    

# IDEA 2 : BRUTE FORCE (80ms 19.08% faster / 14.3mb 23.64%)
        # for idx in range(0,len(nums)-1) : 
        #     if (nums[idx]>nums[idx+1]) : 
        #         return nums[idx+1]
        # return nums[0]


# bruteforce보다 binaray search 가 훨씬 빠를거 같았는데 의외다,,
#solution 도 돌려봤는데 73ms 32.38% faster, 14.3mb 23.64 less나옴