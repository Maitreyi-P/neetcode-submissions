class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if not s or not t:
            return False
        if len(s) != len(t):
            return False

        st = [0]*26
        for i in s:
            st[ord(i)-ord('a')] += 1
        for j in t:
            st[ord(j)-ord('a')] -= 1

        for k in st:
            if k != 0:
                return False
        return True