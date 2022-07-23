from collections import deque
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
    # problem analysis
#     
        
# =======================================================
# idea 1) dfs.. 

        def dfs (r,c):
#             break condition
            if not(0<=r<m and 0<=c<n) : 
                return 0
            if grid[r][c] == 9 or grid[r][c]==0:
                return 0
#           main act
            grid[r][c]=9
            return  1+ dfs(r-1,c)+dfs(r,c-1)+ dfs(r,c+1)+dfs(r+1,c)
             
        m = len(grid)
        n = len(grid[0])
        
        max_area = 0
        areas = [dfs(r,c) for r in range(m) for c in range(n) if(grid[r][c]==1)] or []
        return  max(areas)  if(areas) else  0
        