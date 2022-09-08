class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        #idea 1 ) hash
        hashmap ={}
        for i in nums1 : 
            if(i not in hashmap) : 
                hashmap[i] =1
            else : 
                hashmap[i]+=1
        output = []
      
        for i in nums2 : 
            if(i in hashmap and hashmap[i]>0) :
                hashmap[i]-=1
                output.append(i)
        return output
    
#     79ms 53.30% faster / 14mb 84.41% less
# 중복가능 --> set안됨
#자존감 채우기용^^    