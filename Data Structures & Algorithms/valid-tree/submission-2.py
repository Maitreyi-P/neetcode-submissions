class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
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
            if find(i) == find(j):
                return False

            union(i,j)

        for i in range(len(parent)):
            parent[i] = find(i)

        return len(set(parent)) == 1 