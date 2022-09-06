class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        #problem analysis
        #O(m+n)
        #return 없음 ==> nums1안에 넣엉함
        
        #그냥 for문 
        #mergesort에서 merge할때 처럼 인덱스로?
        #2번 솔루션이랑 비슷한 문제
        # i=j=k=0
        # temp =[]
        # while(i<m || j<n) :
        #     if(nums1[i]<= nums2[j]) : 
        #         i+=1
        #     else (nums1[i]>nums2[j]):
        
        
        #idea 2 ) 뒤에서 부터 비교하기 
        #82ms 8.15% faster / 13.9mb 85.72 less
#         i , j = m-1, n-1
        
#         for p in range(m+n-1, -1, -1) :
#             if j<0  : return 
#             if(i<0 or nums2[j]>=nums1[i]) : 
#                 nums1[p] = nums2[j]
#                 j-=1
#             else : 
#                 nums1[p] = nums1[i]
#                 i-=1
                
             # Set p1 and p2 to point to the end of their respective arrays.
        p1 = m - 1
        p2 = n - 1
    
        # And move p backwards through the array, each time writing
        # the smallest value pointed at by p1 or p2.
        for p in range(n + m - 1, -1, -1):
            if p2 < 0:
                break
            if p1 >= 0 and nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
                  
        