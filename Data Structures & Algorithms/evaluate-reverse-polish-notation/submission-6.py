class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stk = []

        for t in tokens:
            if t == "+":
                a = int(stk.pop())
                b = int(stk.pop())
                val = a + b
                stk.append(val)

            elif t == "-":
                a = stk.pop()
                b = stk.pop()
                val = b - a
                stk.append(val)
            
            elif t == "*":
                a = stk.pop()
                b = stk.pop()
                val = a * b
                stk.append(val)
            
            elif t == "/":
                a = stk.pop()
                b = stk.pop()
                val = int(float(b) / a)
                stk.append(val)
            else:
                stk.append(int(t))
        print(stk)

        ans = int(stk.pop())
        return ans
        