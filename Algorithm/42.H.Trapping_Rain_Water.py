from collections import deque
class Solution:
    def trap(self, h: List[int]) -> int:
        #requirement

        #analysis
        #1<=n<=2*10^4
        #O(n) : twopointer, hashmap, bit manipulation, slidingwindow, monotonic stack

        #idea : two pointers
        

        #실패 결국 solution봄
        # 핵심 아이디어
        # 1. two pointer 
        # 2. min(l,r)- h[i] : i 별로 area 계산해서 합해줌
     
     
        # Runtime 141 ms
        # Beats 79.31%
        # Memory 16 MB
        # Beats 81.6%

        l,r = 0, len(h)-1
        max_left , max_right = h[l], h[r]
        output = 0

        while l<r : 
            

            if h[l]<h[r] :
                this_area = min(max_left, max_right) - h[l]
                output += this_area if this_area>0 else 0 
                l+=1
                max_left = max(max_left, h[l])
            else : 
                this_area = min(max_left, max_right) - h[r]
                output += this_area if this_area>0 else 0 
                r-=1
                max_right = max(max_right, h[r])
        return output

