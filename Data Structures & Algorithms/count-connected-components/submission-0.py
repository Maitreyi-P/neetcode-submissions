class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        edgemap = {i: [] for i in range(n)}
        for a,b in edges:
            edgemap[a].append(b)
            edgemap[b].append(a)

        visit = set()
        count = 0

        for node in range(n):
            if node not in visit:
                q = deque([node])
                visit.add(node)

                while q:
                        node = q.popleft()
                        nei = edgemap[node]
                        for n in nei:
                            if n not in visit:
                                visit.add(n)
                                q.append(n)
                count +=1

        return count
     


                    