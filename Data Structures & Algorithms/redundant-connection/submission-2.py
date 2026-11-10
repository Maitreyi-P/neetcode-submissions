class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        n = len(edges)

        parent = [i for i in range(n)]
        
        def find(x):
            if parent[x] == x:
                return x
            parent[x] = find(parent[x])
            return parent[x]

        def union(x,y):
            rootx = find(x)
            rooty = find(y)

            if rootx != rooty:
                parent[rootx] = rooty


        for u,v in edges:
            if find(u-1) == find(v-1):
                return [u,v]
            union(u-1,v-1)