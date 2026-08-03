class Solution:
    def validPalindrome(self, s: str) -> bool:
        # clean = "".join(char for char in s if char.isalnum())
        # string = clean.lower()

        def isPal(l,r):
            while l<= r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        l = 0
        r = len(s) - 1
        while l < r:
            if s[l] != s[r]:
                return isPal(l+1,r) or isPal(l,r-1)
            l += 1
            r -= 1

        return True