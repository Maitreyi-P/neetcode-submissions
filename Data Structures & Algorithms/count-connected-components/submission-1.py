class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

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

        
        for i,j in edges:
            union(i,j)

        for i, p in enumerate(parent):
            parent[i] = find(i)

        return len(set(parent))