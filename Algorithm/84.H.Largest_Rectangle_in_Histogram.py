class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        #requirements
            #return lagest_rectangle's_area
            # rectangel : h[i] // h[i]~h[i+n] 한개일수도 여러개 걸칠수도


        #analysis
            #1<=N<=10^5 : O(nlogn), O(n)
            
        #idea : monotonic stack
        # stack = [(0,heights[0])] #(i,height[i]) 
        # max_area = 0

        # for i in range(0,len(heights)) : 
        #     if stack and (i-stack[-1][0]+1)*stack[-1][1] <heights[i] : 
        #         stack.append((i,heights[i]))
        #         max_area= max(max_area, heights[i])
        #     else : 
        #         prev_idx, prev_h = stack.pop()
        #         stack.append((prev_idx, min(prev_h, heights[i])))
        #         max_area= max(max_area, (i-stack[-1][0]+1)*stack[-1][1] )
        # return max_area
        
        
        # #test case : [1,2,2] 통과 안됨
        
        #solution 봄 : 
        #중요한건 height decrease 되면 더이상 그 높이로는 rectangle 못만듦 : pop한다는개념
        #Runtime
1010 ms
Beats
82.42%
Memory
30.5 MB
Beats
31.55%
        max_area = 0 
        stack = []  # (i,height)
        for i, h in enumerate(heights) :
            start = i
            while stack and stack[-1][1]>h : 
                idx, height = stack.pop()
                max_area = max(max_area,height*(i-idx))
                start = idx
            stack.append((start,h))
        for i, h in stack :
            max_area = max(max_area, h*(len(heights)-i))     
        return max_area   


Monotonic Stack pattern..
