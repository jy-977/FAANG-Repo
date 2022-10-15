class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
#       right down left up
        dir =[(0,1),(1,0),(0,-1), (-1,0)] 
        
        out = [[0]*n for _ in range(n)]
        val = 1
        dv =0
        i,j= 0,0
        for _ in range(n*n) : 
            out[i][j] = val
            val +=1
            nexti = i+dir[dv][0]
            nextj = j+dir[dv][1]
            if not(0<=nexti<n and 0<=nextj<n) or out[nexti][nextj]!=0: 
                dv=(dv+1)%4    
            i = i+dir[dv][0]
            j = j+dir[dv][1]
        return out
        