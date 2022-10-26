class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
#         monotonic stack

        output = [0]*len(temperatures)
        stack = [] #pair [temp,idx]
        
        for i, temp in enumerate(temperatures) : 
            while stack and temp > stack[-1][0] : 
                stack_temp, stack_idx  = stack.pop();
                output[stack_idx] = i-stack_idx
            stack.append([temp, i])
        return output