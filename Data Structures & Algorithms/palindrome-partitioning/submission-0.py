class Solution:

    def ispal(self, s, i, j):
        while j >= i:
            if s[j]!= s[i]:
                return False
            j-=1
            i+=1
        return True

    def partition(self, s: str) -> List[List[str]]:
        
        res = []
        part = []

        def dfs(i):
            if i >= len(s):
                res.append(part.copy())
                return
            
            for j in range(i, len(s)):
                if self.ispal(s,i,j):
                    part.append(s[i:j+1])
                    dfs(j+1)
                    part.pop()
        dfs(0)
        return res
