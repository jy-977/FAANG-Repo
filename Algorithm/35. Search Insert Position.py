class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
#         문제분석
# 1) search
# 2) 정렬된 array
# 3) O(log n)
        
        left, right = 0,len(nums)-1
        
        while (left<=right) :
            pivot = int((left+right)/2)
            if ( nums[pivot]== target) :
                return pivot
#             right
            elif (nums[pivot]> target ):
                right = pivot-1
                
#             left
            else :
                left = pivot + 1
        if( nums[pivot]>target) : return pivot
        else :  return pivot +1
