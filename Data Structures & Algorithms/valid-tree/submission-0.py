class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        if len(edges) > n-1:
            return False

        edgemap = {i: [] for i in range(n)}
        for a,b in edges:
            edgemap[a].append(b)
            edgemap[b].append(a)

        visit = set()
        
        def dfs(node,parent):
            if node in visit:
                return False

            visit.add(node)
            for nei in edgemap[node]:
                if nei == parent:
                    continue
                if not dfs(nei,node):
                    return False
            return True


        if not dfs(0,-1):
            return False

        if len(visit) != n:
            #disconnected
            return False

        return True

         
                