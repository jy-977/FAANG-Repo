class Solution:
    def search(self, nums: List[int], target: int) -> int:
#        prob analy
#       1) small range
#       2) sorted array
#       3) O(log n) --> binary search

# idea 1) binary search + ...?
#        if( target not in nums ) : return -1
        # k = 1
        # n = len(nums)
        # while(k <n )  :
        #     if(nums[k-1]>nums[k]) : 
        #         break
        #     k+=1
        # print(k)
        
#         left, right = k, k+n-1
#         while(left <= right) : 
            
        
#         while (left<= right) : 
#             mid= int((left+right)/2)
#             if(mid<=)

# idea2  slicing : 52ms (76.67% faster), 14.2mb (56.29mb less)
#       1.  target existanc check 
        if(target not in nums) : 
            return -1
        
#       2.  find rotate point K
        k = 1
        n = len(nums)
        while(k <n )  :
            if(nums[k-1]>nums[k]) : 
                break
            k+=1
        if(k==n) : 
            k = 0
            newnum = nums
        else : newnum =nums[k:]+nums[:k]
            
#       3. binary search 
        left , right = 0 , n-1
        while(left<=right) :
            mid = int((left+right)/2)
            if(newnum[mid]==target) : 
                if(0<=mid<n-k) :
                    return mid+k
                elif(n-k<=mid<n) : 
                    return mid-(n-k)
            elif(newnum[mid]<target) :left = mid+1 
            else : right = mid-1
                
# 이런 쪼그만 인덱스 계산하는게 젤 싫어 ㅠㅠ 어려운것도 아니면서 헷갈려
# mid 가 0일때,,,계산
# 인덱스 계산하는데만 두시간 걸린듯,, 
# 수학식으로 계산하는게 훨 빠름 