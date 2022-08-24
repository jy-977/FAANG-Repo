from collections import deque
class Solution:
    def trap(self, height: List[int]) -> int:
#       problem analysis
#       big range : hashmap
#       logn or n?

# idea 1 : brute force : time exceed
# 처음에 생각할때는 별로 할수 있는 알고리즘이 없다고 생각했음

        level = max(height)
        n = len(height)
        water = 0 
        # print("______________________________")
        
        while (level) :  #loop for level
            # print("levle : ", level, "water : ", water)
            points = deque()
            #find points 
            start = -99
            for idx in range(n) : 
                if height[idx] >=level : 
                    if(start==-99) : 
                        start = idx
                        continue
                    water+=idx-start-1
                    start = idx
            level-=1
        return water
# idea 2 : dp

# idea 3 : 2pointers 




# Review : 
# 처음 풀어보는 hard 문제라 겁먹었는데 생각보다 처음 방법 생각해내는게 어렵진 않았음
# 그래서 categorized 되지 않은 문제가 아닌가 하고 .. 생각했지
# solution 보니까 방법이 여러개더라
# 아직 필요한 알고리즘을 알아내는 눈이 부족하다




#24 AUG 2022




from collections import deque
class Solution:
    def trap(self, height: List[int]) -> int:
        
        #problem analysis
        #1) big range : 
        
        
#         level = max(height)
#         water = 0 
      
#         while (level) :  #loop for level
#             # print("levle : ", level, "water : ", water)
#             points = deque()
#             #find points 
#             start = -99
#             for idx, a in enumerate(height) : 
#                 if a >=level : 
#                     if(start==-99) : 
#                         start = idx
#                         continue
#                     water+=idx-start-1
#                     start = idx
#             level-=1
#         return water

        #2) brute force : .. 웬만하면 쓰지말자 O(n^2)
    
    
        #3) 24/8/2022 --> two pointers (bipolar)
        #container with most water 푼 이후 다시시도!
        L, R =0, len(height)-1  #==> pointer
        LL, RR = 0, len(height)-1 #==> highst pointer
        output = 0
        cumL= cumR =0
        while(L<R) :
            if(height[L]<=height[R]) :
                L+=1
                
                if(height[LL]<=height[L]) :
                    if(height[LL]!=0) : 
                        output += (height[LL] *(L-LL-1))- cumL
                    LL=L
                    cumL  = 0
                else : cumL +=height[L]
                #output accum
            else :
                R-=1
                if(height[RR]<=height[R]) : 
                    if(height[RR]!=0) : 
                        output += (height[RR] *(RR-R-1))- cumR
                    cumR  = 0
                    RR = R
                else : cumR +=height[R]
        return output