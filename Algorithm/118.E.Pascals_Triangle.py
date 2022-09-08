from collections import deque
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        #recursive
        #dp : 64ms 10.73% faster / 13.7 mb 97.45% less

        output =[[1]]
        # f(r) = [[f(r-1,0),0]+[0,f(r-1)]]
        for i in range(1, numRows) :
            output.append([])
            for j in range(i+1) :
                if (j==0 or j==i) : output[i].append(1)
                else : 
                    output[i].append(output[i-1][j-1] + output[i-1][j])
            
        return output