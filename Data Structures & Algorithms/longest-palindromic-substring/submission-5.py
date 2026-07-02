class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        if not s:
            return ""

        length = len(s)
        res = s[0]
        reslen = 1

        for i in range(len(s)):
                
            l,r = i,i
            while r< len(s) and l >= 0 and s[l] == s[r]:
                if (r - l + 1) > reslen:
                    reslen = (r - l + 1)
                    res = s[l : r+1]
                r += 1
                l -= 1
            

            l,r = i, i+1
            while r< len(s) and l >= 0 and s[l] == s[r]:
                if (r - l + 1) > reslen:
                    reslen = (r - l + 1)
                    res = s[l : r+1]
                r += 1
                l -= 1

        return res


            