class Solution:
    def checkValidString(self, s: str) -> bool:
        
        par_stack = []
        star_stack = []

        for i in range(len(s)):
            if s[i] == "(":
                par_stack.append(i)
            elif s[i] == "*":
                star_stack.append(i)
            else:
                if par_stack:
                    par_stack.pop()
                elif star_stack:
                    star_stack.pop()
                else:
                    return False
        
        while par_stack and star_stack:
            if par_stack[-1] < star_stack[-1]:
                par_stack.pop()
                star_stack.pop()
            else:
                return False
        if par_stack:
            return False
        return True

                    
                