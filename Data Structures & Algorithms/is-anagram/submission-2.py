class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        scoded = [0] * 26
        tcoded = [0] * 26

        for i in range(len(s)):
            scoded[ord(s[i]) - ord('a')] += 1
            tcoded[ord(t[i])- ord('a')] +=1
        if scoded != tcoded:
            return False
        


        return True