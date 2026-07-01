class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        courseMap = {i:[] for i in range(numCourses)}

        for c,p in prerequisites:
            courseMap[c].append(p)
        
        order = []

        visit = set()
        cycle = set()

        def dfs(course):
            if course in cycle:
                return False

            if course in visit:
                return True

            cycle.add(course)
            for p in courseMap[course]:
                if not dfs(p):
                    return False
                    
            cycle.remove(course)
            visit.add(course)
            order.append(course)
            return True

        for c in range(numCourses):
            if not dfs(c):
                return []
        return order

