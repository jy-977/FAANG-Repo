class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

# problem analysis
# 1) big range : two pointers, bit manipulation , hash 
# 2) unsorted list 


# idea 1 ) two pointer
# sort --> two pointers
#         left , right =0
#         while (left<=right) :
#             if(nums[left] + nums[right]==target)   return [left,right]
#             elif : 
                
    
# idea 2) for ==> brute force 걍 무조건도는거 (6722ms , 14.9mb)
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if(nums[i]+nums[j]==target): 
        #             return [i, j]
                
# solutions 1) two pass hash table (81ms, 15.2ms) --> bruteforce랑 차이 엄청 많이남...
# hash : dictionary 로 정의

        # hashmap = {}
        # for i in range(len(nums)) : 
        #     hashmap[nums[i]] = i
        # for i in range(len(nums)) : 
        #     complement  = target - nums[i]  # a+ b = target ==> a = target -b를 이용
        #     if(complement in hashmap and hashmap[complement]!=i ) : 
        #         return [i, hashmap[complement]]
        # 의문점 1)
#       [1,2,-1,2,3,3] target : 6 같이 같은 숫자가 여러개 있을때는 해시테이블 어떻게 만듦?
#       {1: 0, 2: 3, -1: 2, 3: 5}
#       마지막 인덱스를 저장함
#       return [i, hash[complement]] 이므로 hash[complement]--> 뒷쪽 인덱스를 필요로함

# solution 2) one pass hash table (97ms 15.2mb)
            hashmap ={}
            for i in range(len(nums)) : 
                complement = target-nums[i]
                if complement in hashmap : 
                    return [i, hashmap[complement]]
                hashmap[nums[i]] = i
        
            

# hash 처음 해봐서 어떻게 정의하는지도 몰랐다,, 변명인가? 
# hash 는 O(1)이기 때문에 big range에 적합함
