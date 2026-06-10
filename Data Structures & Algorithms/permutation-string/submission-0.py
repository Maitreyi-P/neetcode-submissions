class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        n = [0]*26

        for c in s1:
            n[ord(c)-ord('a')] +=1

        window = len(s1)
        i=0
        j=window -1

        while j<len(s2):
            n2 = [0]*26
            for c in range(i,j+1):
                n2[ord(s2[c])-ord('a')] += 1
            # print("n2",n2)
            # print("n",n)
            if n2 == n:
                return True
            else:
                i+=1
                j+=1

        return False

            