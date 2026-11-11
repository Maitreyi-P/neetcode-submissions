class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        

        indegree = [0] * numCourses
        coursemap = defaultdict(list)

        for u,v in prerequisites:
            coursemap[u].append(v)
            indegree[v] += 1

        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        
        res = []
        while q:
            node = q.popleft()
            res.append(node)
            for pre in coursemap[node]:
                indegree[pre] -= 1
                if indegree[pre] == 0:
                    q.append(pre)

        return len(res) == numCourses

        