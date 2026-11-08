class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        
        dp = {}

        def rec(i,j,k):
            if (i,j,k) in dp:
                return dp[(i,j,k)]

            if k == len(s3) and i == len(s1) and j==len(s2):
                return True
            else:
                if k == len(s3):
                    return False 

            
            if i < len(s1) and s1[i] == s3[k]:
                if rec(i+1,j,k+1):
                    dp[(i,j,k)] = True
                    return True

            if j < len(s2) and s2[j] == s3[k]:
                if rec(i,j+1,k+1):
                    dp[(i,j,k)] = True
                    return True

            dp[(i,j,k)] = False
            return False

        return rec(0,0,0)