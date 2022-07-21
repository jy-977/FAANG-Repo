from collections import deque

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

#   problem analysis
# 1) search DFS?
# 2) 
    
# #    idea 1) DFS Stack
#             m = len(image[0])
#             n = len(image)
#             sr_visited = deque([sr])
#             sc_visited = deque([sc])
    
#             sr_stack = deque([sr])
#             sc_stack = deque([sc])
        
#             while(sr_stack and sc_stack ) : 
#                 cur_sr = sr_stack.pop()
#                 cur_sc = sc_stack.pop()

#                 sr_visited.append(cur_sr)
#                 sc_visited.append(cur_sc)
#                 print("r", cur_sr, "c" , cur_sc, "i", image[cur_sr][cur_sc] )
#                 if(image[cur_sr][cur_sc]!=0) : 
#                     image[cur_sr][cur_sc] =color
                    
#                 if(cur_sr==1 and cur_sc==0):
#                     print("cur_sr-1", cur_sr-1,"cur_sc", cur_sc,(cur_sr-1 not in sr_visited)  )
#                     print("not(cur_sr-1 in sr_visited and cur_sc in sc_visited)", (cur_sr-1 not in sr_visited) or (cur_sc not in sc_visited))
#                     print(cur_sr-1 in sr_visited)
#                     print(cur_sc in sc_visited)
#                     print(sr_visited)
#                     print(sc_visited)
                    
#         #                   up

#                 if not(cur_sr-1<0) and  not(cur_sr-1 in sr_visited and cur_sc in sc_visited) : 
#                     print("up")
#                     sr_stack.append(cur_sr-1)
#                     sc_stack.append(cur_sc)

#     #                   left
#                 if not(cur_sc-1<0) and not(cur_sr in sr_visited and cur_sc-1 in sc_visited) : 
#                     print("left")
#                     sr_stack.append(cur_sr)
#                     sc_stack.append(cur_sc-1)

#     #                   down
#                 if not(cur_sr+1>n-1) and not(cur_sr+1 in sr_visited and cur_sc in sc_visited) : 
#                     print("down")
#                     sr_stack.append(cur_sr+1)
#                     sc_stack.append(cur_sc)

#     #                   right
#                 if not(cur_sc+1>m-1) and not(cur_sr in sr_visited and cur_sc+1 in sc_visited) :  
#                     print("right")
#                     sr_stack.append(cur_sr)
#                     sc_stack.append(cur_sc+1)
#             return image

# =============================================================================================================
# idea 2 : dfs recursive 95ms, 13.9mb
            def dfs (x,y,graph) :
    #           1) return condition 
                   # 1-2)out of range check 
                if not(0<=x<n) or not(0<=y<m) : return
    #              1-1)visited check
                if(graph[x][y]!=original or graph[x][y]==color) : return
             
                # 2) main act : coloring
                graph[x][y] = color
                
#               3) indexing
                dfs(x-1,y,graph)
                dfs(x,y-1,graph)
                dfs(x+1,y,graph)
                dfs(x,y+1,graph)
        

#           delta list : left down right up
#             dx = [-1, 0,0,1]
#             dy = [0,-1,1,0]
            
            m = len(image[0])
            n = len(image)
            original = image[sr][sc]
            
            dfs(sr,sc,image)
            # print(image)
            return image
    

#   content 


# BFS DFS차이
# BFS : 최단거리, 
# DFS : 모든 노드, 간단, 느림, 미로찾기= DFS!

# DFS 
# deque!
# recursive

# dfs bfs 아직 많이풀어봐야할듯..