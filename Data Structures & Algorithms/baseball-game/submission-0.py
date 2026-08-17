class Solution:
    def calPoints(self, operations: List[str]) -> int:
        
        score = 0
        stk = []

        for i in operations:
            if i == "+":
                a = stk[-1]
                b = stk[-2]
                stk.append(a+b)
            
            elif i == 'C':
                stk.pop()
            
            elif i == 'D':
                a = stk[-1]
                stk.append(a * 2)

            else:
                stk.append(int(i))

        return sum(stk)