class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        preMap = defaultdict(list)
        for c,p in prerequisites:
            preMap[c].append(p)

        currSet = set()
        visitSet = set()
        res = []

        def cycle(course):
            if course in currSet:
                return False

            if course in visitSet:
                return True

            currSet.add(course)
            for p in preMap[course]:
                if not cycle(p):
                    return False

            currSet.remove(course)
            visitSet.add(course)
            res.append(course)

            return True

        for n in range(numCourses):
            if not cycle(n):
                return []
        return res
            
