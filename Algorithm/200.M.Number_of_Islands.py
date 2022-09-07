class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #bfs 685ms(14.35%) / 16.5mb(64.23%)
        # right, down, left, up
        dr = [0,1,0,-1]
        dc = [1,0,-1,0]
        def bfs(r,c) :
            
            #1)탈출조건
            if(grid[r][c]=="0") : return
            #2)visited - mainaction
            grid[r][c] ="0"
            
            #3)호출
            for i in range(4):
                if(0<=r+dr[i]<m and 0<=c+dc[i]<n) : 
                    bfs(r+dr[i],c+dc[i])

        m = len(grid)
        n= len(grid[0])
        output = 0
        for i in range(m) : 
            for j in range(n) :
                if(grid[i][j]=="1") : 
                    bfs(i,j)
                    output+=1
        return output
    
        #bfs 공식 remind
        #1) 탈출조건
        #2) visited check
        #3) mainaction
        #3)호출..?