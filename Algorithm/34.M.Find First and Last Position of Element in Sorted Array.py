class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
#      prob analy..
#   1) big range : two pointer, bit masking, hashmap
#   2) O(logN) ==> binary search!
#   3) sorted array / list

#==> BINARY SEARCH 

# IDEA 1. binary search. 
        # left, right =0, len(nums)-1
        # while (left<=right ) : 
        #     print("left : ", left, "right", right)
        #     if(nums[left] == target and nums[right]==target) : return [left, right]
        #     mid = int((left + right)/2)
        #     if(nums[mid] <target and nums[left]!= target) :
        #         left = mid
        #     elif(nums[mid]>= target and nums[right]!=target) :
        #         right = mid 
        # return [-1,-1]      
    
# IDEA 2. binary search. with 1 
        # left, right =0, len(nums)-1
        # mid = 0
        # while (left<right ) : 
        #     mid = int((left + right)/2)
        #     if(nums[mid] == target) : 
        #         if(mid-1>=0 and nums[mid-1] == target): return [mid-1, mid]
        #         elif(mid+1<len(nums) and nums[mid+1]== target ) : return [mid, mid+1]
        #         else : return [mid,mid]
        #     if(nums[mid] <target ) :
        #         left = mid
        #     elif(nums[mid]> target) :
        #         right = mid 
        # return [-1,-1]       
        #  문제 제대로 안읽음,, 같은 element의 개수가 2 이상일수 있다는점을 간과했다..
        
# IDEA 3. BINARAY SEARCH & HASH TABLE & set
#         hashmap ={}
#         for i in range(len(nums)): 
#             if(nums[i] not in hashmap) :  hashmap[nums[i]] = 1
#             else : hashmap[nums[i]]+=1
#         print(hashmap)
#         s = sorted(list(set(nums)))
#         left , right = 0, len(s)-1
#         while(left<right) : 
#             print("left", left, "right", right)
#             mid = int((left+right)/2)
#             if(s[mid]== target) :
#                 if(hashmap[])
#             if(s[mid]<target) :
#                 right =mid
#             else : left = mid

# 내가 아는 알고리즘인데 난이도가 높아서 못푸는 문제..
# 답지 절대 보지말것
# IDEA 4 
#         print("----------------")
#         left, right=0, len(nums)-1
#         while(left<=right) :
#             mid = int((left+right)/2)
            
#             print("left", left, "right", right, "mid", mid)
#             if(nums[mid]==target) :
#                 left , right = mid, mid
#                 print("left", left, "right", right)
#                 while(nums[left]==target and nums[right]== target) : 
#                     if left==0 and right == len(nums)-1 :
#                         return [left,right]
#                     elif (left==0 or nums[left]!=nums[left-1]) and (right == len(nums)-1 or nums[right]!=nums[right+1]) : 
#                         return [left,right]
#                     print("leftt", left, "righty=t", right)
#                     if(nums[left-1]==target) : left -=1
#                     elif(nums[right+1]== target) : right+=1
                
#             if(nums[mid]<target) : left = mid+1
#             else : right = mid-1
#         return [-1,-1]
# ... out of ragne 
# 이 알고리즘은 mid로 찾아서 좌우로 넓혀가면서 마지막이 어딘지 찾는 방법

# 결국 솔루션 봄 ㅠㅠㅠ
# left찾고 right찾고 이렇게 두부분으로 나눔

# solution
# 근데 이 solution도 위에 idea 4랑 거의 비슷한거 같은데 약간 구현력이 딸리는듯.. (104ms 78.09% faster , 15.3mb less than 92.49%)

            def bs(nums, target, forStart) :
                print(nums, target, forStart)
                left, right =0, len(nums)-1
                while(left<=right) :
                    if (target not in nums) : return -1
                    mid = int((left+right)/2)
                    if(nums[mid]== target) :
                        if(forStart == True) : 
                            if(mid == left or nums[mid-1]!=target) : return mid
                            right = mid-1
                        else : 
                            if(mid == right or nums[mid+1]!=target) :return mid
                            left = mid +1

                    elif ( nums[mid]> target) : right = mid-1
                    else : left = mid+1
                return -1
            start = bs(nums,target,True)
            if(start ==-1) :  return [-1,-1]
            else : end = bs(nums, target,False)
            return [start,end]
