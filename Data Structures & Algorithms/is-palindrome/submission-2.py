class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        clean = "".join(char for char in s if char.isalnum())
        string = clean.lower()

        l = 0
        r = len(clean) - 1

        while l<= r:
            if string[l] != string[r]:
                return False
            l += 1
            r -= 1
        return True