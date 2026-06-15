class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        #make a map, do dfs for cycle detection

        preMap = {i: [] for i in range(numCourses)}
        for c,p in prerequisites:
            preMap[c].append(p)

        visit = set()

        def dfs(course):
            if course in visit:
                return False
            if preMap[course] == []:
                return True
   
            visit.add(course)
            for p in preMap[course]:
               if not dfs(p): 
                return False
            visit.remove(course)
            preMap[course] = []
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False
        return True