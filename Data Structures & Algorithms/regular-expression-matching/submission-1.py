class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        dp = {}

        def rec(i,j):
            if j == len(p):
                return i == len(s)

            if (i,j) in dp:
                return dp[(i,j)]

            first_match = i < len(s) and (s[i] == p[j] or p[j] =='.')

            if j + 1 < len(p) and p[j+1] == '*':
                dp[(i,j)] =  rec(i, j+2) or (first_match and rec(i+1, j))
                return dp[(i,j)]

            if first_match:
                dp[(i,j)] =  rec(i+1, j+1)
            else:
                dp[(i,j)] = False

            return dp[(i,j)]

        return rec(0,0)
             