from collections import deque
class Solution:
    def climbStairs(self, n: int) -> int:
        
        
# =============================================================================
# # idea 1 : dfs + stack   ==> time exeeding 
#         stack = deque()
#         outputstack = [] #for debugging
#         def recur() : 
#             # 1)return condition
#             if sum(stack)== n : 
#                 outputstack.append(list(stack)) #for debugging
#                 return 
            
#             # 2) main action
#             for step in [1,2] : 
#                 if (sum(stack) + step <= n) :  #prunning? 
#                     stack.append(step)
#                     recur()
#                     stack.pop()
#         recur()
#         return len(outputstack)

# =============================================================================
# # idea 2 : dfs + int  ==>time exeeding 
#         stack = deque()
#         global output
#         output =0
#         def recur() :
#             global output
#             # 1)return condition
#             if sum(stack)== n : 
#                 output+=1
#                 return 
            
#             # 2) main action
#             for step in [1,2] : 
#                 if (sum(stack) + step <= n) :  #prunning? 
#                     stack.append(step)
#                     recur()
#                     stack.pop()
#         recur()
#         return output

# =============================================================================
# idea 3 : dp 55ms 13.9mb
# 점화식..?아이디어 답지찬스!
# 피보나치랑 똑같지 않나?
# f(n)==1 f(2)==2 f(3)=3 f(4)=5 f(5)=8..
# f(n) = f(n-1) + f(n-2)
# recursion + memozation

# 배열로 memozation안하면 더 빠르게도 가능!
        memo = [0 for _ in range(46)]
        memo[1] = 1
        memo[2] = 2
        if(n>2) : 
            for num in range(3, n+1) : 
                memo[num] = memo[num-2] + memo[num-1]
        return memo[n]
    

# 답
# =============================================================================
# dp .. topdown bottom up 
# 뭐라는지 하나도 모르겠다
# 일단 피보나치 하나 외워놓으면 recursion 이나 dp등 이해하는데 되게 많이 도움이 됨 직관적이고 제일 간단한 함수니까..


# dfs공식 
# 1) return condition
# 2) mainaction
# 3) call recursively