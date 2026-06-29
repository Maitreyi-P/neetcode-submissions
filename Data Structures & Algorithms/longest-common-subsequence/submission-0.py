class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        s1 = text1
        s2 = text2

        memo = [[-1] * len(text2) for _ in range(len(text1))]

        def dfs(i,j):

            if i >= len(s1) or j >= len(s2):
                return 0
            
            if memo[i][j] != -1:
                return memo[i][j]

            if s1[i] == s2[j]:
                memo[i][j] = 1 + dfs(i + 1, j + 1)
                # maxlen = 1 + dfs(i + 1,j + 1) 

            else:
                memo[i][j] = max(dfs(i+1, j), dfs(i, j + 1))
                # maxlen = max(dfs(i+1, j), dfs(i, j + 1))

            # return maxlen
            return memo[i][j]

        ans = dfs(0,0)
        return ans