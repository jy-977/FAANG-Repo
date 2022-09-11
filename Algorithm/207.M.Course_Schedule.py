from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #problem analysis 
        #linked list hash,,,, hash?
        
        #create test case
        # output =[]
        # for i in range(10) :
        #     a,b = randint(0,100), randint(0,100)
        #     if([a,b] in output ): 
        #            continue
        #     output.append([a,b])
        # print(output)
#======================================================================        
        #idea 1) hash / link --> time exceed (답은 맞는듯)
        #이런경우 linked list 선언 못하나유.
#         def link(hm, s, d) : 
#             if(s not in hm) : return True
#             if(d in hm[s]) : return False
#             for a in hm[s] :
#                 if not(link(hm, a, d)) : return False
#             return True
        
#         hm = {}
#         for p in prerequisites : 
#             #hashmap making
#             if(p[0] not in hm) :
#                 hm[p[0]]  = [p[1]]
#             else : 
#                 hm[p[0]].append(p[1])
            
#             #valid check 
#             if(p[1] in hm) : 
#                 if not(link(hm, p[1],p[0])) : return False
#         return True

        #solution : DFS / BFS 힌트
        #어디서 DFS / BFS 힌트를 찾을수 있나용...
        

#======================================================================
        # dfs래용..
        # 왜 bfs 는 안되나용
        
        #dfs 공식
        def link(key) : 
            visited.append(key)
            
            #1) 탈출 조건
            print("key : ", key)
            
            print("visited : ", visited)
            if(key not in hm) :
                print("return point 1")
                return True
            
            #2) main action
            for a in hm[key] :
                print("a" ,a)
                if a in visited : 
                    return False;
                if(link(a)==False): return False
                 
            print("return point3")
            return True
        
        hm = {}
        
        #hashmap making
        for p in prerequisites :
            if(p[0] not in hm) :
                hm[p[0]]  = [p[1]]
            else : 
                hm[p[0]].append(p[1])
            
       #valid check 
        for key in hm : 
            print("key-----", key)
            visited = deque([])    
            if(link(key)==False) : return False
            print("visited", visited)
        
        return True
