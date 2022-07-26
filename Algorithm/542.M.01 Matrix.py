
#         def bfs(r,c) :
#             dirs=[(0,-1),(-1,0),(0,1),(1,0)]
#             visited= set()
#             q = deque([((r,c),0)])
            
#             while q : 
#                 for i in range(len(q)):
#                     cur,d = q.popleft();
#                     cur_r,cur_c = cur
#                     if(mat[cur_r][cur_c]==0): return d
#                     visited.add(cur)
#                     for dir in dirs : 
#                         newR , newC = cur_r+dir[0], cur_c+dir[1]
#                         if(newR>=0 and newR<len(mat) and newC>=0 and newC<len(mat[0])):
#                             if(newR,newC) not in visited : 
#                                 q.append(((newR, newC),d+1))
#             return -1
            
            
#         for r in range(len(mat)):
#             for c in range(len(mat[0])):
#                 if(mat[r][c]==1) : 
#                     mat[r][c] = bfs(r,c)
                    
#         return mat
     

# bfs 알고리즘은 맞는데 time limit 걸림...
# 다른 방법을 찾아보는게!
