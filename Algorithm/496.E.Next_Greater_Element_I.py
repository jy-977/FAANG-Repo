class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
            
        # soluiton 1 ) hash, brute force : 
        # 64ms, 86.13faster / 14.1 56.82 less
#         len1 = len(nums1)
#         len2 = len(nums2)
#         hm = dict()
#         output = [-1]*len(nums1)
#         for i in range(len2) : 
#             hm[nums2[i]] = i
            
        
#         for i in range(len(nums1)) : 
#             for j in range(hm[nums1[i]],len2) :
#                 if nums1[i]<nums2[j] : 
#                     output[i] = nums2[j]
#                     break
#         return output
                    
        
               
        # solution 2 ) hashmap , monotonous stack
        # 84ms 77.71 faster 14mb 95.88 less
        len1 = len(nums1)
        len2 = len(nums2)
        hm = dict()
        output = [-1]*len1
        stack = []
        for i in range(len1) : 
            hm[nums1[i]] = i
            
        
        for i in range(len2) : 
            cur = nums2[i]
            
            while stack and cur>stack[-1] : 
                new = stack.pop()
                output[hm[new]] = cur
            if cur in nums1 : 
                stack.append(cur)
        return output
                    