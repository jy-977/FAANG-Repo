#92.49% 91.76mb 

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        #problem analy..
        # - graph
        # - search
        

        #idea 1 : union find
        parent = [i for i in range(n)]
        #find parent
        def findParent(parent, x ) : 
            if parent[x] == x : return x
            parent[x] = findParent(parent,parent[x])
            return  parent[x] 
        print(parent)

        #union parent
        for edge in edges : 
            a = findParent(parent,edge[0])
            b = findParent(parent,edge[1])
            if a<b : parent[b] = a
            else : parent[a] = b
       
        #compare parent
        if findParent(parent, source) == findParent(parent,destination) :
            return True
        else :
            return False