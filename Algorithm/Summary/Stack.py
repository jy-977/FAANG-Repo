#stack 

#monotonic stack ;
# time complexity O(n),
# space complexcity O(n)
output = []*len(arr)
stack = []  # pair : [val, i]

for i, val in enumerate(arr) : 
    while stack and val> stack[-1][0] : # stack[-1][0] 스택 맨 마지막의 [-1]      값 [0] 
        s_val , s_idx = stack.pop()
        output[idx] = ...   
    stack.append([val, i])
return output
