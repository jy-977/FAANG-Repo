from collections import deque
class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:

# idea 1) backtracking, recursive : 
# stack = [] ==> 120ms 15.3mb
# stack == deque() ==> 86ms 15.3mb 
# 성능차이가 생각보다 많이남!

        stack =deque()
        output = []
        
        print(chr(ord('a')+25))
        
        def isAlphabet(a):
            smallA, capitalA = ord('a'), ord('A')
            if(smallA<=ord(a)<smallA+26 or capitalA<=ord(a)<capitalA+26 ): return True
            return False
        
        def backTracking (idx) :
#           1) RETURN CONDITION  
            if(idx == len(s)) : 
                output.append(''.join(stack))
                return

#           2) MAIN ACTION , CALL RECURSIVE
            if(isAlphabet(s[idx])):
                case = [s[idx].lower(),s[idx].upper()]
                for _ in range(2) : 
                    stack.append(case[_])
                    backTracking(idx+1)
                    stack.pop()
                    
            else : 
                stack.append(s[idx])
                backTracking(idx+1)
                stack.pop()
            
        backTracking(0)
        return output    
            
# remind : dfs 공식
# 1) RETURN CONDITION
# 2) MAIN ACTION  : 
# 3) CALL RECURSIVE
