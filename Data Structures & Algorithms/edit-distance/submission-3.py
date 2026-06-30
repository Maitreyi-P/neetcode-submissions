class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        dp = {}

        def rec(i,j):

            if (i,j) in dp:
                return dp[(i,j)]

            if i == len(word1):
                return len(word2) - j
            
            if j == len(word2):
                return len(word1) - i
            
            if word1[i] == word2[j]:
                dp[(i,j)] = rec(i+1, j+1)
                # return rec(i+1, j+1)
                return dp[(i,j)]

            dp[(i,j)] = min(rec(i + 1, j+1), rec(i+1,j), rec(i, j+1)) + 1
            return dp[(i,j)]

        return rec(0,0)
