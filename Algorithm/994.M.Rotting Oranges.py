from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
#       1) problem analysis
#       similar prob : 01 matrix
#       bfs : distance, 최적거리 등 특징이 있으면 bfs


#         def bfs (r,c) : 
#             from collections import deque
#             dir = [(0,-1),(-1,0),(0,1),(1,0)]
#             q = deque([((r,c),0)])
#             while q:
#                 (rr,cc),d = q.popleft()
#                 print(rr,cc,d)
#                 for dr in dir:
#                     newr, newc= rr+dr[0], cc+dr[1]
#                     if(0<=newr<)
                    
                    
#         m = len(grid)
#         n = len(grid[0])
        
#         for 
        
#     bfs구현이 하나만 있는건 아닌데.. 너무 공식에 매몰되서 생각하지 말자
# =====================================================================================
# idea 2 )
#     start point 가 여러개 있을때는 start point 를 큐에 담아놓고 시작한다!

        m = len(grid)
        n = len(grid[0])
        q = deque()
        distance = 0 
        dir = [(0,-1),(-1,0),(1,0),(0,1)]
        
#       start point set
        for r in range(m) : 
            for c in range(n) :
                if(grid[r][c]==2) : q.append((r,c))
                    
#       bfs                    
        while q : 
            cr, cc = q.popleft()
            for dr in dir : 
                if(0<=cr+dr[0]<m and 0<=cc+dr[1]<n and grid[cr+dr[0]][cc+dr[1]]==1) : 
                    grid[cr+dr[0]][cc+dr[1]] = grid[cr][cc] +1
                    q.append((cr+dr[0],cc+dr[1]))
#       return check 
        for r in grid : 
            if(1 in r) : return -1
            else :
                distance = max(distance,max(r))
        return  distance -2  if(distance>0) else distance     
        
        
        
        
        
#       큐 구현 하는 방법
# #       1) 방법
#             1-1)재귀
#             1-2)반복문

#         2)starting point 개수
#             2-1)1개
#             2-2)여러개
