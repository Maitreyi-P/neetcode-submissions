class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        n = len(edges)
        adj = [[] for i in range(n+1)]


        def dfs(u,v):
            #detect cycle
            if visit[u]:
                return True
            
            visit[u] = True
            for nei in adj[u]:
                if nei == v:
                    continue
                if dfs(nei,u):
                    return True
            return False

        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
            visit = [False] * (n+1)
            if dfs(u,-1):
                return [u,v]
        return []
        

