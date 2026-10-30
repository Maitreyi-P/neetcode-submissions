class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        

        if len(edges) != n - 1:
            return False 

        nodemap = defaultdict(list)
        for u,v in edges:
            nodemap[u].append(v)
            nodemap[v].append(u)

        visit = set()

        def cycle(node,parent):
            if node in visit:
                return False
            
            visit.add(node)
            for n in nodemap[node]:
                if n == parent:
                    continue
                if not cycle(n,node):
                    return False

            return True

        if not cycle(0,-1):
            return False

        if len(visit) != n:
            return False

        return True

        