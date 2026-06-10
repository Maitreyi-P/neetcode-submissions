import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        st = "".join(char for char in s if char.isalnum())
        lst = st.lower()
        
        i = 0
        j = len(lst)-1

        while i < j:
            if lst[i] != lst[j]:
                return False
            i+=1
            j-=1
        return True 