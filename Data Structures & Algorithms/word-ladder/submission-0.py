class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        def checkdiff(s1,s2):
            diff = 0
            for i in range(len(s1)):
                if s1[i]!=s2[i]:
                    diff+=1
                if diff>1:
                    return False
            return True    
        
        q = deque()
        visit = set()
        minpath = math.inf

        q.append(beginWord)

        count = 0
        while q:
            count += 1
            for i in range(len(q)):
                s1 = q.popleft()
                visit.add(s1)
                for s2 in wordList:
                    if checkdiff(s1,s2) and s2 not in visit:
                        q.append(s2)
                
                if s1 == endWord:
                    minpath = min(count,minpath)
            
        
        return minpath if minpath != math.inf else 0

        