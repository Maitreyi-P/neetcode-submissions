class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        if x < 0:
            return False
        if 0 <= x <= 9:
            return True

        s = str(x)
        l = 0
        r = len(s) - 1

        while l <= r:
            if s[l] != s[r]:
                return False

            l += 1
            r -= 1
        
        return True
        