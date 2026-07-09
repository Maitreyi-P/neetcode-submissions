class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        def checkdiff(s1,s2):
            diff = 0
            for i in range(len(s1)):
                if s1[i] != s2[i]:
                    diff += 1
            if diff > 1:
                return False
            return True

    
        q = deque()
        q.append(beginWord)

        visit = set()

        minpath = math.inf

        count = 0
        while q:
            count += 1
            for i in range(len(q)):
                s1 = q.popleft()

                if s1 == endWord:
                    minpath = min(minpath, count)

                if s1 in visit:
                    continue

                visit.add(s1)


                for s2 in wordList:
                    if checkdiff(s1,s2):
                        q.append(s2)

        if minpath == math.inf:
            return 0
        return minpath



