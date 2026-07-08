class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        n = [0]*26

        for c in s1:
            n[ord(c) - ord('a')] += 1

        
        window = len(s1)

        l = 0
        r = len(s1) - 1

        while r < len(s2):
            section = s2[l:r+1]
            n2 = [0] * 26

            for c in section:
                n2[ord(c) - ord('a')] += 1

            if n == n2:
                return True
            
            else:
                l += 1
                r += 1

        return False