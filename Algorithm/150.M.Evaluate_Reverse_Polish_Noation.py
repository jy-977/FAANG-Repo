class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        #stack ; 153ms 30faster 14.3mb 62.79 less
        stack = []
        for c in tokens: 
            if c =='+' or c =='-' or c =='*' or c =='/': 
                a = stack.pop()
                b = stack.pop()
                if c=='+' : 
                    stack.append(a+b)
                elif c=='-' : 
                    stack.append(b-a)
                elif c=='*' : 
                    stack.append(a*b)
                elif c=='/' : 
                    stack.append(int(b/a))
            else : 
                stack.append(int(c))
        return stack.pop()