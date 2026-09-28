class Solution:
    def isValid(self, s: str) -> bool:
        stk = []

        if len(s) < 2:
            return False
            

        for i in s:
            if i == "]":
                if not stk or stk[-1] != "[":
                    return False
                stk.pop()
            
            elif i == ")":
                if not stk or stk[-1] != "(":
                    return False
                stk.pop()

            elif i == "}":
                if not stk or stk[-1] != "{":
                    return False
                stk.pop()
            else:
                stk.append(i)

        if not stk:
            return True
        return False