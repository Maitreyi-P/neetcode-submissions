class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        premap = {i:[] for i in range(numCourses)}
        for c,p in prerequisites:
            premap[c].append(p)

        visit = set()
        cycle = set()
        res = []

        def dfs(course):
            if course in cycle:
                return False
            if course in visit:
                return True

            cycle.add(course)
            for p in premap[course]:
                if dfs(p) == False:
                    return False
            cycle.remove(course)
            visit.add(course)
            res.append(course)
            return True

        for c in range(numCourses):
            if not dfs(c):
                return []
                
        return res
        

