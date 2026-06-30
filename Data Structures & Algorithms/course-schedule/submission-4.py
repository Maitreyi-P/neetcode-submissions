class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        courseMap = {i:[] for i in range(numCourses)}

        for c,p in prerequisites:
            courseMap[c].append(p)

        visit = set()
        def dfs(course):
            if course in visit:
                return False

            if courseMap[course] == []:
                return True

            visit.add(course)
            for p in courseMap[course]:
                if not dfs(p):
                    return False
            visit.remove(course)
            courseMap[course] = []
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False
        return True
