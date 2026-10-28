class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        stk = []
        res = [0] * len(temperatures)

        for i in range(len(temperatures)):
            if not stk:
                stk.append([temperatures[i], i])
            else:
                if stk[-1][0] > temperatures[i]:
                    stk.append([temperatures[i], i])
                else:
                    while stk and stk[-1][0] < temperatures[i]:
                        temp,idx = stk.pop()
                        res[idx] = i - idx
                    stk.append([temperatures[i], i])

        return res