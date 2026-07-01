class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []

        pairs = {
            ")":"(",
            "}":"{",
            "]":"["
        }

        for i in range(len(s)):
            if s[i] == "(" or s[i] == "{" or s[i] == "[":
                stack.append(s[i])
            elif s[i] in pairs:
                if len(stack) == 0:
                    return False
                if stack[-1] != pairs[s[i]]:
                    return False
                stack.pop()
        
        if stack:
            return False
        return True
                