class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s1 = [0]*26
        t1 = [0]*26
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            s1[ord(s[i])-ord('a')] += 1
            s1[ord(t[i]) - ord('a')] -= 1
        for j in s1:
            if j != 0:
                return False
        return True

        
            

