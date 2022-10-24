class Solution:
    def findMin(self, nums: List[int]) -> int:
#         problem analysis
# 1) sorted array
# 2) searching
# 3) O(logN)
# 4) small range of len(nums)
            
        #2차 binary search 할때 
        # while l<=r : 로 할꺼면
        #     mid = l+(r-l)//2 
        # 특히 l == R 인 결과가 나와야 할때 적합
        #68ms 68.21% 14.2mb 23.11 % less
        l , r = 0, len(nums)-1
        while l<=r : 
            mid =l+(r-l)//2
            if nums[l] ==nums[r] : 
                return nums[l]
            if nums[l] <=nums[mid] : #not reverese
                if nums[l]< nums[r] : 
                    r = mid
                else : 
                     l = mid+1
            else :  #reverse
                r = mid 
                
