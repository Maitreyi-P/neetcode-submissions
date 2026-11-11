class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        indegree = [0] * numCourses

        coursemap = defaultdict(list)
        for u,v in prerequisites:
            coursemap[u].append(v)
            indegree[v] += 1

        
        q = deque()
        for n in range(numCourses):
            if indegree[n] == 0:
                q.append(n)

        res = []
        while q:
            node = q.popleft()
            res.append(node)
            for p in coursemap[node]:
                indegree[p] -= 1
                if indegree[p] == 0:
                    q.append(p)

        if len(res) == numCourses:
            return res[::-1]
        return []

            