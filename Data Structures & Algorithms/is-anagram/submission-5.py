class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        count = [0] * 26

        for i in s:
            count[ord(i) - ord('a')] += 1
        for j in t:
            count[ord(j) - ord('a')] -= 1


        for k in count:
            if k != 0:
                return False
        return True