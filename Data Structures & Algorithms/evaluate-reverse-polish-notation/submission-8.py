class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stk = []

        for token in tokens:
            if token not in ["+", "-", "*", "/"]:
                stk.append(int(token))
            else:
                b = stk.pop()
                a = stk.pop()
                if token == '+':
                    stk.append(a+b)
                if token == '-':
                    stk.append(a-b)
                if token == '*':
                    stk.append(a*b)
                if token == '/':
                    stk.append(int(float(a/b)))
        return stk [-1]