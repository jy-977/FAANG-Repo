class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        #problem analy..
        # - graph
        # - search
        

        # 4423ms 21.64 slower // 35.87% more
        #idea 2 : dfs 
        g = [[] for i in range(n)]
        visited = [False] *n
        #1.making graph
        for a,b in edges : 
            g[a].append(b)
            g[b].append(a)

        #2.dfs
        def dfs (source):
            if visited[source] : 
                return
            visited[source] = True
            for i in g[source] : 
                dfs(i)
        
        dfs(source)
        if visited[destination] : return True
        else : return False

