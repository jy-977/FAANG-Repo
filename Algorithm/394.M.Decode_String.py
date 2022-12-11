from collections import deque
class Solution:
    def decodeString(self, s: str) -> str:


        ##stack 62ms 22.3% faster / 13.9 mb 20.29 less
        stack = []
        for c in s : 
            
            if c==']' : 
                # 1) pop - repeat characters
                repeat=''
                while stack[-1]!='[' : 
                    repeat = stack.pop()+ repeat
                stack.pop()
                # 2) pop - numbers 
                n=''
                while stack and stack[-1].isdigit() : 
                    n=stack.pop()+n
                # append repeatead 
                for i in range(int(n))  : 
                    stack.extend(repeat)
            else : 
                stack.append(c)
                
        return ''.join(stack)