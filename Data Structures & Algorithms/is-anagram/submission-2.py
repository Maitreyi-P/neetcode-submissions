class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s)!= len(t):
            return False
        
        l = [0]*27

        for i in s:
            l[ord(i) - 96] += 1
        for j in t:
            l[ord(j) - 96] -= 1

        if any(l):
            return False

        return True