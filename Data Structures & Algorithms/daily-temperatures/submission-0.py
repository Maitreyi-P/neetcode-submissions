class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        output = [0]*len(temperatures)
        stk = []

        for i in range(len(temperatures)):
            if not stk:
                stk.append((temperatures[i],i))
            else:
                while stk and temperatures[i] > stk[-1][0]:
                    t,ind = stk.pop()
                    diff = i - ind
                    output[ind] = diff
                
                stk.append((temperatures[i],i))
        return output



        