class Solution:
    def isValid(self, s: str) -> bool:
        #61ms 34.29 faster / 14mb 26.20 less
        stack = []
        def isOpened(c) : 
            if c == '(' or c == '[' or c=='{' : return True
            else :False
        def ispared(a,b) : 
            if a=='(' : 
                if b== ')': return True 
                else : return False 
            elif a=='{' : 
                if b=='}' : return True
                else: return False
            else : 
                if b==']' : return True
                else: return False
                    
        for i,c in enumerate(s) : 
            if(isOpened(c)) : 
                stack.append(c)
            else : 
                if stack : 
                    a = stack.pop()
                    if(not ispared(a , c)) :
                        return False
                else: return False
        if len(stack) ==0 : return True
        else : False
                