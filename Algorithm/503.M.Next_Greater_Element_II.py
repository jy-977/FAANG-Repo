class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
#         1 8 4 3 6 9 1 2 1
#                             1 8 4 3 6 9 1 2 1
#         1                  
#         1 . 8               8
#         8 4
#         8 4 3
#         8 4 3 . 6           8     6
#         8 4 . 6             8   6 6 
#         8 6 . 9             8   6 6 9
#         8 . 9               8 9 6 6 9
#         9 1                 8 9 6 6 9
#         9 1 . 2             8 9 6 6 9   2
#         9 2 1               8 9 6 6 9 * 2 * *
#         --------------------------------------
#         9 2 1 () 이미 완성된건 input 안함
#         9 2 1 . 8           8 9 6 6 9 * 2 * 8
#         9 2 . 8             8 9 6 6 9 * 2 8 8
        
        
#         output = [-1] * len(nums)
#         stack = nums[::-1]
#         print(stack)
#         for i in range(len(nums)-1,-1,-1) : 
#             cur = nums[i]
#             print('cur', cur)
#             while stack and  stack[-1][0]<=cur :  ##stack decreasing 
#                 print("sta", stack)
#                 new = stack.pop()
#                 print('new', new)
#                 if stack : 
#                     output[i] = stack[-1]
#                 output[i] = new[0]
#                 print('out', output)
#                 stack.append((nums[i], i))
#             i = (i+1)%len(nums)
#             print("-----------------------------")
#         return output
    
    
    
        n = len(nums)
        ret = [-1] * n
        stack1 =  nums[::-1]
        # stack = nums[::-1]
        for i in range(n - 1, -1, -1):
            
            
            while stack1 and stack1[-1] <= nums[i]:
                temp = stack1.pop()
            if stack1:
                ret[i] = stack1[-1]
            stack1.append(nums[i])
        return ret