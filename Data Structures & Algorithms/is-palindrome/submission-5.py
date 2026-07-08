import re
class Solution:    
    def isPalindrome(self, s: str) -> bool:
        cleans = re.sub(r'[^A-Za-z0-9]+', '', s)
        finals = str.lower(cleans)
        
        i = 0
        j = len(finals) -1

        while i<j:
            if finals[i] == finals[j]:
                i +=1
                j -=1
            else:
                return False
        return True