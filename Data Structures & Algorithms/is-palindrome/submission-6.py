class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        n = ''
        for c in s:
            if c.isalnum():
                n+=c.lower()

        l = 0
        r = len(n)-1
        while l <= r:
            if n[l]!=n[r]:
                return False
            l+=1
            r-=1

        return True

